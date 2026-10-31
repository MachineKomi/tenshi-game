"""Tenshi concept art v2: gel / slime / liquid-glass / holographic prism style.
Model: gpt-image-2.5-sunburst-2026-09-08 (same pin as maze-so-puzzle-rebirth). Usage: python -I generate_concepts_v2.py OUTDIR [names...]"""
import os, sys, json, base64, urllib.request, urllib.error, concurrent.futures as cf
MODEL = "gpt-image-2.5-sunburst-2026-09-08"
PRICE_OUT, PRICE_TXT = 30, 5   # USD per 1M tokens (as recorded in maze openai-images.mjs)
OUT = sys.argv[1]
STYLE = ("Glossy 'gel and glass' chibi anime game concept art. Cute chibi proportions, big sparkly anime eyes, expressive faces, "
 "clean confident contours in dark plum and local colour, never harsh black. Every surface feels like candy-gloss jelly, translucent "
 "glitter slime and clear liquid glass: wet specular highlights, soft inner glow, coloured light passing through, tiny bubbles and glitter "
 "flecks suspended inside translucent things, and a thin rainbow holographic soap-bubble film shimmering only on edges and rims. "
 "Palette is a pastel prism rainbow: bubblegum pink #FF8FC0, peach #FFB27A, lemon #FFE27A, mint #9BEFC9, baby blue #9CDEFF, lilac #C9B4FF, "
 "with saturated jelly accents hot pink #FF4FA0, tangerine #FF8A2B, sky #3DB8FF and violet #9E6BFF. Bright, premium, polished, "
 "readable, low clutter, child-friendly. Original characters, no franchise likeness. No text, letters, logos, UI labels or watermark.")
P = {
 "keyart": "Key art. Two little angel heroes fly side by side above a sunny, whimsical Ancient Rome: a pretty anime girl angel with long pastel "
   "lavender-pink hair and a flowing white dress with gold trim, and a cute young boy angel with fluffy light-brown hair and a white tunic. "
   "Their halos are glowing lemon gel rings, their wings are white feathers edged with holographic iridescent film. Below, Roman columns and "
   "arches are made of pearlescent opal marble with a rainbow sheen, red banners look like glossy jelly ribbons, and a fountain of clear liquid "
   "glass water holds a cute aqua mermaid girl waving up at them. Prism sparkles and floating bubbles in a bright blue sky.",
 "mermaids": "Character concept sheet on a soft pale pearly background with a faint prism gradient: four versions of the same cute chibi "
   "mermaid girl standing in a row, evenly spaced, full body, same scale. Her tail is translucent glitter jelly with bubbles inside, fins like "
   "holographic glass, laurel-leaf hair clip and seashell jewellery. 1) aqua and baby-blue, sweet and gentle, hands clasped; 2) pink and peach, "
   "silly, giggling and blowing a soap bubble; 3) lilac and violet, brave, holding a small crystal trident; 4) rainbow prism tail, mischievous wink "
   "and a playful pose. Each clearly different in pose and colour.",
 "level": "Side-scrolling 2D platformer level mockup, game screenshot composition, camera side-on. A short cheerful Ancient Rome diorama: "
   "platforms made of chunky pearlescent marble columns with glossy jelly tops, a tiled floor with candy-glass tiles, glossy red jelly banners, "
   "a little temple in the background shimmering with holographic film, sunny sky with soft clouds and drifting bubbles. At the right end a "
   "fountain of sparkling liquid-glass water where an aqua mermaid girl sits waiting. On the left, two tiny chibi angels (girl and boy) jumping, "
   "with gel-ring halos. Simple readable shapes, clear foreground and background layers.",
 "rhythm": "Split game mockup, two halves side by side with a thin glowing holographic divider. Left half: a sparkly rhythm minigame on a fountain "
   "stage at dusk, a cute aqua-haired mermaid girl dancing in a splash of liquid-glass water, glossy star-shaped jelly notes falling toward two "
   "big round jelly buttons at the bottom (one bubblegum pink, one sky blue) that glow from inside. Right half: a tiny cute co-op battle in front "
   "of a playful toy-like Roman fort made of pearlescent stone: two chibi angels and the powered-up mermaid, now glowing with a holographic "
   "aura, splashing rainbow liquid-glass water magic at small round grumpy purple-and-red jelly imps that look silly, not scary.",
}
key = os.environ["OPENAI_API_KEY"]
def call(name, fmt):
    body = {"model":MODEL,"prompt":STYLE+" "+P[name],"size":"1536x1024","quality":"high","n":1,"output_format":fmt}
    if fmt == "webp": body["output_compression"] = 88
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", json.dumps(body).encode(),
          {"Authorization":"Bearer "+key,"Content-Type":"application/json"})
    return json.load(urllib.request.urlopen(req, timeout=600))
def gen(name):
    for fmt in ("webp","png"):
        try:
            r = call(name, fmt); break
        except urllib.error.HTTPError as e:
            err = e.read().decode()[:400]
            if fmt == "png" or "format" not in err and "compression" not in err: return name, "ERR "+err
    open(os.path.join(OUT, f"{name}.{fmt}"),"wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    u = r.get("usage") or {}
    cost = (u.get("output_tokens",0)*PRICE_OUT + u.get("input_tokens",0)*PRICE_TXT)/1e6
    return name, f"{fmt} out_tokens={u.get('output_tokens')} est=${cost:.3f}"
names = sys.argv[2:] or list(P)
with cf.ThreadPoolExecutor(4) as ex:
    for n, info in ex.map(gen, names): print(n, info, flush=True)
