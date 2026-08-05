---
hide:
  - navigation
  - toc
---

# skill-from-text

<p style="font-size: 1.25rem; max-width: 42rem;">
Turn any text or document into a structured, on-demand agent skill — named frameworks, decision rules, and anti-patterns. <strong>Structure, not a summary.</strong>
</p>

[Get started](guide.md){ .md-button .md-button--primary }
[Skill reference](skill-reference.md){ .md-button }
[GitHub](https://github.com/virgiliojr94/skill-from-text){ .md-button }

---

## Why skill-from-text

<div class="grid cards" markdown>

-   :material-file-document-multiple:{ .lg .middle } __Multi-format__

    ---

    PDF, EPUB, DOCX, HTML, Markdown, RTF, MOBI/AZW (via Calibre). Extraction runs
    locally with graceful stdlib fallbacks — no upload, no lock-in.

-   :material-brain:{ .lg .middle } __Structure, not summaries__

    ---

    Named frameworks, mental models, decision rules, and anti-patterns — the
    author's toolkit, captured with their exact terms, not a text report.

-   :material-flash:{ .lg .middle } __On-demand chapters__

    ---

    Per-chapter files load only when the topic is relevant, so a 200-page text
    costs tokens proportional to the question, not the page count.

-   :material-robot-happy:{ .lg .middle } __Multi-agent__

    ---

    One `SKILL.md` runs on Claude Code, GitHub Copilot CLI, and Amp through the
    open Agent Skills standard.

</div>

## Install

**As an agent skill** (gives you the `/skill-from-text` command in Claude Code, Copilot CLI, Amp):

```bash
git clone https://github.com/virgiliojr94/skill-from-text.git ~/.claude/skills/skill-from-text
# then, in your agent session:
/skill-from-text /path/to/text.pdf [skill-name]
```

**As a standalone CLI** (just the text extractor, optional):

```bash
pip install "skill-from-text[pdf,epub,docx]"
skill-from-text /path/to/text.pdf --mode text
```

## Learn more

<div class="grid cards" markdown>

-   :material-sitemap:{ .lg .middle } __[Architecture](ARCHITECTURE.md)__

    ---

    How the deterministic extractor and the spec-driven generator fit together.

-   :material-speedometer:{ .lg .middle } __[Performance](PERFORMANCE.md)__

    ---

    The measured Discovery Loop Tax and real per-conversion token cost.

-   :material-text-open-page-variant:{ .lg .middle } __[Skill Reference](skill-reference.md)__

    ---

    The full `SKILL.md` spec: every step, depth budget, and quality rule.

-   :material-heart:{ .lg .middle } __[Sponsor](https://github.com/sponsors/virgiliojr94)__

    ---

    skill-from-text is free and MIT. Sponsoring funds reviews, releases, and fixes.

</div>
