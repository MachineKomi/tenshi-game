# Tenshi Game — Game Design Document (GDD)

**Version:** 0.2  
**Date:** 2026-10-31  
**Status:** concept locked for first vertical slice

---

## 1. 🎮 High concept

A **cute co-op anime game** where two angel heroes:
1. explore a historical level,
2. befriend a magical creature,
3. strengthen it with a rhythm minigame,
4. then lead it into a small battle to restore balance.

This first version is intentionally tiny and should also function as an **AI learning project** for Amelia.

---

## 2. 🧭 First-slice design lock

### Locked decisions
| Topic | Decision |
|---|---|
| Core structure | Explore → Recruit → Rhythm → Battle |
| Players | 2-player co-op |
| First world | **Ancient Rome** |
| First creature | **Mermaid** |
| Engine | **Godot 4** |
| Ending direction | Happy ending by restoring balance |
| Tone | Cute, bright, magical, playful |
| Scope | Deliberately tiny first vertical slice |

### Not for first slice
- multiple worlds
- big creature roster
- deep army management
- full campaign map
- online multiplayer
- advanced combat systems
- lots of rhythm difficulties
- lots of enemies

---

## 3. ✨ Creative pillars

### Pillar A — Child-friendly co-op
The game should be easy to understand and forgiving to play. Two players should be able to help each other.

### Pillar B — Bright magical anime energy
Visuals should feel colourful, sparkly, warm, fun, and expressive.

### Pillar C — History as playful flavour
The first world is inspired by Ancient Rome, but presented in a light, whimsical, age-appropriate way.

### Pillar D — AI as helper, not boss
The game’s development process should visibly show that humans choose and agents build.

---

## 4. 🎨 Art and inspiration direction

### Inspiration mix
Use only as directional inspiration:
- **Mario** → side-scrolling readability
- **Kirby** → softness and friendliness
- **Pokémon** → collecting and growing creature allies
- **Cardcaptor Sakura / magical girl anime** → charm, sparkles, costumes, magical identity
- **Madoka / Prisma Illya** → magical team vibe, transformed energy (kept age-appropriate)
- **KPop Demon Hunters** → pop-supernatural stylishness and upbeat energy

### Visual rules
- thick readable outlines
- bright colours
- expressive faces
- chibi/cute readability over realism
- low-clutter scenes
- cheerful magical effects
- no grimdark horror
- no realistic violence

### First-world visual theme: Ancient Rome
Think:
- sunny sky
- marble columns
- tiled floors
- banners / arches
- fountains / water motifs
- playful Roman fortification at battle end

### First creature visual theme: Mermaid
Think:
- cute and friendly
- sparkling water magic
- Roman-Mediterranean flavour
- readable silhouette
- suitable as both friend and battle ally

---

## 5. 🕹 Gameplay loop

```text
Platforming level
   ↓
Meet Mermaid
   ↓
Recruit Mermaid
   ↓
Simple rhythm dance
   ↓
Mermaid powers up
   ↓
Tiny co-op battle
   ↓
Reclaim one fortification
```

That is the whole first target.

---

## 6. 🏛 Mode A — Explore Ancient Rome

### Goal
Play one short side-scrolling level and meet the Mermaid.

### Required features
- two players visible at once
- move left/right
- jump
- simple obstacles
- one small end point or encounter point
- one recruitment interaction

### Nice vibe
The level should feel more like a **fun playable diorama** than a big content-heavy stage.

### First-slice acceptance
- both players can move and jump,
- both can reach the encounter area,
- the Mermaid can be recruited,
- the scene clearly reads as Ancient Rome.

---

## 7. 🎵 Mode B — Rhythm upgrade

### Goal
Do one very easy rhythm action to strengthen the Mermaid.

### Required features
- one very short song snippet or beat sequence
- easiest mode only for now
- very low skill floor
- clear success feedback
- visible upgrade result

### First-slice design choice
For the first prototype, **one button per player** is enough.

### First-slice acceptance
- players can start the rhythm sequence,
- each player contributes,
- success upgrades the Mermaid,
- the Mermaid’s powered-up state is visible.

---

## 8. ⚔ Mode C — Tiny battle

### Goal
Lead the upgraded Mermaid in a small co-op battle and reclaim one fortification.

### Required features
- both angel players can move
- one tiny squad or allied unit logic
- one enemy force / demon group
- clear win condition
- visible fortification reclaim result

### Intended feel
Closer to a **mini magical skirmish** than a big strategy game.

### First-slice acceptance
- both generals can move,
- the Mermaid appears as an ally,
- the ally attacks or helps,
- the players can win,
- one fortification changes to “reclaimed”.

---

## 9. 🧒 Human + agent workflow rule

### Humans do
- approve concepts
- choose between options
- review art
- review behaviour
- reject wrong direction
- decide what matters next

### Agents do
- implement prototypes
- generate draft art assets
- create UI mockups
- revise based on feedback
- document what changed
- propose next steps

### Important rule
**Nothing is “approved” just because an agent made it.**

---

## 10. 📋 Approval gates for agents

Agents should stop for review after each of these:

1. **Prototype plan**
2. **Engine/project setup**
3. **Platforming prototype**
4. **Mermaid recruitment prototype**
5. **Rhythm minigame prototype**
6. **Battle prototype**
7. **Connected first slice**
8. **Art/style revision pass**

Each gate should include:
- parent summary,
- Amelia summary,
- screenshots or GIFs where possible,
- clear next recommendation.

---

## 11. 🖼 Visual-document requirement

All major planning docs and agent updates should be easy to skim and should include some combination of:
- emoji section markers,
- checklists,
- short tables,
- simple diagrams,
- screenshots or mockups where useful,
- “for Amelia” summaries.

Avoid giant walls of text when a clearer visual structure is possible.

---

## 12. ✅ First vertical slice checklist

### Must-have
- [ ] Godot project created
- [ ] two angel placeholders controllable
- [ ] one Ancient Rome level scene
- [ ] one Mermaid encounter
- [ ] one Mermaid roster entry / state
- [ ] one easy rhythm screen
- [ ] one visible Mermaid upgrade
- [ ] one tiny battle scene
- [ ] one fortification reclaim result

### Nice-to-have
- [ ] placeholder sound effects
- [ ] sparkly transitions
- [ ] basic save/load
- [ ] lightweight history note about Ancient Rome and mermaids/myth

---

## 13. 🚫 Scope traps to avoid

Do not prematurely add:
- many creatures,
- many worlds,
- long lore,
- complex menus,
- full Pokémon-like systems,
- full tactics systems,
- difficult rhythm gameplay,
- polished production pipelines.

The goal is to **prove the loop**, not build the dream all at once.

---

## 14. 👧 Amelia summary

### Our first game bit is:
- [ ] Rome
- [ ] Mermaid
- [ ] Dance
- [ ] Battle

### Your job:
- [ ] tell us what looks nice
- [ ] tell us what feels fun
- [ ] say “no” if something is wrong
- [ ] help choose what to make next
