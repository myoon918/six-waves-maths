# Six Waves Maths website: handoff for ChatGPT

Read this whole file before changing anything. Last updated 2026-11-18.

## Who you are working for

- Moses, a maths teacher in Sydney (NSW), is building the marketing site for his tutoring studio, **Six Waves Maths**.
- Reply to Moses in **Korean**. Do not end Korean sentences with a colon.
- Make **one change at a time**. When there is a choice, offer **at most 3 options** and mark one as recommended.
- Moses mostly looks at the site **on his phone**. Check every change at phone width (390px).

## Where the site lives

- Live site: https://myoon918.github.io/six-waves-maths/
- Repository (public): https://github.com/myoon918/six-waves-maths
- The whole site is **one file**: `index.html`. CSS, JavaScript and both languages are inside it.
- Raw file to read: https://raw.githubusercontent.com/myoon918/six-waves-maths/main/index.html
- `dark/index.html` and `mix/index.html` are only redirects to the main page. Do not edit them.
- `try/1/`, `try/2/`, `try/3/` are three preview pages for a pending decision (see below).
- Publishing: when a new `index.html` is committed to the `main` branch, GitHub Pages redeploys automatically in about a minute. Moses can do this on github.com: open `index.html`, press the pencil icon, paste the new file, and commit. Or use "Add file", "Upload files".

## How index.html is built

- **Languages.** Every piece of text appears twice: `<k>한국어</k><e>English</e>`. The language button switches `data-lang` on `<html>` (saved in localStorage key `6w-lang`). Any new text must have both `<k>` and `<e>`. Maths stays in English in the Korean version (for example `Solve 2x + 3 = 11.`).
- **Design.** "Alternating" design: dark navy base, and sections with `class="lt"` switch to white using CSS variables. Keep the alternation dark, white, dark, white. Fonts are Inter and Noto Sans KR. One accent colour (sky blue). No shadows.
- **Hero.** A canvas animation: six wave lines turn into particles that orbit and form a blue globe, then the word "succeed" (해내게) is written by particles and flashes. Moses tuned the timing over many rounds. **Do not change the hero animation unless Moses asks.**
- **Bridges.** Each section ends with a blue question line (`<a class="bridge">`). The next section's first line answers it, so parents keep scrolling. Keep this pattern when you add or move sections.
- **Section magnet.** A small script snaps the page to a section start when scrolling stops within 35% of the screen height of it. Long sections are not snapped mid-way.
- Diagrams are drawn in JavaScript (`week()` and `flow()`) or inline SVG.

## Current sections, in order

1. Hero: "We help your child succeed." with a cue line "How can anyone see an erased line?"
2. How we see it: homework daily on an iPad in pen, every stroke, pause and erased line is kept, read before the lesson. Two iPad mockups.
3. The next morning: automatic results message, wrong question returns with a fully worked solution and a similar question, then after 1, 3 and 7 days. Diagram of one wrong question.
4. Day seven, the lesson: 90 minutes, 1 to 4 students, short test, saved questions one-on-one, harder exam-style questions, weekly report. One-week diagram. Value line "Set a goal. Follow the plan. Let your child experience success."
5. One plan per child (`id="each"`): homework at each child's own pace, exam prep for each child's own school, plus four example student cards A to D.
6. Try a day: interactive. Write on a pad and replay the strokes, the next-morning message, the saved questions.
7. The teacher: 20 years in Australian high schools (including selective schools) and at university, father of three daughters.
8. Next-year readiness check: 12 questions, 20 minutes, free, green, amber or red. Only Year 7 to 8 is open.
9. FAQ: 10 questions.
10. Start: free 20-minute check, promise line, contact (DRAFT).

## Rules you must never break

- No real student names, faces, handwriting, records or school names. Every screen is a made-up example.
- No unproven claims: no pass rates, no grade improvement percentages, no testimonials.
- **No comparisons with other tutors or tuition centres**, even if it sounds stronger. Show what we do instead.
- Do not use the phrase "mixed class" (섞인 반). Parents find mixed groups worrying. Lead with "each child has their own plan".
- No job title like "current selective school teacher" (NSW Department of Education policy).
- Never write "Pattern Ladder" (still in testing).
- Past exam questions only after they are rewritten for copyright.
- Ask Moses first before: buying a domain or paid hosting, adding any form that collects parent details, publishing real names or photos.
- Anything not confirmed by Moses stays marked with `<span class="draftmark">DRAFT</span>`.

## Confirmed facts (you may state these)

- One 90-minute lesson a week, groups of 1 to 4.
- Homework every day on an iPad in pen. Every stroke, pause and erased line is kept, and the teacher reads it before the lesson.
- Homework runs at each child's own pace. School exam prep is done for each child separately.
- An automatic results message arrives the next morning.
- A wrong question comes back with a fully worked solution and one similar question, then again after 1, 3 and 7 days.
- Questions the child cannot do are saved and solved one-on-one in the lesson.
- If homework is not done, we follow up straight away.
- From 14 days before a school exam, homework switches to exam-style questions on that school's announced topics.
- Homework time: Years 7 to 9 about 30 to 45 minutes, Years 10 to 12 about 45 to 60 minutes.
- A short weekly report goes to parents after the lesson.
- Studio value: set a goal, follow the plan, experience success.

## Pending decision (handle this first)

Moses is choosing the wording for section 5 (one plan per child). The layout is the same, only the text differs.

- Option 1 https://myoon918.github.io/six-waves-maths/try/1/ Parent's view. "우리 아이만의 숙제, 우리 아이 학교의 시험."
- Option 2 https://myoon918.github.io/six-waves-maths/try/2/ What the teacher does (recommended). "매일, 아이 한 명씩 계획을 다시 짭니다." Before using it, confirm with Moses whether he picks each next homework set himself after reading the working, or whether it follows a fixed sequence. If it is a fixed sequence, reword it.
- Option 3 https://myoon918.github.io/six-waves-maths/try/3/ Shortest. "한 그룹, 네 개의 계획."

When he chooses, copy that option's section 5 text into `index.html` (the block that starts with `<!-- 4b 아이마다 따로 -->`), then the `try/` folder can be deleted.

## Still needed from Moses (keep as DRAFT until he answers)

- Who gets the next-morning message, the student or the parent
- Whether "Years 7 to 12" can be stated, and which Year 11 to 12 courses
- Fees, payment, sibling discount
- Address, days and times, in person or online, lesson language
- Which pen, and options without an iPad
- Trial lesson, make-ups, starting mid-term, notice to stop
- How groups are formed
- Contact method, real name and photo

## How to hand back a change

1. Give Moses the **complete new `index.html`** (not a fragment) as a downloadable file, so he can paste or upload it on GitHub.
2. Tell him in one or two Korean sentences what changed and where to look on the phone.
3. Keep `<k>` and `<e>` in sync for every text change.
