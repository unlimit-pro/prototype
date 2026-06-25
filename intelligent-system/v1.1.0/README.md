# v1.1.0 — Solana On-Chain Hover Preview (8-Module System)

This release replaces the original single-pane token hover preview with a **tabbed 8-module system** that surfaces Solana-native on-chain metrics. Each module is an independent analytical view accessible via a tab bar at the top of the hover card.

> **Note:** All metric values are currently **deterministic mock data** generated client-side via `_tokSeed(sym)` / `_tokRand()`. The data is reproducible per token symbol (same symbol always shows the same values) but does not come from live RPC endpoints or APIs. The architecture is designed as a UI prototype — each module's data generation block is clearly separated and ready to be swapped with real API calls.

---

## Architecture Overview

The hover preview is built around three core functions:

| Function | Role |
|----------|------|
| `showTokPreview(sym, evt)` | Generates all mock data, renders the 8 module panels + tab navigation, positions the popup |
| `switchTokMod(evt, idx)` | Client-side tab switching — toggles `.active` class on tabs and module divs |
| `positionTokPreview(evt)` | Positions the preview relative to the mouse cursor, keeping it within viewport bounds |

The preview element is a single `<div class="tok-preview" id="tokPreview">` in the HTML body that gets fully repopulated on each hover via `el.innerHTML = ...`.

---

## Module-by-Module Breakdown

### Module 1: DEX Pools

**Purpose:** Shows the token's liquidity footprint across Solana's major AMMs.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **Pool Liquidity Score** (0–100) | `Math.round(16 + rnd()*78)` — random range 16–94 | Higher = deeper liquidity pools; scores ≥50 labelled "Adequate", <50 "Thin" |
| **Raydium pool TVL** | `(1.8 + rnd()*12)M` — range $1.8M–$13.8M | Total value locked in the Raydium `SYM/SOL` pool |
| **Raydium APY** | `(8 + rnd()*38)%` — range 8%–46% | Annualized yield from swap fees and LP incentives |
| **Raydium 24h Volume** | `(0.4 + rnd()*4.2)M` — range $400K–$4.6M | 24-hour trading volume for the pool |
| **Raydium Liquidity Depth** | `Math.round(42 + rnd()*48)%` — range 42%–90% | How much of the pool's depth is within 2% of the mid-price; higher = less slippage |
| **Orca pool TVL / APY / Vol / Depth** | Same structure, USDC-denominated pool (SYM/USDC) | Usually slightly smaller range than Raydium; offers concentrated liquidity |

**Real Solana context:** Raydium and Orca are the two dominant DEXs on Solana. Raydium uses an AMM + order book hybrid; Orca uses concentrated liquidity (like Uniswap v3). High liquidity depth (>60%) is critical for large trades to avoid slippage.

---

### Module 2: Wallet Growth

**Purpose:** Analyzes the token's user adoption trajectory via wallet-level activity.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **Active Wallets (24h)** | `Math.round(1200 + rnd()*8800)` — range 1.2K–10K | Unique wallets that transacted the token in the last 24 hours |
| **Momentum Score** (0–100) | `Math.round(20 + rnd()*74)` — range 20–94 | Composite of growth trend; ≥50 labelled positive |
| **24h Growth Rate** | `Math.round((rnd()-0.38) * 32)%` — range -12% to +20% | % change in active wallets over 24 hours |
| **7d Growth Rate** | `Math.round((rnd()-0.30) * 58)%` — range -17% to +41% | % change in active wallets over 7 days |
| **New Wallets (24h)** | `Math.round(80 + rnd()*520)` — range 80–600 | First-time transactors for this token |
| **Wallet Retention** | `Math.round(38 + rnd()*48)%` — range 38%–86% | % of wallets that transacted again after their first trade; higher = sticky user base |
| **Median Wallet Age** | `Math.round(4 + rnd()*42)` days — range 4–46 days | How long the median holder has held the token; older = more conviction |

