# Tenshi Game — Project Intent

**Version:** 0.2  
**Date:** 2026-10-31  
**Working title:** Tenshi Game  
**Co-creators:** Amelia + parent  
**Delivery mode:** AI-assisted, spec-driven development with Codex CLI + Claude Code

---

## 🎯 One-sentence promise

Make a **bright, cute, two-player anime game** where two angel heroes explore a playful historical world, befriend a magical creature, power it up with a simple rhythm game, and then use it in a tiny co-op battle — while Amelia learns how to guide AI.

---

## 🌟 Our north star

This project is **two things at once**:

1. **A little game**
2. **A little learning adventure about AI**

That means:
- agents do the implementation work,
- humans choose what gets made,
- Amelia gets to approve, reject, and redirect ideas,
- every milestone should be explainable in a friendly, visual, bite-size way.

---

## ✅ Agreed project decisions

### Creative direction
- **Genre mix:** platforming + rhythm + battle
- **Players:** 2-player co-op is core
- **Main characters:** two angels / little Tenshi
  - one pretty anime-style female angel
  - one cute young boy angel
- **Style:** bright, colourful, cute, anime, thick outlines, juicy feedback
- **Tone:** fun, playful, magical, lightly educational, low-stress

### Inspiration touchstones
Use these as **inspiration**, not things to copy:
- **Mario** → approachable side-scrolling structure
- **Kirby** → friendliness, charm, easy onboarding
- **Pokémon** → creature collection / growing your team
- **Magical girl anime** (e.g. Cardcaptor Sakura, Madoka Magica, Prisma Illya) → transformation, sparkle, charm, magic
- **KPop Demon Hunters** → energetic pop-magic vibe, team identity, stylish supernatural conflict

### Story direction
- The angels serve a goddess.
- Demons have pushed too far toward heaven.
- The heroes must restore **balance**, not wipe out evil completely.
- Amelia rejected the earlier bad-ending idea.
- Restoring balance gives the **happy ending**.

### Educational approach
- Child-facing material must be simple, visual, and short.
- The AI should show options, not take over.
- Amelia should be given meaningful choices.
- Adults supervise technical setup, safety, permissions, and reviews.

---

## 🧪 Super narrow scope for the first playable slice

**We are deliberately making the first version tiny.**

### First world
- **Ancient Rome** ✅

### First creature
- **Mermaid** ✅

### First playable slice
Build only this loop:

1. **Explore** one very short Ancient Rome side-scrolling level
2. **Meet / recruit** one Mermaid
3. **Play** one easy rhythm minigame
4. **Upgrade** the Mermaid once
5. **Fight** one tiny co-op battle
6. **Reclaim** one fortification

If that works and feels fun, the foundation is proven.

---

## 🛠 Engine decision

### Recommended engine: **Godot 4** ✅

**Why Godot is the best fit right now:**
- much better suited than a custom web stack for a 2D game with multiple gameplay modes,
- faster to prototype platforming, menus, battle scenes, save data, and co-op controls,
- strong fit for agentic development because tasks are easy to split into scenes/scripts,
- can still target desktop first and potentially web export later.

### Working platform plan
- **Primary prototype target:** PC / local build
- **Secondary target later:** browser export if practical

So: **Godot first, web deployment later if helpful**.

---

## 🧱 Non-negotiable guardrails

- Do **not** expand scope before the first tiny loop works.
- Do **not** replace human-approved design with agent assumptions.
- Do **not** remove 2-player co-op from the core vision.
- Do **not** make the first slice hard, punishing, or mechanically busy.
- Do **not** require Amelia to read dense technical material.
- Do **not** create lots of content before the first slice is fun.
- Do **not** publish, merge major changes, or add risky dependencies without adult approval.

---

## 📦 What “done enough” means for v0.1

The first slice is successful if:
- two players can control one angel each,
- they can play a tiny Ancient Rome stage,
- they can recruit one Mermaid,
- they can complete one very easy rhythm interaction,
- the Mermaid becomes stronger in a visible way,
- they can win one tiny battle together,
- the game clearly shows that one fortification was reclaimed.

---

## 👧 Amelia-friendly summary

### We are making:
- [ ] two angel heroes
- [ ] one Rome level
- [ ] one Mermaid friend
- [ ] one dance
- [ ] one battle

### Then later we can add:
- [ ] more places
- [ ] more creatures
- [ ] more dances
- [ ] more battles

**Tiny first. Big later.**
