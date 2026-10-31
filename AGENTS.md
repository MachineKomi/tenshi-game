# Agent Operating Rules — Tenshi Game

Applies to **Codex CLI** and any coding agents working in this repository. Claude Code also reads `CLAUDE.md`.

---

## 1. Read order

Before changing anything, read in this order:
1. `INTENT.md`
2. `GAME_DESIGN_DOCUMENT.md`
3. `docs/VISUAL_OVERVIEW.md`
4. `docs/LEARNING_JOURNEY.md`
5. `docs/HUMAN_IDEA_2026-10-31.md`

Later human decisions override earlier ideas.

---

## 2. Current locked project decisions

Treat these as **approved** unless a human changes them:
- first world = **Ancient Rome**
- first creature = **Mermaid**
- engine = **Godot 4**
- game structure = **explore → recruit → rhythm → battle**
- first scope = **extremely small vertical slice**
- happy ending = **restore balance**
- agents do the building; humans approve/reject direction

Do **not** reopen these as if they were undecided.

---

## 3. Working method

Use:
**spec → plan → tiny task → implement → verify → present visually → wait for approval**

Do not jump straight from concept to lots of code.

### For each feature:
1. State the exact behaviour being built.
2. Define acceptance criteria.
3. Build the smallest testable increment.
4. Run relevant verification.
5. Present results clearly.
6. Stop for human review if the task boundary was reached.

---

## 4. Child-friendly presentation requirement

Every meaningful handoff must have **two layers**.

### A. Parent summary
- **Changed:** what changed
- **Verified:** what was tested
- **Needs decision:** only if truly needed
- **Next:** one recommended tiny next step

### B. Amelia summary
Use simple language and short bullets:
- **We made:** one sentence
- **Try this:** one fun thing to test
- **You choose:** 2–3 easy options

Use checkboxes and keep it short.

---

## 5. Visual reporting requirement

Agent outputs should be easy to skim. Prefer:
- checklists
- small tables
- short sections
- screenshots / GIFs / mockups when useful
- simple diagrams

Avoid giant walls of text.

If a prototype has a visual result, show the visual result.

---

## 6. Engineering priorities

Order of importance:
1. prove the tiny vertical slice
2. keep 2-player co-op working
3. keep the cross-mode loop connected
4. keep implementation understandable and reviewable
5. improve presentation and art
6. only then consider expansion

---

## 7. Scope discipline

Do **not** add major systems beyond the current slice without approval.

Especially avoid prematurely building:
- many levels
- many creatures
- full campaign logic
- online multiplayer
- deep inventory systems
- full rhythm difficulty ladders
- polished production-scale asset pipelines

The current job is to prove:
**Rome → Mermaid → Rhythm → Battle**

---

## 8. Godot expectations

Default stack assumption:
- **Engine:** Godot 4
- **Prototype target:** local desktop build first
- **Possible later target:** browser export

Structure work in a way suitable for Godot scenes/scripts/resources. If proposing a deviation, justify it and request approval first.

---

## 9. Approval gates

Stop and hand off after any of these:
1. project setup complete
2. platforming scene playable
3. Mermaid recruitment working
4. rhythm minigame playable
5. battle scene playable
6. whole vertical slice connected
7. art/style revision pass

Do not silently barrel past multiple approval gates.

---

## 10. Safety / authority boundaries

Do not:
- merge without approval
- publish builds externally without approval
- install large new dependencies without approval
- use paid external tools/services without approval
- treat agent suggestions as product decisions

Humans choose. Agents execute.

---

## 11. Decisions must live in the repo

- Every human decision goes into `decisions/DECISIONS.md` (readable ledger) **and** its raw source (e.g. GDD JSON export) under `decisions/answers/YYYY-MM-DD_*.json`.
- Read `decisions/DECISIONS.md` and `docs/ART_STYLE.md` before building or generating art.
- All art prompts start with the style block in `docs/ART_STYLE.md` §8.
- Never rely on browser storage, chat history or artifact databases as the only copy of a decision.
