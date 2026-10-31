"""Tenshi art-style blend test: 3 blend dials x 3 in-game scenes (9 images).
Every prompt = ART_STYLE.md section 8 house block + blend dial + scene. Model gpt-image-2.5-sunburst-2026-09-08, 1536x1024 high.
Usage: python generate_blend_tests.py <out_dir>   (writes <blend>-<scene>.webp and prompts.json)"""
import os, sys, json, base64, urllib.request, concurrent.futures as cf
MODEL="gpt-image-2.5-sunburst-2026-09-08"; OUT=sys.argv[1]; key=os.environ["OPENAI_API_KEY"]
HOUSE=("Tenshi Game house style: bold, chunky, cute anime game art with a smooth, juicy, polished finish. Characters about 4 heads tall with "
"rounded chunky shapes, big sparkly glossy anime eyes and expressive happy faces. Medium hand-inked outlines in dark plum and local "
"colour (heavier on the outer silhouette, lighter inside), never pure black. Bold cel shading with clean flat fills and one crisp "
"shadow tone, finished with smooth gradient light, crisp glossy specular highlights and a soft rim light. Strongest gel, jelly, "
"liquid-glass and thin holographic-film shine only on eyes, halos, water, magic effects and the most important objects; hair and "
"gold get a soft sheen; skin, cloth and plain stone stay matte and clean. No paper, pencil or brush texture. Pastel prism rainbow "
"palette (bubblegum pink #FF8FC0, peach #FFB27A, lemon #FFE27A, mint #9BEFC9, baby blue #9CDEFF, lilac #C9B4FF) with saturated "
"jelly accents (#FF4FA0, #FF8A2B, #3DB8FF, #9E6BFF). Bright, readable, low clutter, child-friendly. Original characters, no "
"franchise likeness. No text, letters, logos or watermark.")
BLENDS={
 "blend1": "BLEND DIAL: mostly bold cel (C-leaning). Flat fills and crisp hard-edged shadows dominate, outlines on the bolder side of medium, "
   "sticker-like clean shapes. Gloss is a small accent: sharp white specular dots on eyes, halos, the mermaid tail, water and the key object only. "
   "Hair, clothes and buildings stay almost flat.",
 "blend2": "BLEND DIAL: an even 50/50 blend. Bold cel base with clear hard shadows, plus smooth soft gradient lighting over every form, "
   "candy-glossy highlights on hair, eyes and jewellery, juicy jelly and liquid-glass shine on magic, water and the key object.",
 "blend3": "BLEND DIAL: chunky shapes with a rich polished gloss (A-leaning). Keep the chunky silhouettes and medium inked outlines, but shading is "
   "smooth and soft with gentle gradients, glossy vinyl-toy-like sheen on hair and rounded forms, wet candy highlights, soft bloom and glow, "
   "lots of jelly, glitter and liquid-glass shine on magic, water and the key object. Premium and very shiny.",
}
CAST=("The heroes are two angel kids, one girl and one boy: the girl angel has long lavender-pink hair and a white-and-gold dress; the boy angel has "
 "short sky-blue hair and a white-and-gold tunic; both have small white wings and glowing gel-ring halos. The Mermaid has aqua hair and a "
 "glittering pearly tail.")
SCENES={
 "story": "SCENE: a visual-novel story illustration (cutscene CG), wide 3:2. In a sunny Ancient Roman courtyard, the girl angel and the boy angel "
   "lean over the rim of a round marble fountain, delighted, as the Mermaid splashes up out of the sparkling water to meet them. Columns, a red "
   "banner and terracotta roofs behind. Keep the lower fifth of the image calm and simple so a dialogue box could sit there later.",
 "explore": "SCENE: an in-game screenshot of the exploration level, wide 3:2, three-quarter top-down camera. A bright Ancient Roman street with "
   "columns, steps, a fountain and market awnings. The two angel heroes are small game sprites (simplified versions of the characters) walking "
   "together near the centre. A glowing golden key floats on a glossy pedestal as the important object. A tiny silly purple demon peeks from behind "
   "a pillar. Simple glossy jelly UI icons in the corners (hearts and a star counter, no numbers, no text).",
 "dance": "SCENE: an in-game screenshot of the rhythm dance battle, wide 3:2. The Mermaid dances on a stage of shimmering water inside a small "
   "Roman arena, the two angel heroes cheer at the sides. Three lanes of glossy jelly note orbs (pink, blue, violet) slide toward a glassy target "
   "ring at the bottom. A grumpy, silly, round purple demon with tiny horns stands on the opposite side looking flustered, not scary. "
   "A glossy jelly power meter bar at the top with no text.",
}
JOBS=[(b,s) for b in BLENDS for s in SCENES]
def prompt(b,s): return HOUSE+" "+BLENDS[b]+" "+CAST+" "+SCENES[s]
def gen(job):
    b,s=job; name=f"{b}-{s}"
    body={"model":MODEL,"prompt":prompt(b,s),"size":"1536x1024","quality":"high","n":1,"output_format":"webp","output_compression":88}
    r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.openai.com/v1/images/generations",json.dumps(body).encode(),
        {"Authorization":"Bearer "+key,"Content-Type":"application/json"}),timeout=600))
    open(os.path.join(OUT,name+".webp"),"wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    u=r.get("usage",{}); return name, u.get("output_tokens"), round((u.get("output_tokens",0)*30+u.get("input_tokens",0)*5)/1e6,3)
json.dump({f"{b}-{s}":prompt(b,s) for b,s in JOBS},open(os.path.join(OUT,"prompts.json"),"w"),indent=1)
total=0
with cf.ThreadPoolExecutor(5) as ex:
    for x in ex.map(gen,JOBS): total+=x[2] or 0; print(*x, flush=True)
print("total_usd", round(total,3))
