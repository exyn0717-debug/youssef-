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

## 2026-11-03 — واجهة المحاضرة + مراجعة ARB112 (ويب ثابت)

تحقّق في بيئة jsdom + خادم محلي (بدون متصفح حقيقي):

- `node --check app.js` و`node --check` لسكربت `lecture.html`: ناجح.
- 37 محاضرة × شكل واحد: الأقسام الخمسة موجودة في كل محاضرة، صفر أخطاء تشغيل.
- تبديل اللغة: نصوص الواجهة تتغيّر واتجاه الصفحة يتبدّل، **وعناوين المواد وبطاقات
  الملخص والأسئلة وأسماء الملفات تبقى بلغتها الأصلية** في `lecture.html` و`app.js`.
- الاستيراد: 17 مادة / 37 محاضرة / 253 سؤالًا / 33 ملفًا. بنك ARB112 يعرض 55 سؤالًا،
  أولها وآخرها مطابقان للملف المرفق، وفهارس الإجابات الصحيحة كلها داخل نطاق الخيارات.
- `content/library/arb112-review.html` مطابق بايت-ببايت للمرفق (SHA-256 مطابق)، وروابطه
  تعمل عبر HTTP (200)، وكذلك `lecture.html?lecture=arb112-review`.
- صفر أخطاء JS، صفر رسائل `console.error`، وحفظ اللغة/الملاحظات في `method.v2.local` يعمل.
- غير متحقق منه بصريًا: لا يوجد متصفح/Playwright في البيئة؛ التنسيق مُختبَر عبر DOM و`app.css` فقط.

## 2026-11-04 — «ابدأ المحاضرة» يفتح الواجهة الجديدة مباشرة

التغيير: كل الروابط التي تفتح محاضرة داخل المنصة صارت تذهب إلى
`lecture.html?lecture=<id>` عبر الدالة `lectureHref()` في `app.js`
(الرئيسية: «المحاضرة المقترحة» و«إلى المحاضرة»؛ صفوف المواد: «ابدأ المحاضرة»/«مراجعة»؛
نتائج البحث من نوع محاضرة؛ السابق/التالي في القارئ). التكليفات مستثناة فتبقى على
`#/lecture/<id>` لمعاينة PDF ونموذج الإجابة. الكاش `app.js?v=3.5.7`.

- `node --check app.js` ناجح.
- jsdom: 21 تأكيدًا على المنصة — روابط الرئيسية وصفوف ESD217 ونتائج البحث والقارئ كلها
  تشير إلى `lecture.html`، والتكليفات (3) تبقى على القارئ، وتبديل لغة الواجهة يبقي
  المحتوى بلغته الأصلية، وصفر أخطاء تشغيل.
- jsdom: 11 تأكيدًا على `lecture.html` — الأقسام الخمسة، 37 محاضرة في المنتقي،
  اختبار ARB112 بـ55 سؤالًا، الملف الأصلي، وصفر أخطاء تشغيل.
- خادم محلي: `/` و`index.html` و`app.js?v=3.5.7` و`lecture.html?...` والملف الأصلي → 200.
