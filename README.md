<div align="center">

# Wesley Isaias

[![Public example tests](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml/badge.svg)](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml)

**Software Developer · Digital Products · AI Engineering & MCP**

Brazil (UTC−3) · Open to remote roles in Brazil and internationally

[Featured work](#featured-work) · [Tech stack](#tech-stack) · [Zayuni](https://app.zayuni.com) · [🇧🇷 Versão em português](./README.pt-BR.md)

</div>

---

I build AI engineering infrastructure and full-stack web products. My work includes **DevCore**, a model-agnostic engine that runs AI coding agents under deterministic guardrails; the security layer of an **MCP workspace** that connects ChatGPT and Claude to isolated development environments; and full-stack web platforms built with Next.js and Supabase.

I work end to end: requirements, data modeling, UI, integrations, testing and controlled releases. Data integrity, security and privacy are core requirements in all of it.

## Featured work

### DevCore: execution engine for AI coding agents
Separates model reasoning from execution. Models get only an allow-listed tool surface, real checks run in an isolated runner, and every task ends as one reviewable pull request. Routing decides per task whether to skip the model, use a local model, use a stronger model or ask a human.
<br>`Python` `LLM routing` `Ollama-compatible local inference` `Docker` `GitHub API` · **141 automated tests**
<br>**[Case study](./projects/devcore.md)**

### Zayuni Dev Workspace: secure MCP access for AI agents
Security layer for an MCP-based development workspace used from ChatGPT and Claude: a Git gateway that inspects every push and keeps the GitHub token out of the workspace, JWT verification in front of the MCP endpoint, and a tamper-evident audit log.
<br>`MCP` `Python` `Node.js` `OAuth/JWT` `Docker` `Cloudflare Access` · **81 gateway tests + offline security checks in CI**
<br>**[Case study](./projects/mcp.md)**

### Sergipe Surf Federation: athlete and competition platform
Public website and authenticated platform for a state sports federation: athlete registration, memberships, event entries, Pix and card payments with webhooks, rankings and an admin area.
<br>`Next.js 16` `React 19` `TypeScript` `Supabase` `Mercado Pago` `Google Cloud Run` · **21 SQL migrations · lint, typecheck and tests in CI**
<br>**[Case study](./projects/fss.md)**

### Zayuni: SaaS for healthcare professionals
Scheduling, patient records, appointments and financial management for independent practitioners, built for phone, tablet and desktop.
<br>`Supabase` `PostgreSQL` `Responsive web` `Staging → production`
<br>**[Case study](./projects/zayuni.md)** · **[Product](https://app.zayuni.com)**

## Tech stack

| Area | Technologies |
| --- | --- |
| **Languages** | TypeScript, Python, JavaScript, SQL |
| **Front-end** | React 19, Next.js (App Router), responsive interfaces |
| **Back-end & data** | Node.js, Python, Supabase (PostgreSQL, Auth, SQL migrations), REST APIs, webhooks, Mercado Pago (Pix, card) |
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

I'm open to **full-time or contract** roles in software engineering, full-stack development and AI engineering, remote or hybrid, in Brazil or internationally.

<!-- Add your contact links here, e.g.:
[LinkedIn](https://www.linkedin.com/in/your-handle) · [Email](mailto:you@example.com)
-->
