# Changelog

All notable public-facing changes to Husky Performance are recorded here.

For a plain-language overview, start with [Project Status](PROJECT-STATUS.md).

Husky Performance is still pre-release software. Entries under **Unreleased** describe work completed for a future preview but not yet included in the current public download. A change moves into a numbered release only after its package has been built and validated.

Unreleased entries are grouped by completion date, newest first.

## [Unreleased]

### 2026-08-13

- Added private-development saved, pending, review-required, and defaults-review state to **Settings > Reports & Branding**. Shop identity, contact, accent, footer, technician, and logo changes remain staged until **Save Settings**; **Discard branding changes** restores the complete saved profile including its logo; and **Restore defaults for this page** stages standard Husky branding with empty shop fields, Husky blue `#00A6C7`, and no shop logo. Permanent Husky provenance remains, and neither action writes automatically.
- Added private-development saved, pending, review-required, and defaults-review state to **Settings > Backup & Restore** retention. Ordinary edits remain staged until **Save Settings**; **Discard retention changes** restores the saved policy; and **Restore defaults for this page** stages retention disabled, 14 daily, 8 weekly, 12 monthly, and the default Backups folder. Neither action creates, verifies, restores, cleans up, or deletes a backup, and neither writes settings before Save.
- Added private-development review-first defaults to **Settings > Injector Service**. Shop identity, send/provide workflow role, and privacy-safe vehicle inclusion remain staged until **Save Settings**; **Discard changes** restores the saved choices, while **Restore defaults for this page** stages the current shop identity, both workflows, and vehicle inclusion without writing preference files.
- Added a private-development **Restore defaults for this page** action to General & Appearance. It stages Dark, Standard text, and Windows language for review, applies and saves nothing automatically, and works with **Discard appearance changes** to restore the prior saved choices before **Save Settings**.
- Corrected private-development General & Appearance guidance so theme, text-size, and language choices are explicitly staged until **Save Settings**. An accessible live status now distinguishes saved, pending, and restart-required-after-save states; **Discard appearance changes** restores the saved selections without applying them, writing settings, or restarting Husky.
- Corrected private-development Settings search so common option names such as language, retention, and security mode route to the correct category instead of matching category titles only. Search terms include English, Spanish, German, and Russian keywords; zero matches now announce an accessible empty state and hide the previously selected panel, while clearing search restores all eight categories. Searching changes no setting.
- Added private-development **View All** launch points to the Dashboard Saved Logs, Vehicles, and Customers counts. Each action opens the corresponding complete authoritative list, changes no records, and preserves the fixed non-scrolling Dashboard. Native validation confirmed all three routes at the supported minimum window size.
- Added a private-development **Work orders** action to Dashboard Active Work. It stays disabled while the current snapshot is loading, when no active work exists, and after refresh failure; once active work is verified, it opens Customers & Jobs directly on the complete Jobs / Work Orders list. It clears only the narrowing job search, changes no customer or work-order data automatically, and preserves the fixed non-scrolling Dashboard.
- Version 0.9.1 remains the current public preview. This private-development workflow improvement does not authorize or alter a public installer, and the qualified-business feedback hold still blocks any later preview.

### 2026-08-12

- Added a private-development **Open selected** action to Dashboard Latest Imports. It stays disabled until the current Dashboard snapshot loads and one exact imported-log row is selected, then clears prior Saved Logs narrowing and selects that stable record for review. Missing selection, refresh failure, and a record that is no longer active remain non-actionable; no saved log changes automatically.
- Added a private-development **Analyze selected** action to Dashboard Recent Activity. It stays disabled until the current Dashboard snapshot loads and one exact saved-log row is selected, then opens that stable log identity in the existing Analysis channel selector. Missing selection and refresh-failure states remain non-actionable, no data changes automatically, and the fixed non-scrolling layout remains intact.
- Corrected the private-development Dashboard's **Active Work** card so it no longer appears as a yellow warning for every queue. It now derives neutral **Empty**, informational **Active**, or warning **Needs attention** from the exact active, waiting, overdue, due-today, quality-check, and ready-for-pickup work-order counts. The visible icon, color, background, accessible state, and path-free guidance remain synchronized; no work order changes automatically.
- Version 0.9.1 remains the current public preview. This private-development correction does not authorize or alter a public installer, and the qualified-business feedback hold still blocks any later preview.

### 2026-08-11

