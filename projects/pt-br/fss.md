# Federação Sergipana de Surf: plataforma de atletas e competições

[← Voltar ao perfil](../../README.pt-BR.md) · [🇺🇸 English](../fss.md)

| | |
| --- | --- |
| **Cliente** | Federação Sergipana de Surf |
| **Papel** | Desenvolvedor full-stack: arquitetura, front-end, banco de dados, pagamentos e deploy |
| **Status** | Em desenvolvimento ativo, publicado em ambiente de homologação |
| **Tecnologias** | Next.js 16 (App Router) · React 19 · TypeScript · Supabase (PostgreSQL, Auth) · Mercado Pago · Docker · Google Cloud Run e Cloud Build |
| **Evidências** | Typecheck e lint sem erros · 49 testes automatizados passando · 21 migrações SQL · CI no GitHub Actions e no CircleCI |

## Contexto

Uma federação esportiva estadual fazia manualmente o cadastro de atletas, as filiações, as inscrições em etapas e o ranking. Ela precisava de um site público moderno e de uma plataforma em que atletas e equipe resolvessem esses processos online.

## O que construí

**Site público:** informações da federação, etapas, ranking e apoiadores, com metadados de SEO, imagens Open Graph, sitemap e manifesto de aplicativo web.

**Plataforma do atleta:**
- cadastro, login e recuperação de senha com Supabase Auth (sessão no servidor)
- perfil do atleta com foto e validação de dados de identificação
- filiação e inscrição em etapas
- carteirinha digital verificável por código, com QR code

**Pagamentos:**
- Pix e cartão de crédito via Mercado Pago
- processamento de webhooks para confirmação assíncrona
- fluxos de retorno e status que não confiam no redirecionamento do navegador

**Área administrativa:** gestão de filiados e operação das competições pela equipe da federação.

**Dados de competição:** importação de resultados do LiveHeats, a plataforma de pontuação das competições, e ranking com detalhamento de pontos por etapa.

## Práticas de engenharia

- **Banco como código:** 21 migrações SQL versionadas no Supabase.
- **Portões de qualidade:** typecheck estrito do TypeScript, ESLint e testes com o test runner do Node na CI.
- **Entrega em contêiner:** imagem Docker gerada pelo Cloud Build e publicada no Cloud Run (região de São Paulo), fixada pelo digest da imagem.
- **Ambientes separados:** homologação é validada antes da produção, e dados reais de filiados nunca aparecem em testes ou material público.
- **Regra permanente:** nenhuma implementação, migração, deploy ou rollback pode causar perda de dados de usuários reais.
