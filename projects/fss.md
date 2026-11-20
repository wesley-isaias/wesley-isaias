# Sergipe Surf Federation: athlete and competition platform

[← Back to profile](../README.md) · [🇧🇷 Português](./pt-br/fss.md)

| | |
| --- | --- |
| **Client** | Federação Sergipana de Surf (state surfing federation, Brazil) |
| **Role** | Full-stack developer: architecture, front-end, database, payments and deployment |
| **Status** | In active development, deployed to a staging environment |
| **Stack** | Next.js 16 (App Router) · React 19 · TypeScript · Supabase (PostgreSQL, Auth) · Mercado Pago · Docker · Google Cloud Run & Cloud Build |
| **Evidence** | Clean typecheck and lint · 49 automated tests passing · 21 SQL migrations · CI on GitHub Actions and CircleCI |

## Context

A state sports federation ran athlete registration, memberships, event entries and rankings by hand. It needed a modern public website and a platform where athletes and staff handle these processes online.

## What I built

**Public website:** federation information, events and stages, rankings, supporters, with SEO metadata, Open Graph images, a sitemap and a web app manifest.

**Athlete platform:**
- sign-up, sign-in and password recovery with Supabase Auth (server-side sessions)
- athlete profile with photo and identity data validation
- membership and stage entries
- a digital membership card verifiable by code, with a QR code

**Payments:**
- Pix and credit card through Mercado Pago
- webhook processing for asynchronous payment confirmation
- return and status flows that do not trust the client-side redirect

**Admin area:** membership management and competition operations for the federation's staff.

**Competition data:** import of results from LiveHeats, the competition scoring platform, and a ranking with a per-stage score breakdown.

## Engineering practices

- **Database as code:** 21 versioned SQL migrations in Supabase.
- **Quality gates:** TypeScript strict typecheck, ESLint and the Node test runner in CI.
- **Containerized delivery:** Docker image built by Cloud Build and deployed to Cloud Run (São Paulo region), pinned by image digest.
- **Separate environments:** staging is validated before production, and real member data never appears in tests or public material.
- **Permanent rule:** no implementation, migration, deploy or rollback may cause data loss for real users.
