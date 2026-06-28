# Mentor Guide — Running the Money (Finance Game)

This is the one doc a banker/mentor needs during play. It explains the spreadsheet, the **golden rules**,
and an **event → action** table that maps every board space and card to exactly which tab you edit.

Full game reference (board, cards, stock, profiles, win logic) → **[game-mechanics.md](game-mechanics.md)** ·
card list → [sheet/card-decks.csv](sheet/card-decks.csv) · board → [sheet/board-spaces.csv](sheet/board-spaces.csv).

---

## 1. The big picture — what the tabs are

Each team has a clean **Financial Statement** tab (Cashflow-101 style) that they read. Everything they
see is **calculated automatically** from a few data tabs you edit. You never type onto a statement.

```
   YOU EDIT (4 data tabs)                          PLAYERS / YOU READ (auto, read-only)
   ─────────────────────                           ───────────────────────────────────
   Transaction Log   ─┐
   Statement Items   ─┼─►  formulas  ─►   Financial Statement ×6   (each team's clean view)
   Holdings          ─┤                   Balance Dashboard        (all 6 teams leaderboard)
   Market Prices     ─┘   (just the round-driver cell — see §6)
   (Profiles & Status = seed only: team names + $2,000 start cash. Set once, don't touch.)
```

| Tab | You edit? | What it holds |
|---|---|---|
| **Transaction Log** | ✅ constantly | One row per **cash movement** (signed: `+` in, `−` out). |
| **Statement Items** | ✅ often | One row per thing a team **owns / owes / earns** — assets, deals, skills, debts, and the starting income/expense lines. |
| **Holdings** | ✅ on stock trades | Each team's **share counts** per instrument. |
| **Market Prices** | ✅ once per round | Change **only the round-driver cell** at round close (§6). |
| Profiles & Status | ⛔ seed only | Team, profile, $2,000 start cash. |
| Financial Statement ×6 | ⛔ read-only | The player view. Auto-calculated. |
| Balance Dashboard | ⛔ read-only | Mentor leaderboard — Net Equity, passive/expense ratio, win flag. |

---

## 2. The golden rules

1. **Cash moved?** → add a row to **Transaction Log** (signed amount). *Cash on the statement updates.*
2. **Did they gain/lose something they OWN, OWE, or EARN?** → add/edit a row in **Statement Items**
   (an asset, a deal, a skill bump, a new or repaid debt).
3. **Stocks?** → change the share count in **Holdings**.
4. Most real events are **two actions** — e.g. *buy a deal* = a `−` cash row **and** a Statement Items
   Asset row. Cash is "the money leaving"; Statement Items is "the thing you now own."
5. **Never type onto a Financial Statement or the Balance Dashboard.** They recompute themselves.

> Keep every number a multiple of **$50 / $100** (Rule of Zeroes). Stocks are the exception — they ride a
> **$10 grid** (Rule of Tens).

---

## 3. Payday (the most important habit)

When a team **passes or lands on START / an Extra Payday**, they collect their **net cash flow**.

- **Read the team's `Monthly Cash Flow` cell off their statement** and log **that exact number** as a `+`
  Payday row in the Transaction Log.
- Their recurring rent, subscriptions, and debt payments are **already netted into that number** — so
  **never** log rent/subs/debt as separate rows. Only one-off events (bills, taxes, card draws) get a row.
- **Stock dividends are already in that number too.** The statement auto-adds **$5 × shares** of each of
  the 4 stable stocks (99 Speedmart, Tenaga, Maybank, Maxis) as passive income — so the Monthly Cash Flow
  you read already includes them. **Never log a separate dividend row** (§5, §9).
- Payday grows over the game: buying assets/skills raises it, taking debt lowers it. Always re-read the
  current value rather than reusing an old one.

---

## 4. Event → Action table

`TXN` = add a Transaction Log row · `ITEMS` = add/edit a Statement Items row · `HOLD` = edit Holdings.

