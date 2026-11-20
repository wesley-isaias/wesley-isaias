<div align="center">

# Wesley Isaias

[![Public example tests](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml/badge.svg)](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml)

**Software Developer · Digital Products · AI Engineering & MCP**

Brazil (UTC−3) · Open to remote roles in Brazil and internationally

[The story](https://wesley-isaias.github.io/wesley-isaias/) · [Featured work](#featured-work) · [Tech stack](#tech-stack) · [Zayuni](https://app.zayuni.com) · [🇧🇷 Versão em português](./README.pt-BR.md)

</div>

---

**Zayuni is the product: a healthcare SaaS. To build it quickly as a small team without risking patient data or production, I built the infrastructure around the AI agents that help develop it:** the **MCP workspace** controls *where* agents work and *what* they can reach, and **DevCore** controls *how* their tasks run and *how* the result is verified.

**[▶ Read the story: a scrolling walkthrough of the whole system](https://wesley-isaias.github.io/wesley-isaias/)**

I work end to end: requirements, data modeling, UI, integrations, testing and controlled releases. Data integrity, security and privacy are core requirements in all of it.

## Featured work

### 1 · The product

#### Zayuni: practice management for health professionals
Scheduling, patient records, care history and finances in one app for phone, tablet and desktop. Appointments sync to Google Calendar and iCloud, Pix charges as BR Codes, and payment receipts read by OCR on the device, so receipts never leave the phone. Every row is scoped per account with row-level security.
<br>`Expo` `React Native Web` `Python` `FastAPI` `Supabase` `PostgreSQL RLS` `Cloud Run` · **425 backend tests · 51 SQL migrations · 442 commits**
<br>**[Case study](./projects/zayuni.md)** · **[Product](https://app.zayuni.com)**

### 2 · The AI infrastructure behind it

#### Zayuni Dev Workspace: secure MCP access for AI agents
*Where agents work.* ChatGPT and Claude connect over MCP to an isolated container that holds no credentials. A Git gateway inspects every push and keeps the GitHub token out of the workspace, a JWT verifier guards the MCP endpoint, and a tamper-evident audit log records every action.
<br>`MCP` `Python` `Node.js` `OAuth/JWT` `Docker` `Cloudflare Access` · **81 gateway tests + offline security checks in CI**
<br>**[Case study](./projects/mcp.md)**

#### DevCore: execution engine for AI coding agents
*How tasks run.* The model only proposes actions through allow-listed tools. A router picks the cheapest capable route (no model, local model, stronger model or human), checks run in an isolated runner, and every task ends as one reviewable pull request.
<br>`Python` `LLM routing` `Ollama-compatible local inference` `Docker` `GitHub API` · **141 automated tests**
<br>**[Case study](./projects/devcore.md)**

### 3 · The same discipline, for a client

#### Sergipe Surf Federation: athlete and competition platform
Public website and athlete platform for a state sports federation: registration, memberships, event entries, Pix and card payments with webhooks, rankings imported from LiveHeats, and an admin area.
<br>`Next.js 16` `React 19` `TypeScript` `Supabase` `Mercado Pago` `Google Cloud Run` · **49 tests · 21 SQL migrations · lint and typecheck in CI**
<br>**[Case study](./projects/fss.md)**

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
