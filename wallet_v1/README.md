# Unlimit Wallet — Low-Fidelity Clickable Prototype

**Wireframe style:** White background, black/grayscale wireframe aesthetic. All screens are fully interactive with clickable navigation, modals, form flows, and state transitions.

## Vision

Unlimit is a Solana-native cryptocurrency wallet that redefines the user experience for on-chain finance. While existing wallets like Phantom and Solflare treat token accounts as a technical headache users must manage themselves, Unlimit makes the entire account system **completely invisible**. Combined with a gamified "Wealth Recovery" hook that provides immediate financial value on first use, Unlimit creates a wallet that is simultaneously simpler for beginners and more powerful for pro traders.

### Core Design Principles

| Principle | Description |
|-----------|-------------|
| **Wealth Recovery First** | Every import triggers a scan of all token boxes, uncovering locked SOL rent — instant trust |
| **Invisible Infrastructure** | No "Add Token" button. No "Create Associated Token Account." Everything auto-provisions |
| **Plain English Security** | Pre-sign simulation: "You are giving 10 SOL to receive 5M BONK. This site is 12 days old (Medium Risk)" |
| **Social by Default** | Copy-trading, Blinks (shareable trade links), and a gamified TURBO toggle make trading viral |
| **Non-Custodial & Encrypted** | BIP-39 seed phrases encrypted with AES-256-GCM. Keys never leave the device |

---

## Sprint Architecture

```
┌────────────────────────────────────────────────────────────────┐
│                    UNLIMIT WALLET ROADMAP                       │
├───────────┬───────────────┬────────────────┬───────────────────┤
│ SPRINT 1  │   SPRINT 2    │    SPRINT 3    │     SPRINT 4      │
│ Foundation│  Invisible    │  Intelligence  │  Social Trading   │
│ & Hook    │  Token Mgr    │  & Security    │  & Turbo Game     │
├───────────┼───────────────┼────────────────┼───────────────────┤
│ We found  │ No Add Token  │ Pre-Sign Sim   │ Copy-Trade Feed   │
│ 0.04 SOL  │ button        │ Whale Tags     │ TURBO Priority    │
│ locked in │ Auto-ATA      │ Jupiter Swap   │ Blinks (X/DC)     │
│ your old  │ Zero-Failure  │ Risk Scoring   │ Referral Loop     │
│ accounts  │ Transfers     │ Settings       │ Lead Trader       │
├───────────┼───────────────┼────────────────┼───────────────────┤
│Weeks 1-2  │  Weeks 3-4    │   Weeks 5-6    │    Weeks 7-8      │
└───────────┴───────────────┴────────────────┴───────────────────┘
```

---

## Sprint 1: The Foundation & The "Free SOL" Hook

**Goal:** Establish trust and provide immediate financial value.

### Key Screens

| Screen | Purpose |
|--------|---------|
| **Wealth Recovery Splash** | "Your old wallets may hold forgotten SOL locked in empty accounts." CTA: Import Wallet |
| **Path Selection** | Create New Wallet / Import Existing Wallet (seed phrase, private key, JSON backup) |
| **Terms Gate** | Non-custodial notice. "You — and only you — control your keys." |
| **Wallet Setup** | Name your wallet |
| **Password Creation** | 4-segment live strength meter. AES-256-GCM encryption notice |
| **Seed Phrase Reveal** | BIP-39 12-word phrase, blurred by default. Anti-screenshot overlay |
| **Seed Confirmation** | Word-picker — place shuffled words back in correct order |
| **Success / Scan** | Wallet created → redirect to main wallet |
| **Import + Recovery Scan** | Import seed → animated scanning → "We found 0.05 SOL locked in 3 empty token accounts" → Reclaim button |

### The Account Indexer

When a user imports a wallet, Unlimit doesn't just show a balance. It scans every "Token Box" (Associated Token Account / ATA) created by the user:

1. **Fetch all ATAs** via `connection.getParsedTokenAccountsByOwner()`
2. **Identify empty ATAs** — those with 0 balance but still holding rent-exempt reserve
3. **Calculate recoverable SOL** — `0.00203928 SOL per ATA` × number of empty accounts
4. **Present recovery UI** — "We found X SOL locked in your old empty accounts. Click to reclaim it."
5. **Build reclaim transaction** — close each empty ATA, collect rent back to user's wallet

### Technical Stack
- **Key Generation:** `window.crypto.getRandomValues(16)` → BIP-39 entropy → 12-word mnemonic
- **Key Derivation:** BIP-44 path `m/44'/501'/0'/0'` → Ed25519 (SLIP-0010) → 64-byte keypair
- **Encryption:** PBKDF2 (210k iterations) → AES-256-GCM for local seed storage
- **Address Format:** base58-encoded 32-byte public key (44 characters)

---

## Sprint 2: The "Invisible" Token Manager

**Goal:** Make the "one token = one account" Solana headache completely invisible.

### Key Features

