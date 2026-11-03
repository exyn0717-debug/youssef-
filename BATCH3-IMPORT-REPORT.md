# تقرير الدفعة الثالثة — 2026-11-03

## الخلاصة
- المستلم: 19 ملف PDF.
- الملفات الجديدة التي تحتاج نشرًا: **صفر** — كل ملف في هذه الدفعة منشور أصلًا على GitHub وفي الموقع.
- مكرر تمامًا (نفس البايتات) مع ملف منشور: 8 ملفات.
- مكرر بنفس المحتوى مع اختلاف بايتات ملف PDF: 3 ملفات.
- مكرر داخل الدفعة نفسها: 8 ملفات (أسماء مختلفة، نفس البايتات).

طريقة التحقق: SHA-256 لكل ملف، ثم استخراج النص الداخلي وعدد الصفحات لكل ملف اختلفت بايتاته، ثم مقارنة النص بعد التطبيع (IMPORT-POLICY بند 1 و3 و4).

## جدول المطابقة: كل ملف مُرفَق ← مكانه المنشور
| الملف المُرفَق | الحالة | المكان المنشور |
|---|---|---|
| `tutorial 3.pdf` | مطابق بالبايتات | `content/library/mat121-tutorial-3-chapter1.pdf` |
| `Assignment_1.pdf` | مطابق بالبايتات | `content/library/mat121-assignment-1.pdf` |
| `Assignment_1 model answer..pdf` | مطابق بالبايتات | `content/library/mat121-assignment-1-model-answer.pdf` |
| `Assignment 2.pdf` | مطابق بالبايتات | `content/library/mat121-assignment-2-6.pdf` |
| `Assignment 2 model answer.pdf` | مطابق بالبايتات | `content/library/mat121-assignment-2-model-answer.pdf` |
| `Assignment 3.pdf` | مطابق بالبايتات | `content/library/mat121-assignment-3-5.pdf` |
| `Hook's Law Experiment.pdf` | مطابق بالبايتات | `content/library/phy111-exp-1-hookes-law.pdf` |
| `lec4 Math1.pdf` | مطابق بالبايتات | `content/library/mat111-lecture-4-limits-continuity.pdf` |
| `lec1 Math1.pdf` | نفس المحتوى (25 صفحة، نص متطابق) | `content/library/mat111-lecture-1-intro.pdf` |
| `lec2 Math1.pdf` | نفس المحتوى (16 صفحة، نص متطابق) | `content/library/mat111-lecture-2-functions.pdf` |
| `EXP.2 Simple Pendulum.pdf` | نفس المحتوى (6 صفحات، نص متطابق) | `content/library/phy111-exp-2-pendulum.pdf` |

## المكرر داخل الدفعة (لم يُضف)
- `Assignment_1 1.pdf` و`Assignment_1 2.pdf` و`Assignment_1 3.pdf` = `Assignment_1.pdf`.
- `Assignment_1 model answer. 1.pdf` = `Assignment_1 model answer..pdf`.
- `Assignment 2 model answer 1.pdf` و`Assignment 2 model answer 2.pdf` = `Assignment 2 model answer.pdf`.
- `Assignment 6.pdf` = `Assignment 2.pdf`.
- `Assignment 5.pdf` = `Assignment 3.pdf`.

## الفرق الحقيقي في الموقع — وتم إصلاحه في هذه الدفعة
عند فحص كل محاضرة منشورة مقابل ملفاتها، ظهر أن **7 محاضرات في ESD217** كانت منشورة بمحتوى نصي كامل لكن بلا أي ملف PDF مرتبط بها، فكانت صفحتها تظهر بدون قسم «ملفات المحاضرة»:

المناخ مقابل الطقس · طبقات الغلاف الجوي · الشعاب المرجانية والمحيطات · تغيّر المناخ على مر السنين · أسباب تغيّر المناخ · النظام المناخي · مؤشرات المناخ

السبب: المحاضرات 1–8 كلها موجودة داخل ملف واحد `esd217-part1-2026.pdf` (153 صفحة)، وقد تم التحقق من ذلك من فهرس الملف نفسه في صفحته الثانية:

> Lectures schedule of Part 1 — Climate Change Concept / Climate vs. Weather / Atmosphere layers / Coral reef bleaching / Climate change over years / Climate change causes / Climate System / Climate indicators

الإصلاح (بدون نسخ ملفات ولا اختراع محتوى):
- أُضيف الحقل `related_file_ids` للمحاضرات السبع في بيانات الموقع، ويشير إلى ملف الجزء الأول المنشور أصلًا.
- `app.js`: دالة `lectureFiles()` تُرجِع ملفات المحاضرة الخاصة ثم الملف الكامل المرتبط، مع وسم `related`، ووسم ظاهر في الواجهة يوضّح للمستخدم أن هذا **ملف الجزء الأول كاملًا وليس ملفًا منفصلًا للمحاضرة**.
- ترقية كاش الأصول إلى `app.js?v=3.5.1`.

النتيجة: كل محاضرة منشورة (32 محاضرة) أصبح لها الآن ملف واحد على الأقل. لم تُضف أي نسخة مكررة للـ PDF ولم يتغيّر عدد الملفات (28) ولا عدّادات الملفات في تبويب «الملفات».

## فجوات حقيقية لم تُعالج (لا يوجد ملف لها أصلًا)
هذه ليست ناقصة بسبب الاستيراد، بل لأن الملف لم يُرفَع بعد:
- **MAT111**: المحاضرة 3 غير موجودة (الموجود 1 و2 و4 و5 + ملاحظتان مباشرتان).
- **MAT121**: ورقتا مسائل Tutorial 1 وTutorial 2 غير مرفوعتين (الموجود Tutorial 3 فقط).
- **PHY111**: توجد محاضرة واحدة (`Lect__3.pdf` — حركة بتسارع ثابت) وتجربتان؛ باقي محاضرات المقرر وتجاربه غير مرفوعة.
- **CSE013**: 3 محاضرات + ملف أنظمة العد.
- **ESD217**: المحاضرات 2–8 موجودة نصيًا ومصدرها ملف الجزء الأول، وليست ملفات منفصلة. الجزء الثاني من المقرر غير مرفوع.

## تحقق
- `index.html` JSON صالح: 17 مادة، 32 محاضرة، 198 سؤالًا، 28 ملفًا.
- كل مسارات `content/library/*` المرجعية موجودة على القرص (28/28) وبأحجام مطابقة للبيانات.
- `node --check app.js` ناجح، واختبار منطق `lectureFiles()` على البيانات الفعلية: 32/32 محاضرة لها ملف، وصفر محاضرة فارغة.
