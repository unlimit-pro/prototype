# Crypto Wallet UI Prototype — Complete Documentation# Crypto Wallet UI Prototype - Complete Documentation



A comprehensive, low-fidelity wireframe prototype for a cryptocurrency wallet inspired by **MetaMask** and **Phantom Wallet**. Features **48 fully-documented tasks** with in-depth implementation specifications and **fully interactive UI prototypes** across 4 progressive sprints.A comprehensive, low-fidelity wireframe prototype for a cryptocurrency wallet inspired by **MetaMask** and **Phantom Wallet**. Features **36 fully-documented tasks** with in-depth implementation specifications and **fully interactive UI prototypes** across 3 progressive sprints.



**Version**: 4.0 — Onboarding-First Architecture  **Version**: 3.0 - Production-Ready  

**Status**: ✅ Complete | **Total Tasks**: 48 | **Sprints**: 4 | **On-chain Integration**: Full RPC/Contract Focus | **Interactive Elements**: 70+  **Status**: ✅ Complete | **Total Tasks**: 36 | **On-chain Integration**: Full RPC/Contract Focus | **Interactive Elements**: 60+  

**Architecture**: Static HTML5 + Embedded CSS + Vanilla JavaScript (Zero Dependencies)**Architecture**: Static HTML5 + Embedded CSS + Vanilla JavaScript (Zero Dependencies)



------



## 🚀 Quick Start## 🚀 Quick Start



1. **Open `management.html`** → Project dashboard with all 48 tasks (click any task ID to view full description)1. **Open `management.html`** → Project dashboard with all 36 tasks (click any task ID to view full description)

2. **Navigate sprints** → `sprint1.html` (Onboarding), `sprint2.html` (Core Wallet), `sprint3.html` (Transactions + Advanced)2. **Navigate to sprints** → `sprint1.html`, `sprint2.html`, `sprint3.html` for interactive UI prototypes

3. **All files work offline** → No server, API, or internet required3. **All files work offline** → No server, API, or internet required



------



## 📋 Project Overview## 📋 Project Overview



### Purpose### Purpose

A production-grade prototype demonstrating enterprise wallet architecture with:A production-grade prototype demonstrating enterprise wallet architecture with:

- Onboarding-first design: users cannot reach the wallet without completing account setup- Progressive feature rollout across 3 sprints (cumulative architecture)

- Progressive feature rollout across 4 sprints (cumulative architecture)- Backend-focused specifications with blockchain integration

- Backend-focused specifications with blockchain integration- Security-first design patterns from MetaMask/Phantom

- Security-first design patterns derived from MetaMask and Phantom- Real-world UX patterns and edge cases

- Real-world UX patterns and edge cases for first-time crypto users- Low-fidelity B&W UI prototypes for each sprint

- Low-fidelity B&W UI prototypes for each sprint

### Key Inspiration Sources

### Key Inspiration Sources- **MetaMask**: Multi-chain support, hardware wallet integration, security patterns

- **MetaMask**: Welcome → Terms → Password-first → Seed reveal (blur) → Word-picker confirmation → Success screen- **Phantom**: Multi-network support, transaction optimization, advanced settings UI

- **Phantom**: Clean path-selection cards, password before seed, one-click blur/reveal, recovery-phrase word tiles- **Industry Standards**: EIP-1559 gas handling, ENS resolution, token approvals, audit logging

- **Industry Standards**: EIP-1559 gas handling, ENS resolution, token approvals, BIP-39/44 wallet derivation, audit logging

### Target Users

### Target Users- **Product Managers**: Use `management.html` to track 36-task roadmap

- **Product Managers**: Use `management.html` to track 48-task roadmap across 4 sprints- **Frontend Developers**: Use `sprint1.html`, `sprint2.html`, `sprint3.html` as interactive wireframes

- **Frontend Developers**: Use sprint HTML files as interactive wireframes — especially the onboarding flow in `sprint1.html`- **Backend Developers**: Use detailed task descriptions for API/database design

- **Backend Developers**: Use detailed task descriptions for API/database design- **Security Teams**: Review 2FA, transaction validation, and audit logging implementations

- **Security Teams**: Review seed phrase handling, 2FA, transaction validation, and audit logging

---

---

## 🏗️ Architecture

## 🏗️ Architecture

### Tech Stack

### Tech Stack- **Frontend**: HTML5, CSS3, Vanilla JavaScript (no frameworks)

- **Frontend**: HTML5, CSS3, Vanilla JavaScript (no frameworks)- **State Management**: In-browser localStorage for UI state

- **State Management**: In-browser localStorage for UI state- **Styling**: Low-fidelity B&W wireframes (production-ready CSS patterns)

- **Styling**: Low-fidelity B&W wireframes (white background, black borders, no colour fills)- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation support

- **Accessibility**: Semantic HTML, ARIA labels, keyboard navigation support- **Security**: CSP-ready, no inline event handlers, modular code structure



### Design Principles### Design Principles

1. **Onboarding-First**: Users must complete Sprint 1 onboarding before accessing the wallet dashboard1. **Progressive Enhancement**: Sprint 1 (core) → Sprint 2 (transactions) → Sprint 3 (advanced)

2. **Progressive Enhancement**: Sprint 1 (onboarding) → Sprint 2 (core wallet) → Sprint 3 (transactions) → Sprint 4 (advanced)2. **Cumulative Architecture**: Each sprint includes all features from previous sprints

3. **Cumulative Architecture**: Each sprint prototype includes all features from previous sprints3. **Low-Fidelity Design**: B&W wireframes with focus on functionality and interactivity

4. **Low-Fidelity Design**: B&W wireframes with focus on functionality, interaction patterns, and flow logic4. **Separation of Concerns**: UI files separate from management/specs

5. **Security First**: Seed phrase blur/reveal, word-picker confirmation, password strength, 2FA patterns throughout5. **User-Centric**: All features designed with wallet user workflows in mind

6. **Audit Trail**: All critical operations logged and traceable

---7. **Security First**: Multi-factor authentication, rate limiting, encryption patterns



## 📁 File Structure---



```## 📁 File Structure

wallet_v1/

├── README.md                    ← You are here (complete documentation)```

├── management.html              ← Project dashboard (48 tasks across 4 sprints)wallet_v1/

├── sprint1.html                 ← Sprint 1: Onboarding & Account Setup (12 tasks)├── README.md                    ← You are here (complete documentation)

├── sprint2.html                 ← Sprint 2: Core Wallet Foundation (12 tasks, cumulative)├── management.html              ← Project dashboard (36 tasks)

└── sprint3.html                 ← Sprint 3+4: Transactions + Advanced (24 tasks, cumulative)├── sprint1.html                 ← Core Wallet (12 tasks - foundational features)

```├── sprint2.html                 ← Transaction Layer (12 tasks - sends/receives/history)

└── sprint3.html                 ← Advanced Dashboard (12 tasks - settings/API/logging)

**Notes**:```

- `sprint1.html` is the **pure onboarding prototype** — splash, path selection, terms, create/import flows, and a minimal dashboard destination.

- `sprint2.html` is the **core wallet dashboard** — assumes onboarding is complete; opens directly on the dashboard.**File Sizes**: 

- `sprint3.html` is the **full cumulative demo** — dashboard + transaction history + advanced settings.- management.html: ~45KB

- sprint1.html: ~28KB

---- sprint2.html: ~42KB

- sprint3.html: ~48KB

## 🎯 Sprint 1: Onboarding & Account Setup (12 Tasks)- **Total**: ~163KB (all files, completely self-contained)



### Overview---

The onboarding sprint is the **mandatory entry point** for all new users. Inspired by MetaMask's and Phantom's onboarding UX, it guides the user through either creating a brand-new wallet or importing an existing one — with security-first validation at every step. No part of the wallet dashboard is accessible until onboarding is completed and an `onboarding_complete` flag is stored.

## 🎯 Phase 0: Onboarding & First-Time User Experience (12 Tasks)

### Design Inspiration

| Pattern | MetaMask | Phantom | Our Implementation |### Overview

|---------|----------|---------|-------------------|The onboarding phase provides a comprehensive first-time user experience for users who don't yet have a wallet. It guides new users through either creating a new wallet or importing an existing one, with proper security validation and setup completion. This is the entry point before accessing the main wallet dashboard.

| Welcome screen | Full-screen with fox logo + "Get started" CTA | Large "P" logo + tagline + CTA | Wireframe [W] app-mark + tagline |

| Path selection | Two side-by-side cards with icons + descriptions | Two stacked options with arrow indicators | Two large bordered cards, icon placeholder, description copy |### User Flows

