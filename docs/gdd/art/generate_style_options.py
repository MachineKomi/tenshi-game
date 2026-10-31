"""Tenshi art-style comparison: same subject, three finishes. Model gpt-image-2.5-sunburst-2026-09-08, 1024x1024 high."""
import os, sys, json, base64, urllib.request, concurrent.futures as cf
MODEL="gpt-image-2.5-sunburst-2026-09-08"; OUT=sys.argv[1]; key=os.environ["OPENAI_API_KEY"]
SUBJECT=("Same scene for a style comparison: a cute chunky chibi anime girl angel (long lavender-pink hair, white-and-gold dress, gel-ring halo, "
 "small white wings) leaning on the rim of a Roman marble fountain, smiling at a cute chibi aqua-haired mermaid girl with a glitter tail who "
 "splashes up out of the water. Waist-up framing, square composition, soft sunny Roman courtyard background with a column and a red banner. "
 "Big sparkly anime eyes, chunky rounded proportions, expressive happy faces, child-friendly. Original characters, no franchise likeness. "
 "No text, letters, logos or watermark. Palette: pastel prism rainbow (bubblegum pink, peach, lemon, mint, baby blue, lilac) with saturated jelly accents.")
STYLES={
 "style-a-gloss": "STYLE A, modern juicy gloss: clean polished digital anime rendering, smooth gradients, wet candy-gloss highlights on hair and eyes, "
   "translucent jelly and liquid-glass water with bubbles inside, thin holographic rainbow film on edges, bright bloom. Very shiny and premium, no paper texture.",
 "style-b-handmade": "STYLE B, juicy gloss with a hand-illustrated finish: chunky cel-shaded anime with visible hand-inked coloured lineart of varying "
   "weight, subtle coloured-pencil and watercolour-paper grain in the shadows and backgrounds, gouache-like painted background. Glossy jelly highlights, "
   "liquid-glass water, glitter and holographic sheen kept on eyes, halo, tail, water and magic, so the shine pops against the soft hand-made texture. "
   "Feels like a premium illustrated storybook crossed with a modern anime game.",
 "style-c-cel": "STYLE C, chunky bold cel shading: thick dark-plum outlines, flat bright colour fills with one crisp shadow tone, sticker-like simple shapes, "
   "very readable at small sizes. Shine and gel effects are used only on magic, water, the halo and UI-like sparkles, everything else is flat and clean.",
}
def gen(n):
    body={"model":MODEL,"prompt":STYLES[n]+" "+SUBJECT,"size":"1024x1024","quality":"high","n":1,"output_format":"webp","output_compression":88}
    r=json.load(urllib.request.urlopen(urllib.request.Request("https://api.openai.com/v1/images/generations",json.dumps(body).encode(),
        {"Authorization":"Bearer "+key,"Content-Type":"application/json"}),timeout=600))
    open(os.path.join(OUT,n+".webp"),"wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    u=r.get("usage",{}); return n, u.get("output_tokens"), round((u.get("output_tokens",0)*30+u.get("input_tokens",0)*5)/1e6,3)
with cf.ThreadPoolExecutor(3) as ex:
    for x in ex.map(gen,STYLES): print(*x, flush=True)
