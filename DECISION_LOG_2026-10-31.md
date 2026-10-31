# Decision Log — 2026-10-31

## New decisions confirmed

- planning docs should be more visual and child-friendly
- agents should do implementation and asset creation
- humans approve/reject plans, ideas, art assets, and revisions
- inspiration references include Pokémon, Kirby, Mario, magical girl anime, and KPop Demon Hunters
- first historical world = Ancient Rome
- first magical creature = Mermaid
- scope should be super narrow
- engine recommendation selected = Godot 4 for the first prototype

## Rationale for engine choice

Godot is a better fit than a custom web stack for the current spec because the game needs:
- 2D scene management
- platforming
- rhythm minigame flow
- battle scene flow
- local co-op input handling
- faster prototype iteration

Web/browser can still be considered later via export or later deployment strategy.

## Art style decided (GDD Part 0, evening)

- finish = blend of A (juicy gloss) + C (bold & chunky): C's bold chunky design, A's smooth polished shine
- shine = magic things + anything non-magical that is super important / needs highlighting
- texture = none (smooth digital)
- outlines = medium hand-inked
- proportions = cute, ~4 heads tall
- sprites = same style, simplified
- full record: `decisions/DECISIONS.md`; spec: `docs/ART_STYLE.md`
