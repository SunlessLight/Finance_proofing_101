# Game Mechanics — Life-Size "Monopoly × Cashflow 101"

**A personal-finance event for college students.** This is the single, complete reference for the whole
game: the **board**, the **cards**, the **stock market**, and the **financial statement** that ties them
together — plus how players play and how mentors run the money. If you've never been part of planning
(e.g. a teacher or a new volunteer), read this top to bottom and you'll understand everything.

Companion docs: **[player.md](player.md)** (one-page player handout) · **[mentor.md](mentor.md)** (banker
operating manual) · **[dashboard/index.html](dashboard/index.html)** (the projected live market).

---

## 1. What this game is

A life-size board game that fuses **Monopoly** (move around a board, buy things, draw event cards) with
**Cashflow 101** (each team runs a financial statement, earns income, and builds passive income to
"escape the rat race"). Teams of students play ~8–13 rounds while a **live stock market ticks on its own**
on a projected dashboard.

**The signature twist — a live, independent market.** A dashboard projected on a screen shows stocks and
an index moving on their *own* timer, independent of the board. News breaks, prices surge and crash as
real time passes — but teams **can only trade during a short window each round**. Watching an asset bleed
before you're allowed to act is the engine for teaching **behavioral finance** (FOMO, panic-selling).

**The three things players should feel:**
1. **Debt & cashflow management** — good vs. bad debt, why net cashflow matters more than income.
2. **Behavioral finance** — FOMO, hype, lifestyle creep, the cost of panic-selling and over-trading.
3. **Wealth accumulation** — passive income, compounding, and that the best early investment is *yourself*.

