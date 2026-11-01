"""Generate only current-release blocks from GitHub's published latest release.

Run --write to prepare changes; default checks without writing. Never publishes.
Use --release-json for a retained API response during offline review.
"""
import argparse
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = "Limited-Underground/Husky-Performance-Releases"
START, END = "<!-- current-release:start -->", "<!-- current-release:end -->"


def generate(release):
    tag = release["tag_name"]
    if not re.fullmatch(r"v\d+\.\d+\.\d+", tag) or release.get("draft") or release.get("prerelease"):
        raise ValueError("Expected a published stable three-part version")
    version = tag[1:]
    assets = {a["name"]: a for a in release["assets"]}
    name = f"Husky-{version}-win-x64.zip"
    required = [name, name + ".sha256"]
    for key in required:
        asset = assets[key]
        expected = f"https://github.com/{REPO}/releases/download/{tag}/{key}"
        if asset["browser_download_url"] != expected or not re.fullmatch(r"sha256:[0-9a-f]{64}", asset["digest"]):
            raise ValueError("Unexpected asset URL or missing SHA-256")
    manifest = {"version": version, "tag": tag, "releaseUrl": release["html_url"],
                "portableUrl": assets[name]["browser_download_url"],
                "checksumUrl": assets[name + ".sha256"]["browser_download_url"],
                "sha256": assets[name]["digest"].split(":")[1].upper(),
                "installerUrl": None, "unsigned": "unsigned" in release["body"].lower()}
    msi = f"Husky-{version}-win-x64.msi"
    # Publication is the qualification boundary; never invent an MSI URL.
    if msi in assets:
        manifest["installerUrl"] = assets[msi]["browser_download_url"]
    block = f"""{START}
## Current release: Husky Performance {version}

- [Portable Windows x64 ZIP]({manifest['portableUrl']})
- [ZIP SHA-256 checksum file]({manifest['checksumUrl']})
- [Release notes and known limits]({manifest['releaseUrl']})

ZIP SHA-256: `{manifest['sha256']}`

"""
    block += (f"[Windows x64 installer]({manifest['installerUrl']})\n\n" if manifest["installerUrl"]
              else f"**Installer:** No MSI is published for {version}. Fresh-install, upgrade and uninstall qualification remain pending; use the portable ZIP.\n\n")
    signing = "Unsigned software; Windows may show publisher or reputation warnings. " if manifest["unsigned"] else "See release notes for signing status. "
    block += f"{signing}Free for personal and business use, with no activation or expiry.\n{END}"
    outputs = {"CURRENT-RELEASE.json": json.dumps(manifest, indent=2) + "\n"}
    for filename in ("README.md", "PROJECT-STATUS.md", "TESTING-PARTNERS.md", "CHANGELOG.md"):
        text = (ROOT / filename).read_text(encoding="utf-8")
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError(f"Missing or ambiguous current-release markers: {filename}")
        outputs[filename] = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
        if outputs[filename].count("## Current release") != 1:
            raise ValueError(f"Duplicate current-release heading: {filename}")
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-json", type=Path)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    if args.release_json:
        release = json.loads(args.release_json.read_text(encoding="utf-8-sig"))
    else:
        req = urllib.request.Request(f"https://api.github.com/repos/{REPO}/releases/latest", headers={"User-Agent": "Husky-release-docs"})
        with urllib.request.urlopen(req, timeout=30) as response:
            release = json.load(response)
    stale = []
    for filename, expected in generate(release).items():
        path = ROOT / filename
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            stale.append(filename)
            if args.write:
                path.write_text(expected, encoding="utf-8")
    if stale and not args.write:
        raise SystemExit("Stale release documentation: " + ", ".join(stale) + "; run tools/sync-release.py --write, review, then publish with authorization")
    print("PASS: latest release documentation " + ("prepared" if args.write else "matches"))


if __name__ == "__main__":
    main()