**Real Solana context:** Solana's low fees enable high-frequency wallet activity. When a token shows high active wallet growth but low median age, it may indicate farming/sybil activity rather than organic adoption. Retention >50% is considered healthy.

---

### Module 3: Staking & Yield

**Purpose:** Evaluates the token's native staking ecosystem and validator network health.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **Staking Yield Score** (0–100) | `Math.round(20 + rnd()*72)` — range 20–92 | Overall staking attractiveness; ≥50 = "Attractive" |
| **Staking APY** | `(4.2 + rnd()*3.8)%` — range 4.2%–8.0% | Annualized staking yield after inflation |
| **Total Staked** | `(42 + rnd()*48)M SOL` — range 42M–90M SOL | Total native SOL staked (for SOL this is network-wide; for SPL tokens this would be relevant staking pool deposits) |
| **Stake Ratio** | `Math.round(38 + rnd()*42)%` — range 38%–80% | % of circulating supply currently staked |
| **Active Validators** | `Math.round(800 + rnd()*800)` — range 800–1,600 | Number of validators actively validating the network |
| **LST Dominance** | `(12 + rnd()*28)%` — range 12%–40% | Share of staking dominated by Liquid Staking Tokens (jitoSOL, mSOL, bSOL, INF) |
| **Inflation Rate** | `(3.2 + rnd()*2.4)%` — range 3.2%–5.6% | Current SOL inflation rate (Solana has a disinflationary schedule starting at ~8% and declining to 1.5%) |
| **MEV Tips (24h)** | `(0.4 + rnd()*2.2)K SOL` — range 400–2,600 SOL | Max Extractable Value tips paid to validators in the last 24h; higher = more network economic activity |

**Real Solana context:** Solana uses an inflation-based staking model where ~6.5–8% of new SOL is distributed to stakers annually. LSTs like JitoSOL add a MEV-reward layer on top. A high LST dominance can indicate centralization risk if a single LST provider controls too much stake.

---

### Module 4: Tokenomics

**Purpose:** Analyzes supply distribution, inflation pressure, and unlock schedules — critical for understanding future dilution risk.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **Tokenomics Score** (0–100) | Composite: `65 - top10*0.4 + burn*8 - unlock*0.3` (clamped 1–99) | Higher = more favorable supply dynamics; ≥55 = "Healthy" |
| **Circulating Supply** | `totalSupply * (0.4–0.9)` — scaled per token type (BONK/PIPPIN in trillions, SOL in millions) | Tokens currently in circulation |
| **Circ / Total Ratio** | `circSupply / totalSupply * 100` — range ~40%–90% | % of total supply that's circulating; low ratio = future unlock dilution risk |
| **Holders** | `Math.round(1200 + rnd()*88000)` — range 1.2K–89.2K | Total unique wallet addresses holding the token |
| **Top 10 Concentration** | `(22 + rnd()*56)%` — range 22%–78% | % of total supply held by the top 10 wallets; >50% = high concentration risk |
| **Emission Rate** | `(1.2 + rnd()*4.8)%/mo` — range 1.2%–6.0%/mo | Monthly inflation rate from ecosystem releases, staking rewards, etc. |
| **Burn Rate** | `(0.2 + rnd()*1.8)%/mo` — range 0.2%–2.0%/mo | Monthly token burn (destruction) rate; coloured green if >0.5%/mo |
| **Unlock Schedule** | `Math.round(12 + rnd()*58)% unlocked` — range 12%–70% | % of tokens already vested/unlocked; >40% = amber (moderate risk) |

**Real Solana context:** Tokenomics is especially important on Solana due to the prevalence of VC-backed tokens with large unlock schedules. A token with <50% circulating supply and >50% top-10 concentration is high risk. Burn mechanisms (like BONK's or SOL's fee-burning) are deflationary forces that offset emission.

---

### Module 5: DeFi Health