**Design principle — "Rule of Zeroes":** every figure is a multiple of **$50 / $100** so banker
volunteers stay fast and error-free. **One exception:** stock prices move on a **$10 grid** ("Rule of
Tens" — stocks only, so swings feel like a real market). Use `$` or `RM` 1:1 at print time.

### The three parts, and how they connect

```
   BOARD  ───────────►  buy assets / skills, pay bills, draw cards, collect paydays
   CARDS  ───────────►  Life Happens · Campus Life · Temptation · Opportunity deals · Market News
   STOCK MARKET ─────►  live dashboard prices, traded only in the round's Trading Window
        │                         │                          │
        └─────────────┬──────────┴──────────────┬───────────┘
                      ▼                          ▼
              FINANCIAL STATEMENT  (Income · Expenses · Assets · Liabilities)
                      ▼
              Win = Passive Income ≥ Monthly Expenses  (escape the rat race)
```

Everything a team does on the board or in the market lands on **one financial statement per team**
(a Google Sheet, Cashflow-101 style). That statement is the scoreboard.

---

## 2. Logistics, roles & run-of-show

| Item | Value |
|---|---|
| Audience | College students |
| Participants | **30 max** |
| Teams | **6 teams of 5** |
| Total play time | **~2 hours** |
| Rounds | **~8 rounds** ("semesters") expected; the market script runs **up to 13** so fast teams don't run out |
| Dice | **Two dice, summed** (no doubles bonus) — a 36-space lap is ~5 throws |
| Guest speaker | **~1 hr, BEFORE the game** (priming) |

**Roles**
- **MC / Facilitator** — runs the clock, calls round starts/ends, opens the Trading Windows.
- **Bankers / Mentors** — operate the Google Sheet ledger; log every cash move and trade. See
  [mentor.md](mentor.md). Suggest ≥1 banker per 2–3 teams.
- **Market Operator** — runs the projected dashboard (play/pause, advance rounds, open Trading Window)
  and changes the **one round-driver cell** in the sheet at each round close (§6).

**Run-of-show**

| Time | Segment |
|---|---|
| 0:00–0:20 | Arrival, team formation (6×5), hand out profiles + financial statements |
| 0:20–1:20 | **Guest speaker (priming)** — compounding hook, assets vs liabilities, "start this week" (MY), the 3 traps (FOMO / lifestyle creep / scams). Ends with "watch for this in the game." |
| 1:20–1:35 | Rules briefing + practice turn; market operator demos the dashboard |
| 1:35–3:35 | **The game — ~8–13 rounds** (board phase + 3-min Trading Window each) |
| 3:35–3:55 | **Debrief** — final net equity, who escaped; tie game moments back to the speaker's three traps |

**Materials:** printed board (36 tiles, **45cm × 45cm** each), team financial statements, **two dice**,
money/tokens, printed card decks, term-deposit tokens, projector + screen, laptop running the dashboard,
banker laptop(s) with the Google Sheet.

---

## 3. How a round works

**Each round has two phases:**

1. **Board phase (~2–3 min/team).** Teams take turns: **roll two dice → move → resolve the space.**
   Passing or landing on **START** or an **Extra Payday** collects net cashflow. During this phase the
   dashboard market moves and news breaks, but **no trading is allowed** — teams can only watch.
2. **Trading Window (3 min).** The board pauses; the market **freezes** at the round's closing prices.
   Every team may buy/sell stocks and the index fund, lock/redeem term deposits, pay down debt, or sell a
   deal. When time is up, the next round begins.

**The behavioral lesson:** teams watch a stock pump or crash for minutes before they're allowed to act,
mimicking illiquid/locked assets and forcing them to plan instead of reacting impulsively.

**Liquid vs. illiquid (this split is itself a lesson):**
- **Liquid → the live dashboard:** stocks + index fund; prices move constantly; traded each window.
- **Illiquid → physical cards:** businesses & real estate (Opportunity deals) are slow; they can only be
  sold in a Trading Window and **resell at half price** unless a Market News card offers a buyer (§5.5).

---

## 4. The Board — 36 spaces

A square board: **4 corners + 4 sides × 8 spaces.** Corners are at positions **1, 10, 19, 28**. Movement
is clockwise. There are **no "dead" corners** — START is the only special corner; the other three are
active spaces (Vending Machine, an Opportunity, Food Stall), so every landing does something.

### 4.1 Space-type catalog

| Type | Count | What happens |
|---|---|---|
| **START / Payday** (corner) | 1 | Pass or land → collect net cashflow |
| **Ownable Asset** | 7 | Buy on landing; pays passive income every payday; charges **landing rent** if already owned (§4.3) |
| **Skill Up / Invest in Yourself** | 4 | Pay → **permanent** income bump every payday |
| **Opportunity / Deal** | 6 | Draw a Small/Big Deal card (illiquid asset → passive income) |
| **Life Happens** (Chance) | 4 | Draw from your **profile's** sub-deck (2 out / 2 in / 1 skill-up) |
| **Campus Life** (Community Chest) | 3 | Draw a shared social event card (gain or loss) |
| **Temptation** (Doodad) | 2 | Discretionary spend ($50–$300 per card) |
| **Fixed Bill** | 2 | Pay a recurring bill (phone / rent top-up) |
| **Market News** | 3 | Draw a **buyer-offer** card — lets a deal owner sell at a premium (§5.5) |
| **Extra Payday** | 3 | Collect net cashflow mid-lap |
| **Tax** | 1 | Income Tax ($200) |

### 4.2 Full space sequence (1–36)

| # | Space | Type | Effect |
|---|---|---|---|
| **1** | START — "New Semester" | Corner/Payday | Collect net cashflow |
| 2 | Life Happens | Chance | Draw your profile sub-deck |
| 3 | Online Shop | Ownable Asset | Buy $1,000 → +$300/payday |
| 4 | Temptation | Doodad | Pay $50–$300 |
| 5 | Opportunity | Deal | Draw Small/Big Deal |
| 6 | Campus Laundromat | Ownable Asset | Buy $3,500 → +$1,050/payday |
| 7 | Online Course | Skill Up | Pay $500 → +$150/payday permanent |
| 8 | Campus Life | Community Chest | Draw card |
| 9 | Market News | News | Draw a buyer-offer card |
| **10** | Vending Machine | Corner/Ownable Asset | Buy $1,500 → +$450/payday |
| 11 | Opportunity | Deal | Draw Small/Big Deal |
| 12 | Life Happens | Chance | Profile sub-deck |
| 13 | Extra Payday | Payday | Collect net cashflow |
| 14 | Income Tax | Tax | Pay $200 |
| 15 | Dorm Sublet | Ownable Asset | Buy $2,000 → +$600/payday |
| 16 | Opportunity | Deal | Draw Small/Big Deal |
| 17 | Professional Certification | Skill Up | Pay $1,000 → +$300/payday permanent |
| 18 | Extra Payday | Payday | Collect net cashflow |
| **19** | Opportunity | Corner/Deal | Draw Small/Big Deal |
| 20 | Campus Life | Community Chest | Draw card |
| 21 | Parking Spot | Ownable Asset | Buy $2,500 → +$750/payday |
| 22 | Life Happens | Chance | Profile sub-deck |
| 23 | Phone Bill | Fixed Bill | Pay $100 |
| 24 | Coding Bootcamp | Skill Up | Pay $1,500 → +$450/payday permanent |
| 25 | Opportunity | Deal | Draw Small/Big Deal |
| 26 | Market News | News | Draw a buyer-offer card |
| 27 | Extra Payday | Payday | Collect net cashflow |
| **28** | Food Stall | Corner/Ownable Asset | Buy $3,000 → +$900/payday |
| 29 | Life Happens | Chance | Profile sub-deck |
| 30 | Temptation | Doodad | Pay $50–$300 |
| 31 | E-bike Rental Fleet | Ownable Asset | Buy $4,000 → +$1,200/payday |
| 32 | Opportunity | Deal | Draw Small/Big Deal |
| 33 | Marketing Course | Skill Up | Pay $2,000 → +$600/payday permanent |
| 34 | Campus Life | Community Chest | Draw card |
| 35 | Rent Top-up | Fixed Bill | Pay $300 |
| 36 | Market News | News | Draw a buyer-offer card |

### 4.3 Ownable assets & landing rent

The 7 ownable-asset spaces are bought **on landing** (one owner per space, no Monopoly colour-sets or
house-building). Each pays its owner passive income **every payday** — about **30% of the buy price**, so
the asset pays for itself in ~3–4 paydays:

| Asset (space) | Buy price | Passive / payday | **Landing rent if owned** |
|---|---|---|---|
| Online Shop (3) | $1,000 | $300 | $150 |
| Campus Laundromat (6) | $3,500 | $1,050 | $500 |
| Vending Machine (10) | $1,500 | $450 | $200 |
| Dorm Sublet (15) | $2,000 | $600 | $300 |
| Parking Spot (21) | $2,500 | $750 | $350 |
| Food Stall (28) | $3,000 | $900 | $450 |
| E-bike Rental Fleet (31) | $4,000 | $1,200 | $600 |

**Landing rent (Monopoly-style).** When a team lands on an asset space someone **else** already owns, the
visitor pays the owner **half that space's passive income** (rounded down to the $50 grid — the table
above) as a one-time payment. This rewards owning assets *twice*: a payday stream **and** rent from
visitors. (Rent applies only to the 7 board asset spaces — Opportunity deals are cards, not spaces, so
they have no rent.)