| Board space / card | TXN (cash) | ITEMS (own/owe/earn) | HOLD |
|---|---|---|---|
| **START / Extra Payday** | `+` Monthly Cash Flow (read off statement) | — | — |
| **Income Tax** (sp.14) | `−200` | — | — |
| **Fixed Bill** — Rent Top-up `−300` (sp.35) / Phone `−100` (sp.23) | `−` the amount | — | — |
| **Temptation / Doodad** | `−` per card ($50–$300) | — | — |
| **Campus Life** | `±` per card | — | — |
| **Life Happens** — cash card | `±` per card | — | — |
| **Life Happens** — *skill-up card* ("+$100/payday") | **none** | **Skill Up** row: `Amount` = +100 | — |
| **Ownable Asset** — buy (Online Shop / Campus Laundromat / Vending / Dorm Sublet / Parking / Food Stall / E-bike Rental Fleet) | `−` buy price | **Asset** row: `Amount`=price, `Cashflow`=+/payday | — |
| **Ownable Asset** — *land on one OWNED by another team (rent)* | `−` rent (visitor) **and** `+` rent (owner) | — | — |
| **Opportunity / Deal** — buy | `−` cost | **Opportunity - Small** or **Opportunity - Big** row: `Amount`=cost, `Cashflow`=+/payday | — |
| **Market News** — *buyer offer, owner sells the deal* | `+` the premium sale price | **delete** that deal's Opportunity row (or set `Amount`/`Cashflow` to 0) | — |
| **Skill Up** (Online Course / Cert / Bootcamp / Marketing Course) | `−` cost | **Skill** row: `Amount`=permanent bump | — |
| **Buy a stock** | `−` (shares×price) **and** `−50` fee | — | set the share count |
| **Sell a stock** | `+` (shares×price) **and** `−50` fee | — | set the share count (often back to 0) |
| **Stock dividend** (4 stable stocks) | **none** — auto, paid in the payday number | — | — (driven by the Holdings share count) |
| **Repay debt** | `−` amount repaid | **Liability** row: lower the balance (payment auto-recalcs) | — |
| **No cash to pay → forced personal loan** | `+` loan drawn (the shortfall) | **Liability** row: `Amount`=balance, `Rate`=0.1 | — |

### How a Statement Items row is shaped
`Team, Section, Item, Amount, Cashflow, Rate, Note` — Section is one of
`Income | Skill | Skill Up | Expense | Asset | Opportunity - Small | Opportunity - Big | Liability`.

| You're adding… | Section | Amount | Cashflow | Rate |
|---|---|---|---|---|
| An ownable board asset | `Asset` | its value/cost | its **passive income** per payday | — |
| A bought Opportunity deal | `Opportunity - Small` / `Opportunity - Big` | its cost | its **passive income** per payday | — |
| A net-worth item (no income) | `Asset` | its value | `0` | — |
| A board Skill-Up bump | `Skill` | the **income bump** per payday | *(blank)* | — |
| A Life-Happens skill-card bump | `Skill Up` | the **income bump** per payday | *(blank)* | — |
| A debt | `Liability` | the **balance** | `=Amount*Rate` (auto) | `0.1` or `0.025` |

An **Asset** or **Opportunity** row shows under Assets (value) *and* Income (its cashflow), and counts
toward Passive Income; a **Liability** shows under Liabilities (balance) *and* Expenses (its payment).
**Skill / Skill Up rows are income only** — active income that lifts Cash Flow but **not** passive income
(see §7). Stocks are the exception — they come from Holdings, so **never** add a stock row to Statement Items.

**Debt payments auto-calculate.** A `Liability` row's `Cashflow` = `=Amount*Rate` (`Rate` = `0.1` for 10%
consumer/personal debt, `0.025` for the 2.5% student loan). So you **only ever edit the balance** — the
payment and the Expenses line recalculate themselves.

---

## 5. Special cases (the easy-to-get-wrong ones)

- **Landing rent (NEW).** When a team lands on an ownable-asset space another team **already owns**, the
  visitor pays the owner **½ that space's passive income**: Online Shop **$150** · Campus Laundromat
  **$500** · Vending **$200** · Dorm Sublet **$300** · Parking **$350** · Food Stall **$450** · E-bike
  Rental Fleet **$600**. Log **two** Transaction rows: `−` for the
  visitor, `+` for the owner. (No Statement Items change — the asset still belongs to the owner.)