**Purpose:** Measures the token's integration and economic activity across the Solana DeFi ecosystem.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **DeFi Health Score** (0–100) | `Math.round(14 + rnd()*78)` — range 14–92 | Overall DeFi ecosystem engagement; ≥50 = "Active" |
| **TVL (all protocols)** | `(8 + rnd()*180)M` — range $8M–$188M | Total value locked across all protocols where the token is used |
| **Active Protocols** | `Math.round(2 + rnd()*10)` — range 2–12 | Number of DeFi protocols with active pools/markets for this token |
| **Supply / Borrow Rates** | Supply: `(3 + rnd()*18)%`, Borrow: `(6 + rnd()*24)%` | Lending market rates — wide spread suggests low liquidity utilization |
| **Stablecoin Backing** | `Math.round(40 + rnd()*50)%` — range 40%–90% | % of token liquidity paired with stablecoins; higher = more "blue chip" liquidity |
| **DEX Vol / Mcap Ratio** | `(0.08 + rnd()*0.42)x` — range 0.08x–0.50x | Daily DEX volume divided by market cap; >0.3x = high trading velocity |
| **Protocol Fees (24h)** | `(0.2 + rnd()*4.8)M` — range $200K–$5M | Aggregate fees generated by protocols using this token |
| **Revenue / Fee Ratio** | `(12 + rnd()*38)%` — range 12%–50% | % of fees that flow to token holders as revenue (vs. going to LPs/protocol) |

**Real Solana context:** Solana DeFi is dominated by lending protocols (Kamino, Marginfi, Solend) and DEXs (Raydium, Orca, Jupiter). A token's DeFi Health is strong when it has multiple active lending pools, deep stablecoin liquidity, and when protocol fees are meaningfully distributed back to token holders.

---

### Module 6: Authority

**Purpose:** Audits the token's on-chain authority controls — the most critical safety check for any Solana token.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **Mint Authority** | `rnd() > 0.60` — 40% chance "Revoked" | If active, new tokens can be minted at any time → **warn**; Revoked = **safe** |
| **Freeze Authority** | `rnd() > 0.75` — 25% chance "None" | If active, wallets can be frozen (assets seized) → **danger**; None = **safe** |
| **Upgrade Status** | `rnd() > 0.55` — 45% chance "Frozen" | Upgradable = program can be changed; Frozen = immutable |
| **LP Locked** | `rnd() > 0.38` — 62% chance "Locked" | Locked = liquidity provider tokens are locked (cannot be rug-pulled); Unlocked = **danger** |
| **Contract Verified** | `rnd() > 0.25` (0.6 for MEOW/SHADOW) — 75% chance "Verified" | Verified on Solscan or similar explorer |
| **Safety Composite** (0–100) | Weighted scoring from all above metrics | ≥70 = "Low Risk" (safe), 48-69 = "Caution" (warn), <48 = "High Risk" (danger) |

**Real Solana context:** These are the **first things experienced Solana traders check**. An active mint authority means the team can diluite holders at will. Freeze authority gives the team power to blacklist wallets. These checks are done on-chain via the SPL Token program — anyone can query them. A token with both mint and freeze revoked is considered "sufficiently decentralized."

---

### Module 7: Security

