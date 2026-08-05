## 📥 Install

> **Two ways to use it, do not confuse them:**
> - **As an agent skill** (the `/skill-from-text` command in Claude Code, Copilot CLI, or Amp) → **`git clone` into your skills folder** (below). This is what gives you the slash command and the full convert-a-text flow.
> - **As a standalone CLI** (just the text extractor) → `pip install skill-from-text`, then `skill-from-text --help`. This does **not** register the agent skill; it only installs the extraction engine. See [the CLI section](#standalone-cli-pip).

The skill follows the open [Agent Skills](https://github.com/agentskills/agentskills) standard, so a single install works for any compatible host.

**GitHub Copilot CLI** (personal skill):

```bash
git clone https://github.com/virgiliojr94/skill-from-text.git ~/.copilot/skills/skill-from-text
# then, in a `copilot` session:
/skills reload
/skills info skill-from-text
```

Or the cross-agent path that Copilot CLI and Amp both discover:

```bash
git clone https://github.com/virgiliojr94/skill-from-text.git ~/.agents/skills/skill-from-text
```

**Claude Code**:

Copy this into your Claude Code session:

```
Install skill-from-text: https://raw.githubusercontent.com/virgiliojr94/skill-from-text/master/SKILL.md
```

Or manually using standard `git clone` (ensures modular engine files are fetched correctly):

```bash
git clone https://github.com/virgiliojr94/skill-from-text.git ~/.claude/skills/skill-from-text
```

Then in any agent session:

```bash
/skill-from-text ~/path/to/your-text.pdf
# or
/skill-from-text ~/path/to/your-text.epub
```

### Standalone CLI (pip)

`pip install skill-from-text` is a **separate, optional** path. It installs only the
text-extraction engine as a CLI, for scripting or to grab the optional extractors;
it does **not** register the `/skill-from-text` agent skill (use the `git clone` above
for that).

```bash
pip install "skill-from-text[pdf,epub,docx]"   # engine + optional extractors
skill-from-text ~/path/to/text.pdf --mode text  # or: python -m text_to_skill ...
skill-from-text --check                          # report which extractors are installed
```

---


---

[← Back to the README](../README.md)