- Corrected the private-development Dashboard's **Continue in Analysis** action so it no longer returns to the generic Saved Logs list. It starts disabled, becomes available only after the exact latest saved log supplies real graphable preview channels, and opens that same log in the existing Analysis channel selector. Empty, needs-channel, and unavailable states stay disabled, and no data changes automatically.
- Replaced unconditional Dashboard success claims with evidence-backed library, import, analysis, and backup states. The private-development Dashboard now distinguishes checking, empty, review, usable, ready, needs-attention, and unavailable conditions from real loaded results while keeping the fixed non-scrolling layout.
- Expanded the verified recovery-point browser with explicit refresh, aggregate-only inspection, privacy-safe summary copy, folder handoff, and restore-review handoff. Each action remains operator initiated, re-verifies its selected backup, exposes no full backup path, and never restores, deletes, cleans up, or uploads automatically.
- Expanded read-only storage accounting to include Husky-managed video and Injector Exchange files and to base drive-pressure guidance on the complete known Husky footprint. The checks read metadata and report limitations; they do not compact or delete data.
- Version 0.9.1 remains the current public preview. No later public preview is authorized until an established automotive business completes meaningful workflow testing, provides substantive feedback, and the owner reviews that feedback.

### 2026-08-10

- Added a bounded, read-only Data Library health check covering encrypted-file state, protected-key presence, SQLite integrity, schema version, drive headroom, logical stored-content totals, reusable-page accounting, and privacy-safe summary copy. The action does not repair, compact, delete, upload, or expose customer records.
- Added explicit, verified backup handoffs and draft retention-policy controls with conservative defaults and protected-invalid-file handling. Cleanup remains a separate acknowledged action; recovery-point inspection and ordinary verification do not remove files.

### 2026-08-09

- Updated the separate guided external-test companion for a future controlled package. Its eleven-step plan now covers every current core workflow, rejects Simulator and retired workspace names, requires copied or fictional test data, permits unavailable fixture-dependent work to be marked Not tested, and uploads nothing automatically. This companion update is not part of the published 0.9.1 download.

## [0.9.1] - 2026-08-09

### Changed

- Removed Simulator completely from navigation, Saved Logs actions, implementation, help, localization, and package resources so the public trial stays focused on useful professional workflows.
- Added operator-reviewed two-log comparison reports and versioned shared comparison templates with bounded stable-channel matching, exact source identity, stale-review rejection, and privacy-minimized history.
- Kept Dashboard fixed and non-scrolling while strengthening keyboard, enlarged-text, selector, list, grid, report, and Saved Logs accessibility behavior.
- Expanded direct packaged acceptance for log import/review, customer-designed reports, customer/work-order and vehicle history, exact Tune Library attach/export, backup/recovery, and two-installation Injector Service exchange.

### Reliability and safety

- Hardened encrypted database migration/replacement, backup archive inspection, atomic backup completion, restore boundaries, first-use key publication, and recovery identity creation under concurrency and failure.
- Hardened CSV, ASNU, injector-exchange, support-package, guided-test-package, calibration-file, and managed-source processing against hostile sizes, duplicate entries, non-finite values, stale fingerprints, and partial output.
- Preserved copied/fictional-data guidance, local encrypted storage, no automatic uploads, post-expiration view/export access, and explicit review gates for sensitive exports and recovery actions.

### Validation

- Release build: zero warnings and zero errors; foundation checks: 92/92.
- Final coordinated stabilization: Safe 60/60 and Full 94/94 with zero failed or skipped checks.
- The exact final 0.9.0-to-0.9.1 MSI lifecycle passes install, launch, repair, major upgrade/relaunch, downgrade rejection, uninstall, cleanup, and isolated user-data preservation.
- The published release contains exactly one MSI, one compact ZIP, and one checksum sidecar. GitHub's server-side digests and separate anonymous public downloads match the retained release files byte-for-byte.

### Known limitations

- This is unsigned pre-release demonstration software and is not approved for production shop use.
- Windows 10, independent clean-machine/shop testing, signing, licensing completion under LIC-003, legal review, and production acceptance remain open gates.

## [0.9.0] - 2026-08-03

### Added

- Added multi-select business types for Performance / Tuning, Injector Testing / Cleaning, and Diesel Diagnostics / Fuel-System shops. Supported combinations adjust the recommended starting view without removing Professional capabilities or records.
- Added bounded bulk and large-log import/review improvements, Husky-native customer session-report layouts, Tune Library originals and lineage, linked work records, and strengthened backup/recovery workflows.
- Added the current accessibility, localization, and shared-scrollbar corrections across the Windows desktop application.