- **Market News buyer offer (NEW).** A card names a buyer for a specific deal. The **owner** of that deal
  may sell it for the offered **premium**: `+` the premium in Transaction Log **and delete** that deal's
  Asset row (its passive income stops). If the **drawer doesn't own** the deal, they may sell/auction the
  *card* to the team that does — that's a side cash deal between two teams (log both teams' cash rows).
- **Forced personal loan (NEW).** A team that must pay but has no cash takes a 10% loan: `+` the shortfall
  in Transaction Log (so they can pay), **and** add a **Liability** row (`Amount` = balance, `Rate` 0.1).
  Their payday drops by the auto payment until they repay it.
- **Trading fee (NEW).** Every stock buy or sell also costs a flat **$50**: log a separate `−50` row
  (Type `Fee`). It does not touch Holdings or Statement Items.
- **Stock dividends (NEW).** The 4 **stable** stocks (99 Speedmart, Tenaga, Maybank, Maxis) pay **$5 per
  share** — **fully automatic**. The statement reads `shares × $5` straight from Holdings and adds it to
  **Passive Income** (so it *counts toward escaping*) and to Cash Flow. You do **nothing**: no Transaction
  Log row, no Statement Items row. Growth stocks, Dogecoin, and the S&P 500 pay $0. (Setup formula: §9c.)
- **Selling an illiquid asset/deal** at the forced **half price** (no buyer card): `+` half the value in
  Transaction Log **and** delete that asset's Statement Items row.
- **Selling a stock** → `+` shares×current price (and the `−50` fee) in Transaction Log **and** set the
  Holdings share count to 0. No Statement Items row involved.
- **The % debt step-down** (auto via `=Amount*Rate`): **10% loans** repay **$500 → payment −$50**; the
  **2.5% student loan** repays **$2,000 → payment −$50**. You just edit the balance.
- *(There is no Burnout / Go-to-Burnout / Chill Zone anymore — those corners were removed. No skip-turn or
  jail handling.)*

---

## 6. Round close — the one-cell market update

At the end of each round, the market operator changes **one cell**: the **round driver** in the **Market
Prices** tab (cell **R1**, the number just right of "Current Round →") to the round number that just closed.
All 9 Current Prices jump to that round's closing price and every team's stock holdings revalue
automatically. *(That's it — you no longer type 9 prices. The full prices for all 13 rounds are pre-stored
in the tab; see the one-time setup in §9.)*

---

## 7. Winning

- **Primary — escape the rat race:** the first team whose **Passive Income ≥ Monthly Expenses**. Their
  statement's **Escaped Rat Race?** cell shows ✅; watch the **Balance Dashboard** for all teams at once.
- **Passive Income** = income from owned **assets / opportunity deals, plus stock dividends** ($5/share on
  the 4 stable stocks, auto from Holdings). Salary, active income, **Skill-Up bumps, and stock capital
  gains do NOT count** — escaping means your investments cover your bills.
- **No escapee at time-out:** highest **Passive/Expense ratio** (Balance Dashboard col H); if still tied,
  highest **Net Equity**.

---

## 8. Worked examples

**A) Team 3 buys the "Laundromat share" Big Deal ($4,000 → +$1,200/payday).**
1. Transaction Log: `Round, Team 3, Deal, Laundromat share, -4000`.
2. Statement Items: `Team 3, Opportunity - Big, Laundromat share, 4000, 1200, ,`.
→ Cash −$4,000; "Laundromat share" appears under Assets; "(passive) $1,200" under Income; Passive Income
+$1,200 (this *does* count toward escaping).

**B) Team 3 later draws/receives the Laundromat buyer card and sells for $6,000.**
- Transaction Log: `Team 3, Deal, Sold Laundromat share to investor, +6000`.
- Statement Items: delete the Laundromat Opportunity row.
→ Cash +$6,000 (a $2,000 capital gain over the $4,000 cost); Passive Income −$1,200.

**C) Team 5 lands on Team 6's Food Stall (owned).**
- Transaction Log: `Team 5, Other, Rent to Team 6 (Food Stall), -450` **and** `Team 6, Other, Rent from Team 5, +450`.

