# Deployment — ENG YOUSSEF 3.0

## النشر على GitHub Pages — **منشور** (2026-11-03)

- الرابط: **https://exyn0717-debug.github.io/youssef-/**
- واجهة المحاضرة: `lecture.html?lecture=esd217-concept`،
  واختبار مراجعة العربية: `lecture.html?lecture=arb112-review`،
  والملف الأصلي: `content/library/arb112-review.html`.
- `has_pages: true`، و`build_type: workflow`، وآخر تشغيل لسير العمل `✓ success`
  («Configure Pages → Upload static site → Deploy → Reported success!»).
- **إعداد مطلوب مرة واحدة من صاحب المستودع (تم):** في
  https://github.com/exyn0717-debug/youssef-/settings/pages اختر
  **Build and deployment → Source: `GitHub Actions`**. إنشاء موقع Pages يحتاج صلاحية
  Admin ولا يملكها توكن التكامل ولا `GITHUB_TOKEN`، فلا تستخدم `enablement: true`
  في `configure-pages` (يفشل دائمًا بـ `Resource not accessible by integration`).
- سير العمل `.github/workflows/pages.yml` يعمل عند كل push إلى
  `main` أو يدويًا (`workflow_dispatch`)، ويرفع مجلد المستودع كاملًا
  كصفحات ثابتة عبر `upload-pages-artifact` + `deploy-pages`. إن لم يكن Pages مُفعّلًا،
  يتخطى النشر ويكتب رسالة واضحة بدل أن يفشل.
- السير لا يصرّح بـ `environment: github-pages`: سياسة الفروع الافتراضية لتلك البيئة تسمح
  بـ `main` فقط، ولا يملك توكن التكامل صلاحية تعديلها. النشر يتم مباشرة عبر
  `actions/deploy-pages` بصلاحية `pages: write`، فينشر الفرع الحالي بلا بوابة إضافية.
- الملف `.nojekyll` يمنع معالجة Jekyll، فتُقدَّم ملفات `content/` و`vendor/` و`assets/` كما هي.
- كل المسارات نسبية، فالموقع يعمل تحت `/youssef-/` بدون تعديل. النسخة الثابتة لا تحتاج
  خادم Python: الحسابات والمزامنة ومساعد Claude معطّلة تلقائيًا (`__STATIC_WEB__`).
- ملاحظة CDN: قد يبقى الرد القديم `There isn't a GitHub Pages site here` مخزّنًا مؤقتًا
  للمسار المجرّد `/youssef-/` لبضع دقائق بعد أول نشر؛ `/?v=1` أو `index.html?v=1` يعمل فورًا.
- **تم (2026-11-04):** صار `branches: [main]`، فأي push إلى `main` يعيد النشر تلقائيًا؛
  و`workflow_dispatch` من `main` يبقى متاحًا للتحديث اليدوي.

## نسخة الخادم الكاملة (Python)

1. ثبّت المتطلبات وشغّل خلف HTTPS (nginx/Caddy). اضبط `METHOD_PUBLIC_ORIGIN` و`METHOD_ALLOWED_ORIGINS` على نطاقك العام، وإلا سترفض طلبات الدخول القادمة عبر الوكيل.
2. لتفعيل Claude اضبط `ANTHROPIC_API_KEY` و`CLAUDE_MODEL` (افتراضي `claude-sonnet-4-6`). راقب التكلفة في لوحة Anthropic.
3. وجّه الوكيل رؤوس `X-Forwarded-Proto` و`Host`. لـ SSE عطّل التخزين المؤقت للـ `/api/ai/chat` (`proxy_buffering off`).
4. البيانات في `METHOD_DATA_DIR` (افتراضي `./data`). احتفظ بنسخ احتياطية خارج الخادم.
5. Docker: ابنِ الصورة وشغّلها مع متغيرات البيئة ومجلد بيانات دائم.
6. بعد الترقية من 2.0 لا توجد بيانات اعتماد إدارة؛ الطلاب يستخدمون رمز الاستعادة أو يتواصلون مع صاحب الموقع.