| Feature | Description |
|---------|-------------|
| **Auto-Provisioning** | No "Add Token" button. If a user receives a token, Unlimit detects it and creates the ATA automatically in the background |
| **Zero-Failure Transfers** | When sending to a recipient without an ATA for that token, Unlimit bundles the "Create ATA" instruction so the transaction never fails |
| **Send Flow** | 3-step wizard: recipient → gas tier → confirm/broadcast. Shows ATA check in real-time |
| **Receive** | QR code + base58 address. "Any token sent here is auto-detected. No setup needed." |
| **Jupiter Swap** | Integrated swap with slippage control, rate display, and Jupiter logo |
| **Activity Feed** | Shows auto-provisioned tokens with special "auto" badge and zero-failure transfers with "Z-F" badge |
| **Wallet Header** | Wallet selector dropdown with "Add / Import Wallet" and "Lock Wallet" options. Notification bell + Lock button + Settings gear |
| **Lock / Disconnect** | Lock button (🔒) in header instantly locks the wallet with a full-screen overlay. Wallet dropdown also has a "Lock Wallet" option. Unlock via password — follows Phantom and Solflare lock patterns |

### How Zero-Failure Works

```
Normal Wallet:
  User sends USDC → recipient has no USDC ATA → TX FAILS ❌

Unlimit Wallet:
  User sends USDC → Scanner detects missing ATA 
  → Bundles: [CreateATA + Transfer] → TX SUCCEEDS ✅
```

### Asset Table
- Sortable by value and name
- Auto-created tokens shown with pill badge
- No "Add Token" button — all tokens appear automatically
- 24h price change indicators

---

## Sprint 3: The Intelligence & Security Layer

**Goal:** Beat MetaMask's security and Phantom's simplicity with AI-enhanced transaction intelligence.

### Pre-Sign Simulation

Before the user clicks "Approve," the wallet shows exactly what is happening in **plain English**:

**Example:** *"You are giving 10 SOL (≈$1,690) to receive 5,000,000 BONK. This site pump.fun was created 12 days ago (Medium Risk). No suspicious code detected."*

#### Risk Scoring Matrix

| Factor | Weight | Example |
|--------|--------|---------|
| Site Age | High | < 7 days = High Risk, < 30 days = Medium |
| Contract Verification | High | Unverified = High Risk |
| Transfer Size | Medium | > 50% of wallet balance = Warning |
| Suspicious Instructions | High | `closeAccount`, `transferAuthority`, `approve` |
| Known Phishing | Critical | Blocklist check against community DB |

### Whale Tags

When a user looks at a token, show real-time smart-money badges:

- **Bullish** — "Being bought by 5 Smart-Money Wallets"
- **Accumulating** — "3 high-win-rate wallets entered this position"
- **Bearish** — "Sold by 2 smart-money wallets"
- **Categories:** SOL Ecosystem, Meme, DeFi, AI Agents

### Settings Panel

| Section | Components |
|---------|-----------|
| **Security** | Auto-lock timer, Pre-sign simulation toggle, Whale alerts, Phishing detection |
| **Account** | Wallet name, .sol domain, Export backup, Remove wallet |
| **Preferences** | Currency (USD/EUR/GBP), Language |

---

## Sprint 4: Social Trading & The "Turbo" Game

**Goal:** Viral growth mechanisms that turn every user into a "Lead Trader."

### Social Copy-Trading

- **Trade Feed** — Real-time feed of trades from verified traders
- **Trader Profiles** — Avatar, win rate (%), follower count, recent trades
- **Copy Trade** — One-click "Copy Trade" button on any trade in the feed
- **Risk Controls** — Configurable per-trade limit (1/2/5 SOL max), slippage tolerance
- **Disclaimer** — "Copy-trading carries risk. The trader you follow may lose money."
- **Wallet Header** — Full wallet dropdown with "Add / Import" and "Lock Wallet" options, Lock button (🔒), Settings gear

### TURBO Toggle

A gamified priority-fee button that ensures your trade lands first during high-traffic meme launches:

```
TURBO Toggle States:
  OFF (🐢) — Standard Solana priority fees
    Land rate: 62% during congestion

  ON  (⚡) — Elevated priority fees (configurable multiplier)
    Land rate: 94% during congestion
    Pulsing gold border animation
    Priority slider: 1x → 20x normal fees
```

The key insight: Unlike Ethereum where gas is expensive, Solana priority fees are fractions of a cent. "Turbo" gamifies what is essentially free speed — making users feel like they have a trading superpower.

### Blinks (Social Links)

Share your trades on X (Twitter), Discord, or Telegram as clickable links. Anyone who clicks can buy the same token directly via Unlimit.

**How it works:**
1. Create a Blink for any token or trade
2. Share the link (`https://unlimit.so/blink/bonk-vnda8x9k...`)
3. Anyone who clicks can buy directly via Unlimit
4. Creator earns **0.5% fee** on click-through trades

### Viral Loop
```
User trades → Creates Blink → Shares on X/DC
  → Follower clicks → Buys via Unlimit
  → Follower becomes Lead Trader → Creates own Blink
  → ∞
```