### Changed

- In the historical 0.9.0 package, Simulator remained visible but disabled. Version 0.9.1 supersedes that state and removes Simulator completely.
- The weekly public package now identifies version 0.9.0, retains the five-day evaluation that begins with the first successfully saved real log, and preserves view/export access after expiration.

### Privacy and safety

- Processing and encrypted storage remain local to the computer; nothing is uploaded automatically.
- Sensitive backup, restore, inventory, tune-original, and source-extraction actions use explicit fail-closed acknowledgement boundaries.
- This remains unsigned pre-release evaluation software and is not approved for production shop use. Use copied logs and fictional or test customer information.

### Validation

- The Release solution built with zero warnings and zero errors.
- All 113 foundation checks passed, along with 100% Spanish literal coverage, complete German/Russian catalogs, the application-wide scrollbar audit, and native Public Demonstration verification that Simulator is disabled.
- The MSI, public bundle ZIP, and standalone checksum were downloaded again from the published release and matched their exact local byte counts and SHA-256 identities.
- Installer lifecycle mutation remains unperformed on this development computer because a related Husky product is installed; independent clean-machine, Windows 10, signing, legal, licensing completion under LIC-003, and final production acceptance remain open gates.

### Detailed development record

### 2026-08-02

#### Added

- Added a pending-intake resolution worksheet and non-applying validation-evidence staging manifest to Husky Planner. Every generated resolution begins blank and remains tied to the exact verified intake hash. Completed items require a supported resolution, resolver, date, and rationale; ready items also require evidence references. Staging preserves those references only as SHA-256 digests, leaves every gate unchanged, records `AWAITING_NEW_VALIDATION_RUN`, and keeps the target run `NOT_ASSIGNED`. Duplicate or altered identities are refused, and staging cannot apply evidence to the old run, change readiness, approve a release, or authorize distribution.

- Added a strict candidate-evidence handoff receiver and append-only pending-validation intake queue to Husky Planner. A handoff must match the active run, canonical checklist, exact retained reconciliation-report hash, recomputed minimized items, privacy boundary, and generated Markdown before a named receiver can append it. Every verified queue entry remains `PENDING_MANUAL_VALIDATION` with zero gates changed; duplicate or altered identities are refused, and intake cannot change readiness, approve a release, or authorize distribution.

- Added a source-reverifying reconciliation-report browser and privacy-minimized candidate-evidence handoff to Husky Planner. Reports are displayed only after their exact retained adjudication, hashes, recommendations, active run, and canonical-checklist identity are recomputed and verified. The handoff replaces raw evidence references with SHA-256 digests and excludes names, notes, rationale, local paths, and machine/user identity; it remains routing metadata only and cannot prove a gate, change readiness, approve a release, or authorize distribution.

- Added strict completed-adjudication review and a separate canonical release-checklist reconciliation report to Husky Planner. Completed Markdown is accepted only while its JSON template, reviewed-evidence identity, hashes, validation run, unresolved requirements, and SHA-256-identified checklist remain exact. A second acknowledged review atomically preserves the source and reports only candidate-support or no-change recommendations; every canonical status remains unchanged, zero gates are promoted, and the report cannot change readiness, approve a release, or authorize distribution.

- Added a hash-verifying, read-only reviewed-evidence browser and a separate manual gate-adjudication worksheet to Husky Planner. Every ledger entry must retain its exact four files, match the active evidence run, pass three SHA-256 checks, and reparse to the recorded decisions, tests, identities, and counts before it is displayed as verified. A verified entry can produce one atomic JSON/Markdown worksheet whose items begin unadjudicated with no gate effect; duplicate worksheets are refused, and creation cannot change readiness, approve a release, or authorize distribution.

- Added guarded completed-form review and an append-only reviewed-evidence ledger to Husky Planner. The importer parses the human-readable worksheet, reconciles its schemas, exact validation run, full requirement inventory, dates, evidence fields, tester metadata, and candidate identity, then requires a named reviewer and explicit acknowledgement. Accepted forms and their SHA-256 hashes are atomically preserved together; exact duplicates and reused record identities with changed content are refused. Intake cannot change readiness, prove a gate by itself, approve a release, or authorize distribution.

