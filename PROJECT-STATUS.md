# Husky Performance by Limited Underground — Project Status

_Last updated: August 13, 2026_

This page is the plain-language source of truth for what people can download today, what is being validated, and what remains before a production release.

Husky Performance is proprietary, pre-release Windows software for professional automotive performance shops. It is under active development and is not yet approved for production shop use.

**Public-release hold:** Version 0.9.1 remains the current preview. No later public preview will be published until an established automotive business completes meaningful workflow testing, provides substantive feedback, and the owner reviews that feedback.

## Quick links

- [Download Husky Performance 0.9.1 Public Demonstration Preview](https://github.com/Limited-Underground/Husky-Performance-Releases/releases/tag/v0.9.1-public-demo)
- [Read the detailed public changelog](CHANGELOG.md)
- [Learn about becoming a testing partner](TESTING-PARTNERS.md)
- [Follow Husky Performance on Facebook](https://www.facebook.com/HuskyPerformanceApp)

## Currently Available

### Husky Performance 0.9.1 Public Demonstration Preview

The current public release is an unsigned five-day Windows x64 evaluation. The evaluation begins with the first successfully saved real log, not when the application is installed. After expiration, existing information remains available for safe viewing, export, backup, and restore.

Version 0.9.1 includes:

- Local ECU-log import, bulk review, source provenance, and saved-log organization
- Full-resolution exact-sample analysis and compatible two-log comparison
- Operator-reviewed customer session and comparison reports with bounded, reusable layouts
- Customer, vehicle, work-order, workflow, board, and privacy-safe history records
- Exact-original Tune Library storage, lineage, review history, relationships, and protected export
- Injector Service intake, association, reporting, and signed request/results exchange workflows
- Complete and configuration/records backup, verified recovery review, and Recovery & Rollback
- Fixed non-scrolling Dashboard plus current keyboard, screen-reader, enlarged-text, and scrollbar corrections
- English, Spanish, German, and Russian interface/report support
- Local encrypted demonstration storage with no automatic telemetry or uploads
- Complete removal of Simulator from the product and package

Use copied logs and fictional or test customer information only. Windows may show an unknown-publisher warning because the preview is not code-signed.

The release page contains exactly one MSI, one compact ZIP, and one checksum sidecar. The compact ZIP SHA-256 is:

`F705A83F8E84B7E5EB8A645449DD782879F8CD12129EC948B82324947E0A26DC`

## In Progress

Development continues on practical professional value rather than visual simulation:

- External Windows 10 and independent clean-machine/shop acceptance for the published trial
- Usability feedback from established performance and injector-service businesses
- Log review, comparison, exact-data analysis, and customer-designed reporting
- Customer, vehicle, work-order, Tune Library, and Injector Service workflows
- Backup, restore, recovery, security, accessibility, and performance evidence
- Read-only Data Library health, storage-accounting, and backup-recovery tools completed after 0.9.1 and still undergoing private validation
- Evidence-backed Dashboard states that distinguish ready, empty, review, and unavailable conditions without unconditional success claims
- An evidence-backed Active Work card that remains neutral for an empty queue, informational for routine active work, and warns only when exact waiting, overdue, due-today, quality-check, or ready-for-pickup counts require attention
- Direct, navigation-only Dashboard launch points from Saved Logs, Vehicles, and Customers counts to their complete authoritative lists, with no record changes and no loss of the fixed non-scrolling layout
- Option-aware Settings search that routes common names such as language, retention, and security mode to the correct category, supports multilingual keywords, and shows an accessible empty state instead of leaving a stale settings panel visible
- Honest staged General & Appearance choices with an accessible pending-change state, an advance language-restart warning, and a discard action that restores the saved theme, text size, and language without applying or saving anything
- A review-first General & Appearance **Restore defaults for this page** action that stages Dark, Standard text, and Windows language without applying, saving, or restarting; **Save Settings** remains explicit and Discard restores the prior saved choices
- Review-first Injector Service defaults that stage the current shop identity, both send/provide workflows, and privacy-safe vehicle information without writing preference files; accessible saved/pending/defaults-review states and Discard keep Save explicit
- Review-first Backup & Restore retention defaults that stage the conservative disabled / 14 daily / 8 weekly / 12 monthly / default Backups-folder baseline without creating, verifying, restoring, cleaning up, or deleting a backup; accessible saved/pending/review-required/defaults-review states and Discard keep Save explicit
- Review-first Reports & Branding defaults that stage standard Husky branding—empty shop fields, Husky blue `#00A6C7`, and no shop logo—while permanent Husky provenance remains; accessible saved/pending/review-required/defaults-review states and full-profile Discard keep Save explicit
- An exact latest-log Analysis handoff that remains disabled until a real graphable preview loads, then opens that same saved log in the existing channel-selection workflow
- A selection-gated Recent Activity handoff that opens the exact selected saved log in Analysis, stays disabled without a current loaded row, and refuses stale rows after a refresh failure
- A selection-gated Latest Imports handoff that opens the exact selected imported-log record in Saved Logs, clears stale narrowing filters, and refuses stale or missing records
- A snapshot-gated Active Work handoff that remains disabled during checking, empty, and refresh-failure states, then opens the complete Jobs / Work Orders list without changing any record automatically
- Guided external-test coverage for the current eleven core workflows
- Production licensing, Owner/team administration, publisher identity, code signing, privacy, and legal review

Passing local or packaged checks do not by themselves make Husky production-ready. The public trial does not waive the independent, legal, signing, licensing, or production-acceptance gates.

## Potential Next Trial Release

Work after 0.9.1 remains limited to validated corrections and explicitly approved workflow improvements recorded under [Unreleased](CHANGELOG.md).

There is no authorized next public trial today. The qualified-business feedback gate must be satisfied first; only then can an exact candidate, safety text, package, installer lifecycle, and owner publication decision be evaluated. Simulator is not current or planned product scope.

## Roadmap

### Nearer-term priorities

- Gather useful feedback from qualified gasoline, diesel, dyno, and injector-service shops
- Expand practical log analysis, comparison, and reporting workflows
- Strengthen customer, vehicle, work-order, Tune Library, and chronological history workflows
- Continue Injector Service intake, testing, exchange, analysis, and customer reporting
- Complete external Windows, backup/recovery, security, accessibility, and performance evidence

### Required before a paid production release

- Production licensing and enforceable Owner/team administration
- Trusted Windows code signing and publisher identity
- Privacy, terms, disclaimers, and legal review
- Clean-machine and supported-Windows acceptance
- Independent shop testing and owner production acceptance
- Final production package and installer approval

### Longer-term possibilities

These are possibilities rather than promises and are outside the immediate release path:

- Optional hybrid or multi-computer synchronization
- Multi-location shop operations
- Customer portals, scheduling, and remote dashboards
- Public plug-in capabilities
- Evidence-bounded AI-assisted interpretation
- Read-only calibration context tools

Calibration writing or automatic tune changes are not part of the current approved product scope.

## How status is reported

- **Currently Available** means included in the public download linked above.
- **In Progress** means implemented or actively being refined in private development; it is not necessarily downloadable yet.
- **Potential Next Trial Release** means candidate scope that still requires a separate release decision.
- **Roadmap** means intended direction or possible future work, not a delivery promise.

The [public changelog](CHANGELOG.md) records released changes and work completed after the current preview.