| Terms of use | Mandatory scrollable box + checkbox before password | Shown before seed phrase | Mandatory checkbox — blocks progression |

| Password screen | Before seed phrase; live strength meter (5 bars) | Before seed phrase; strength label | Before seed phrase; 4-segment strength bar |**Flow 1: New User → Create Wallet**

| Seed phrase display | Blurred 3×4 grid; click to reveal; copy button | Blurred pill list; click to reveal | Blurred monospace grid; "Reveal" toggle; copy |```

| Seed confirmation | Shuffled word-chip buttons → numbered target slots | Word-picker tiles with click-to-select | Shuffled chip grid → numbered slots; Reset button |Landing Page 

| Import flow | Single textarea OR 12 individual inputs toggle | 12/24-word individual input grid | 12-input grid with "Switch to 24 words" toggle |  ↓

| Success screen | "All Done!" + wallet-ready summary | "You're all set" + go to wallet CTA | Completion screen + summary card + go to wallet CTA |Choose: Create New / Import Existing 

  ↓ (Create New selected)

### User FlowsWallet Setup (Name, Network)

  ↓

**Flow A — Create New Wallet**Generate & Display Seed Phrase (12 words)

```  ↓

[Splash] → [Path Selection] → [Terms of Use] → [Create: Wallet Setup (Step 1/5)]Confirm Seed Phrase (User enters words to verify)

  → [Create: Password (Step 2/5)] → [Create: Seed Phrase Reveal (Step 3/5)]  ↓

  → [Create: Seed Phrase Confirm — Word Picker (Step 4/5)] → [Success (Step 5/5)]Set App Password / Security Setup

  → [Dashboard]  ↓

```Success → Dashboard (Sprint 1 Core Wallet)

```

**Flow B — Import Existing Wallet**

```**Flow 2: New User → Import Wallet**

[Splash] → [Path Selection] → [Terms of Use] → [Import: Phrase Entry (Step 1/3)]```

  → [Import: Password (Step 2/3)] → [Import: Success (Step 3/3)] → [Dashboard]Landing Page 

```  ↓

Choose: Create New / Import Existing 

### Sprint 1 Task Details  ↓ (Import Existing selected)

Enter Seed Phrase (12 or 24 words)

| Task ID | Component | Type | Title | Detailed Description |  ↓

|---------|-----------|------|-------|----------------------|Set App Password / Security Setup

| WLT-001 | Frontend/UI | Feature | Splash Screen | Full-screen centered splash with: (1) a square wireframe app-mark placeholder `[W]`, (2) the app name "Wallet" in bold 36px, (3) a tagline "Your keys. Your assets.", (4) a single primary "Get Started" button. No network selection or other controls. Purpose: brand impression + entry gate. Inspired by Phantom's clean minimal splash. Auto-proceeds after button tap on mobile; click required on desktop. |  ↓

| WLT-002 | Frontend/UI | Feature | Path Selection Screen | Two large bordered option cards stacked vertically (max-width 480px, centered). Card 1: icon `[+]` "Create a new wallet" + description "Generate a new wallet and recovery phrase." Card 2: icon `[↓]` "Import an existing wallet" + description "Enter a recovery phrase you already have." Each card is fully clickable (not just a button inside it). Hover state darkens border. Inspired by MetaMask's "New to MetaMask?" card layout. Back link returns to Splash. |Success → Dashboard (Sprint 1 Core Wallet)

| WLT-003 | Frontend/UI | Feature | Terms of Use Screen | Mandatory acceptance screen shown after path selection, before any wallet setup. Contains: (1) section title "Terms of Use", (2) a scrollable box (160px height) with placeholder terms text, (3) checkbox "I have read and agree to the Terms of Use", (4) primary CTA "I Agree — Continue" disabled until checkbox is checked. Based on MetaMask's mandatory terms gate which cannot be bypassed. Prevents continuation without acceptance. |```

| WLT-004 | Frontend/UI | Feature | Create: Wallet Setup | Step 1/5 progress dot stepper (●○○○○). Form fields: (1) "Wallet Name" text input, default "My Wallet", 3–30 char validation, (2) "Primary Network" dropdown (Ethereum, Polygon, Arbitrum, Optimism, Base), (3) info note: "You can add more networks later." Back → Path Selection. Continue → Password. Inline validation on blur (red border + error label beneath input). |

| WLT-005 | Frontend/UI | Feature | Create: Password Setup | Step 2/5. Two password inputs (New Password / Confirm Password). Live password strength bar: 4 segments, fills left-to-right as requirements met (1 = 8+ chars, 2 = uppercase, 3 = number, 4 = special char). Strength label below bar: "Weak / Fair / Good / Strong". Confirm input turns green border when both fields match. "Show password" checkbox toggles input type. Inspired by MetaMask's password creation step which precedes seed phrase exposure. Continue disabled until strength ≥ "Good" (3/4) and passwords match. |### Onboarding Tasks

| WLT-006 | Frontend/UI | Feature | Create: Seed Phrase Reveal | Step 3/5. Security context banner at top: "Write down your Secret Recovery Phrase and store it somewhere safe. Never share it with anyone." Seed phrase area: 12 words displayed in a 3×4 numbered grid (monospace font), **blurred by default** (CSS `filter: blur(6px)`). A centered overlay button "👁 Click to reveal" removes the blur on click (toggle; clicking again re-blurs). Copy button (clipboard icon) beside the grid copies the phrase as a space-separated string; shows "Copied!" toast for 2s. Checkbox: "I have written down my recovery phrase." Continue button disabled until checkbox is ticked. Inspired by MetaMask's blur-to-reveal pattern which prevents shoulder-surfing. |

| WLT-007 | Frontend/UI | Feature | Create: Seed Phrase Confirm (Word Picker) | Step 4/5. Header: "Confirm your Recovery Phrase". Two zones: (1) 12 numbered target slots (empty bordered squares, 3×4 grid) labelled 1–12, (2) below it, 12 shuffled word chip buttons. User clicks chips in correct sequence order to fill target slots. Clicking a chip moves it to the next empty slot and visually dims it in the chip pool. Clicking a filled target slot removes the word and returns it to the chip pool. When all 12 slots are filled, the "Verify" button activates. "Reset" button clears all slots and returns chips to pool. For prototype: any complete entry proceeds to success screen. Inspired by MetaMask's word-picker confirmation which proves the user has physically written down or memorised words — not just taken a screenshot. || Task ID | Component | Type | Title | Description |

| WLT-008 | Frontend/UI | Feature | Create: Success Screen | Step 5/5. Large circular checkmark (○ with ✓, B&W line art, 64px). Title: "Wallet Created!" Subtitle: "You're all set — your wallet is ready to use." Summary card: Wallet Name, Primary Network, Address (truncated `0x742d...a51b`, copy icon). Two CTAs: primary "Go to Wallet Dashboard", secondary link "View Recovery Phrase" (re-opens Step 3 in read-only mode). Inspired by Phantom's "You're all set" completion screen with clean summary. ||---------|-----------|------|-------|-------------|

| WLT-009 | Frontend/UI | Feature | Import: Phrase Entry | Step 1/3. Section title "Import Wallet". Sub-header: "Enter your Secret Recovery Phrase." 12 individual labeled text inputs in a 3×4 grid (word 1 through word 12). Toggle link below grid: "Switch to 24-word phrase" — expands grid to 24 inputs, toggle changes to "Switch to 12-word phrase". Network dropdown: same options as Create flow. Paste support: if user pastes a full space-separated phrase into Input 1, auto-distribute words across all inputs (split on whitespace, trim). Continue → Import Password. || WLT-001 | Frontend/UI | Feature | Welcome/Landing Screen | Create landing page with app intro, key value propositions, and two call-to-action buttons (Create New Wallet, Import Existing). Simple B&W design with progress indicator. Support "Skip for Now" for testing. |

| WLT-010 | Frontend/UI | Feature | Import: Password + Success | Step 2/3 (password) then Step 3/3 (success). Password screen is identical to Create: Password (WLT-005) with same strength bar and validation. Success screen shows "Wallet Imported!" with same summary card layout as WLT-008 (wallet name from step 1, network, truncated address). CTA: "Go to Wallet Dashboard". || WLT-002 | Frontend/UI | Feature | Wallet Creation Options | Build decision screen allowing users to choose between "Create New" and "Import Existing" wallet paths. Display icons/text explaining each option. Track user selection for next steps. |