- Added atomic owner-decision and external-tester review forms to Husky Planner. One explicit action creates a human-readable worksheet plus structured JSON containing the current 17 decision/design requirements and eight external-test requirements, all tied to one evidence run. Candidate version, commit, package checksum, decisions, and outcomes remain blank; form creation cannot change readiness, approve a release, create a software package, or authorize distribution.

- Added a read-only Release Review window to Husky Planner. Owners can inspect every unresolved release requirement, filter it by package, external evidence, licensing/roles, or owner/legal dependency, and see the exact next action and evidence-run identity. The reader rejects mixed-run, duplicate, invalid, or count-mismatched evidence, and the window cannot create a package, change status, record approval, or authorize distribution.

- Added versioned known-issue and one-version rollback guidance to Preview Safety. Four release-limit groups disclose distribution authorization, incomplete external acceptance, pre-release data risk, and manual package-specific updates. Six ordered recovery steps match Husky Recovery & Rollback, require a verified Complete Backup and retained package checksums, and warn never to open a newer-schema library with an older package. The screen links to Manual Updates and explicitly cannot authorize the running copy for distribution.

- Added a dedicated Preview Safety status screen in Help & Support. It shows the running build boundary, distinguishes an empty or fictional library from protected existing customer data and a currently verified Complete Backup, exposes only bounded backup identity rather than its full path, repeats copied/isolated-data and no-automatic-upload rules, refreshes verification on demand, and opens Backup & Restore directly when action is required.

- Added bounded bulk export for verified Tune Library originals. Operators can review and export up to 25 selected exact revisions into a new non-overwriting folder with a checksum manifest. Husky verifies every source and destination, requires Professional shop-administration authorization and explicit acknowledgement, supports cancellation with incomplete-folder cleanup, and records per-revision plus batch audit evidence. Open Shop attributes the action to a local operator and does not claim verified owner identity or tune safety.

### 2026-08-01

#### Added

- Added immutable review checkpoints for exact Tune Library revisions. A Professional shop administrator can record Changes Requested or Accepted for Shop Workflow only after entering a reason and acknowledging that the decision applies to the checksum-identified stored file and is not a technical safety claim. Every decision is append-only, retains its checksum and Open Shop attribution, survives Complete Backup, merge, and selected-tune recovery, and remains visible as history. Open Shop honestly attributes decisions to a local shop operator rather than pretending to identify an individual approver.

- Added explicit Tune Library relationships for exact revisions. Operators can connect a revision to the saved logs and work orders where it was used, review those links from the library, and remove an incorrect relationship without changing either record. Husky rejects relationships that would mix known vehicles, records link/unlink audit history, and preserves related logs, work orders, lineage, and tune originals during Complete Backup, merge, and selected-tune recovery. The relationship does not compare or interpret calibration contents.

- Added immutable Tune Library version lineage. When attaching a distinct existing file, the operator can identify its parent tune and record a revision note; Husky inherits the parent vehicle, refuses cross-vehicle revision links, and displays the complete baseline-to-branch history without comparing or interpreting calibration contents. Complete Backup, merge, and selected-revision recovery preserve the required parent chain.

- Added a persistent, read-only Tune Library for existing calibration files. Husky encrypts and checksum-verifies exact originals up to 128 MB, rejects exact duplicates, links them to an optional vehicle and work order, exports only to a new destination, and preserves reversible archive history with audit records. Complete Backup, merge, and selected-item recovery retain Tune Library originals; Configuration / Records Backup explicitly excludes and reports them. Husky does not interpret maps, change values, write calibrations, flash vehicles, or claim a tune is safe.

- Added multi-file selection to Import Log with a review-first batch queue. Operators can choose several CSV logs at once, inspect and save each file through the existing complete channel/metadata review, skip an unsuitable current file, or cancel the remaining queue without undoing logs already committed safely to the local library.

- Added per-log persistence for local Simulator road-video chapters, synchronization offset, and bounded playback rate. Reopening a saved log restores reference-only chapter order without rehashing multi-gigabyte originals. Persisted SHA-256 identity is paired with current file length and modification time, so missing or changed files are rejected with reselect guidance. Removing Video clears only that log's preference; no video contents, GPS, or route data are stored.

- Added consecutive local road-video selection for camera recordings split across multiple MP4/MOV chapters. Simulator orders selected files consistently, treats decoded chapter durations as one continuous video timeline, advances automatically at each boundary, and retains the same log offset and playback state. Single-file selection remains supported, and footage remains reference-only and local.

