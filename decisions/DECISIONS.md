# Tenshi Game: Decision Ledger

The single place where human decisions are recorded. **Agents must read this before building, and must add every new human decision here** (with the raw answer file under `decisions/answers/`). Later decisions override earlier ones.

| Status | Meaning |
|---|---|
| 🔒 Locked | Approved by the humans. Don't reopen it. |
| ✅ Decided | Answered by the humans. Can be refined. |
| ⏳ Open | Still waiting for an answer. |

---

## 🔒 Locked (from INTENT.md, 2026-10-31)

| Topic | Decision |
|---|---|
| First world | Ancient Rome |
| First creature | Mermaid |
| Engine | Godot 4 |
| Players | 2-player local co-op |
| Structure | Explore → Recruit → Rhythm → Battle |
| Ending | Restore balance (happy ending) |
| Scope | Tiny vertical slice first |

## ✅ Art style (GDD Part 0, answered 2026-10-31 by Amelia + parent)

Source: `decisions/answers/2026-10-31_gdd-answers.json`

| Decision | Answer | Human note |
|---|---|---|
| Finish (`art_style`) | **Blend of A (juicy gloss) and C (bold and chunky)**: C's bold, chunky design with A's smooth, polished shine. They ticked A but explained the blend in the note. | "C will be easier to nail consistently, especially details in VN cut scenes and CGs." |
| Where shine goes (`shine_amount`) | Magic things, **plus anything non-magical that's very important or needs highlighting** | |
| Texture (`texture`) | None, smooth digital | |
| Outlines (`outline`) | Medium hand-inked lines | |
| Proportions (`proportions`) | Cute but a bit taller, about 4 heads tall | |
| Sprites vs illustrations (`sprite_match`) | Same style, simplified | |

→ This is written up as the style spec in `docs/ART_STYLE.md`.

## ⏳ Open (25 left, to answer in the GDD)

Art style: `style_blend` (new 2026-10-31: blend test, 3 mixes of A + C shown in story, explore and dance scenes) · Story: `demon_fate`, `goddess_role` · Heroes: `angel_names`, `angel_outfit`, `controls` · Loop: `slice_length`, `fail_rule` · Rome: `rome_features`, `camera`, `history` · Mermaid: `mermaid_personality`, `mermaid_colour`, `mermaid_name`, `recruit_how` · Dance: `dance_feel`, `note_style`, `miss_note`, `upgrade_look`, `music_source` · Battle: `battle_style`, `enemy_look`, `fort_reclaim` · Making it: `art_pipeline`, `review_style`

## Process feedback from the humans

- 2026-10-31: the GDD "Save answers" button should **download a file**, not copy to the clipboard. Fixed in the GDD.
- 2026-10-31: the "Something else" box had an annoying character limit. Fixed: it's now a 4000-character text area, and notes allow 8000.
- 2026-10-31: all decisions must always be preserved in this repo.
