import unittest

from extract_title import extract_title

class TestTitleExtraction(unittest.TestCase):
    def test_markdown_test(self):
        md = """
# Heading 1

This is **bold** text and _italic_ text.

## Heading 2

Another paragraph with a [link](https://example.com)
        """
        node = extract_title(md)
        expected_result = ("Heading 1")
        self.assertEqual(node, expected_result)

    def test_markdown_test_2(self):
        md = """
---
title: Birthday Blog 🎂
date: 2025-08-08
draft: false
summary: Looking back and forward, planning where to go and appreciating how far I've come
tags:
  - life lessons
  - goals
---

# 🎯 Use what you have

If there’s one thing this year slapped into my head, it’s this — **you can do a lot with a little**.  
Doesn’t matter if life handed you the **worst possible card** — you can still grind your way up 🪜. Slowly, sure, but you’ll get there.  

---

I’ll be honest — I fell for the *“you can get it now”* trap.  
Not literally *today*, but that vibe you get when you look up to people like **Andrew Tate**, **Iman Gadzhi**, or whoever inspires you — that fast grind, flashy results energy.  

It’s seductive. It makes your brain think: *“Yeah, I’ll just work hard, move fast, and boom — done.”*  
**Reality check:** it is a lot harder than I thought 😅.  

---

When I started my journey earlier this year, I was *fired up*.  
And yeah, I got things moving — but man, it was way harder than I imagined.  

Halfway through, life basically told me to **chill**. Slow down.  
Handle things as they are. *(Also, my laptop died 💀)*  

Was it frustrating? Yes. Was it necessary? **Absolutely.**  
It forced me to breathe 🌬️ and figure out the *minimum viable way* to keep moving forward.  

---

Somewhere along the way, I started looking at life like a big board game 🎲 — zooming out, seeing the patterns from above 🪂.  
And honestly? That shift in perspective changed everything.  

So, here’s the real takeaway: **Slow down 🐌.**  
Constant, small effort >>> short bursts of obsession.  

If you can’t see a new habit becoming part of your actual everyday life — don’t even bother forcing it.  
Show up daily, even if it’s only for **5 minutes**.  

**Detach from the outcome. Give it 3 months. Then let the results speak for themselves.**

---

## 🚀 The next three months?

- **Touch typing** (writing this blog like this right now… and I suck 🤦🏽‍♂️)  
- **Backend development** — been at it for a month and a half, and I plan to finish.  
- **Revisit frontend development**, maybe dust off some **3D rendering**.  
- *Maybe* dip into **crypto** after that.  

But here’s the big one: I **promise** a **fully working Android app** before the end of the year 📱.  
It won’t be perfect — but by then, I’ll be in a rhythm where new projects drop every other week.  

Basics first. Always.  

And yeah… *Web too easy pffff…* just kidding 😏.  

---

## 🥂 Birthday toast to the journey

Here’s to **showing up** even when nobody’s clapping.  
Here’s to **failing, laughing, and trying again**.  
Here’s to the **next year being wilder and better than we can imagine**.  

And here’s to you — for being here, for caring, for chasing your own thing while I chase mine.  

**Happy Birthday to me — but cheers to *our* journey 🛤️.**
        """
        node = extract_title(md)
        expected_result = ("🎯 Use what you have")
        self.assertEqual(node, expected_result)

    def test_mutliple_headers(self):
        with open("/home/tradix/Projects/static-sitegenerator/src/blab.md", "r", encoding="utf-8") as f:
            content = f.read()

        node = extract_title(content)
        expected_result = ("🚀 The Hustler’s Dilemma")
                           # "🔥 My (Slightly Crazy) Dream",
                           # "🧠 Mindset Muscles",
                           # "⚔️ Life’s Contradictions",
                           # "🎤 Final Thoughts (For Now)")
        self.assertEqual(node, expected_result)

if __name__ == "__main__":
    unittest.main()