| WLT-011 | Backend/Security | Security | Seed Phrase Encryption & Storage | Client-side: generate 12-word BIP-39 mnemonic on Create flow using ethers.js `Wallet.createRandom()`. Derive wallet address using BIP-44 path `m/44'/60'/0'/0/0` for Ethereum-compatible chains. Encrypt seed phrase using AES-256-GCM with key derived from user password via PBKDF2 (100,000 iterations, SHA-256, 16-byte random salt). Store only the encrypted blob + salt + IV in localStorage. Never transmit seed to any server. On import, validate each word against BIP-39 wordlist before proceeding. || WLT-003 | Frontend/UI | Feature | Create Wallet - Setup Screen | Implement form for wallet setup: wallet name, network selection (Ethereum/Polygon/Arbitrum/Optimism), and initial settings. Validate input (name 3-30 chars). Show setup completion progress (1/4). |

| WLT-012 | Frontend/State | Integration | Onboarding State Management | Track onboarding progress in localStorage. Keys: `onboarding_complete` (bool), `wallet_name` (string), `wallet_network` (string), `wallet_address_preview` (truncated, safe to store). On app load: if `onboarding_complete` is false or missing, redirect to Splash (WLT-001). Prevent direct URL navigation to dashboard (check flag on every route). "Reset Onboarding" option in Sprint 4 Settings (for prototype testing). Progress preserved across page refreshes so user can resume a partially completed flow. || WLT-004 | Frontend/UI | Feature | Seed Phrase Generation & Display | Generate 12-word BIP-39 seed phrase. Display in secure, easy-to-read format (monospace, numbered, grouped). Add copy-to-clipboard functionality with user feedback. Show security warning about keeping seed safe. |

| WLT-005 | Frontend/UI | Feature | Seed Phrase Confirmation | Create confirmation screen where user must enter seed words in correct order. Show 12 input fields (or sample 3-4 random words for strict validation). Provide feedback on correctness. Prevent progression until all words verified. |

---| WLT-006 | Frontend/UI | Feature | Password/Security Setup | Build password creation form with strength validation. Require 8+ chars, uppercase, lowercase, number, special char. Show password strength meter. Add checkbox for password confirmation. Display optional 2FA introduction. |

| WLT-007 | Frontend/UI | Feature | Onboarding Completion Screen | Show "Wallet Ready" confirmation page with wallet name, network, and summary. Add button to proceed to main dashboard. Display next steps (fund wallet, explore features). |

## 🎯 Sprint 2: Core Wallet Foundation (12 Tasks)| WLT-008 | Frontend/UI | Feature | Import Wallet Form | Build textarea for importing existing wallet by seed phrase. Support 12 or 24 word phrases. Validate BIP-39 compliance. Display network selection. Show gas/setup requirements on review screen. |

| WLT-009 | Backend/Service | Integration | Wallet Creation Service | Implement backend wallet generation using BIP-39/BIP-44 standards. Derive addresses for specified networks. Store encrypted seed (client-side only, never server-stored). Generate wallet addresses and keys. |

### Overview| WLT-010 | Backend/Security | Security | Seed Phrase Encryption & Storage | Implement client-side encryption for seed phrases using AES-256. Store only encrypted seed in local storage. Generate encryption key from user password. Support seed recovery via password. Never transmit seed to server. |

Sprint 2 delivers the main wallet dashboard, visible only after onboarding is complete. It covers balance display, asset list, and quick-action modals (Send, Receive, Swap). This sprint establishes the core UI shell and the backend infrastructure the entire product is built upon.| WLT-011 | Backend/Recovery | Feature | Account Recovery Setup | Create recovery code generation (10 single-use codes). Display for user to save. Store hashed codes server-side. Allow account recovery via codes if password forgotten. Implement recovery flow in settings (Sprint 3). |

| WLT-012 | Frontend/State | Integration | Onboarding State Management | Implement localStorage tracking for onboarding completion (flag: "onboarding_complete"). Show onboarding only on first visit. Allow users to restart onboarding from settings. Persist user's wallet name and network choice across sessions. |

### Prototype File: `sprint2.html`

Opens directly on the dashboard. Assumes onboarding is complete. Navigation links to sprint1 and sprint3.---



| Task ID | Component | Type | Title | Detailed Description |## 🎯 36 Tasks - Detailed Breakdown

|---------|-----------|------|-------|----------------------|

| WLT-101 | Frontend/UI | Feature | Dashboard Layout | Main wallet dashboard: sticky header (logo, network selector, settings icon), hero balance card, 4 quick-action buttons (Send / Receive / Swap / Bridge), asset table, footer navigation. Responsive grid (max-width 1000px, centered). Sticky header with z-index:100. Single-column layout inspired by MetaMask's and Phantom's mobile-first approach. |### Sprint 1: Core Wallet Foundation (12 Tasks)

| WLT-102 | Frontend/UI | Feature | Balance Display | Total balance card showing USD total (large monospace font), breakdown row: Network name, wallet address (truncated, copy icon), last-sync timestamp. Sub-row: 24h change (% and USD delta, B&W wireframe uses +/- prefix and ▲▼ arrows). Real-time update via polling (30s). |

| WLT-103 | Frontend/UI | Feature | Asset List | Sortable table: columns = Asset Name, Token Symbol, Balance, USD Value, 24h Change. Header click toggles sort asc/desc. Filter text input above table. "Add Token" button opens a modal with contract address input. Supports up to 100+ rows via virtual pagination (show 10, "Load More" button). || Task ID | Component | Type | Title | Description |

| WLT-104 | Backend/DB | Infrastructure | Database Schema | Tables: `users` (id, email_hash, password_hash, 2fa_secret, created_at), `wallets` (id, user_id, name, encrypted_seed, address, network_id), `networks` (id, name, rpc_url, chain_id, explorer_url), `assets` (id, wallet_id, token_address, symbol, name, decimals, balance, usd_value), `transactions` (id, wallet_id, hash, type, from_address, to_address, amount, gas_used, status, block_number, created_at), `settings` (user_id, key, value), `api_keys` (id, user_id, key_hash, permissions, ip_whitelist, last_used_at, revoked_at), `activity_logs` (id, user_id, action, metadata_json, ip, user_agent, status, created_at). Indexes on wallet_id, user_id, created_at, status. ||---------|-----------|------|-------|-------------|

| WLT-105 | Backend/API | Infrastructure | REST API Setup | Express.js (Node) or FastAPI (Python) server. Base path: `/api/v1/`. Middleware: JWT auth (except /auth routes), request-id header, structured JSON logging, error handler returning `{error, code, requestId}`. CORS: whitelist specific origins. Response envelope: `{success, data, meta}`. Rate limiting: 100 req/min per IP (unauthenticated), 500 req/min per JWT. || WLT-101 | Frontend/UI | Feature | Dashboard Layout | Create main wallet dashboard with header, balance card, asset list, action buttons. Responsive grid layout with sticky header. |

| WLT-106 | Backend/Auth | Security | Authentication | JWT flow: 1h access token, 7d refresh token (rotation on every use). bcrypt password hashing (cost=12). Login rate limit: 5 failed attempts → 15-min exponential-backoff lockout. Support Web3 signature auth (EIP-191 personal_sign + EIP-712 typed data). Endpoints: POST /auth/login, POST /auth/refresh, POST /auth/logout, POST /auth/web3-login. || WLT-102 | Frontend/UI | Feature | Balance Display | Display total wallet balance in USD with breakdown by asset. Show network, wallet address, last sync time. Real-time update capability. |

| WLT-107 | Frontend/UI | Feature | Header & Navigation | Sticky header: left = [Logo] [Wallet Name Dropdown (multi-wallet)], center = [Network Badge pill], right = [Notifications bell] [Settings gear] [Avatar initials]. Wallet Name Dropdown: lists all wallets, "+ Add Wallet" link. Network Badge: click opens network switcher overlay (radio select). || WLT-103 | Frontend/UI | Feature | Asset List | Display user's assets in sortable/filterable table. Show token name, address, balance, USD value, price change. Support pagination for 100+ assets. |

| WLT-108 | Backend/Integration | Integration | Balance Integration | GET /wallets/{id}/balance: queries blockchain via RPC (eth_getBalance + ERC-20 balanceOf for tracked tokens). Converts to USD via CoinGecko /simple/price. Caches in Redis (30s TTL). Returns: `{totalUsd, assets: [{symbol, balance, usdValue, change24h}]}`. Handles multi-chain by fanning out per network then aggregating. || WLT-104 | Backend/DB | Infrastructure | Database Schema | Design and implement users, wallets, networks, assets, transactions tables. Add indexes for performance. Support multi-wallet per user. |