- Added the first synchronized local road-video mode to Simulator playback. An optional MP4 or MOV can now replace the synthetic scenery while the stable cockpit gauges and evidence-based overlays remain on top; play, pause, timeline seeking, playback speed, and a manual log offset stay synchronized. Video remains reference-only and local—nothing is uploaded. Multi-chapter footage, attachment persistence, codec validation, and owner visual acceptance remain open work.

- Added streaming import support for Car Scanner Pro semicolon-delimited long CSV exports (`SECONDS`, `PID`, `VALUE`, and `UNITS`). Asynchronous PID measurements are normalized to a deterministic 10 Hz review timeline while preserving the existing positional CSV path.

#### Improved

- Bounded multi-file Import Log selection to 100 unique paths per review batch and added exact outcome accounting. Batch completion and cancellation now disclose saved, duplicate, skipped, and failed counts plus any remaining files not imported, while preserving logs already committed to the local library. These batch messages are available in English, Spanish, German, and Russian.

- Made Simulator video synchronization controls follow the attached-video lifecycle. Offset, rate, nudge, Apply Sync, and Reset Sync now begin disabled, become available only after a local video is attached or restored, and disable again when playback fails, the video is removed, or the loaded log is cleared.

- Rejected non-finite and extreme Simulator road-video synchronization values before they reach playback or persistence. `NaN`, infinity, and offsets outside ±86,400 seconds now receive bounded input guidance; the stored-preference loader and writer enforce the same limit so malformed local settings cannot create an invalid media seek.

- Kept displayed Simulator video synchronization values in the active Windows number format after Apply Sync, frame nudges, Reset Sync, and reopening a saved log. Decimal-comma users now see `18,13` and `0,998364` consistently while the culture-independent stored values remain unchanged.

- Made Simulator road-video offset and rate entry accept the active Windows decimal format as well as a decimal point. Decimal-comma users can enter values such as `18,13` and `0,998364`; ambiguous thousands separators remain rejected, while persisted synchronization stays culture-independent.

- Added keyboard alignment controls for active Simulator road video: `Alt+Left` moves video 0.10 second earlier, `Alt+Right` moves it 0.10 second later, and `Alt+0` restores neutral synchronization. Tooltips disclose the shortcuts, and each command uses the same immediate seek and durable per-log save path as its button.

- Added a one-click Reset Sync action for Simulator road video. It restores a neutral `0.00 s` offset and `1.000000` playback rate, seeks the local video immediately, discloses the result, and persists the reset for that log without changing recorded timing or samples.

- Made repeated Simulator video-alignment clicks latest-value-wins per log. An older queued preference write is discarded when that same log already has a newer offset or rate request, preventing rapid frame nudges from restoring a stale intermediate value without allowing activity on another log to cancel its save.

- Made Simulator video-alignment changes durably complete before their interface actions finish. Apply Sync and each ±0.10-second nudge now await the per-log local preference write, so persistence failures are reported instead of becoming unobserved background errors.

- Added immediate ±0.10-second Simulator video-alignment nudges. Each nudge seeks local video immediately, shows the resulting offset and playback rate, persists per log, and does not modify log timing or exact samples.

- Hardened the local GoPro playback-proxy cache. Valid proxies are reused, new copies remain uniquely partial and unplayable until length verification and atomic promotion complete, and stale cleanup is restricted to Husky-named top-level cache entries. The active proxy, originals, `.LRV` sidecars, subdirectories, and unrelated temporary files are never cleanup targets.

- Added a tightly bounded Simulator video-rate correction beside the log offset. Small camera/proxy clock differences can now be compensated from 0.95× through 1.05× without changing the recorded log timeline or exact gauge samples, and the applied six-decimal rate is disclosed. The supplied GoPro proxy set's evidence-based starting value is approximately `0.998364`.

- Added automatic local GoPro proxy fallback when Windows cannot decode a selected high-frame-rate camera original. Husky keeps the MP4 as the authoritative source, locates its matching `GL...LRV` sidecar, creates an isolated temporary `.mp4` playback proxy, and retries on the same synchronized timeline. Originals remain unchanged and nothing is uploaded. Native Windows probing confirmed that all three supplied 768×432 proxies open successfully; the 119.88-fps original is rejected by the current Windows WPF codec stack.

- Kept the Simulator responsive while a large local road-video file is verified. Reference-only identity work now runs away from the interface thread; playback waits for Windows to confirm that the codec opened, reports decoded dimensions, and safely restores generated scenery with a clear error when decoding fails. The file remains local and nothing is uploaded.