**Purpose:** Deep-dive security audit indicators beyond basic authority controls — program governance, multisig protection, and audit history.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **Security Score** (0–100) | Weighted: base 40 + upgrade revoked (18) + multisig (12) + audit recency + bounty (8) + timelock (10) + renounced (15) | ≥68 = "Strong", 45–67 = "Moderate", <45 = "Weak" |
| **Program Upgrade** | `rnd() > 0.55` — 45% chance "Revoked" | Active = program can be changed (risk of malicious upgrade); Revoked = locked forever |
| **Multisig** | `rnd() > 0.48` — 52% chance "Active" | Active = upgrades require multiple signers; None = single-key risk |
| **Audit Recency** | Random from `['< 30d', '1-3mo', '3-6mo', '6-12mo', '> 12mo']` | More recent = better; colour-coded green → red |
| **Bug Bounty** | `rnd() > 0.35` — 65% chance "Active" | Active bounty program = ongoing security investment |
| **Timelock** | `rnd() > 0.60` — 40% chance "Active" | Active timelock = upgrades have a delay (can't be frontrun) |
| **Ownership** | `rnd() > 0.55` — 45% chance "Renounced" | Renounced = no admin control; Active = admin can still change parameters |
| **Program DAO** | Derived from upgrade + ownership + multisig flags | Multisig DAO = governed by multiple signers; EOA = externally owned account (single wallet) |

**Real Solana context:** Security on Solana goes beyond standard token checks. Program upgrade authority (whether the program's BPF upgrade slot is still active) and multisig protection are Solana-specific. A project that has revoked its upgrade authority, has multisig, a timelock, and a recent audit is considered "blue chip" by Solana security standards.

---

### Module 8: RPC Activity

**Purpose:** Network-level activity and transaction health metrics — reveals how much real on-chain usage the token is generating.

| Metric | Data Generation | Interpretation |
|--------|----------------|----------------|
| **RPC Activity Score** (0–100) | Composite: base 30 + TX count/tier + TPS/20 - fail rate*5 (clamped) | ≥50 = "High traffic", <50 = "Low activity" |
| **TX Count (24h)** | `rnd() * 240000` (4.8M for SOL) | Total transactions involving this token in 24h |
| **Unique Signers** | `TX count * (0.12–0.46)` | Unique wallet addresses that signed transactions; higher = more organic activity |
| **Avg Priority Fee** | `(2 + rnd()*18) µSOL` — range 2–20 µSOL | Average priority fee paid per transaction; higher = more network congestion for this token |
| **Peak TPS** | `Math.round(400 + rnd()*1200)` — range 400–1,600 | Peak transactions-per-second observed |
| **TX Fail Rate** | `(0.4 + rnd()*2.8)%` — range 0.4%–3.2% | % of failed transactions; >1.5% highlighted red (may indicate bot spam or broken contracts) |
| **Program Calls** | `Math.round(12 + rnd()*38)` | Number of distinct program instructions called in transactions |
| **Compute Units** | `TX count * (2.4–6.6)` | Total compute units consumed; higher = more complex program interactions |

**Real Solana context:** Solana's high throughput means RPC data is rich with signal. Unique signers vs. total TX count helps distinguish real activity from bot spam. Priority fees in µSOL (micro-SOL) indicate bidding pressure for block space. A high TX count with low unique signers and high fail rate is a classic botting pattern.

---

## CSS Component Library

The preview uses a set of reusable CSS classes across all modules:

| Class | Purpose |
|-------|---------|
| `.tok-mod-grid` | 2-column grid container for metric cells |
| `.tok-mod-item` | Individual metric cell with label + value |
| `.tok-mod-item.full` | Spans full width (for score bars) |
| `.badge-sm` | Status pill (`.safe`/`.warn`/`.danger`/`.info`/`.off`) |
| `.tp-bar-track` / `.tp-bar-fill` | Progress bar with gradient fill (`.neg`/`.neutral`/`.accent`) |
| `.tp-dex-chip` | DEX protocol badge (`.ray`/`.orca`/`.jup`) |
| `.tok-mod-tabs` / `.tok-mod-tab` | Tab navigation bar |
| `.tok-module` | Module panel, toggled via `.active` |

---

## Mock Data Engine

All 8 modules use the deterministic random system:

```
seed = _tokSeed(sym)   → FNV-1a hash of token symbol
rnd  = _tokRand(seed)  → Returns function that generates values seed1, seed2, ...
```

This ensures:
- **Reproducibility:** Same token always shows identical mock values across hovers
- **Variety:** Different tokens show different values because their seeds differ
- **Realistic ranges:** Every metric is bounded within realistic Solana value ranges

To replace with real data, each data-generation block (sections 1–8 inside `showTokPreview`) can be replaced with `fetch()` calls to Solana RPC providers (Helius, Triton), Solscan API, Birdeye API, or Jupiter API.
