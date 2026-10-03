# ClassYar — کلاس‌یار

پروژهٔ درس مهندسی نرم‌افزار

پلتفرم وب دانشجویی برای اشتراک جزوه و نمونه‌سؤال، جست‌وجو بر پایهٔ **استاد، استان و واحد دانشگاهی**،
امتیازدهی به جزوه و استاد، نظرها و لینک گروه‌های کلاسی. استادان می‌توانند جزوه‌ها را تأیید کنند
و برای دانشجویان فعال نمرهٔ تشویقی ثبت کنند.

**وضعیت:** فاز مستندسازی (Sprint 0) — کد در Sprint 1 شروع می‌شود.

## تیم

| نام | نقش در Sprint 1 |
|-----|------------------|
| [مریم قندی زنجانی] | Product Owner |
| [ملیکا شهبازی ] | Scrum Master |
| [مائده رضایی ، آنیسا فروغمند ] | Developer |
| [ محمدمهدی ذوالقدر] | Tester |

نقش‌ها هر Sprint می‌چرخند.

## ساختار مخزن

```
docs/                       مستندات
  01-vision.md              سند چشم‌انداز
  02-requirements/
    personas.md             پرسوناها
    user-stories.md         ۱۰ داستان کاربر اولیه
latex/                      نسخهٔ LaTeX اسناد (PDF در latex/output)
slides/session-01/          اسلایدهای معرفی پروژه (Marp)
templates/                  قالب‌های رسمی درس
```

فهرست کامل مستندات: [docs/README.md](docs/README.md)

## فناوری

Node.js + Express، React، PostgreSQL، Prisma، GitHub Actions. دلیل انتخاب در بخش ۸.۲ سند چشم‌انداز آمده است.

## ساخت PDF از اسناد

نیاز: XeLaTeX، بستهٔ `xepersian` و فونت Vazirmatn.

```bash
python latex/build_tex.py          # تبدیل docs/*.md به latex/*.tex (نیازمند pandoc)
cd latex
xelatex -output-directory=output 01-vision.tex
xelatex -output-directory=output 01-vision.tex
```

## شفافیت دربارهٔ استفاده از هوش مصنوعی

طبق قوانین درس، استفاده از AI مجاز و مشروط به شفافیت است. پیش‌نویس اولیهٔ اسناد این مخزن با کمک
Claude (Anthropic) نوشته شده و سپس توسط تیم بازبینی و اصلاح شده است.

## مشارکت

شاخه‌بندی و قالب کامیت: [CONTRIBUTING.md](CONTRIBUTING.md)

## مجوز

[MIT](LICENSE)