---

## Technical Architecture

### Tech Stack
- **Frontend:** Static HTML5 + Embedded CSS + Vanilla JavaScript (Zero Dependencies)
- **Cryptography:** Web Crypto API (PBKDF2, AES-256-GCM), Ed25519 (tweetnacl)
- **Chain Interaction:** `@solana/web3.js`, SPL Token Program, System Program
- **RPC Providers:** Helius (primary) → QuickNode (fallback) → public endpoint
- **Price Feeds:** Jupiter Price API v6, CoinGecko fallback

### State Management
| Mechanism | Purpose |
|-----------|---------|
| `localStorage` | Onboarding state, wallet name, network, custom tokens, settings |
| `sessionStorage` | Wallet lock flag |
| Module `let` | Screen state, send step, swap rates, filter state |

### Screen Navigation
- Sprint 1: Single-page screen system with CSS toggle (`.screen.active`)
- Sprint 2: Single page with modal overlays for Send/Receive/Swap + Lock overlay
- Sprint 3: 4-tab layout (Portfolio / Transactions / Intelligence / Settings) + Lock overlay
- Sprint 4: 3-tab layout (Trade Feed / TURBO / Blinks) + Lock overlay

### Lock / Disconnect Flow

Modeled after Phantom's instant-lock and Solflare's idle-timeout patterns:

```
User clicks 🔒 (header or dropdown) → Full-screen overlay replaces app
  → "Wallet Locked" + Password input
  → Enter password → Overlay dismissed, wallet resumes
  → (Prototype: any non-empty password unlocks)

User clicks 🚪 Disconnect (dropdown or lock overlay) 
  → Clears onboarding flag + wallet data from localStorage
  → Redirects to sprint1.html (fresh onboarding)
```

The lock flow provides a security escape hatch that users expect from well-established wallets. It is available on every post-onboarding screen (sprint2, sprint3, sprint4) via:
1. **Header action bar** — Lock icon button (🔒)
2. **Wallet dropdown** — "🔒 Lock Wallet" option below "Add / Import Wallet"
3. **Wallet dropdown** — "🚪 Disconnect" option — clears session, returns to onboarding
4. **Lock overlay** — "🚪 Disconnect Wallet" button below the unlock form

### Sprint Isolation

Each sprint prototype is now self-contained — no cross-sprint navigation links exist:
- **sprint1.html** — Cannot navigate to sprint2-4 (only the completion flow advances)
- **sprint2.html** — Cannot navigate to sprint3 or sprint4 (Settings gear + "View All" now show "Coming Soon" toasts)
- **sprint3.html** — Cannot navigate to sprint4 (Social Trading icon + Trade button show "Coming Soon" toasts; Send/Receive/Swap still link back to sprint2)
- **sprint4.html** — Cannot navigate to earlier sprints (Settings gear shows "Coming Soon" toast)

### Simplified Architecture

- **Solana Mainnet only** — No network switcher, no cluster pills, no Devnet/Testnet toggles. Network management is removed from Settings.

### Onboarding Guard
```
sprint1.html → if onboarding_complete redirect to sprint2.html
sprint2.html → if not onboarding_complete redirect to sprint1.html
```

---

## Reference Wallets

Unlimit was designed by studying the best practices from:

| Wallet | What We Learned |
|--------|----------------|
| **Phantom** | Iconic dark UI, simple onboarding, excellent dApp connector UX, pre-built transaction confirmation |
| **Solflare** | Multi-wallet management, staking-first design, clean tabbed navigation, .sol domain integration |
| **MetaMask** | Market-leading security UIs, token approval management, phishing detection, EIP-712 signing |

### What Unlimit Does Differently
- **Wealth Recovery** — Neither Phantom nor Solflare proactively reclaims locked rent SOL
- **Invisible ATAs** — Both Phantom and Solflare require manual token addition
- **Pre-Sign Plain English** — MetaMask shows hex data; Unlimit shows human-readable explanations
- **Whale Tags** — No existing wallet shows smart-money accumulation in real-time
- **Social Trading** — Copy-trading and Blinks are native, not bolted-on
- **TURBO Toggle** — Gamified priority fees make Solana's near-zero gas feel like a superpower

---

## File Structure

```
wallet_v1/
├── README.md          — This document
├── management.html    — Project dashboard & sprint navigation (internal only)
├── sprint1.html       — Onboarding + Wealth Recovery landing page
├── sprint2.html       — Main wallet: Invisible Token Manager, Send/Receive/Swap
├── sprint3.html       — Intelligence layer: Pre-Sign, Whale Tags, Transactions, Settings
└── sprint4.html       — Social Trading, TURBO Toggle, Blinks
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **v1.0** | May 2025 | Unlimit brand launch. Wealth Recovery, Invisible ATA, Pre-Sign Sim, Social Trading |
| v0.x | Apr 2025 | Original Phantom/MetaMask-inspired prototype (pre-Unlimit rebrand) |
