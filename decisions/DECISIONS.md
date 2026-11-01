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

## ✅ Art style blend (answered 2026-11-01)

Source: `decisions/answers/tenshi-gdd-answers-2026-11-01.json`

| Decision | Answer | Human note |
|---|---|---|
| Blend dial (`style_blend`) | **Blend 3, chunky with rich gloss** | Amelia: "because it's the shiniest, I just love it because it's shiny." Parent liked Blend 1, because outlines make AI art more readable and consistent. → Outlines stay clear and medium in every image (see `docs/ART_STYLE.md`). |

## ✅ Story, heroes, loop and Rome (answered 2026-11-01)

Source: `decisions/answers/tenshi-gdd-answers-2026-11-01.json`

| Decision | Answer | Human note / what it means |
|---|---|---|
| Angel names (`angel_names`) | **Girl: Serena (セレナ) · Boy: Sora (天)** | Sora's kanji 天 means sky or heaven. |
| Demon fate (`demon_fate`) | **Some become friends** | A sorry demon waves goodbye, and could become a future creature. |
| Goddess (`goddess_role`) | **One picture at the start** | One still picture with one line of text. |
| Angel outfits (`angel_outfit`) | **Magical girl sparkle** | Pastel outfits, ribbons, a transformation pose. Boy angel gets the matching version. |
| Controls (`controls`) | **Support both** | Shared keyboard (WASD + Space / arrows + Enter) and two gamepads. |
| Slice length (`slice_length`) | **5 to 8 minutes** | |
| When you mess up (`fail_rule`) | **Custom rule per mode** (see below) | |
| Rome features (`rome_features`) | **Columns, fountain, red banners, sunny sky, little temple, arches and an aqueduct** | Amelia adds: some rainbows, and some cute little monsters that are good and are with the Mermaid. |
| Camera (`camera`) | **One shared screen that zooms** | Zoom out up to a limit; for now, stop players moving further apart. Later: split into split screen when too far apart, and merge back when close again. |
| History (`history`) | **Fun fact card at the end, plus more** | Also Latin words on signs, and history cards collected in a **history book** you can read. Reading them could power up your creatures, so learning is rewarded. |

**Fail rule, in the humans' words (summarised):**
- **Platforming:** you only get set back a little. If one player survives, the other comes back at their friend's position. If both are knocked out, restart at frequent checkpoints.
- **Rhythm:** you can't fail. How well you dance decides the power-ups and other rewards.
- **Battle:** described as an auto-battle against generals, in the style of "avarice 3" and Vampire Survivors. You *can* lose, but there's no penalty: just try again, with tips on how to make it easier (rescue more creatures, or dance more to power them up).
- Note: this also hints at the answer to `battle_style`, which is still open.

### Notes for building (agent)
- The slice grows from about 3 minutes to 5 to 8. Build the shortest playable version first, then stretch it.
- Camera: build shared zoom plus a distance limit first. Dynamic split screen is a later upgrade, not part of the first slice.
- History book, creature power-ups from reading, and demon friends are **after the first slice**. The first slice gets the fact card and a few Latin signs.

## ⏳ Open (14 left, to answer in the GDD)

Mermaid: `mermaid_personality`, `mermaid_colour`, `mermaid_name`, `recruit_how` · Dance: `dance_feel`, `note_style`, `miss_note`, `upgrade_look`, `music_source` · Battle: `battle_style`, `enemy_look`, `fort_reclaim` · Making it: `art_pipeline`, `review_style`

## Process feedback from the humans

- 2026-10-31: the GDD "Save answers" button should **download a file**, not copy to the clipboard. Fixed in the GDD.
- 2026-10-31: the "Something else" box had an annoying character limit. Fixed: it's now a 4000-character text area, and notes allow 8000.
- 2026-10-31: all decisions must always be preserved in this repo.