| WLT-109 | Backend/RPC | Infrastructure | RPC Provider Setup | Primary: Infura, fallback: Alchemy, tertiary: QuickNode. Provider health checked every 60s. Circuit breaker: 3 failures in 10s → switch provider. Exponential backoff: 100ms → 200ms → 400ms → 800ms, cap 5s. Request queue: max 10 concurrent per provider. Batch calls (eth_call multicall) to reduce RPC count. || WLT-105 | Backend/API | Infrastructure | REST API Setup | Set up Express/FastAPI server with v1 endpoints. Implement authentication middleware, error handling, logging. Support CORS for frontend. |

| WLT-110 | Backend/Cache | Performance | Caching Layer | Redis: balances 30s TTL, gas prices 60s, token metadata 24h, ENS names 24h, price data 5m. LocalStorage (frontend): wallet address, network preference, onboarding_complete, UI state (active tab, sort order). Cache invalidation: explicit eviction on TX confirmation. LRU eviction policy, 256MB max. || WLT-106 | Backend/Auth | Security | Authentication | Implement JWT token flow (1h access, 7d refresh). Hash passwords with bcrypt. Add rate limiting (5 failed logins/15min). Support Web3 signature auth (EIP-191). |

| WLT-111 | Backend/Sync | Service | Blockchain Sync Service | Background worker (cron + WebSocket hybrid). On new block: scan watched addresses for Transfer events (ERC-20 Transfer topic). Update `assets.balance` and insert `transactions` rows. Batch updates: collect 10s of events then write in DB transaction. WebSocket preferred (eth_subscribe); polling fallback (eth_getFilterLogs every 15s). Re-org handling: mark affected TXs as `unconfirmed`, re-check after 6 blocks. || WLT-107 | Frontend/UI | Feature | Header & Navigation | Create sticky header with logo, network selector, settings icon. Add breadcrumb navigation. Support dropdown menus. |

| WLT-112 | Backend/Data | Integration | Asset Metadata Integration | Token metadata source: CoinGecko /coins/list + /coins/{id}/contract/{address}. 1inch Token List as fallback. Fetch: name, symbol, decimals, coingecko_id. Cache 24h. On "Add Token" (custom address): fetch metadata from contract ABI (name(), symbol(), decimals() calls). Handle unknown tokens with "Unknown Token" placeholder. || WLT-108 | Backend/Integration | Integration | Balance Integration | Query blockchain via RPC. Calculate total balance in USD using price feeds. Cache results (30s refresh). Handle multi-chain requests. |

| WLT-109 | Backend/RPC | Infrastructure | RPC Provider Setup | Integrate Infura, Alchemy, Quicknode as providers. Implement provider rotation with fallback. Add request queuing and circuit breaker. |

---| WLT-110 | Backend/Cache | Performance | Caching Layer | Implement Redis caching for balances (30s), gas prices (1m), metadata (24h). Add cache invalidation on updates. LocalStorage for frontend state. |

| WLT-111 | Backend/Sync | Service | Blockchain Sync Service | Create background service to sync wallet data from blockchain. Handle block scanning, event listening. Batch updates to reduce RPC calls. |

## 🎯 Sprint 3: Transaction Management (12 Tasks)| WLT-112 | Backend/Data | Integration | Asset Metadata Integration | Fetch token metadata (name, decimals, symbol) from CoinGecko/1Inch. Cache for 24h. Support custom token addition. |



### Overview### Sprint 2: Transaction Management (12 Tasks)

Sprint 3 builds the full transaction layer on top of the core wallet. Users can send (3-step modal with gas tiers), receive (QR code), view paginated history, filter, and track gas. Prototype: `sprint3.html` which is cumulative (Sprint 2 dashboard + transaction layer + Sprint 4 advanced settings in tabbed panel).

| Task ID | Component | Type | Title | Description |

| Task ID | Component | Type | Title | Detailed Description ||---------|-----------|------|-------|-------------|

|---------|-----------|------|-------|----------------------|| WLT-201 | Frontend/UI | Feature | Transaction History | Display paginated transaction table with date, type, recipient/sender, amount, status, tx hash. Support sorting and infinite scroll. Show 10-100 transactions. |

| WLT-201 | Frontend/UI | Feature | Transaction History Panel | Paginated table below the asset list: columns = Date/Time, Type (Sent/Received/Swap/Approve), Asset, Amount, USD Value, Status badge (Pending/Confirmed/Failed), TX Hash (truncated, explorer link icon). Default sort: most recent first. Show 10 rows; "Load More" appends 10. Click any row → Transaction Detail Modal. || WLT-202 | Frontend/UI | Feature | Send Modal Enhancement | Extend send modal from S1 with gas estimation (3 tiers: Standard/Fast/Instant). Show fees in USD. Add recipient validation (ERC-55 checksum). |

| WLT-202 | Frontend/UI | Feature | Send Modal — Enhanced | Multi-step modal (3 steps): Step 1 = Recipient (address input with inline ENS resolution, asset selector dropdown with balances, amount input with "Max" button). Step 2 = Review (recipient, amount, asset, 3 gas tiers: Standard ~2min / Fast ~30s / Instant ~10s with USD costs each). Step 3 = Confirm (spinner "Broadcasting…" then "✓ Success — TX Hash: 0x…"). || WLT-203 | Frontend/UI | Feature | Receive Modal Enhancement | Add transaction history link. Show ENS name if available. Display QR code. Support address copying with feedback. |

| WLT-203 | Frontend/UI | Feature | Receive Modal — Enhanced | Address display + large QR code placeholder `[QR Code — 160×160px]`. ENS name shown above address if resolved. Copy address button. Network selector (switch displayed network without leaving modal). Share button (native share API). "View in Explorer" link. || WLT-204 | Backend/API | Feature | Transaction API | Implement GET /transactions with filtering, pagination, sorting. GET /transactions/{hash} for details. Support block range queries. Add TX count per address. |

| WLT-204 | Backend/API | Feature | Transaction API | GET /wallets/{id}/transactions — params: page, limit, type, asset, dateFrom, dateTo, search (TX hash or address). Returns paginated `{data, total, page, pages}`. GET /transactions/{hash} — full TX details (gas used, block confirmations, decoded input data). POST /wallets/{id}/transactions/export — returns CSV download URL (90-day data). || WLT-205 | Backend/Service | Feature | Send Transaction Service | Build TX building, signing, and broadcasting. Support hardware wallet signing. Implement nonce management and tx replacement. Add confirmation polling. |

| WLT-205 | Backend/Service | Feature | Send Transaction Service | Build TX: `{to, value, data, gasLimit, maxFeePerGas, maxPriorityFeePerGas, nonce, chainId}`. Sign with decrypted private key (requires password re-entry). Broadcast via eth_sendRawTransaction. Poll receipt every 5s for up to 5 min. On receipt: update TX status, trigger balance refresh. RBF support: if pending >5min, offer "Speed Up" (bump priority fee 10%) or "Cancel" (0 ETH TX to self, same nonce). || WLT-206 | Frontend/UI | Feature | Transaction Filtering | Add filter buttons (All/Sent/Received/Pending/Failed). Implement filter state management. Support date range filtering. Real-time filter updates. |

| WLT-206 | Frontend/UI | Feature | Transaction Filtering | Filter bar above transaction table: pill buttons [All] [Sent] [Received] [Swap] [Pending] [Failed]. Active pill: filled black background. Date range picker (from/to inputs). Asset filter dropdown. Search box (TX hash or address). Filters combinable. Filter state persists in URL query params. "Reset" link clears all filters. || WLT-207 | Backend/Validation | Security | Transaction Validation | Validate recipient address format. Check sender balance >= amount + gas. Verify gas limits. Check nonce sequence. Rate limit sends (10 TX/minute). |

| WLT-207 | Backend/Validation | Security | Transaction Validation | Pre-flight checks before signing: (1) ERC-55 checksum on recipient address, (2) balance ≥ amount + estimated gas, (3) gasLimit within bounds (21,000 min, 5,000,000 max), (4) nonce == current account nonce, (5) recipient not in internal blacklist, (6) rate limit (10 sends/minute/wallet). On failure: return `{code, field, message}` for inline UI display. || WLT-208 | Backend/Gas | Integration | Gas Calculation | Calculate gas for different transaction types (transfers, approvals, swaps). Fetch current gas prices from network. Estimate fees in USD. Support custom gas limits. |

| WLT-208 | Backend/Gas | Integration | Gas Calculation | EIP-1559 fee model: fetch baseFee from latest block header. Suggest: Standard = baseFee×1.1 + 1.5 Gwei priority, Fast = baseFee×1.2 + 2.5 Gwei, Instant = baseFee×1.5 + 5 Gwei. gasLimit = eth_estimateGas × 1.2 buffer. USD cost = gasLimit × maxFeePerGas × ETH_USD / 1e18. Refresh every 30s using eth_feeHistory (50 blocks). || WLT-209 | Backend/Tracking | Feature | Transaction Tracking | Track TX status from pending → confirmed. Listen to receipt events. Update balance on confirmation. Store full TX history with gas used, blocks to confirm. |

