# Personal Finance Event — Life-Size "Monopoly × Cashflow 101"

> **Archive / design history.** The live, authoritative rules now live in
> **[game-mechanics.md](game-mechanics.md)** (with [player.md](player.md) and [mentor.md](mentor.md)).
> This file is kept only as the original planning log — some details below (44-space board, old profile
> numbers, etc.) are **superseded** by the post-playtest changes. Links to `number-system.md` and
> `board-and-cards.md` are dead — that content was merged into `game-mechanics.md`.

A running summary of the planning discussion (migrated from the Gemini chat).

---

## 1. The Concept

Host a personal-finance event for **college students**, built as a **life-size board game** combining **Monopoly** (move around a board, buy properties, draw event cards) and **Cashflow 101** (each player has a financial statement, earns income, builds passive income to escape the "rat race").

- **Audience:** college students, **30 participants max**
- **Teams:** **6 teams of 5**, each with its own financial statement
- **Focus topics:** debt & cashflow management; behavioral finance & wealth accumulation
- **A guest speaker** will be invited (topic TBD — see topic menu below).

### The signature twist: a live, independent market
A **dashboard projected on a whiteboard** shows a live **stock market** (a few individual stocks + a stock index chart) and **business news**. Crucially, the market moves **on its own timer, independently of the board** — news breaks, stocks surge/  crash, businesses gain/lose approval as real time passes. This is designed to create real FOMO, panic-selling, and market-anxiety to teach **behavioral finance**.

---

## 2. Decisions Locked In

### Trading mechanic → **Option C: "Market Trading Window"** (chosen)
Separate board time from trading time to keep realism without overwhelming the bank:
- Teams roll dice and move around the board for a **timed round (~10 min = "one semester")**.
- During the round, the dashboard news/charts move, but **no stock trading is allowed** — teams can only buy properties they land on, pay expenses, and handle event cards. They must *watch* the market move without acting.
- When the timer hits zero, the board pauses and a **~3-min Trading Window** opens: every team can adjust their portfolio, pay debts, or buy index funds at that round's final prices.
- **Behavioral lesson:** watching a stock bleed for 8 minutes before being allowed to sell mimics illiquid/locked-up assets and forces strategy discussion under pressure.

(Rejected: Option A "real-time open market" — too chaotic, overwhelms the bank. Option B "trade only on board spaces" — too restrictive, disconnects teams from the dashboard.)

### Liquid vs. illiquid asset split
- **Stocks + Index Funds → live dashboard** (liquid, prices move constantly).
- **Businesses + Real Estate → physical opportunity cards** drawn when landing on an "Opportunity" space (illiquid, slow). This split *itself* teaches the liquid vs. illiquid distinction.

### Math constraint — "Rule of Zeroes"
- **Every number must be a multiple of $50 or $100.** No granular figures.
- Examples: salary $3,000, rent $1,000, groceries $500.
- Keeps the banker volunteers fast and error-free.

### Savings mechanic — avoid percentage interest
- **Do NOT** use a % savings account (manual interest math per team per round kills the game).
- Use **flat "Term Deposit / Bond" tokens**: lock $1,000 → after 2 trading windows, redeem for $1,200. Flat math.
- Or use the **S&P 500 Index Fund** on the dashboard that ticks up slowly/steadily to teach passive accumulation without custom math.

### Job profiles — **6 archetypes (locked)**
All tuned to the **same ~$1,000 net cash flow** at start (no pay-to-win), but with **deliberately
distinct components + liability balances**. Personality emerges through **forced profile-specific
"Life Happens" cards**. Full numbers in [number-system.md](number-system.md); cards in [board-and-cards.md](board-and-cards.md).
- **The Hustler** — variable side-gig income (absorbs "part-timer"), small gear loan.
- **The Med/Law Student** — high income **+** big student-loan liability ($20k); deepest negative equity, strongest engine.
- **The Scholarship Kid** — low allowance, zero debt, low expenses.
- **The Shopaholic** — decent income, credit-card + BNPL debt, high lifestyle spend.
- **The Wealthy Kid** *(new)* — high allowance **but** high lifestyle expenses (forced premium spends).
- **The Influencer / Social Media** *(new)* — income spikes with virality, spends on gear/image, FOMO-prone.

### Financial statement structure (Cashflow-style, per team)
- **Income:** part-time jobs, internships, parental allowance.
- **Expenses:** rent, food, streaming subscriptions, phone bills.
- **Liabilities:** student loans, credit-card debt, Buy-Now-Pay-Later (BNPL).
- **Assets:** index funds, stocks, side-hustle businesses.