### 4.4 Skill Up — invest in yourself

A **top $-for-$ return on the board** — like assets and Opportunity deals (also ~30%), a skill pays back
in ~3 paydays, then pure profit. This is the "income is your biggest lever at 20 / the best asset is
*you*" lesson, made mechanical. The catch: the bump is a **permanent** active-income increase that does
**not** count toward escaping (see §9) — so skills *grow your payday so you can buy passive assets
faster*, while assets/deals are what actually win the game.

| Skill space | Cost | **Permanent** income bump / payday |
|---|---|---|
| Online Course (7) | $500 | +$150 |
| Professional Certification (17) | $1,000 | +$300 |
| Coding Bootcamp (24) | $1,500 | +$450 |
| Marketing Course (33) | $2,000 | +$600 |

Teams also get **extra skill chances from the Life Happens decks** (each profile has one free
**+$100/payday** skill-up card — §5.1).

---

## 5. Cards

### 5.1 Life Happens — profile sub-decks (forced, per profile)

When a team lands on Life Happens, they draw from **their own profile's** deck. Every deck is exactly
**5 cards: 2 cash-out, 2 cash-in, 1 skill-up** (a free **+$100/payday** permanent bump). This is where
profile personality bites, and it sprinkles "invest in yourself" moments across the game.

**Hustler**

| # | Type | Card | Effect |
|---|---|---|---|
| 1 | Cash out | Client ghosted you — a gig falls through | Lose $500 this payday |
| 2 | Cash out | Burnout from juggling gigs | Pay $300 to recover |
| 3 | Cash in | Side-gig goes viral | Collect $1,000 |
| 4 | Cash in | A repeat client signs a retainer | Collect $500 |
| 5 | Skill-up | Free freelance masterclass | **+$100/payday** permanent (add as Income row) |

**Med/Law Student**

| # | Type | Card | Effect |
|---|---|---|---|
| 1 | Cash out | Exam fees + textbooks | Pay $500 |
| 2 | Cash out | Stress-related health issue | Pay $300 |
| 3 | Cash in | Top of the class — research stipend | Collect $500 |
| 4 | Cash in | Paid teaching-assistant shift | Collect $300 |
| 5 | Skill-up | Free clinical-skills workshop | **+$100/payday** permanent (add as Income row) |

**Scholarship Kid**

| # | Type | Card | Effect |
|---|---|---|---|
| 1 | Cash out | Family needs help back home | Pay $300 |
| 2 | Cash out | Laptop repair before finals | Pay $200 |
| 3 | Cash in | Scholarship excellence bonus | Collect $500 |
| 4 | Cash in | Won a case-competition prize | Collect $300 |
| 5 | Skill-up | Free online certification — scholarship perk | **+$100/payday** permanent (add as Income row) |

**Shopaholic**

