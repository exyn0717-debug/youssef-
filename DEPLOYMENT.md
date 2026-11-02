# Deployment — ENG YOUSSEF 3.0

1. ثبّت المتطلبات وشغّل خلف HTTPS (nginx/Caddy). اضبط `METHOD_PUBLIC_ORIGIN` و`METHOD_ALLOWED_ORIGINS` على نطاقك العام، وإلا سترفض طلبات الدخول القادمة عبر الوكيل.
2. لتفعيل Claude اضبط `ANTHROPIC_API_KEY` و`CLAUDE_MODEL` (افتراضي `claude-sonnet-4-6`). راقب التكلفة في لوحة Anthropic.
3. وجّه الوكيل رؤوس `X-Forwarded-Proto` و`Host`. لـ SSE عطّل التخزين المؤقت للـ `/api/ai/chat` (`proxy_buffering off`).
4. البيانات في `METHOD_DATA_DIR` (افتراضي `./data`). احتفظ بنسخ احتياطية خارج الخادم.
5. Docker: ابنِ الصورة وشغّلها مع متغيرات البيئة ومجلد بيانات دائم.
6. بعد الترقية من 2.0 لا توجد بيانات اعتماد إدارة؛ الطلاب يستخدمون رمز الاستعادة أو يتواصلون مع صاحب الموقع.