| WLT-209 | Backend/Tracking | Feature | Transaction Tracking | State machine: `draft → broadcast → pending → confirmed / failed`. WebSocket: eth_subscribe('newHeads') → on new block, poll pending TXs via eth_getTransactionReceipt. Confirmation threshold: 1 block default, 6 blocks for high-value TX (>$1,000). On status=0 (failure): decode revert reason from receipt logs. Emit WebSocket event to frontend on any status change. || WLT-210 | Backend/Integration | Feature | ENS Support | Resolve ENS names to addresses. Support reverse ENS lookup (address → name). Cache for 24h. Handle invalid names gracefully. |

| WLT-210 | Backend/Integration | Feature | ENS Support | ENS resolution: call PublicResolver.addr(namehash(name)) via eth_call. Reverse lookup: ReverseRegistrar.node(address). Cache 24h. In Send Modal: type "vitalik.eth" → resolves inline below input within 500ms. In TX History: show ENS name instead of address where available. Handle failures gracefully (show raw address). || WLT-211 | Backend/Chains | Feature | Multi-Network Support | Enable transactions on Ethereum, Polygon, Arbitrum, Optimism. Display network selector. Support network-specific RPC calls. Store network config. |

| WLT-211 | Backend/Chains | Feature | Multi-Network Support | Network config in `networks` table. Supported: Ethereum (1), Polygon (137), Arbitrum One (42161), Optimism (10), Base (8453). Network switch: re-fetch balance and TX history for new chain. Cross-chain TX detection (same address, multiple chains). Network-specific explorer URLs for TX links. Adding network = inserting one row + RPC endpoint (no code change). || WLT-212 | Backend/Tokens | Feature | Token Approvals | Implement ERC-20 approve flow (allowance checking, increase allowance). Support EIP-2612 permits. Show approval status in UI. |

| WLT-212 | Backend/Tokens | Feature | Token Approvals | ERC-20 approve() flow: read current allowance, display in Send Modal review step if spending from an approved protocol. Support EIP-2612 permit (off-chain approval via signature). "Approve" step shown before swap/bridge if allowance < amount. Show approval in TX History as type "Approve" with spender address. Revoke: send approve(spender, 0) TX. |

### Sprint 3: Advanced Features (12 Tasks)

---

| Task ID | Component | Type | Title | Description |

## 🎯 Sprint 4: Advanced Features (12 Tasks)|---------|-----------|------|-------|-------------|

| WLT-301 | Frontend/UI | Feature | Settings UI - Tabbed Interface | Create tabbed settings page with Account, Security, Preferences, API, Activity tabs. Smooth tab switching with tab state persistence. |

### Overview| WLT-302 | Backend/Settings | Feature | Settings Management | Implement GET/PUT /account/settings. Store user preferences (currency, theme, notifications). Support default settings. Validate input before saving. |

Sprint 4 adds settings, API key management, activity logging, 2FA, price tracking, and backup/recovery — "power user" and "security" features. In the HTML prototype these are included in `sprint3.html` as a tabbed settings panel on the full cumulative demo.| WLT-303 | Frontend/UI | Feature | API Key Management UI | Display API keys with last used timestamp. Show permissions for each key. Implement create/revoke dialogs. Copy key to clipboard button. |

| WLT-304 | Frontend/UI | Feature | Activity Logs UI | Display 90-day login/action history. Show timestamp, action type, IP address, user agent, status. Support export to CSV. Implement pagination (50 entries/page). |

| Task ID | Component | Type | Title | Detailed Description || WLT-305 | Backend/API | Feature | API Key Generation | Create secure key generation (SHA-256, 32 bytes). Implement permission scoping (read_balance, read_history, execute_tx, manage_keys). Add IP whitelist support (CIDR). |

|---------|-----------|------|-------|----------------------|| WLT-306 | Backend/Logging | Feature | Activity Logging | Log all user actions: login, transactions, settings changes, API calls. Store in activity_logs table. Add 90-day retention policy. Implement log export API. |

| WLT-301 | Frontend/UI | Feature | Settings UI — Tabbed Interface | Tabbed settings page accessible from header gear icon. Tabs: [Account] [Security] [Networks] [Preferences] [API Keys] [Activity Log]. Tab state persists in URL hash (e.g. `#security`). Smooth content-switch (no page reload). Back to Wallet button in header. Each tab section described in WLT-302 to WLT-312. || WLT-307 | Backend/Auth | Security | Two-Factor Authentication | Implement TOTP (RFC 6238). Generate 10 backup codes. Support device fingerprinting. Add 2FA requirement for sensitive actions. |

| WLT-302 | Backend/Settings | Feature | Settings Management | GET/PUT /account/settings. Schema: `{currency: USD|EUR|GBP, theme: light|dark, language: en, notifications: {txConfirmed: bool, priceAlert: bool}, autoLock: 5|15|30|never}`. Partial updates via PATCH. Settings changes logged in activity_logs. Optimistic UI update: apply immediately, revert on API failure. || WLT-308 | Backend/API | Feature | Settings API | Implement PUT /account/settings for all preference types. Add validation for each setting type. Support partial updates. Log all setting changes. |

| WLT-303 | Frontend/UI | Feature | API Key Management UI | List of API keys: columns = Name, Permissions, Created, Last Used, IP Whitelist, Actions (Copy / Revoke). "Create Key" modal: name input, permission checkboxes (read_balance / read_history / execute_tx / manage_keys), IP whitelist textarea (CIDR, one per line). On create: key shown once in "Copy now — will not be shown again" dialog. Revoking requires typing key name to confirm. || WLT-309 | Backend/Logging | Feature | Smart Contract Logging | Log contract interactions (approvals, swaps, stake). Decode function calls from tx data. Store contract method + args. Link to blockchain explorer. |

| WLT-304 | Frontend/UI | Feature | Activity Log UI | Table: Timestamp, Action Type (Login / TX Sent / Settings Changed / API Call / Recovery Code Used), IP Address, User Agent (browser), Status (Success / Fail / Blocked). Pagination: 50 entries/page. Filter by Action Type. Export: "Download CSV (last 90 days)" button. Warning banner if any "Failed Login" entries exist in the last 24h. || WLT-310 | Backend/Events | Service | Event Monitoring | Listen to blockchain events (Transfer, Approval, Swap). Real-time notifications to users. Store event history. Support custom event filters. |

| WLT-305 | Backend/API | Feature | API Key Generation | Generate: `crypto.randomBytes(32)` → hex → prefix `wlt_`. Store: SHA-256 hash (never store plaintext after creation). Enforce permissions array against allowed scopes. IP whitelist: validate CIDR notation server-side. Key returned to client ONLY in the creation response. Revoke: set `revoked_at`, stop accepting immediately (no grace period). || WLT-311 | Backend/Price | Feature | Price Tracking | Fetch historical token prices (daily). Store price data for charts. Calculate portfolio value over time. Support price alerts (optional). |

| WLT-306 | Backend/Logging | Feature | Activity Logging | Log events: LOGIN_SUCCESS, LOGIN_FAIL, TX_SENT, TX_FAILED, SETTINGS_CHANGED, API_KEY_CREATED, API_KEY_REVOKED, RECOVERY_CODE_USED, 2FA_ENABLED, 2FA_DISABLED. Schema: `{id, user_id, action, metadata (JSON), ip, user_agent, status, created_at}`. Retention: 90 days (cron delete). Rows are immutable (no UPDATE/DELETE via API). || WLT-312 | Backend/Security | Feature | Backup & Recovery | Implement encrypted backup of private keys (BIP-39 mnemonic). Generate recovery codes. Support account recovery via codes. Zero-knowledge backup (client-side encryption). |

| WLT-307 | Backend/Auth | Security | Two-Factor Authentication | TOTP per RFC 6238 (30s windows, SHA-1, 6 digits). Setup flow in Security tab: (1) QR code for authenticator app (Google Authenticator / Authy), (2) verify first code, (3) show 10 backup codes (display once, store bcrypt hashes). 2FA required for: Login (if enabled), execute_tx API, changing security settings, creating/revoking API keys. Trusted device: store hashed device fingerprint to skip 2FA for 30 days. |

