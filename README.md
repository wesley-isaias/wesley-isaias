<div align="center">

# Wesley Isaias

[![Public example tests](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml/badge.svg)](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml)

**Software Developer · Digital Products · AI Engineering & MCP**

Brazil (UTC−3) · Open to remote roles in Brazil and internationally

[The story](https://wesley-isaias.github.io/wesley-isaias/) · [Featured work](#featured-work) · [Tech stack](#tech-stack) · [Zayuni](https://app.zayuni.com) · [🇧🇷 Versão em português](./README.pt-BR.md)

</div>

---

**Zayuni is the product: a healthcare SaaS that I develop with AI coding agents inside a strict delivery process.** Every change starts from an approved issue, runs through tests, CI and review, and reaches production only through an explicit promotion. To make that safe, I built and run **Zayuni DevWS**, my own MCP server: ChatGPT and Claude work in my repositories through an isolated workspace that holds no credentials, with every push inspected and every action audited.

**[▶ Read the story: a scrolling walkthrough of the whole system](https://wesley-isaias.github.io/wesley-isaias/)**

I work end to end: requirements, data modeling, UI, integrations, testing and controlled releases. Data integrity, security and privacy are core requirements in all of it.

## Featured work

### 1 · The product

#### Zayuni: practice management for health professionals
Scheduling, patient records, care history and finances in one app for phone, tablet and desktop. Appointments sync to Google Calendar and iCloud, Pix charges as BR Codes, and payment receipts read by OCR on the device, so receipts never leave the phone. Every row is scoped per account with row-level security.
<br>`Expo` `React Native Web` `Python` `FastAPI` `Supabase` `PostgreSQL RLS` `Cloud Run` · **425 backend tests · 51 SQL migrations · 442 commits**
<br>**[Case study](./projects/zayuni.md)** · **[Product](https://app.zayuni.com)**

### 2 · The AI infrastructure behind it

#### Zayuni DevWS: my own MCP server for AI agents
*Where agents work.* In daily use since November 2026, including from ChatGPT on my phone. Seven Docker services: OAuth with MFA and a fail-closed JWT check, a workspace with no credentials, a Git gateway that holds the token and refuses pushes to `main`, an egress proxy, and an HMAC-chained audit log anchored to a write-locked bucket.
<br>`MCP` `Python` `Node.js` `OAuth/JWT` `Docker Compose` `Cloudflare` · **81 gateway tests · branch → push → PR from a phone, PC off**
<br>**[Case study](./projects/mcp.md)**

### 3 · The same discipline, for a client

#### Sergipe Surf Federation: athlete and competition platform (in development)
Public website and athlete platform for a state sports federation, in development on staging: registration, memberships, event entries, Pix and card payments with webhooks, rankings imported from LiveHeats, and an admin area.
<br>`Next.js 16` `React 19` `TypeScript` `Supabase` `Mercado Pago` `Google Cloud Run` · **49 tests · 21 SQL migrations · lint and typecheck in CI**
<br>**[Case study](./projects/fss.md)**

### Lab

#### DevCore: prototype engine for AI coding tasks
An experiment from October 2026: the model only proposes actions through allow-listed tools, a router picks the cheapest capable route (no model, local model, stronger model or human), and checks run in an isolated runner before a pull request is opened. It is not part of the production workflow.
<br>`Python` `LLM routing` `Ollama-compatible local inference` `Docker` · **141 automated tests**
<br>**[Notes](./projects/devcore.md)**

## Tech stack

| Area | Technologies |
| --- | --- |
| **Languages** | TypeScript, Python, JavaScript, SQL |
| **Front-end** | React 19, Next.js (App Router), Expo / React Native Web, PWA, responsive interfaces |
| **Back-end & data** | Python (FastAPI), Node.js, Supabase (PostgreSQL, Auth, row-level security, SQL migrations), REST APIs, webhooks, Pix (BR Code, Mercado Pago), Google Calendar & CalDAV |
| **AI engineering** | Model Context Protocol (MCP), coding-agent orchestration, model routing (local ↔ frontier ↔ human), Ollama-compatible local inference, agent telemetry |
| **Security** | OAuth/JWT verification (RS256, fail-closed), credential isolation, Git push inspection, HMAC-chained audit logs, least privilege |
| **Infrastructure** | Linux, Docker, Google Cloud Run & Cloud Build, Cloudflare, GitHub Actions, CircleCI |
| **Practices** | Pull-request review, automated testing, staging → production releases, reversible migrations |

## Reproducible public example

[**AI tool authorization policy — Python + unit tests + CI**](./examples/agent-policy/README.md). A small, independent demonstration of deny-by-default checks. This is educational code, **not** extracted from the private MCP infrastructure.

## How I work

- **Small, verifiable changes:** each change has a clear scope, acceptance criteria and tests before it goes to review.
- **Data integrity first:** releases and migrations are planned to be reversible, and user data stays isolated per account.
- **Secure by default:** least privilege, no secrets in code, and explicit approval for destructive operations.
- **AI with accountability:** agents speed up delivery, while people keep ownership of review, release and production.

## About code access

Most of my professional work is in private repositories. The case studies above cover the problems, architecture and engineering decisions without exposing proprietary code or client data. I'm glad to walk through code and design choices in technical interviews.

## Let's talk

I'm open to **full-time or contract** roles in software development, full-stack development and AI engineering, remote or hybrid, in Brazil or internationally.

<!-- Add your contact links here, e.g.:
[LinkedIn](https://www.linkedin.com/in/your-handle) · [Email](mailto:you@example.com)
-->
