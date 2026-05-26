# Development Roadmap

**Project:** Unlimit · Intelligent System  
**Schedule:** 24-Month Roadmap  
**Last updated:** 2026-05-26

The development schedule is divided into four six-month phases designed to move the platform from a foundational analytics tool to an institutional intelligence leader.

---

## Pricing Tiers & Feature Mapping

| Feature Category                | Free | Pro | Pro+ | Enterprise |
|---------------------------------|------|-----|------|------------|
| Market Overview, Top 100, Heatmap | ✔    | ✔   | ✔    | ✔          |
| Intelligence Feed (basic)       | ✔    | ✔   | ✔    | ✔          |
| Basic Alerts, 24h history       | ✔    | ✔   | ✔    | ✔          |
| 10 wallet slots, 7d history     | ✔    | ✔   | ✔    | ✔          |
| Elite Wallet tracking           |      | ✔   | ✔    | ✔          |
| Whale detection/alerts          |      | ✔   | ✔    | ✔          |
| Token analytics (holding time, P&L) |      | ✔   | ✔    | ✔          |
| AI/ML Predictive Insights       |      | ✔   | ✔    | ✔          |
| Anomaly Detection, AI Assistant |      |     | ✔    | ✔          |
| Smart Money Leaderboard         |      | ✔   | ✔    | ✔          |
| Copy Trading, Portfolio         |      | ✔   | ✔    | ✔          |
| Token Discovery Feed, DEX Analytics |      | ✔   | ✔    | ✔          |
| Social Sentiment, Widget Builder|      | ✔   | ✔    | ✔          |
| Strategy Backtesting, Rebalancer|      |     | ✔    | ✔          |
| API Playground, SDK, Webhooks   |      |     | ✔    | ✔          |
| Mobile Apps, Push Notifications |      |     | ✔    | ✔          |
| Unlimited wallets, 90d history  |      | ✔   | ✔    | ✔          |
| 10k API calls/day               |      | ✔   | ✔    |            |
| Unlimited API, custom endpoints |      |     |      | ✔          |
| White-label, on-prem, SLA       |      |     |      | ✔          |
| Multi-chain, advanced reporting |      |     |      | ✔          |

---

## Phase Overview

| Phase | Period | Status |
|---|---|---|
| Phase 1 · Foundation | Months 1–6 | In Progress |
| Phase 2 · Expansion | Months 7–12 | Planned |
| Phase 3 · Scale | Months 13–18 | Planned |
| Phase 4 · Leadership | Months 19–24 | Planned |

---

## Phase 1 · Foundation — Months 1–6

**Summary:** Launch the core analytics platform including wallet tracking, basic alerts, and token metrics.

**Goal:** Build an initial base of 5,000+ users and establish 3–5 major Solana protocol partnerships.

### Core Analytics
- Market Overview Dashboard with real-time Solana network stats
- Top 100 Token Rankings with price, volume, and 24h change
- Fund Flow Heatmap for visual capital movement
- Intelligence Feed with AI-enriched news (basic tier)

### Wallet & Token Tracking
- Elite Wallet tracking — logic-based thresholds for volume, win rate, and P&L
- Whale Wallet detection and alert subscription (activates once wallets meet criteria)
- Token detail page: price charts (own indexing service), top holders, news
- Token analytics: holding time and P&L calculations per holder

### Alerts & Signals
- Basic price alerts with 24-hour history
- Live elite signals via WebSocket (<5s latency)
- Alert rules engine with in-app and email delivery

### Data & Infrastructure
- Proprietary data indexing for candlestick charts (replaces third-party sources such as CoinGecko for core data)
- Third-party sources (e.g. CoinGecko, news feeds) retained only for non-core data
- UTC timestamp standardisation for all system calculations; browser-side conversion for user-facing display
- API rate limiting and short-TTL caching to optimise data source costs and reduce redundant calls
- Console logging of available token data points to identify analytics expansion opportunities

### User Experience
- Informational tooltips and contextual guides to help users interpret data values correctly
- Semantic versioning in prototype URLs (e.g. `v1/index.html`) to allow teams to navigate specific versions
- AI/ML predictions presented as informational signals only, with explicit disclaimer that they are not financial guarantees
- Free plan: 10 wallet slots, 7-day data history, 1,000 API calls/day

---

## Phase 2 · Expansion — Months 7–12

**Summary:** Deploy advanced AI models for Predictive Insights and Anomaly Detection.

