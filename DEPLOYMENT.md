# Deployment — ENG YOUSSEF 3.0

## النسخة المنشورة على GitHub Pages (ثابتة، 2026-11-03)

- الرابط: **https://exyn0717-debug.github.io/youssef-/**
- واجهة المحاضرة: `lecture.html?lecture=esd217-concept`،
  واختبار مراجعة العربية: `lecture.html?lecture=arb112-review`.
- النشر عبر **GitHub Actions**: `.github/workflows/pages.yml` يعمل عند كل push إلى
  `arena/e1f085f7-youssef` (أو يدويًا `workflow_dispatch`)، يضبط Pages بصلاحية
  `pages: write` ثم يرفع مجلد المستودع كاملًا كـ artifact وينشره عبر `deploy-pages`.
  الملف `.nojekyll` يمنع معالجة Jekyll، فتُقدَّم ملفات `content/` و`vendor/` و`assets/` كما هي.
- كل المسارات نسبية، فالموقع يعمل تحت `/youssef-/` بدون تعديل. النسخة الثابتة لا تحتاج
  خادم Python: الحسابات والمزامنة ومساعد Claude معطّلة تلقائيًا (`__STATIC_WEB__`).
- عند دمج العمل في `main`، حدّث `branches:` في سير العمل إلى `main` إذا أردت أن يبقى
  النشر تابعًا للفرع الافتراضي.
- لتحديث النشر: ادفع (push) إلى الفرع نفسه، فـ Actions يبني وينشر تلقائيًا.

## نسخة الخادم الكاملة (Python)

1. ثبّت المتطلبات وشغّل خلف HTTPS (nginx/Caddy). اضبط `METHOD_PUBLIC_ORIGIN` و`METHOD_ALLOWED_ORIGINS` على نطاقك العام، وإلا سترفض طلبات الدخول القادمة عبر الوكيل.
2. لتفعيل Claude اضبط `ANTHROPIC_API_KEY` و`CLAUDE_MODEL` (افتراضي `claude-sonnet-4-6`). راقب التكلفة في لوحة Anthropic.
3. وجّه الوكيل رؤوس `X-Forwarded-Proto` و`Host`. لـ SSE عطّل التخزين المؤقت للـ `/api/ai/chat` (`proxy_buffering off`).
4. البيانات في `METHOD_DATA_DIR` (افتراضي `./data`). احتفظ بنسخ احتياطية خارج الخادم.
5. Docker: ابنِ الصورة وشغّلها مع متغيرات البيئة ومجلد بيانات دائم.
6. بعد الترقية من 2.0 لا توجد بيانات اعتماد إدارة؛ الطلاب يستخدمون رمز الاستعادة أو يتواصلون مع صاحب الموقع.
