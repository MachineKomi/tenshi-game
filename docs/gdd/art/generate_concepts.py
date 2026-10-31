import os, sys, json, base64, urllib.request, concurrent.futures as cf
OUT = sys.argv[1]
STYLE = ("Bright cute chibi anime game concept art, thick clean dark outlines, saturated cheerful colours, "
         "soft cel shading, sparkles, child-friendly, low clutter, no text, no words, no letters.")
P = {
 "keyart": "Key art: two little angel heroes with white feathered wings and golden halos flying side by side over a sunny whimsical Ancient Rome of marble columns, arches, red banners and a fountain. One is a pretty teen anime girl angel with long pastel hair and a flowing white-and-gold dress; the other is a cute young boy angel with messy hair and a tunic. A friendly aqua mermaid waves from the fountain.",
 "mermaids": "Character concept sheet: four versions of the same cute chibi mermaid girl standing in a row on a plain light background, each with a distinct palette and pose: 1) aqua-blue, sweet and gentle, hands clasped; 2) pink-peach, silly, giggling with a bubble; 3) purple-lavender, brave, holding a little trident; 4) rainbow-sparkle tail, mischievous wink. Roman-Mediterranean touches like laurel hairpieces and seashell jewellery. Evenly spaced, full body, same scale.",
 "level": "Side-scrolling 2D platformer level mockup, game screenshot style: a short cheerful Ancient Rome diorama with marble column platforms, tiled floor, red banners, a little temple in the background, sunny sky with fluffy clouds, a sparkling fountain at the right end where a mermaid waits. Two tiny chibi angel characters (girl and boy) jumping on the left. Simple readable shapes.",
 "rhythm": "Split game mockup. Left half: a sparkly rhythm minigame screen with two big round glowing buttons at the bottom (one pink, one blue) and star notes falling toward them, a cute mermaid dancing in the centre on a fountain stage. Right half: a tiny cute co-op battle in front of a playful Roman fort, two chibi angels and a powered-up glowing mermaid splashing water magic at small round cartoon imp demons that look silly not scary.",
}
key = os.environ["OPENAI_API_KEY"]
def gen(name):
    body = json.dumps({"model":"gpt-image-1-mini","prompt":STYLE+" "+P[name],"size":"1536x1024",
                       "quality":"medium","output_format":"webp","output_compression":70,"n":1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", body,
          {"Authorization":"Bearer "+key,"Content-Type":"application/json"})
    try:
        r = json.load(urllib.request.urlopen(req, timeout=300))
    except urllib.error.HTTPError as e:
        return name, "ERR "+e.read().decode()[:300]
    open(os.path.join(OUT,name+".webp"),"wb").write(base64.b64decode(r["data"][0]["b64_json"]))
    return name, r.get("usage")
with cf.ThreadPoolExecutor(4) as ex:
    for n,u in ex.map(gen, P): print(n,u)