- Corrected arcade-like road markers exposed by native Simulator screenshots. Highway edge motion is now faint neutral gray, Brake Test uses subdued safety orange, and alternating red/white markers remain scoped to Drag Strip; peripheral-flow emphasis scales each scenario's intended opacity instead of brightening suppressed markers. A fresh six-screenshot review and the complete 26-assertion native scenario workflow pass.
- Added slow, bounded lane-and-shoulder width evolution to Simulator playback. Road-edge convergence now varies gently by integrated distance and scenario while cockpit geometry stays fixed; Drag Strip remains nearly uniform, Highway and Brake Test remain restrained, Closed Test Road receives more natural variation, and stationary playback returns to the exact baseline.
- Smoothed Simulator road evolution across evidence-detected scenario boundaries. Curvature, elevation, pavement texture, peripheral flow, and roadside density now blend through the photographic environment's 550-ms transition instead of snapping at one recorded sample; the blend remains deterministic during pause, seek, replay, and manual environment overrides.
- Added restrained, distance-synchronized pavement texture and scenario-specific roadside variation to Simulator playback. The subtle perspective layer follows the existing bounded curve and elevation model, remains subdued on Highway and Drag Strip, and disappears completely during stationary or unknown playback.
- Added bounded, distance-driven road evolution to Simulator playback. Scenario-specific bends, gentle elevation changes, and restrained peripheral flow now follow recorded speed and integrated visual distance while the cockpit and gauges remain stable. Drag Strip stays nearly straight, Stationary/unknown playback stays exactly still, and all visual movement remains tightly bounded.
- Limited whole-session Simulator playback to 10 recorded minutes or 250,000 samples. Five-minute segments are recommended for focused pulls, braking tests, and other events. Extended logs remain importable and reviewable, but Simulator rejects them before loading channel arrays and directs the operator to create a bounded segment.

#### Validation

- Added a compiled isolated persistence regression proving that three ordered Simulator video chapters, the `18.13`-second offset, and the `0.998364` rate survive store reconstruction. The same test independently proves changed-file rejection, missing-file rejection, and durable per-log preference removal without using private footage or the normal Husky library.

- Imported the complete owner-supplied 219,636,786-byte Armada log containing 3,136,309 source measurements into 187,881 review samples across 66 numeric channels. It archived into the encrypted test library and reopened through the production log-review service; recorded vehicle speed ranged from 0 to 103.15 mph.
- The full development solution builds with zero warnings and errors, and all 111 foundation checks pass. These Unreleased changes are not included in public version 0.8.99.

### 2026-07-31

#### Added

- Added evidence-driven photographic Simulator environments for Highway, Drag Strip, Brake Test, Garage/Paddock, and a neutral closed test road. Auto mode classifies bounded recorded segments instead of treating every log as a race-track session.
- Added recorded-event overlays for qualified drag-tree staging and finish markers, the optional brake-test cow, and the optional non-drag 100+ mph “Welcome to Mexico” sign. Humor remains off by default and never changes recorded evidence.
- Added native end-to-end validation using owner-supplied real logs and isolated drag, brake, highway, and mixed-session fixtures.

#### Improved

- Synchronized scenery, scenario transitions, drag timing, finish distance, brake-stop behavior, road motion, and subtle cockpit body response to the recorded playback timeline while keeping gauges on exact saved samples.
- Corrected packaged cockpit resources, initial Track View rendering, full-screen compact gauge placement, per-segment drag/highway scope, and cross-scenario overlay cleanup.

#### Validation

- Real-log import, saved review, scenario detection, native overlay workflows, full-screen behavior, and zero-warning builds passed their recorded checkpoints. Packaged owner visual acceptance remains a separate open gate.
- None of the July 31 Unreleased work is included in public version 0.8.99.

### 2026-07-30

#### Added

- Added a dedicated Log Simulator workspace in private development. It replays exact samples from a saved log on their original recorded timeline with play, pause, explicit Stop/reset, restart, timeline scrubbing, and 0.25x through 4x playback.
- Added editable virtual dashboards with up to eight available numeric channels, common channel presets, per-gauge Analog, Dial, Digital, LED Ring, or Bar presentation, Small/Medium/Large sizing, optional recorded Min/Max values, a snapping alignment grid, and per-log layout persistence.
- Added qualified 0–60 mph, 0–100 mph, 1/8-mile, 1/4-mile, custom acceleration, and braking calculations. Results remain unavailable unless the selected log contains the required speed, RPM, throttle, time-continuity, starting-condition, and uninterrupted-run evidence.
- Added a public [Project Status](PROJECT-STATUS.md) page that clearly separates Currently Available, In Progress, Potential Next Trial Release, and Roadmap information.