| # | Type | Card | Effect |
|---|---|---|---|
| 1 | Cash out | BNPL bill comes due | Pay $400 |
| 2 | Cash out | "Limited drop" — you must buy it | Pay $300 |
| 3 | Cash in | Returned an impulse buy | Collect $200 |
| 4 | Cash in | Sold old clothes online | Collect $300 |
| 5 | Skill-up | Free personal-finance bootcamp | **+$100/payday** permanent (add as Income row) |

**Wealthy Kid**

| # | Type | Card | Effect |
|---|---|---|---|
| 1 | Cash out | Friends' overseas trip — FOMO, you go | Pay $1,000 |
| 2 | Cash out | You treat the whole group | Pay $300 |
| 3 | Cash in | Allowance bonus from parents | Collect $500 |
| 4 | Cash in | Sold a designer item | Collect $300 |
| 5 | Skill-up | Family pays for an executive course | **+$100/payday** permanent (add as Income row) |

**Influencer**

| # | Type | Card | Effect |
|---|---|---|---|
| 1 | Cash out | A post flops + algorithm change | Lose $500 income this payday |
| 2 | Cash out | Gear upgrade to stay relevant | Pay $500 |
| 3 | Cash in | Brand deal! A sponsor pays big | Collect $1,000 |
| 4 | Cash in | Follower-milestone bonus | Collect $300 |
| 5 | Skill-up | Free content-creator workshop | **+$100/payday** permanent (add as Income row) |

### 5.2 Campus Life (Community Chest) — shared deck

Mixed social gains/losses, same for everyone (10 cards):

| # | Card | Effect |
|---|---|---|
| 1 | Won a hackathon | Collect $500 |
| 2 | Group project — you covered materials | Pay $200 |
| 3 | Landed a tutoring gig | Collect $300 |
| 4 | Cracked phone screen | Pay $200 |
| 5 | Birthday money from relatives | Collect $300 |
| 6 | Society membership fees | Pay $100 |
| 7 | Helped a junior → referral bonus | Collect $200 |
| 8 | Caught a cold during finals | Pay $100 |
| 9 | Won a scholarship raffle | Collect $400 |
| 10 | Treated friends to a meal | Pay $150 |

### 5.3 Temptation (Doodad) — shared deck ($50–$300)

Discretionary spend, same for everyone (6 cards):

| # | Card | Effect |
|---|---|---|
| 1 | Midnight bubble-tea run for the squad | Pay $50 |
| 2 | Concert tickets just dropped | Pay $300 |
| 3 | A sale you can't resist | Pay $200 |
| 4 | New phone case + accessories | Pay $100 |
| 5 | Food-delivery binge week | Pay $150 |
| 6 | Impulse subscription | Pay $50 now **and** $50 again next payday |

### 5.4 Opportunity / Deal cards (illiquid assets → passive income)

Teams choose to **buy or pass**. Assets are **illiquid**: sellable only in a Trading Window, at **half
price** unless a Market News buyer card offers a premium (§5.5).

| Small Deal | Cost | Passive/payday | | Big Deal | Cost | Passive/payday |
|---|---|---|---|---|---|---|
| Resell sneakers online | $500 | $150 | | Small e-commerce brand | $3,000 | $900 |
| Used-textbook flipping | $500 | $150 | | Laundromat share | $4,000 | $1,200 |
| Print-on-demand store | $500 | $150 | | Co-own a campus cafe | $4,000 | $1,200 |
| Vending route add-on | $1,000 | $300 | | Rental room near campus | $5,000 | $1,500 |
| Tutoring service | $500 | $150 | | Food-truck share | $3,000 | $900 |
| Event photography gigs | $1,000 | $300 | | Co-working desk rental | $5,000 | $1,500 |

(6 Small + 6 Big = 12 deal cards.)

### 5.5 Market News — buyer offers (the Cashflow-101 "sell the deal" mechanic)

The 3 Market News board spaces draw from a **buyer-offer deck** (one card per deal, 12 total). Each card
is an investor offering to buy a specific business at a **~1.5× premium**:

| # | Buyer offer | Sells which deal | Cost → Sale price |
|---|---|---|---|
| 1 | An investor wants to buy your sneaker-resale business | Resell sneakers online | $500 → **$800** |
| 2 | A bookstore wants your textbook-flipping operation | Used-textbook flipping | $500 → **$800** |
| 3 | A brand wants to acquire your print-on-demand store | Print-on-demand store | $500 → **$800** |
| 4 | A vendor wants to buy out your vending route | Vending route add-on | $1,000 → **$1,500** |
| 5 | A learning center wants your tutoring service | Tutoring service | $500 → **$800** |
| 6 | An agency wants your event-photography gigs | Event photography gigs | $1,000 → **$1,500** |
| 7 | A retailer wants to acquire your e-commerce brand | Small e-commerce brand | $3,000 → **$4,500** |
| 8 | An operator wants to buy your laundromat share | Laundromat share | $4,000 → **$6,000** |
| 9 | A chain wants to buy out your campus cafe | Co-own a campus cafe | $4,000 → **$6,000** |
| 10 | A landlord wants to buy your rental room | Rental room near campus | $5,000 → **$7,500** |
| 11 | A franchise wants your food-truck share | Food-truck share | $3,000 → **$4,500** |
| 12 | A property firm wants your co-working desks | Co-working desk rental | $5,000 → **$7,500** |

