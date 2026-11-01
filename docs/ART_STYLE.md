# Tenshi Game: Art Style Spec

**Status:** DECIDED by Amelia + parent. Finish chosen 2026-10-31; blend dial chosen 2026-11-01 (**Blend 3, chunky with rich gloss**). The §8 block below includes it.
**Decision record:** `decisions/DECISIONS.md` and `decisions/answers/2026-10-31_gdd-answers.json`
**Owner:** humans approve, agents follow

> Every image prompt, sprite, UI screen and effect must follow this spec. If a later human decision conflicts with it, the human decision wins and this file gets updated.

---

## 1. One-line style

**Bold, chunky, cute anime with a smooth, juicy, polished shine.** The clean shapes and confident outlines of style C, finished with style A's glossy highlights. Gel, slime, liquid glass and holographic shine are saved for magic and for whatever matters most, in the rainbow prism palette (the same family as Maze so Puzzle and SSS).

## 2. The decision

| Question | Answer |
|---|---|
| Finish | **A + C blend**: C's bold, chunky design with A's smooth, polished, shiny surfaces |
| Shine | On magic things, **plus anything non-magical that's very important or needs highlighting** |
| Texture | **None.** Smooth digital, no paper or pencil grain |
| Outlines | **Medium hand-inked lines** in coloured or plum ink, heavier on the outer silhouette and lighter inside |
| Proportions | **Cute but a bit taller**, about 4 heads tall |
| Sprites | **Same style, simplified** for small sizes (fewer details, same lines, palette and shine rules) |
| Blend dial (2026-11-01) | **Blend 3, chunky with rich gloss**: soft smooth shading, glossy toy-like hair, plenty of glow and glitter, still with the chunky shapes and medium inked outlines |

Why the humans chose this: style C is easier to keep consistent, especially for detailed VN cut scenes and CGs. Style A adds the juicy, premium feel.

Blend vote (2026-11-01): Amelia chose Blend 3 "because it's the shiniest". Her parent preferred Blend 1, because clear outlines make AI art more readable and consistent. **So the outlines are not negotiable:** every image keeps clear medium plum outlines around each character and object, even with all the gloss, and sprites can lean a little toward Blend 1 if they get muddy at small size.

**Reference images** (in `docs/gdd/art/`):
- `style-c-cel.webp`: the base for shapes, outlines and readability.
- `style-a-gloss.webp`: the target for highlights, wet shine and liquid glass.
- `style-b-handmade.webp`: rejected (no paper texture).

## 3. Palette (shared with MSP / SSS)

| Role | Colours |
|---|---|
| Prism pastels | `#FF8FC0` pink · `#FFB27A` peach · `#FFE27A` lemon · `#9BEFC9` mint · `#9CDEFF` baby blue · `#C9B4FF` lilac |
| Jelly accents | `#FF4FA0` hot pink · `#FF8A2B` tangerine · `#FFD62E` lemon · `#2EE6A8` mint · `#3DB8FF` sky · `#9E6BFF` violet |
| Ink | `#352340` plum, for lines and text. Never pure black |
| Holographic film | the conic film stops in `D:\GameDev\Skills\vn-gel-glass\assets\tokens.json` |

## 4. Rendering rules

- **Base rendering:** bold cel shading. Clean flat fills, one crisp shadow tone, and an occasional second shadow for depth. Shapes are simple and sticker-readable.
- **Polish layer:** smooth gradient light on top of the cel base. Crisp, glossy specular highlights on hair, eyes, lips, jewellery and rounded forms, plus a soft rim light. Polished, never airbrushed mush.
- **Shine tier 1, always glossy:** eyes, halos, the Mermaid's tail and fins, water, every spell and magic effect, buttons, rewards, and anything the player must notice (goals, keys, the fort banner).
- **Shine tier 2, glossy sheen:** hair (glossy, toy-like ribbon highlights), gold trim, polished marble.
- **Shine tier 3, matte:** skin (soft blush only), cloth, plain stone, background foliage.
- **Jelly / slime:** translucent with coloured light passing through, bubbles and glitter inside, and a wet highlight on top.
- **Liquid glass:** clear and refractive, with a thin rainbow film only on edges and rims. Never a thick rainbow band.
- **No texture:** no paper grain, pencil, watercolour or brush noise.

## 5. Characters