#### Improved

- Reworked Simulator gauges with original Husky instrument artwork: layered bezels, recessed faces, detailed major/minor scales, numeric scale labels, tapered needles, dimensional hubs, high-contrast digital windows, and a progressive 24-segment LED-ring presentation.
- Improved Simulator full-screen ownership and exit behavior. Full screen now provides a visible exit action, supports Escape, removes the redundant nested Full Screen action, and closes with the main application.
- Added Essentials, Engine Performance, Fuel and Air, Temperatures, Wheel and Chassis, and Clear All gauge presets that select only compatible channels recorded in the current log and preserve the eight-gauge readability limit.
- Improved the high-channel-count editor with search, a wider control area, usable vertical scrolling, disabled horizontal overflow, and unclipped style, size, and Min/Max controls.
- Added explicit Edit Dashboard and Close Editor states, automatic per-log layout saving, movable gauges, and a movable or hideable performance panel. Playback locks layout changes.
- Added complete Simulator help and English, Spanish, German, and Russian interface coverage.

#### Safety and limitations

- Simulator visual bands and LED colors represent position within a channel's finite recorded range. They are not calibrated warning limits or vehicle-safety thresholds.
- Simulator performance values are analysis aids, not certified track timing, automatic diagnosis, tuning instructions, or machine-control decisions.
- An experimental inside-car/track visualization exists in private development but is not considered presentation-ready and is not approved for promotional screenshots. Gauge-dashboard quality remains the priority.
- None of the July 30 Unreleased work is included in public version 0.8.99 merely because it appears here.

#### Validation

- Current private-development Release builds complete with zero build warnings and zero build errors.
- Coordinated native Windows testing passes Simulator playback, Stop/reset, presets, independent gauge choices, layout persistence, edit locking, full-screen exit, main-window shutdown, selected-log handoff, malformed-preference recovery, and qualified performance disclosure.
- Spanish literal-interface coverage is complete for the current development surface, and the German and Russian catalogs pass their current automated coverage and placeholder checks.
- Package, installer, clean-machine, Windows 10/11, signing, licensing, legal, owner, and independent-shop acceptance remain separate release gates.

### 2026-07-29

#### Improved

- Confirmed Husky Performance's business-only product direction. Future Preview builds always use Professional business capabilities, and the customer-facing desktop no longer reads the retired Personal development override. Guided Setup always uses Business / Shop identity and Professional Open Shop access, and Customers always presents business customer/shop and work-order workflows. Historical Personal-mode data readers remain only for migration and regression safety and are not an offered product path.
- Restricted the private licensing registry to new Professional business licenses. Personal issuance is rejected even if the registry service is called directly, and the admin screen no longer offers it. Historical Personal records remain visible only as legacy support and migration data.
- Added a central language-pack catalog for language codes, cultures, names, aliases, safe English fallback, and translation lookup. The shell, Settings, and Guided Setup language choices now come from this catalog instead of separate hand-maintained lists. A translation-management utility exports a reviewable UTF-8 CSV and reports missing entries and unsafe format-placeholder changes, making existing translations easier to maintain and future languages easier to add.
- Added owner-selectable Professional business profiles for performance/tuning shops, injector testing/cleaning businesses, and combined businesses. The Dashboard identifies the selected profile, orders its summary cards by the business's configured priorities, and prioritizes its Quick Launch actions. Reports opens at a relevant starting template with profile-specific guidance while keeping every report template available and preserving later user choices. Guided Setup presents a short recommended starting path for the selected business. Profiles are presentation choices only: every Dashboard summary and Professional workspace remains available, and changing profiles never moves, hides, or deletes records.
- Added a read-only, filterable chronological vehicle history that brings existing vehicle lifecycle events, linked logs, work-order activity, and injector-service records into one view without inventing missing history.
- Expanded German and Russian interface coverage across the Support and Vehicles workspaces.
- Added German and Russian translations for the complete offline Support help library, including instructions, notes, actions, and privacy guidance.
- Improved German and Russian wording for vehicle details, assignments, capacity summaries, archive controls, and vehicle state labels.
- Clarified the saved analysis-channel preset workflow so users can select channels, choose **Save Current**, name the preset, and reuse it later.
- Saved analysis workspaces now remember which analysis panels were left expanded or collapsed for each saved log.