| WLT-308 | Backend/API | Feature | Settings API | PUT /account/settings (full update). PATCH /account/settings (partial). PUT /account/settings/notifications. PUT /account/settings/security (triggers 2FA re-auth for sensitive fields like autoLock, 2FA toggle). POST /account/settings/reset (reset to defaults). All changes append to activity_logs. Return updated settings object on success. |---

| WLT-309 | Backend/Logging | Feature | Smart Contract Interaction Logging | For every TX with non-empty `data` field: attempt ABI decode using 4-byte function signature lookup (4byte.directory API or local DB of common signatures). Store: `{contract_address, function_name, decoded_args}` in `transactions.decoded_data`. Display in TX History as "Swap on Uniswap" or "Stake on Lido" instead of raw hex. Link to contract on block explorer. |

| WLT-310 | Backend/Events | Service | Event Monitoring & Notifications | Subscribe to wallet-relevant events: ERC-20 Transfer (to/from address), ERC-721 Transfer, custom contract events. On event: create notification `{type, title, body, txHash, timestamp}`. Deliver via WebSocket to connected clients. Store in `notifications` table. Frontend: bell icon shows unread count badge. Notification dropdown lists recent 20. Mark-as-read on click. |## 🧪 Testing & Verification

| WLT-311 | Backend/Price | Feature | Price Tracking & Portfolio History | Fetch daily close prices for all held tokens (CoinGecko /coins/{id}/market_chart, 90-day range). Store in `price_history` table: `{token_id, date, price_usd}`. Calculate portfolio value time series via join with daily asset snapshots. Expose GET /wallets/{id}/portfolio-history?days=7|30|90. Alerts: configurable price threshold in settings. |

| WLT-312 | Backend/Security | Feature | Backup & Recovery | Recovery codes: 10 single-use alphanumeric codes (8 chars each), shown once on success screen (WLT-008), stored bcrypt-hashed server-side. Recovery flow: "Forgot password?" → email + recovery code → set new password. Used code marked `consumed_at`. Encrypted seed backup: re-encrypt with BIP-38-inspired passphrase derivation. Export as encrypted JSON file. Account deletion: POST /account/delete requires password + 2FA + recovery code. |### How to Test



---#### Management Dashboard (management.html)

1. **Click any Task ID** (WLT-101 through WLT-312) to open task detail modal

## 🧪 Testing & Verification2. Verify modal shows: Title, ID, Sprint, Priority, Component, Detailed Description

3. Close modal by clicking X or outside

### sprint1.html — Onboarding Flow (Primary Focus)4. Click sprint navigation buttons to open prototype files



**Create Path (11 steps):**#### Sprint 1: Core Wallet (sprint1.html)

1. Splash → click "Get Started"- Balance Display: $12,547.32 with network badge

2. Path Selection → click "Create a new wallet" card- Asset List: 4 sample tokens with sorting/filtering

3. Terms → check checkbox → "I Agree — Continue" becomes active → click- Send Modal: Enter recipient, amount, select asset

4. Wallet Setup (Step 1/5) → enter name, select network → Continue- Receive Modal: Shows address with copy button

5. Password (Step 2/5) → type weak password → strength bar shows 1 segment, Continue disabled; type strong password → 4 segments, passwords match → Continue enabled → click- Swap Modal: Select assets, see exchange rate

6. Seed Reveal (Step 3/5) → page loads with blurred grid → click "👁 Click to reveal" → words appear; click copy → "Copied!" toast; check "I have written down my recovery phrase" → Continue enabled → click- Settings Navigation: Links to Sprint 2/3

7. Word Picker (Step 4/5) → click all 12 shuffled chips (any order for prototype) to fill slots; try clicking a filled slot → word returns to chip pool; click Reset → all slots clear; re-fill all 12 → Verify button activates → click

8. Success (Step 5/5) → checkmark animation; verify summary card; click "Go to Wallet Dashboard"#### Sprint 2: Transaction Layer (sprint2.html)

9. Dashboard stub loads (Sprint 1 destination)- All Sprint 1 features (balance, assets, modals)

- Transaction History: 6 sample transactions with types

**Import Path:**- Filtering: All/Sent/Received/Pending/Failed buttons

1. Splash → "Import an existing wallet" card → Terms → Import phrase grid- Enhanced transaction item display with status indicators

2. Type words in individual inputs OR paste "word1 word2 ... word12" into Input 1 → auto-distributes- Transaction detail modal with gas and explorer info

3. Click "Switch to 24-word phrase" → grid expands to 24 inputs; switch back → returns to 12- Settings Navigation: Links to Sprint 1/3

4. Continue → Password → continue → Import Success → Dashboard

#### Sprint 3: Advanced Dashboard (sprint3.html)

### sprint2.html — Core Wallet Dashboard- All Sprint 1 & 2 features (balance, assets, transactions)

- Balance card: $12,547.32 with network badge, address, last-synced timestamp- Tabbed interface: Account, Security, Preferences, API, Activity

- Asset table: 4 tokens; click column headers to sort asc/desc- Tab Switching: Content changes per tab

- Send modal: 3-step (recipient → gas tier review → confirm)- Security toggles and password/recovery code management

- Receive modal: QR placeholder, copy address, network selector- API key management with permissions

- Swap modal: asset selectors, exchange rate display- Activity log table with status indicators

- Settings Navigation: Links to Sprint 1/2

### sprint3.html — Transactions + Advanced (Cumulative)

- All sprint2 features +### Browser Compatibility

- Transaction history table with 6 sample TXs; click row → detail modal✅ Chrome 90+, Firefox 88+, Safari 14+, Edge 90+

- Filter pills: All / Sent / Received / Swap / Pending / Failed

- Settings gear → tabbed panel: Account / Security / Preferences / API Keys / Activity Log---

- API key creation modal with permission checkboxes

- Activity log table with action types and status badges## 🔒 Security Architecture

- 2FA setup flow in Security tab

### Authentication & Authorization

### Browser Compatibility- **JWT tokens**: 1h access, 7d refresh with rotation

✅ Chrome 90+ | Firefox 88+ | Safari 14+ | Edge 90+- **Rate limiting**: 5 failed login attempts/15 minutes

- **Password policy**: 8+ chars, uppercase, number, special char

---- **Web3 auth**: EIP-191, EIP-712 signature support



## 🔒 Security Architecture### Transaction Security

- **Address validation**: ERC-55 checksum verification

### Onboarding Security (Sprint 1)- **Balance checks**: Verify before submission

- **Seed phrase**: blurred at rest in UI; explicit user action required to reveal- **Gas estimation**: Safe limits with 3 tiers (Standard/Fast/Instant)

- **Word-picker confirmation**: prevents copy-paste or screenshot re-entry; user must demonstrate knowledge of word sequence- **Nonce management**: Prevent replay, handle replacements

- **Password-before-seed**: password encrypts the seed — consistent with MetaMask v10+ and Phantom patterns- **Rate limiting**: 10 transactions/minute per user

- **AES-256-GCM encryption**: seed encrypted client-side before any localStorage write

- **PBKDF2 key derivation**: 100,000 iterations, SHA-256, 16-byte random salt### Two-Factor Authentication

- **Onboarding gate**: `onboarding_complete` flag checked on every app load; no route skipping- **TOTP**: RFC 6238 standard (30-second windows)

- **Backup codes**: 10 single-use recovery codes

### Authentication & Authorization (Sprint 2)- **Trusted devices**: Optional device fingerprinting

- **JWT tokens**: 1h access, 7d refresh with rotation on every use

- **Rate limiting**: 5 failed login attempts → 15-min exponential-backoff lockout### Audit & Logging

- **Web3 auth**: EIP-191 + EIP-712 (no password needed for hardware wallet users)- **Comprehensive logging**: All actions tracked with timestamp, IP, user agent

- **90-day retention**: Immutable audit trail

### Transaction Security (Sprint 3)- **Event types**: Login, transactions, settings changes, security events, API calls

- **ERC-55 checksum**: invalid addresses rejected before signing- **Admin access**: Complete history review capability

- **Balance pre-flight**: amount + gas must not exceed available balance

- **Gas bounds**: 21,000 min / 5,000,000 max gasLimit enforced server-side### API Security

- **Nonce management**: sequential nonce from node prevents replay or gaps- **API key hashing**: SHA-256 storage with salt

- **RBF support**: speed-up and cancel flows prevent stuck transactions- **Permission scoping**: Granular access control (read_balance, read_history, execute_transaction, manage_keys)

- **IP whitelist**: CIDR notation support

### 2FA & Audit (Sprint 4)- **Rate limiting**: 1000 requests/hour per key

- **TOTP RFC 6238**: 30-second windows, ±1 window tolerance (90s drift max)

