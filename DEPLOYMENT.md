# Deployment — ENG YOUSSEF 3.0

## النشر على GitHub Pages (جاهز — خطوة واحدة من صاحب المستودع، 2026-11-03)

- الرابط بعد التفعيل: **https://exyn0717-debug.github.io/youssef-/**
- واجهة المحاضرة: `lecture.html?lecture=esd217-concept`،
  واختبار مراجعة العربية: `lecture.html?lecture=arb112-review`.
- **الخطوة المطلوبة مرة واحدة (تحتاج صلاحية Admin، لا يملكها توكن التكامل ولا `GITHUB_TOKEN`):**
  افتح https://github.com/exyn0717-debug/youssef-/settings/pages ثم
  **Build and deployment → Source: `GitHub Actions`**. بعدها أعد تشغيل سير العمل
  (أو ادفع أي تغيير) وينشر الموقع تلقائيًا.
- سير العمل `.github/workflows/pages.yml` يعمل عند كل push إلى
  `arena/e1f085f7-youssef` أو يدويًا (`workflow_dispatch`)، ويرفع مجلد المستودع كاملًا
  كصفحات ثابتة عبر `upload-pages-artifact` + `deploy-pages`. إن لم يكن Pages مُفعّلًا،
  يتخطى النشر ويكتب رسالة واضحة بدل أن يفشل.
- لا تستخدم `enablement: true` في `configure-pages`: إنشاء موقع Pages يحتاج صلاحية
  إدارة المستودع، ويفشل دائمًا بـ `Resource not accessible by integration` من أي توكن CI.
- الملف `.nojekyll` يمنع معالجة Jekyll، فتُقدَّم ملفات `content/` و`vendor/` و`assets/` كما هي.
- كل المسارات نسبية، فالموقع يعمل تحت `/youssef-/` بدون تعديل. النسخة الثابتة لا تحتاج
  خادم Python: الحسابات والمزامنة ومساعد Claude معطّلة تلقائيًا (`__STATIC_WEB__`).
- عند دمج العمل في `main`، حدّث `branches:` في سير العمل إلى `main` إن أردت أن يبقى
  النشر تابعًا للفرع الافتراضي.

## نسخة الخادم الكاملة (Python)

1. ثبّت المتطلبات وشغّل خلف HTTPS (nginx/Caddy). اضبط `METHOD_PUBLIC_ORIGIN` و`METHOD_ALLOWED_ORIGINS` على نطاقك العام، وإلا سترفض طلبات الدخول القادمة عبر الوكيل.
2. لتفعيل Claude اضبط `ANTHROPIC_API_KEY` و`CLAUDE_MODEL` (افتراضي `claude-sonnet-4-6`). راقب التكلفة في لوحة Anthropic.
3. وجّه الوكيل رؤوس `X-Forwarded-Proto` و`Host`. لـ SSE عطّل التخزين المؤقت للـ `/api/ai/chat` (`proxy_buffering off`).
4. البيانات في `METHOD_DATA_DIR` (افتراضي `./data`). احتفظ بنسخ احتياطية خارج الخادم.
5. Docker: ابنِ الصورة وشغّلها مع متغيرات البيئة ومجلد بيانات دائم.
6. بعد الترقية من 2.0 لا توجد بيانات اعتماد إدارة؛ الطلاب يستخدمون رمز الاستعادة أو يتواصلون مع صاحب الموقع.