#### Fixed

- Clarified vehicle assignment in Logs & Analysis after an owner workflow exposed misleading disabled-state behavior. The vehicle selector now renders the readable vehicle name instead of a raw internal record, assignment requires both an unassigned active log and a selected active vehicle, and nearby guidance explains when a log is already assigned. Existing assignments remain protected from silent reassignment.

- Corrected additional English fallback text that could appear while using German or Russian.
- Improved consistency of localized dynamic labels and vehicle states.

#### Validation

- Verified an isolated PrivatePreview build still visibly identifies itself as `DEVELOPMENT LICENSE • PROFESSIONAL • SIMULATION` when the retired Personal override is deliberately set, while retaining its Preview label and backup-before-use warning.
- Replaced the obsolete Personal-owner validation path with coordinated checks for the three supported Professional business profiles.
- Verified that the private registry accepts Professional business registration and rejects attempted Personal issuance at its service boundary.
- Verified the language catalog, catalog-generated shell/Settings/Guided Setup choices, CSV export, English fallback, and numbered-placeholder safety.
- Verified real Guided Setup behavior for the Business / Shop identity label, Professional Open Shop default, all five setup steps, revisiting, safe Quick Setup, Skip for now, and deferred re-prompt.
- Verified Professional business-profile selection, safety preview, immutable audit history, restart persistence, reversible switching, dashboard summary-card and Quick Launch priority, unchanged full navigation, profile-specific report starting points, retained access to every report template, preservation of a user's report-template choice during refresh, profile-specific Guided Setup instructions, and safe fallback for unknown or retired profile IDs.
- Verified the vehicle-history data contract and compatibility with supported libraries that do not yet contain injector-session detail tables.
- Expanded automated localization checks to protect German and Russian coverage from regression.

## [0.8.99] - 2026-07-26

### Added

- Released the first five-day Public Demonstration Preview for Windows x64.
- Added a self-contained MSI installer and portable ZIP package; no separate .NET or PowerShell installation is required.
- Added local ECU-log importing, saved-log organization, full-resolution analysis, channel comparison, customers, vehicles, injector-service workflows, reports, exports, backup, and restore.
- Added English, Spanish, German, and Russian interface and report support.
- Added an encrypted, demonstration-specific local database.
- Added visible Public Demonstration and not-for-production identification.
- Added safe viewing, export, backup, and restore access after the five-day evaluation expires.

### Changed

- The five-day evaluation begins after the first successfully saved real log import rather than at installation.
- The Public Demonstration uses a separate application-data location and does not open, move, modify, or package data from another Husky installation.
- A new Public Demonstration installation starts with zero logs, vehicles, customers, and work orders.

### Privacy and safety

- Processing and storage remain local to the computer.
- Husky does not automatically upload logs, customer information, diagnostics, reports, or usage data.
- Reports and exports created during the demonstration remain clearly identified as trial output.

### Fixed

- Prevented the Public Demonstration from inheriting development or private-preview access.
- Prevented a new public evaluator from being blocked by private-preview backup requirements before the first import.
- Prevented the Public Demonstration from opening data preserved by another Husky installation.

### Known limitations

- This is unsigned pre-release demonstration software, so Windows may display an unknown-publisher warning.
- It is not approved or intended for production shop use. Use copied logs and fictional or test customer information.
- German and Russian specialized automotive terminology still benefits from review by native-speaking performance professionals.
- Analysis and injector calculations are descriptive aids, not automatic diagnosis, pass/fail, tuning, or machine-control decisions.
- Independent clean-machine coverage, Windows 10 acceptance, code signing, legal review, and production-release approval remain incomplete.

[Unreleased]: https://github.com/Limited-Underground/Husky-Performance-Releases/compare/v0.9.1-public-demo...HEAD
[0.9.1]: https://github.com/Limited-Underground/Husky-Performance-Releases/releases/tag/v0.9.1-public-demo
[0.9.0]: https://github.com/Limited-Underground/Husky-Performance-Releases/releases/tag/v0.9.0-public-demo
[0.8.99]: https://github.com/Limited-Underground/Husky-Performance-Releases/releases/tag/v0.8.99-public-demo