- **Backup codes**: 10 single-use, bcrypt-hashed, invalidated on use### Data Protection

- **Immutable audit log**: no UPDATE/DELETE on activity_logs via API- **HTTPS enforcement**: Required for all endpoints

- **90-day retention**: GDPR-aligned, automated cron deletion- **CORS whitelisting**: Specific origin restriction

- **CSRF tokens**: All state-changing requests protected

---- **XSS prevention**: No inline event handlers

- **SQL injection prevention**: Parameterized queries

## 📊 Backend Specifications Summary

---

### Database Schema (8 Tables)

- **users**: Account data, 2FA settings, recovery options, password hash## 📊 Backend Specifications Summary

- **wallets**: Multi-wallet per user, encrypted seed blob + salt + IV, BIP-44 address

- **networks**: Chain config (chain_id, RPC URL, explorer URL) — add chain = insert one row### Database Schema

- **assets**: Token balances, USD values, metadata (symbol, decimals, CoinGecko ID)- **users**: Account data, 2FA settings, recovery options

- **transactions**: Full TX history, status state machine, decoded contract data, gas actuals- **wallets**: Multi-wallet support per user, network-specific

- **api_keys**: Hashed keys, permission scopes, IP whitelist, revocation timestamp- **networks**: Chain configuration (RPC URLs, explorers)

- **activity_logs**: Immutable audit trail, 90-day TTL, all user actions with metadata JSON- **assets**: Token tracking with balances and prices

- **price_history**: Daily token prices for portfolio history charts- **transactions**: Full TX history with status tracking

- **settings**: User preferences and security options

### REST API Endpoints (28+)- **api_keys**: Secure key management with permissions

- **Auth**: POST /auth/login, /auth/refresh, /auth/logout, /auth/web3-login

- **Wallets**: GET/POST/PUT/DELETE /api/v1/wallets### REST API Endpoints (25+)

- **Balance**: GET /wallets/{id}/balance- **Wallet**: GET/POST/PUT/DELETE /api/v1/wallets

- **Assets**: GET/POST /wallets/{id}/assets- **Assets**: GET /api/v1/wallets/{id}/assets

- **Transactions**: GET /wallets/{id}/transactions, GET /transactions/{hash}, POST /wallets/{id}/transactions/export- **Transactions**: GET /api/v1/wallets/{id}/transactions

- **Send TX**: POST /wallets/{id}/send- **Gas**: GET /api/v1/gas-prices

- **Gas**: GET /api/v1/gas-prices- **Send TX**: POST /api/v1/wallets/{id}/send

- **Settings**: GET/PATCH/PUT /account/settings- **Settings**: GET/PUT /api/v1/account/settings

- **API Keys**: POST/GET/DELETE /account/api-keys- **API Keys**: POST/GET/DELETE /api/v1/account/api-keys

- **Activity**: GET /account/activity-logs- **Activity Logs**: GET /api/v1/account/activity-logs

- **Portfolio**: GET /wallets/{id}/portfolio-history- **Authentication**: POST /api/v1/auth/login, /auth/refresh, /auth/logout



---### RPC Integration

- **Providers**: Infura, Alchemy, Quicknode (with fallback chains)

## 💡 Key Design Patterns- **Methods**: eth_getBalance, eth_call, eth_estimateGas, eth_sendRawTransaction

- **Caching**: 30s for balances, 1m for gas prices, 24h for metadata

### Onboarding-First Gate- **Error handling**: Circuit breaker pattern, exponential backoff, provider rotation

```

App Load → Check localStorage.onboarding_complete### Blockchain Features

  ├─ false / missing → redirect to sprint1.html Splash screen- **Multi-chain support**: Ethereum, Polygon, Arbitrum, Optimism, Base (expandable)

  └─ true           → load wallet dashboard- **Contract interaction**: ERC-20/721 support, ABI decoding

```- **Gas optimization**: EIP-1559 with dynamic pricing

- **ENS integration**: Name resolution and reverse lookup

### Cumulative Prototype Architecture- **Event monitoring**: Real-time blockchain event listening

- **sprint1.html**: Onboarding ONLY (12 screens, ends at dashboard stub)- **Token approvals**: ERC-20 allowance management, EIP-2612 permits

- **sprint2.html**: Onboarding assumed complete + Core Wallet (Sprint 2 features)

- **sprint3.html**: All prior + Transactions + Advanced Settings (Sprint 3+4 features)---



### Password Strength Bar Logic## 💡 Key Design Patterns

```

score = 0### Cumulative Feature Implementation

if length >= 8:       score += 1   → "Weak"  (1 segment)- **Sprint 1**: Core features only (no transaction history)

if has uppercase:     score += 1   → "Fair"  (2 segments)- **Sprint 2**: Includes all Sprint 1 + transaction layer

if has number:        score += 1   → "Good"  (3 segments)- **Sprint 3**: Includes Sprint 1 & 2 + advanced features

if has special char:  score += 1   → "Strong" (4 segments)

Continue button enabled only if score >= 3 AND passwords match### Error Handling

```- User-friendly error messages with recovery options

- Detailed logging for debugging (not shown to users)

### Word Picker State- Graceful degradation when services unavailable

```- Automatic retry with exponential backoff

state = { pool: [...12 shuffled words], placed: [null × 12] }

clickChip(word)   → placed[firstEmpty] = word; pool.remove(word)### Performance Optimization

clickSlot(index)  → pool.add(placed[index]); placed[index] = null- Data caching at multiple levels (Redis, browser localStorage)

reset()           → placed = [null × 12]; pool = [...all 12 shuffled]- Lazy loading for assets and modals

verifyEnabled     → placed.every(w => w !== null)- Virtualized lists for 100+ transactions

```- Batch RPC calls for efficiency

- CDN-ready asset serving

---

### Real-time Updates

## 🚀 Development Roadmap- WebSocket support for live balance/transaction updates

- Polling fallback (30s for balance, 15s for pending TX)

### Sprint 1 — Onboarding (Weeks 1–2)- Event-driven cache invalidation

- Build all 11 onboarding screens (WLT-001 to WLT-010)- User notification system

- Client-side BIP-39 seed generation and AES-256-GCM encryption (WLT-011)

- Onboarding gate logic with localStorage state management (WLT-012)---

- Word-picker confirmation and blur/reveal interactions

- Password strength bar component## 🚀 Development Roadmap



### Sprint 2 — Core Wallet (Weeks 3–4)### Phase 1: Foundation (Weeks 1-2)

- Database migrations (WLT-104), REST API scaffold (WLT-105)- Sprint 1 implementation: Core wallet features

- Authentication (WLT-106), RPC providers (WLT-109)- Database setup with migrations

- Dashboard UI, balance display, asset list (WLT-101 to WLT-103)- RPC provider integration

- Balance integration and caching (WLT-108, WLT-110)- Authentication system

- Blockchain sync service (WLT-111), asset metadata (WLT-112)

### Phase 2: Transactions (Weeks 3-4)

### Sprint 3 — Transactions (Weeks 5–6)- Sprint 2 implementation: Transaction management

- Transaction history UI and filtering (WLT-201, WLT-206)- Gas estimation and fee calculations

- Enhanced Send/Receive modals (WLT-202, WLT-203)- ENS name resolution

- Transaction API, tracking, validation, gas (WLT-204 to WLT-209)- Multi-network support

- ENS integration (WLT-210), multi-network (WLT-211), token approvals (WLT-212)

### Phase 3: Advanced (Weeks 5-6)

### Sprint 4 — Advanced Features (Weeks 7–8)- Sprint 3 implementation: Settings and API management

- Settings tabbed UI (WLT-301 to WLT-302, WLT-308)- 2FA implementation

- 2FA TOTP flow (WLT-307)- Activity logging and audit trail

- API key management (WLT-303, WLT-305)- Backup/recovery system

- Activity logging (WLT-304, WLT-306)

- Smart contract logging (WLT-309), event monitoring (WLT-310)### Post-MVP Features

- Price tracking (WLT-311), backup and recovery (WLT-312)- Hardware wallet support (Ledger, Trezor)

- NFT gallery and management

### Post-MVP Features- Portfolio analytics and charts

- Hardware wallet support (Ledger/Trezor via WebHID/WebUSB)- Mobile app version

- NFT gallery with collection view- Solana and other chain support

- Portfolio analytics with B&W sparkline charts- DeFi protocol integrations

- Mobile PWA with biometric auth- Custom token import/management

- Solana, Base, Cosmos chain support

- DeFi protocol integrations (Uniswap, Aave, Lido)---

- Watch-only wallet mode

## 📈 Metrics & Performance

---

