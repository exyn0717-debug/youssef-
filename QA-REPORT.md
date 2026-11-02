# QA Report — ENG YOUSSEF 3.3 (2026-11-02)

## Passed
- Backend: 10 branding/platform tests + 5 student/AI tests passed (separate runs).
- Batch 2: 20 PDFs received; 8 new public files added, 8 exact duplicates skipped, 3 same-content duplicates skipped, 1 certificate kept private.
- MAT121 assignments appear in a dedicated Assignments tab, separate from lectures; model answers are attached as uploaded.
- PHY111 includes Hooke’s Law experiment; MAT111 includes Lecture 4 Limits/Continuity and Lecture 5 Basic Derivatives.
- Browser live: home stats 17/28/198, assignments tab 3 items, assignment PDF preview 1/3, MAT111 derivatives PDF preview 1/13, mobile no horizontal overflow, zero JS errors.
- Static GitHub edition: same assignment organization and PDF preview, zero API requests and zero JS errors.
- Offline 3.3: home stats 17/28/198, assignment PDF preview works, zero network requests and zero JS errors.
- `/api/health` returns version 3.3.0.
- No `/api/admin` routes; legacy admin rows/sessions removed on startup.
- Student registration/recovery and Claude unconfigured behavior remain covered by tests. Live Claude response NOT verified because no `ANTHROPIC_API_KEY` is configured.
- Sensitive/file-like paths return 404; security headers present.

## Not verified / limitations
- Live Claude API call (no key). Configure `ANTHROPIC_API_KEY` and `CLAUDE_MODEL` on the server to enable.
- LMS/SIS protected pages remain unreachable; official links only, no invented deadlines.
- Scanned/handwritten PDFs are preserved as original files; no OCR or invented summaries.
- Assignment model answers are preserved as uploaded; open-ended assignment questions were not converted into invented multiple-choice questions.
- Coursera certificate containing a full name is private and excluded from public GitHub/static packages.
- Docker build not executed in this environment.