### Board — **44 spaces (locked)**, student-themed
Full sequenced layout + card decks in [board-and-cards.md](board-and-cards.md). Composition:
Opportunity/Deal ×6 · Ownable Asset ×5 · **Skill Up / Invest in Yourself ×3** · Life Happens ×5 ·
Campus Life ×5 · Temptation ×4 · Fixed Bill ×4 · Market News ×3 · Extra Payday ×3 · Tax ×2 · 4 corners.
- **Light ownable assets** (Dorm Sublet, Vending Machine, Food Stall…): buy on landing, pay passive income each payday. No Monopoly colour-sets / house-building (too heavy for 30 in 2 hrs).
- **Skill Up spaces** — the "best asset in your 20s is *you*" theme: pay → **permanent income bump**. Best $-for-$ return on the board, deliberately rivalling stock/asset spending.
- **Payday / Extra Payday:** collect net income (income + passive + skill bumps − expenses).
- **Market News spaces:** flip a scripted dashboard headline (board → live-market link; watch, don't trade).

### Win conditions
- **Primary:** first team whose **passive income > monthly expenses** (escape the rat race).
- **Tie-breaker / time-out:** when total game time ends, **highest net equity (assets − liabilities)** wins.

### Round / time structure — **locked**
- **~2 hrs of play.** Per round: ~2–3 min roll/act per team + a **3-min Trading Window**; arc extended to **~8 rounds** (trim later rounds to fit the clock).
- Speaker runs **~1 hr before** the game (priming) per the brief in §3b.

### Tech / tooling — **locked: hybrid**
- **Google Sheet** for the ledgers: team financial statements + a transaction log (banker picks a team, enters `+$500` / `-$200`, ledger + win-tracker recompute). 5-tab spec below in §6.
- **Projected web dashboard** for the live market — see [dashboard/index.html](dashboard/index.html). Self-contained (opens by double-click), auto-ticks so the market "moves on its own," with a **Trading Window** button that freezes prices for the 3-min trade.

---

## 3. Guest-Speaker Topic Menu (reference)

### Original four
1. **Cash Flow & Debt Management (defensive):** mathematics of debt / compound interest against you, good vs. bad debt, zero-based budgeting, credit-score mechanics.
2. **Wealth Accumulation (offensive):** index funds vs. stock picking, real-estate/REIT basics, real passive income vs. "side hustles."
3. **Behavioral Finance (psychology) — best for a live mixed audience:** lifestyle creep, financial FOMO/speculation, sunk-cost fallacy.
4. **Risk Management:** emergency funds (3–6 months) + insurance, tax efficiency.

> For college students, the guidance was: lead with **Debt Management** and **Behavioral Finance**; behavioral finance resonates universally with a live audience.

### Additional topics that matter for 18–20s (added)
5. **Time value of money / compounding as the hook:** start-at-20 vs start-at-30 graph — the single most motivating concept for this age. This *is* the "investing early" theme, made visceral.
6. **Income & earning power first:** the underrated truth at 20 — the biggest lever isn't cutting RM5 coffees, it's growing income (skills, first salary negotiation, freelancing). Counterintuitive and memorable.
7. **First-paycheck "plumbing":** automating finances — separate accounts, pay-yourself-first, set-and-forget standing instructions. Highly actionable and demo-able.
8. **Scams & financial fraud targeting youth (MY-specific):** crypto/forex "get-rich-quick" schemes, Ponzi, Macau scams, mule-account recruitment. Young people are *the* target demographic — genuinely protective.
9. **"How do I actually start?" walkthrough (MY):** opening a broker, low-cost ETFs, robo-advisors, the RM100 first buy. The game abstracts this; real students freeze at the first step.

> **Design principle:** the speaker should *complement* the game, not repeat it. The game already teaches debt mechanics + behavioral finance through play. The speaker's highest-value role is the real-world bridge the game can't do: *"how do I actually start, in real life, with real money?"*

---

## 3b. Speaker Brief — Zeit Invest (Malaysia, ~1 hr, PRIMING slot)

**Candidate:** Zeit Invest — investing/ETF-focused creator, speaks natively to a Malaysian Gen-Z audience. Strong fit for the "start investing early + how to actually start in MY" angle.

**Slot decision:** Speaker goes **BEFORE the game (priming)**. The job is to plant mental models that students will then *feel* in play — so the game becomes live proof of the talk. The speaker should end each beat with a "watch for this in the game" seed.

**Depth over breadth — the 1-hour rule:** pick ONE narrative arc, not a survey. Below is one story in 4 beats.

| Time | Beat | Priming purpose (seed for the game) |
|------|------|--------------------------------------|
| ~10 min | **The compounding hook** — start-at-20 vs start-at-30 graph | "Time in the market is your unfair advantage — notice it compound across semesters." |
| ~10 min | **The 2 mental models** — assets vs liabilities; liquid vs illiquid | Directly primes the financial statement + the stocks-are-liquid / property-is-illiquid split. |
| ~20 min | **"Start this week" walkthrough (MY)** — which account, which ETF/robo, RM100 first buy (EPF/ASNB context, local brokers, low-cost ETFs) | The unique value only a real practitioner gives; maps to the dashboard index fund + trading window. |
| ~15 min | **The 3 traps that kill young investors** — FOMO/hype, lifestyle creep, scams | "The market dashboard will try to make you panic-sell — I want you to catch yourself doing it." |
| ~5 min | **Q&A + "what to watch for"** | Sets intent before they play. |

**Cut from the 1-hour talk** (each needs its own 30 min — they'd turn the hour into a shallow tour): real estate/REITs, tax efficiency, insurance/ILPs, credit-score mechanics. Let the *game* carry debt; let the *speaker* carry investing-early + behavior.

---

## 4. Stock market — **locked**

8 stocks + 1 index on the live dashboard; bonds/MMF stay as the flat **term-deposit token** (lock
$1,000 → redeem $1,200). ETF + MMF as separate live lanes were **cut** as too much to track.
- **4 stable:** MegaMart, PowerGrid, SafeBank, TeleCom.
- **4 growth:** NovaTech, BioCure, DriveX, **MoonChain** (the meme/bubble that pumps then crashes).
- **1 Index Fund** (S&P-style): steady climb — the "boring wins" anchor.

**Simulation = scripted custom price path, themed on real history** (not a literal historical replay).
Dashboard time = abstract **market sessions, not calendar years** — mapping rounds to 5-year jumps would
smooth out volatility and kill the FOMO/panic effect. So the fictional tickers keep the drama while each
round's *theme + headlines* are drawn from real events (dot-com, 2021 meme mania, 2022 Luna/FTX, 2008
contagion, a **1997 Asian Crisis** nod, COVID V-recovery). The **30-year compounding story stays with the
speaker's slide.** Scripted **8-round arc**: R1 calm → R2 tech rally + MoonChain pump → R3 meme mania →
R4 euphoric peak + first cracks → **R5 CRASH** → R6 second leg down → R7 recovery (rewards index/dip-buyers)
→ R8 finale. Stock prices now move on a **$10 grid** (stocks-only "Rule of Tens"; rest of the economy stays
$50/$100), 4s ticks × 60 sessions/round. Full per-tick path + news in
[dashboard/market-script.json](dashboard/market-script.json) (mirrored in `index.html`).

---

## 5. Bank tooling — Google Sheet 5-tab spec

1. **Profiles** — 1 row/team: profile, starting income/expenses/assets/liabilities, net cash flow (locked template).
2. **Transaction Log** — round, team, type (payday / bill / board event / deal / trade), +/− amount.
3. **Balance Dashboard** — `SUMIF`-driven per team: cash, total assets, liabilities, **net equity**, **passive income vs expenses** (win tracker).
4. **Holdings** — per team: shares per stock/index + term deposits.
5. **Market Prices** — each round's closing price per instrument; Holdings value = `shares × price` (the market↔ledger link).

> A mentor reads the dashboard's round-closing prices, logs trades in the Transaction Log, and
> Holdings/Balance recalc automatically.

---

## 6. Resolved questions (was "Open Questions")

- [x] **Game scope:** stock market is the only live/independent element; businesses & real estate are land-on Opportunity/Deal cards (illiquid).
- [x] **Round structure:** ~8 rounds (board phase + 3-min trading window each), ~2 hrs+ total play.
- [x] **Exact numbers:** designed in [number-system.md](number-system.md) (Rule of Zeroes).
- [x] **The dashboard:** self-contained web app, auto-ticking, scripted prices + timed news ([dashboard/](dashboard/)).
- [x] **Bank logistics:** Google Sheet (5 tabs above); trades logged by mentor in the 3-min window.
- [x] **Event cards:** decks designed in [board-and-cards.md](board-and-cards.md).
- [x] **Speaker slot:** before the game (priming) — see §3b.
- [ ] **Still open:** exact volunteer headcount; final print/production of board + cards; stock detail tuning (flagged for later).

---

## 7. Artifacts in this repo

- [number-system.md](number-system.md) — all figures: profiles, assets, skill-ups, stocks, term deposits.
- [board-and-cards.md](board-and-cards.md) — 44-space sequence + all card decks.
- [dashboard/index.html](dashboard/index.html) + [dashboard/market-script.json](dashboard/market-script.json) — projected live market.
- **Google Sheet** — import-ready package in [sheet/](sheet/) (5 CSVs + [sheet/README.md](sheet/README.md) with all formulas). Live seeded copy ("Profiles" tab) created in Drive: [Finance Game — Team Ledger](https://docs.google.com/spreadsheets/d/129Tafhy5raa2vrx3oItibB4n_O8Bxap-IaCg6O-0fBo/edit).