**How it plays:**
- If the **drawing team owns** that exact deal, they may sell it now for the offered (premium) price — a
  capital gain, and the lesson: a great illiquid asset is worth far more when a *buyer appears* than at the
  forced half-price fire-sale.
- If the drawing team **doesn't own it**, they may **sell/auction the card** to the team that does (the
  two teams agree a price). This keeps the mechanic alive across a short game, where a perfect
  draw-owns-it match is otherwise rare.
- Selling: the owner collects the premium; the deal's income stops (remove its asset line).

> Note: these board **Market News buyer cards** are separate from the **dashboard news headlines** (§6),
> which narrate the stock-market story on their own timer. The board space no longer flips a dashboard
> headline — the dashboard runs its own news.

---

## 6. The Stock Market

**8 stocks + 1 index fund on the live dashboard.** Bonds/MMF are handled by a flat **term-deposit token**
(below). Stock prices move on a **$10 grid** (Rule of Tens) — ~$10–30 per round so swings feel like a real
market; trades stay clean (shares × a $10-multiple price).

**Objectives / what the market teaches:** the steadily-climbing **S&P 500** rewards patience ("boring
wins"); **Dogecoin** pumps then craters to punish FOMO; the **R6 crash** punishes those who chased hype;
the locked Trading Window forces strategy over reaction; the **trading fee** (below) punishes churning; and
the **stable-stock dividends** (below) teach *income vs. growth* — a slow, lower-risk cashflow play that
keeps paying even through the crash. **The tickers are real-world examples** so the session doubles as "what
kind of asset is this in real life" (an **ℹ Stock Info** button on the dashboard describes each one).

| Instrument (real-life example) | Type | Start | Div/share | Behaviour across R1–R13 |
|---|---|---|---|---|
| 99 Speedmart | Stable (retail) | $100 | **$5** | Low swings; dips when capital chases crypto (R3) and on cost inflation (R10) |
| Tenaga | Stable (utility) | $110 | **$5** | Flat-ish; safe-haven bid in the crash, big rally on the R10 energy spike |
| Maybank | Stable (bank) | $140 | **$5** | Dips on the probe/crash (R5–R6), recovers, slips again on R12 rate cuts |
| Maxis | Stable (telco) | $90 | **$5** | Slow, steady; defensive bid in the panic (R7–R8) |
| Nvidia | Growth (tech / AI) | $130 | — | Rallies hard, crashes hard, leads the recovery, AI boom #2 (R12) |
| Moderna | Growth (biotech) | $100 | — | Drifts low; binary FDA-approval breakout (R11) |
| Tesla | Growth (EV hype) | $140 | — | Hype run-up to R4, sharp fall in the crash, EV-demand slump |
| **Dogecoin** | Meme / crypto | **$40** | — | **$40 → ~$290 peak (R5) → ~$20 crash** — the FOMO trap |
| **S&P 500** | Index fund | $100 | — | **Steady climb $100 → ~$230**, never crashes — "boring wins" |

**How it moves — scripted, themed on real history (not a literal replay).** Dashboard time is abstract
**market sessions**, not calendar years. Each round's *theme + headlines* are drawn from real events
(dot-com / AI boom, 2021 meme mania, 2022 Luna/FTX, 2008 contagion, a 1997 Asian-Crisis nod, COVID-style
V-recovery, an energy crisis). The 13-round arc:

1. **R1 — calm** intro · 2. **R2 — AI/tech rally** (Nvidia) · 3. **R3 — crypto mania** (Dogecoin pumps) ·
4. **R4 — EV hype** (Tesla goes vertical) · 5. **R5 — euphoric peak** + first cracks · 6. **R6 — CRASH**
(crypto bubble bursts, contagion) · 7. **R7 — second leg down** · 8. **R8 — capitulation** (dividends
shine) · 9. **R9 — recovery** (rewards index/dip-buyers) · 10. **R10 — energy spike** (Tenaga rallies) ·
11. **R11 — biotech breakthrough** (Moderna FDA) · 12. **R12 — AI boom #2** (Nvidia) · 13. **R13 — finale**
(S&P 500 leads; Dogecoin near zero).

The auto-ticking dashboard (`dashboard/index.html`) shows a 3×3 grid of 9 mini-charts + a news banner; the
operator uses **Play/Pause**, **Next round**, **Open Trading Window**. Full per-tick path + timed news live
in [dashboard/market-script.json](dashboard/market-script.json).

**The news engine (teach players to read the news).** Each round is driven by one clear **riser** and one
clear **faller**, tied to its headlines:
- **In the Trading Window**, two **🔮 Upcoming** lines preview the *next* round — one stock hinted to rise,
  one to fall — so teams can position *before* the move. (Across the 13 rounds every stock gets its turn as
  a featured riser or faller.)
- **During the round**, the matching headline breaks: the news box **flashes red** and the affected stock
  cards **blink** (green = rising, maroon = falling). The riser fires early, the faller later.
- The lesson is **balance**: when one sector jumps, a rival sector usually dips (rate cut → banks & retail
  up; crypto crash → safe-haven index up). Yet across all the noise the **S&P 500 quietly grinds upward to
  the end** — the payoff for patient, diversified holding.

**Trading fee (anti-churn).** Each stock trade (buy *or* sell) costs a flat **$50 brokerage fee**. This
makes constant in-and-out trading expensive and rewards buy-and-hold (especially the index). It also
mirrors real spreads/commissions. *(See the behavioral note in §9.)*

**Dividends (the income-vs-growth lesson).** The **4 Stable stocks** (99 Speedmart, Tenaga, Maybank,
Maxis) each pay a **fixed $5 per share, every payday**. The Growth stocks, Dogecoin, and the S&P 500 pay
**nothing** — a lesson in itself: *mature, stable companies pay dividends; growth companies reinvest;
speculation pays nothing.* Three things make this teach the right ideas:

- **It's a fixed dollar amount, so the *yield* floats.** $5 on a $90 Maxis is a ~5.5% yield; $5 on a
  pricey $160 Maybank is ~3%. The dashboard shows each stable stock's live yield — watch it **rise as the
  price falls in the R6 crash** (same $5 ÷ a lower price). That's how real dividend yields move.
- **You get paid to wait.** Because the $5 never changes, a stable stock keeps paying right through the
  crash while its price dips — the cushion that makes dividend investing a calmer, beginner-friendly way to
  build **cashflow**. This *counts as passive income* toward escaping the rat race (§9).
- **It's deliberately a *slow* engine, not a dominant one.** At ~3–5.5% per payday it sits well below board
  assets/Opportunity deals (~30% per payday), so a dividend portfolio is a genuine but **secondary**
  cashflow stream — never strictly better than buying a deal. Dividends are collected **automatically at
  payday** (folded into net cashflow, like all passive income — no separate step).

**Term Deposit / Bond token (flat, no live chart, no per-round %):**
- Lock **$1,000 → redeem $1,100** after 2 trading windows (and **$2,000 → $2,200**).
- Deliberately a **low, safe** return — clearly below the index's long-run climb, so it teaches "safe =
  lower return, but it never crashes." Flat math keeps bankers fast.

### How the market links to the ledger (the auto-price formula)

Every team's stock value lives in the sheet's **Holdings** tab (`shares × Current Price`). The **Current
Price** of all 9 instruments is driven by **one cell**: the **round driver** in the Market Prices tab.

- The 13 rounds of official **closing prices** (from `market-script.json`) are stored in the sheet.
- At each round close, the **Market Operator changes the single driver cell** to the new round number;
  all 9 prices jump to that round's close and every team's holdings revalue automatically.
- No more typing 9 prices each round. Full formula in [mentor.md](mentor.md) (§ one-time sheet setup).

---

## 7. The 6 Financial Profiles

All six start at the **same ~$1,000 net cashflow** (no pay-to-win) and **$2,000 cash**, but with
deliberately **distinct income/debt/lifestyle mixes** and **liability balances** — so each team faces a
different strategic problem. Personality then emerges through the forced **Life Happens** decks (§5.1).

| Profile | Salary/Allowance | Side income | Total income | Living | Lifestyle/Subs | Debt payment | Total expenses | **Net** | Liability balance |
|---|---|---|---|---|---|---|---|---|---|
| **Hustler** | $500 | $2,500 | $3,000 | $1,500 | $300 | $200 | $2,000 | **$1,000** | Gear loan $2,000 |
| **Med/Law Student** | $3,500 | $0 | $3,500 | $1,900 | $200 | $400 | $2,500 | **$1,000** | Student loan $16,000 |
| **Scholarship Kid** | $1,800 | $0 | $1,800 | $700 | $100 | $0 | $800 | **$1,000** | None |
| **Shopaholic** | $3,000 | $0 | $3,000 | $1,000 | $600 | $400 | $2,000 | **$1,000** | Credit card $3,000 + BNPL $1,000 |
| **Wealthy Kid** | $4,000 | $0 | $4,000 | $2,000 | $1,000 | $0 | $3,000 | **$1,000** | None |
| **Influencer** | $3,000 | $500 | $3,500 | $1,200 | $800 | $500 | $2,500 | **$1,000** | Gear loan $4,000 + Phone $1,000 |

### Debt mechanic — % of balance, $50 clean steps

Each liability's monthly payment = **a fixed rate × its remaining balance**, so it **shrinks as the debt
is paid down** while staying on the grid:
- **10% liabilities** (consumer/high-interest — gear, credit card, BNPL, phone, forced personal loans):
  repay **$500 → payment −$50**.
- **2.5% liability** (the student loan, low-interest): repay **$2,000 → payment −$50**.

### Starting net equity (the tie-breaker)

Each profile also starts with **profile-flavored net-worth assets** (laptop, savings…) on top of the
$2,000 cash. They add to net equity but pay **$0 income**, so the $1,000 net cashflow stays equal.

| Profile | Cash | + Assets | − Liabilities | = **Net equity** |
|---|---|---|---|---|
| Wealthy Kid | $2,000 | $2,000 | $0 | **+$4,000** |
| Scholarship Kid | $2,000 | $2,000 | $0 | **+$4,000** |
| Hustler | $2,000 | $2,000 | $2,000 | **+$2,000** |
| Influencer | $2,000 | $4,000 | $5,000 | **+$1,000** |
| Shopaholic | $2,000 | $2,000 | $4,000 | **$0** |
| Med/Law Student | $2,000 | $1,500 | $16,000 | **−$12,500** |

Teaching tension: the Med/Law student is "broke" today but has the strongest income engine and the
lowest-rate debt; the Wealthy Kid looks comfortable but bleeds $3,000/payday in lifestyle; the Shopaholic's
net worth is "fake" (depreciating wardrobe/gadgets) and offset by debt.

### Detailed profile statements
Every line sums to the totals in the §7 summary table. Liabilities show **balance @ rate → monthly
payment**; assets pay **$0 income** (they only lift net equity).

**Hustler**

| Category | Item | Amount |
|---|---|---|
| Income | Café job | $500 |
| Income | Freelance | $1,500 |
| Income | Reselling | $1,000 |
| Living | Rent | $900 |
| Living | Groceries | $400 |
| Living | Transport | $200 |
| Lifestyle | Software | $150 |
| Lifestyle | Eating out | $150 |
| Debt | Gear loan | $2,000 @ 10% → $200/payday |
| Asset | Laptop & gear | $1,500 |
| Asset | Savings | $500 |

**Med/Law Student**

| Category | Item | Amount |
|---|---|---|
| Income | Clerkship stipend | $3,500 |
| Living | Rent near hospital | $1,400 |
| Living | Groceries | $300 |
| Living | Commute | $200 |
| Lifestyle | Streaming | $100 |
| Lifestyle | Gym | $100 |
| Debt | Student loan | $16,000 @ 2.5% → $400/payday |
| Asset | Equipment & textbooks | $1,000 |
| Asset | Savings | $500 |

**Scholarship Kid**

| Category | Item | Amount |
|---|---|---|
| Income | Stipend | $1,800 |
| Living | Dorm | $400 |
| Living | Food | $300 |
| Lifestyle | Phone | $50 |
| Lifestyle | Streaming | $50 |
| Debt | None | — |
| Asset | Emergency savings | $1,500 |
| Asset | Laptop | $500 |

**Shopaholic**

| Category | Item | Amount |
|---|---|---|
| Income | Junior exec salary | $3,000 |
| Living | Rent | $600 |
| Living | Groceries | $400 |
| Lifestyle | Fashion | $400 |
| Lifestyle | Subscriptions | $200 |
| Debt | Credit card | $3,000 @ 10% → $300/payday |
| Debt | BNPL | $1,000 @ 10% → $100/payday |
| Asset | Wardrobe (depreciates) | $1,500 |
| Asset | Gadgets (depreciates) | $500 |

**Wealthy Kid**

| Category | Item | Amount |
|---|---|---|
| Income | Family allowance | $4,000 |
| Living | Apartment | $1,500 |
| Living | Dining | $500 |
| Lifestyle | Designer | $600 |
| Lifestyle | Clubbing | $400 |
| Debt | None | — |
| Asset | Designer watch & goods | $2,000 |

**Influencer**

| Category | Item | Amount |
|---|---|---|
| Income | Sponsorships | $3,000 |
| Income | Merch | $500 |
| Living | Rent | $800 |
| Living | Food | $400 |
| Lifestyle | Appearance | $500 |
| Lifestyle | Editing subs | $300 |
| Debt | Camera/gear loan | $4,000 @ 10% → $400/payday |
| Debt | Phone | $1,000 @ 10% → $100/payday |
| Asset | Camera & studio gear | $3,000 |
| Asset | Designer wardrobe | $1,000 |

---

## 8. The Financial Statement (the scoreboard)

Each team reads a clean **Financial Statement** tab (Cashflow-101 style) — Income, Expenses, Assets,
Liabilities, and a summary box (Cash Flow, Net Equity, Passive Income, escape flag). It is **read-only**
and recomputes itself from the data the bankers edit. Mentors operate it via [mentor.md](mentor.md).

**Payday.** Passing/landing on START or an Extra Payday collects **net cashflow** (income + passive +
skill bumps − expenses). Recurring rent/subs/debt are already netted into that number — only **one-off**
events (bills, taxes, cards) are logged separately.

**How each event flows in:**
- **Buy an ownable asset / Opportunity deal** → an Asset (lifts **passive income** → helps escape).
- **Skill Up / Life-Happens skill card** → an Income row (lifts **active income / cash flow only** — does
  **not** help escape).
- **Take/repay debt** → a Liability balance (its payment = balance × rate, auto).
- **Buy/sell a stock** → a share-count change (auto-valued by the live price) + the $50 fee.
- **Stock dividends** → an **auto Passive Income line** computed from Holdings (shares × $5 for the 4
  stable stocks). The $5/share is fixed; the yield floats with price. Counts toward escaping (§9).
- **Landing rent** → cash from the visitor to the owner.

**Forced personal loan.** A team that must pay but has **no cash** is forced to take a **personal loan at
10%** (balance grows by what they owe; payment = balance × 10%). This models how a cash crunch pushes
people into expensive consumer debt — and drags their payday down until they repay it.

---

## 9. Win conditions

- **Primary — escape the rat race:** the **first team whose Passive Income ≥ Monthly Expenses** wins.
  Passive income = income from **owned assets / Opportunity deals, plus stock dividends** (the $5/share on
  the 4 stable stocks). Salary, active income, **Skill-Up bumps, and stock capital gains do NOT count**
  (skills grow your payday so you can *buy* passive assets faster, and a price rise is only realised cash
  when you sell — neither is recurring passive income). This is classic Cashflow: you escape when your
  investments cover your bills.
- **If no team escapes by time-out:** the **highest Passive Income ÷ Monthly Expenses ratio** wins (who
  came closest). If still tied, **highest Net Equity** (assets − liabilities).

### Behavioral note — are we teaching the *right* stock behavior?

A live worry from playtesting: teams swing-trade (buy low / sell high) because the scripted market mostly
trends up, which can look like "trading is smart." Two things keep the lesson honest:
1. **The crash + the index do the teaching.** The R6 crash punishes hype-chasers; the boring S&P 500 more
   than doubles. The intended takeaway is *time in the market beats timing it.*
2. **Friction makes churn cost real money.** The **$50/trade fee** means constant in-and-out trading bleeds
   cash, so patient index-holding wins. **Dividends reinforce this** — you only collect the $5/share by
   *holding* the stable stocks, so the income reward also points away from churning and toward buy-and-hold.
3. **Name it in the debrief.** Explicitly contrast the swing-trader who got caught in R6 with the patient
   index-holder, and say it plainly: *"you could time it because you'd already seen the arc — in real life
   you can't see the next tick."*

---

## 10. Quick guides

- **Players:** see **[player.md](player.md)** — your profile, taking a turn, the Trading Window, buying
  assets/skills/deals, rent, term deposit, how you win, and the 3 traps to watch.
- **Mentors / bankers:** see **[mentor.md](mentor.md)** — which sheet tab to edit for every board space and
  card, worked examples, edge cases, and the one-time sheet formulas (auto-price driver, ratio column).

---

## 11. Appendix — materials & repo artifacts

- **Board:** 36 printed tiles, **45cm × 45cm** each (4 corners + 4 sides × 8). Layout source:
  [sheet/board-spaces.csv](sheet/board-spaces.csv) + [sheet/board-grid.csv](sheet/board-grid.csv).
- **Cards:** [sheet/card-decks.csv](sheet/card-decks.csv) — Life Happens (6×5), Campus Life, Temptation,
  Opportunity (6+6), Market News buyer offers (12).
- **Dashboard:** [dashboard/index.html](dashboard/index.html) + [dashboard/market-script.json](dashboard/market-script.json) — the projected live market.
- **Ledger:** the Google Sheet (Transaction Log, Statement Items, Holdings, Market Prices, 6 Financial
  Statements, Balance Dashboard, Profiles seed). Operated per [mentor.md](mentor.md).
- **Design history:** [discussion.md](discussion.md) — the original planning log (superseded by this doc).