**D) Team 1 must pay a $500 bill but has $0 cash → forced personal loan.**
- Transaction Log: `Team 1, Other, Forced personal loan, +500` then `Team 1, Card, Exam fees + textbooks, -500`.
- Statement Items: `Team 1, Liability, Personal loan, 500, =Amount*Rate, 0.1, forced @10%`.
→ Liabilities +$500; Expenses shows "Personal loan payment $50".

**E) Team 5 buys 10 Nvidia @ $150, sells later @ $200.**
- Buy: Holdings → Team 5 Nvidia = 10. Transaction Log `Team 5, Trade, Buy 10 Nvidia @150, -1500` **and** `Team 5, Fee, Brokerage, -50`.
- Sell: Holdings → Nvidia = 0. Transaction Log `Team 5, Trade, Sell 10 Nvidia @200, +2000` **and** `Team 5, Fee, Brokerage, -50`.
→ Net gain $500 − $100 in fees = **$400** (the fee is the anti-churn lesson).

**F) Team 2 buys the "Online Course" Skill-Up ($500 → +$150/payday).**
1. Transaction Log: `Team 2, Skill, Online Course, -500`.
2. Statement Items: `Team 2, Skill, Online Course, 150, , ,`.
→ Cash −$500; Total Income and Cash Flow +$150; **Passive Income unchanged** (a skill doesn't escape you).

---

## 9. One-time sheet setup (only if you're updating the workbook formulas)

You've already built the sheet; these two are the **only** formula changes the playtest rules require.

**(a) Auto-updating market prices** — in the **Market Prices** tab:
1. Confirm columns **C:O** hold the 13 rounds of closing prices (R1…R13, pre-filled from
   `dashboard/market-script.json`) and cell **R1** (right of "Current Round →") is the round driver (1–13).
2. In **B2** paste `=INDEX($C2:$O2,1,$R$1)` and drag down to **B10**.
→ Now changing **R1** alone re-prices all 9 instruments (§6). Holdings' `Total Value` (col L) is unchanged
— it still VLOOKUPs col B by name.

**(b) Passive/Expense ratio column** — in the **Balance Dashboard** tab:
- Add a **Passive/Expense Ratio** column. For Team 1's row: `=F2/G2` (Passive ÷ Monthly Expenses); copy
  down for all six rows. This is the time-out tie-break metric (§7).

**(c) Auto stock dividends** — so the 4 stable stocks pay $5/share with **zero** per-round work:
1. In the **Market Prices** tab, column **P** (`Div/share`) holds each instrument's fixed dividend: `5`
   for 99 Speedmart/Tenaga/Maybank/Maxis, `0` for the rest. (Flat — never changes during play.)
2. In the **Holdings** tab, column **M** (`Monthly Dividend`) is `=MMULT(B2:J2,'Market Prices'!$P$2:$P$10)`
   for each team row — shares × Div/share, summed. It auto-recomputes whenever a share count changes.
3. In each **Financial Statement** tab, add the team's dividend into **two** summary cells so it both pays
   out and counts toward escaping: append `+VLOOKUP($B$1,Holdings!$A:$M,13,FALSE)` to **Total Income (B4)**
   *and* to **Passive Income (B10)**.
→ Dividends now flow into the **payday number automatically** (Monthly Cash Flow) and lift Passive Income
— no Transaction Log or Statement Items rows, ever.

---

## 10. Common mistakes

- ❌ Typing onto a Financial Statement or the Balance Dashboard. They're formulas — edit the **data** tabs.
- ❌ Logging rent / subscriptions / debt payments as separate cash rows. They're **already** in the payday
  number. Only one-off bills, taxes, cards, fees, and rent-to-another-team get a row.
- ❌ Forgetting the **$50 fee** on a stock trade, or the **second rent row** (+ owner) on a landing.
- ❌ Adding a stock as a Statement Items row. Stocks live in **Holdings** only.
- ❌ Hand-logging a stock **dividend**. It's automatic (Holdings col M → the payday number). Logging a `+`
  row double-counts it. And remember: stock **dividends** count as passive income, but stock **capital
  gains** (price rises) do **not** — only the $5/share dividend on the 4 stable stocks does.
- ❌ Forgetting the second action — a bought asset/deal/skill needs **both** a cash row and a Statement
  Items row, or the statement won't reflect it.
- ❌ Off-grid numbers. Keep everything to $50 / $100 steps (stocks $10).