- About 4 heads tall: cute and chunky, with rounded hands and feet and a big head.
- Big, sparkly, glossy anime eyes and expressive faces.
- Medium hand-inked outlines that make a clear silhouette against busy backgrounds.
- Each hero, creature and faction owns one identity colour, used everywhere they appear.
- **Angel outfits (2026-11-01):** magical-girl sparkle: pastel outfits, ribbons, a transformation pose. The boy angel gets a matching magical-boy version (same ribbons and pastel colours, shorts or tunic). Halos and small wings stay.
- Readable at sprite size. Sprites keep the same style with fewer details.
- Child-friendly: no scary, gory or suggestive content. Demons look silly, not frightening.
- Original characters only, with no franchise likeness (for example, avoid a red-haired mermaid with a green tail).
- **Modest outfits:** the Mermaid wears a covered swim or crop top (shell trim is fine), never a bikini or cleavage. Statues in backgrounds are clothed. Add this to every prompt that shows her. (The 2026-10-31 blend test drew shell bikini tops; fix that in the next round.)

## 6. UI

Use the `vn-gel-glass` rules: **glass** for information and panels, **jelly** for buttons and names, plum ink with a solid white outline, and squash-and-stretch motion. Always honour Reduce Motion and Reduce Transparency. See `D:\GameDev\Skills\vn-gel-glass\principles\PRINCIPLES.md` and `engine\GODOT.md`.

## 7. Image generation settings

| Setting | Value |
|---|---|
| Model | `gpt-image-2.5-sunburst-2026-09-08` (same pin as Maze so Puzzle) |
| Quality | `high` for concepts and assets; `xhigh` only for approved master art |
| Size | 1536x1024 for scenes, 1024x1024 for characters and comparisons |
| Format | webp at quality 88 for review; png for runtime assets that need alpha |
| Cost seen | about $0.04 for 1536x1024 high, about $0.054 for 1024x1024 high |

**Scripts:** `docs/gdd/art/generate_concepts_v2.py` and `generate_style_options.py`. Keep every prompt with its output.

## 8. Prompt style block

Start every image prompt with this exact block, and change only the subject after it. Status: approved by the humans' Blend 3 vote, 2026-11-01.

```
Tenshi Game house style: bold, chunky, cute anime game art with a smooth, juicy, richly glossy finish. Characters about 4 heads
tall with rounded chunky shapes, big sparkly glossy anime eyes and expressive happy faces. Clear medium hand-inked outlines in dark
plum and local colour around every character and object (heavier on the outer silhouette, lighter inside), never pure black, never
lost under the shine. Soft, smooth shading with gentle gradients over a clean cel base, glossy vinyl-toy-like sheen on hair and
rounded forms, wet candy highlights, a soft rim light and gentle bloom. Lots of jelly, glitter, liquid-glass and thin
holographic-film shine on eyes, halos, water, magic effects and the most important objects; skin stays matte with soft blush;
cloth and plain stone stay clean. No paper, pencil or brush texture. Pastel prism rainbow palette (bubblegum pink #FF8FC0, peach
#FFB27A, lemon #FFE27A, mint #9BEFC9, baby blue #9CDEFF, lilac #C9B4FF) with saturated jelly accents (#FF4FA0, #FF8A2B, #3DB8FF,
#9E6BFF). Bright, readable, low clutter, child-friendly, modest outfits (the Mermaid wears a covered swim top, statues are clothed).
Original characters, no franchise likeness. No text, letters, logos or watermark.
```

**For sprites,** add: "Simplified small game sprite: fewer details, same outlines, palette and shine; keep the silhouette crisp and readable."

## 9. Blend test (2026-10-31)

Same house block, plus one "blend dial" line, drawn in three game moments (story CG, exploring screen, dance battle). Script: `docs/gdd/art/generate_blend_tests.py`. Prompts: `docs/gdd/art/blend/prompts.json`. Cost: $0.40 for 9 images (1536x1024 high).

| Dial | What changes |
|---|---|
| Blend 1 · Mostly bold cel | Flat fills, crisp shadows, shine only as small sparkles on tier-1 things |
| Blend 2 · Even mix | The block as written: cel base plus soft light, candy shine on hair and eyes |
| Blend 3 · Chunky with rich gloss | Softer shading, glossy toy-like hair, lots of glow and glitter |

**Result (2026-11-01): Blend 3 won.** Its dial line is now part of the §8 block. Blends 1 and 2 stay in the repo as reference only.