- **Page Load Time**: <500ms

## 📈 Performance Targets- **Modal Open Time**: <100ms

- **Tab Switch Time**: <50ms

| Metric | Target |- **Transaction Filter Time**: <100ms (1000+ transactions)

|--------|--------|- **API Response Time**: <200ms (cached), <1s (fresh)

| Splash → Dashboard (cold start) | < 1 s |- **Database Query Time**: <50ms (indexed queries)

| Screen transition (onboarding) | < 150 ms |- **RPC Call Time**: <500ms (with provider diversity)

| Word picker chip interaction | < 50 ms |

| Modal open/close | < 100 ms |---

| Tab switch (Settings) | < 50 ms |

| TX filter apply | < 100 ms (1,000+ TXs) |## 🎓 Implementation Guide

| API response (cached) | < 200 ms |

| API response (fresh RPC) | < 1 s |### For Frontend Developers

1. Start with Sprint 1 (sprint1.html) - understand layout and components

---2. Review interactive patterns: modals, forms, filtering

3. Implement responsive design patterns

## 🔗 Code Reference Snippets4. Add accessibility features (ARIA labels, keyboard nav)

5. Connect to backend APIs (WLT-108 onwards)

### BIP-39 Seed Generation (Client-side, ethers.js)

```javascript### For Backend Developers

import { ethers } from 'ethers';1. Set up database schema (WLT-104)

const wallet   = ethers.Wallet.createRandom();2. Implement authentication (WLT-106)

const mnemonic = wallet.mnemonic.phrase; // "abandon ability able ..."3. Create API endpoints (WLT-105, 204)

const address  = wallet.address;         // "0x..."4. Integrate RPC providers (WLT-109)

```5. Add caching layer (WLT-110)

6. Implement transaction service (WLT-205, 209)

### AES-256-GCM Seed Encryption (WebCrypto API)7. Add security features (WLT-207, 307)

```javascript8. Set up activity logging (WLT-306)

const encryptSeed = async (phrase, password) => {

  const salt = crypto.getRandomValues(new Uint8Array(16));### For Product Managers

  const iv   = crypto.getRandomValues(new Uint8Array(12));1. Use management.html as project dashboard

  const keyMaterial = await crypto.subtle.importKey(2. Click tasks to see detailed requirements

    'raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveKey']3. Track sprint progress (Core → Transactions → Advanced)

  );4. Review testing guide for QA checklist

  const key = await crypto.subtle.deriveKey(5. Plan post-MVP features based on user feedback

    { name: 'PBKDF2', salt, iterations: 100_000, hash: 'SHA-256' },

    keyMaterial, { name: 'AES-GCM', length: 256 }, false, ['encrypt']### For Security Teams

  );1. Review authentication patterns (WLT-106)

  const enc = await crypto.subtle.encrypt({ name: 'AES-GCM', iv }, key,2. Validate transaction security (WLT-207, 208)

    new TextEncoder().encode(phrase)3. Audit logging implementation (WLT-306)

  );4. 2FA setup verification (WLT-307)

  return { salt: btoa(String.fromCharCode(...salt)),5. Penetration test deployment

           iv:   btoa(String.fromCharCode(...iv)),

           data: btoa(String.fromCharCode(...new Uint8Array(enc))) };---

};

```## 🔗 Integration Examples



### EIP-1559 Gas Estimation### Ethers.js Integration

```javascript```javascript

const getGasTiers = async (provider) => {// Get wallet balance

  const block     = await provider.getBlock('latest');const balance = await provider.getBalance(walletAddress);

  const baseFee   = block.baseFeePerGas; // BigInt in wei

  const standard  = baseFee * 110n / 100n + ethers.parseUnits('1.5', 'gwei');// Get token balance

  const fast      = baseFee * 120n / 100n + ethers.parseUnits('2.5', 'gwei');const contract = new ethers.Contract(tokenAddress, ERC20_ABI, provider);

  const instant   = baseFee * 150n / 100n + ethers.parseUnits('5',   'gwei');const balance = await contract.balanceOf(walletAddress);

  return { standard, fast, instant };

};// Estimate gas

```const gasEstimate = await provider.estimateGas({ to, data, value });



---// Send transaction

const tx = await signer.sendTransaction({ to, value, gasLimit, gasPrice });

## 📚 Learning Resources```



- **Ethers.js**: https://docs.ethers.org/### API Usage Example

- **BIP-39 Wordlist**: https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt```javascript

- **BIP-44 Paths**: https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki// Get wallet data

- **EIP-1559 Gas Model**: https://eips.ethereum.org/EIPS/eip-1559const response = await fetch('/api/v1/wallets/123', {

- **MetaMask Onboarding Docs**: https://docs.metamask.io/wallet/how-to/onboard-users/  headers: { 'Authorization': 'Bearer {token}' }

- **Phantom Wallet Guide**: https://phantom.app/learn/crypto-101/how-to-create-a-phantom-wallet});

- **WebCrypto AES-GCM**: https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/encrypt

- **RFC 6238 TOTP**: https://datatracker.ietf.org/doc/html/rfc6238// Send transaction

const result = await fetch('/api/v1/wallets/123/send', {

---  method: 'POST',

  headers: { 'Authorization': 'Bearer {token}' },

## 📝 Version History  body: JSON.stringify({

    to: '0x...',

**v4.0** (April 29, 2026) — Onboarding-First Architecture    amount: '1.5',

- Promoted Onboarding from informal "Phase 0" to formal **Sprint 1** (WLT-001 to WLT-012)    asset: 'ETH'

- Renumbered all sprints: Core Wallet = Sprint 2, Transactions = Sprint 3, Advanced = Sprint 4  })

- Total tasks updated to **48** (12 per sprint × 4 sprints)});

- Enhanced all 12 onboarding task descriptions with detailed MetaMask/Phantom UX pattern references```

- Redesigned `sprint1.html` — full MetaMask/Phantom-inspired low-fi onboarding flow:

  - Splash screen with [W] app-mark and tagline---

  - Path selection with two large clickable option cards

  - Terms of use with mandatory acceptance gate## 📚 Learning Resources

  - Password-before-seed pattern (MetaMask v10+ / Phantom style)

  - 3×4 blurred seed phrase grid with blur/reveal toggle- **Ethers.js**: https://docs.ethers.org/

  - Word-picker chip confirmation (shuffled chips → numbered target slots)- **Web3.js**: https://web3js.readthedocs.io/

  - 12-input word grid for import with paste-to-auto-distribute- **EIP Standards**: https://eips.ethereum.org/

  - "Switch to 24-word phrase" toggle on import screen- **MetaMask Docs**: https://docs.metamask.io/

  - 5-dot progress stepper on all create-path screens- **OpenZeppelin**: https://docs.openzeppelin.com/contracts/

  - Password strength bar (4-segment live feedback)- **OWASP**: https://owasp.org/www-project-top-ten/

  - Success screens with summary cards for both paths

- Added MetaMask/Phantom design comparison table---

- Added AES-256-GCM and EIP-1559 code reference snippets

- Added word-picker state pattern and password strength bar logic sections## 📝 Version History

- Updated roadmap to 4 sprints / 8 weeks

**v3.0** (April 29, 2026) - Production-Ready

**v3.0** (April 29, 2026) — Production-Ready (36 tasks, MetaMask/Phantom patterns)  - 36 tasks with in-depth descriptions

**v2.0** (April 25, 2026) — Expanded (36 tasks, on-chain integration)  - MetaMask/Phantom research and patterns

**v1.0** (April 20, 2026) — Initial (24-task prototype)- Cumulative feature implementation

- Consolidated documentation

---- Complete security specifications

- Removed redundant markdown files

**Project**: Crypto Wallet Prototype  

**Version**: 4.0 — Onboarding-First Architecture  **v2.0** (April 25, 2026)

**Status**: ✅ Complete  - Expanded to 36 tasks

**Total Tasks**: 48 (Sprint 1: 12 Onboarding · Sprint 2: 12 Core · Sprint 3: 12 Transactions · Sprint 4: 12 Advanced)  - On-chain integration details

**Created**: April 2026 | **Last Updated**: April 29, 2026  

**License**: MIT | **Dependencies**: None (fully self-contained)**v1.0** (April 20, 2026)

- Initial 24-task prototype

---

**Project**: Crypto Wallet Prototype  
**Version**: 3.0 - Production-Ready  
**Status**: ✅ Complete  
**Created**: April 2026  
**License**: MIT

**Files**: 5 (README.md + 4 HTML files)  
**Total Size**: ~163KB  
**Dependencies**: None (fully self-contained)  
**Last Updated**: April 29, 2026