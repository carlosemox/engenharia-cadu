**PASS — bounded local release review. No concrete blockers found.** No edits or commits. All 80 monitored files remained unchanged between hash checks.

- Third parties: 2,566 metadata records; no definitions republished; candidate states remain explicitly not homologated.
- Safety: escaped HTML, text-only DOM rendering, HTTPS GitHub client links, relative metadata fetch under same-origin CSP.
- Behavior: paging, combined filters, reset, empty/error states passed.
- Downloads/navigation: filenames, localized routes, portable Markdown links and generated parity passed.
- Translations: all 20 preserve permission limits.
- Styling: reuses `factory.css`; responsive rules inspected.

Validation: **9 library tests + 10 read-only story tests passed**; validator passed **2,558 local links**. Browser rendering, actual download behavior and deployed fetch/CSP: **NOT_RUN**, reserved for post-deploy browser review.

SHA-256:

| Scope | Hash |
|---|---|
| Generator | `549843c8655ebab799326d4c1d8d9ae4f48422ba9c5eb55f9143d105ee9f996f` |
| Client JS | `679b33fb99fe5a9b88621c69d9a73b47c5fb0f56529d077bbc2e3706330a814d` |
| Library CSS | `2b1d462927c810a394a2b56c7842d071085bd79d23a8ae31bc4614d921b28370` |
| Metadata | `5c831913dfe03a7a19d7d5a93f856c01fcab193984ac50cb88846b2b614a844a` |
| 20 translations manifest | `ae4e88e84309b2d2f8eb0b7dc09816b565b5e56c7c0a65978547ab56c58c8dba` |
| 35 generated library files manifest | `c3bf5ab80934b10ab7e4d6488b4e7ed2f0de5101d84391cf31c819720f8643c4` |

Manifest hashes use sorted repository-relative paths, each line formatted `SHA256␠␠path\n`. Approval applies to this working-tree snapshot, not subsequent changes.