#!/usr/bin/env python3
"""تبدیل docs/*.md به latex/*.tex با pandoc.
   اجرا از ریشهٔ مخزن:  python3 latex/build_tex.py
   فایل‌های .md منبع اصلی‌اند؛ فایل‌های .tex را دستی ویرایش نکنید."""
import pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent

DOCS = [
    # (منبع، خروجی، عنوان، زیرعنوان، سربرگ)
    ("docs/01-vision.md", "latex/01-vision.tex",
     "سند چشم‌انداز", "پروژهٔ کلاس‌یار", "سند چشم‌انداز — کلاس‌یار"),
    ("docs/02-requirements/personas.md", "latex/personas.tex",
     "سند پرسوناها", "پروژهٔ کلاس‌یار", "سند پرسوناها — کلاس‌یار"),
    ("docs/02-requirements/user-stories.md", "latex/user-stories.tex",
     "داستان‌های کاربر", "پروژهٔ کلاس‌یار", "داستان‌های کاربر — کلاس‌یار"),
    ("docs/03-design/architecture.md", "latex/architecture.tex",
     "سند معماری", "پروژهٔ کلاس‌یار", "سند معماری — کلاس‌یار"),
]

# صفحهٔ عنوان بدون tabular: \maketitle با xepersian در LaTeX جدید خطا می‌دهد
HEAD = r"""\documentclass[12pt, a4paper]{article}
\input{preamble}
\fancyhead[R]{\small %(header)s}
\fancyhead[L]{\small نسخهٔ \lr{۱.۰}}

\begin{document}

\begin{titlepage}
\centering
\vspace*{3cm}
{\Huge\bfseries %(title)s\par}
\vspace{0.5cm}
{\LARGE\bfseries %(subtitle)s\par}
\vspace{0.5cm}
{\large پلتفرم اشتراک جزوه، نمونه‌سؤال و ارزیابی استادان\par}
\vspace{2cm}
{\large تهیه‌کنندگان:\par}
{\large مریم قندی زنجانی، ملیکا شهبازی، آنیسا فروغمند، مائده رضایی، محمدمهدی ذوالقدر\par}
\vspace{0.5cm}
{\large دانشگاه آزاد زنجان\par}
\vspace{1cm}
{\large ۱۴۰۵/۰۷/۱۱\par}
\end{titlepage}

\tableofcontents
\newpage

"""
TAIL = "\n\\end{document}\n"

NUM = re.compile(r"^(#+)\s+[۰-۹0-9]+(?:\.[۰-۹0-9]+)*\.?\s+")

def prepare(md: str) -> str:
    lines = md.split("\n")[1:]                       # حذف عنوان H1 (روی صفحهٔ عنوان می‌آید)
    out = []
    for ln in lines:
        ln = NUM.sub(r"\1 ", ln)                     # شماره‌گذاری را LaTeX می‌دهد
        out.append(ln)
    text = "\n".join(out)
    return text.replace("🔴 ", "").replace("🟡 ", "")  # فونت وزیرمتن شکلک ندارد

def finish(tex: str) -> str:
    tex = tex.replace("---", "—").replace("--", "–")   # خط تیرهٔ یونیکد
    # بلوک‌های کد (نمودار، JSON) باید چپ‌به‌راست چاپ شوند
    tex = tex.replace("\\begin{verbatim}", "\\begin{LTR}\n\\begin{verbatim}")
    tex = tex.replace("\\end{verbatim}", "\\end{verbatim}\n\\end{LTR}")
    # شمارهٔ نسخه مثل ۱.۱ در متن فارسی برعکس نشود
    tex = re.sub(r"(?<![\\\w{])([۰-۹]+\.[۰-۹]+)", r"\\lr{\1}", tex)
    # پیوست‌ها بدون شماره ولی در فهرست مطالب
    return re.sub(
        r"\\section\{(پیوست[^}]*)\}",
        r"\\section*{\1}\\addcontentsline{toc}{section}{\1}", tex)

for src, dst, title, sub, header in DOCS:
    md = (ROOT / src).read_text(encoding="utf-8")
    body = subprocess.run(
        ["pandoc", "-f", "markdown-smart-auto_identifiers", "-t", "latex",
         "--wrap=preserve", "--columns=50", "--shift-heading-level-by=-1",
         "--no-highlight"],
                input=prepare(md), capture_output=True, text=True,
        encoding="utf-8", check=True).stdout
    (ROOT / dst).write_text(
        HEAD % dict(title=title, subtitle=sub, header=header) + finish(body) + TAIL,
        encoding="utf-8")
    print("wrote", dst)