**Goal:** Launch Pro and Enterprise tiers and expand the team to 15 members.

### AI & Predictive Intelligence
- AI/ML-based Predictive Insights — framed as informational signals with explicit disclaimer (not financial guarantees)
- Anomaly Detection model for unusual on-chain activity
- AI Market Assistant (RAG chatbot) for contextual token queries
- AI News Curator — news re-ranked by relevance to user portfolio and preferences

### Advanced Wallet Intelligence
- Smart Money Leaderboard (500+ elite wallets)
- Elite Wallet deep-dive with full P&L tracking and holding-time analysis
- Whale Consensus Scanner — cross-wallet signal aggregation
- Copy Trading and Portfolio mirroring with configurable allocation and daily cap

### Pro & Enterprise Tiers
- Pro plan ($45/mo): 90-day history, 10,000 API calls/day, unlimited wallet tracking, 14-day free trial
- Enterprise plan: custom endpoints, white-label options, SLA support, full API access (modelled on existing Helas partnership)
- Gold package (future consideration): advanced dashboard customisation, priced 20–30% above Pro

### Advanced Discovery & Analytics
- Token Discovery Feed (live) for newly launched tokens
- DEX Pool Analytics with health colour scale
- Social Sentiment analysis and Sentiment Heatmap
- Custom Widget Dashboard builder

### Infrastructure & Architecture
- HTTP-based internal microservice communication to leverage horizontal pod scaling
- Circuit breaker patterns to gracefully handle service threshold failures under high traffic
- Dedicated Kubernetes nodes allocated to data-heavy services (e.g. Token Metric) to mitigate ingestion latency from token program event subscriptions
- Microservice decoupling: Token Metric, Wallet Aggregator, Feature Builder, and Anomaly Detector separated to resolve cross-service dependency issues
- Architecture and flow diagrams documenting microservice structure and data paths (draw.io / Mermaid)
- API developed to enable front-end integration

### Team & Process
- Phase scope documented in Confluence, reviewed, and frozen before prototyping begins
- Team expansion to 15 members including QA and front-end hires; wallet team recruitment to follow
- Transition to Claude Pro for prototyping and diagramming tasks

---

## Phase 3 · Scale — Months 13–18

**Summary:** Release the API platform for third-party developers and launch mobile applications.

**Goal:** Secure 5+ institutional clients and release a developer-facing API platform.

### API Platform
- Public REST API for third-party developers with versioned endpoints
- API Playground — live browser-based endpoint testing tool
- Tiered API rate limits: Free (1k/day), Pro (10k/day), Enterprise (unlimited)
- Developer documentation, SDK references, and webhook support

### Institutional Clients
- Target 5+ institutional clients with dedicated account management
- Custom data endpoints and full data history for enterprise contracts
- On-premises deployment options and SLA guarantees
- Enterprise API partnerships (expanding on Helas partnership model)

### Mobile Applications
- iOS and Android mobile applications with core dashboard features
- Push notifications for price alerts and elite wallet signals
- Mobile-first responsive layout across all key views

### Platform Maturity
- Strategy Backtesting engine for user-defined trading rules
- Portfolio Rebalancer and Strategy Comparison tools
- Multi-Wallet Dashboard for institutional and power users
- Advanced auto-DCA and ladder execution strategies

---

## Phase 4 · Leadership — Months 19–24

**Summary:** Introduce white-label solutions for exchanges and begin multi-chain expansion research.

**Goal:** Target 200,000 users and a path to profitability with $2M+ monthly recurring revenue (MRR).

### White-Label & Partnerships
- White-label analytics platform for exchanges and financial institutions
- Configurable branding, custom domains, and modular feature licensing
- Institutional intelligence packages with co-branded reporting
- Expanded partnership programme building on established exchange integrations

### Multi-Chain Expansion
- Research and feasibility analysis for Ethereum, Base, and other EVM chains
- Unified cross-chain wallet tracking and P&L aggregation
- Chain-agnostic anomaly detection and smart money signals
- Multi-chain heatmap and fund flow visualisation

### Revenue & Growth
- Target: 200,000 active users
- Target: $2M+ monthly recurring revenue (MRR)
- Self-serve onboarding funnel optimised for conversion
- Referral and affiliate programme scaling

### Platform Intelligence
- Advanced AI model iteration informed by production signal accuracy data
- Institutional-grade research reports with AI-generated summaries
- Predictive risk scoring across token, wallet, and protocol dimensions
