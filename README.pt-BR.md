<div align="center">

# Wesley Isaias

[![Public example tests](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml/badge.svg)](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml)

**Desenvolvedor de Software · Produtos Digitais · Engenharia de IA e MCP**

Brasil (UTC−3) · Aberto a oportunidades remotas no Brasil e no exterior

[Projetos](#projetos-em-destaque) · [Tecnologias](#tecnologias) · [Zayuni](https://app.zayuni.com) · [🇺🇸 English version](./README.md)

</div>

---

Desenvolvo infraestrutura de engenharia de IA e produtos web full-stack. Meu trabalho inclui o **DevCore**, um motor agnóstico de modelo que executa agentes de código com controles determinísticos; a camada de segurança de um **workspace MCP** que conecta ChatGPT e Claude a ambientes de desenvolvimento isolados; e plataformas web full-stack com Next.js e Supabase.

Atuo de ponta a ponta: requisitos, modelagem de dados, interface, integrações, testes e entregas controladas. Integridade de dados, segurança e privacidade são requisitos centrais em todo esse processo.

## Projetos em destaque

### DevCore: motor de execução para agentes de código
Separa o raciocínio do modelo da execução. O modelo só acessa um conjunto restrito de ferramentas, as verificações reais rodam em um executor isolado, e cada tarefa termina em um único pull request revisável. Um roteador decide, por tarefa, se dispensa o modelo, usa um modelo local, usa um modelo mais forte ou pede decisão humana.
<br>`Python` `Roteamento de LLMs` `Inferência local compatível com Ollama` `Docker` `API do GitHub` · **141 testes automatizados**
<br>**[Estudo de caso](./projects/pt-br/devcore.md)**

### Zayuni Dev Workspace: acesso MCP seguro para agentes de IA
Camada de segurança de um workspace de desenvolvimento baseado em MCP, usado a partir do ChatGPT e do Claude: um gateway Git que inspeciona cada push e mantém o token do GitHub fora do workspace, verificação de JWT na frente do endpoint MCP e um log de auditoria à prova de adulteração.
<br>`MCP` `Python` `Node.js` `OAuth/JWT` `Docker` `Cloudflare Access` · **81 testes do gateway + checks de segurança offline na CI**
<br>**[Estudo de caso](./projects/pt-br/mcp.md)**

### Federação Sergipana de Surf: plataforma de atletas e competições
Site público e plataforma autenticada para uma federação esportiva estadual: cadastro de atletas, filiações, inscrições em etapas, pagamentos por Pix e cartão com webhooks, ranking e área administrativa.
<br>`Next.js 16` `React 19` `TypeScript` `Supabase` `Mercado Pago` `Google Cloud Run` · **21 migrações SQL · lint, typecheck e testes na CI**
<br>**[Estudo de caso](./projects/pt-br/fss.md)**

### Zayuni: SaaS para profissionais de saúde
Agenda, cadastro de pacientes, atendimentos e gestão financeira para profissionais autônomos, com interface para celular, tablet e computador.
<br>`Supabase` `PostgreSQL` `Web responsiva` `Staging → produção`
<br>**[Estudo de caso](./projects/pt-br/zayuni.md)** · **[Produto](https://app.zayuni.com)**

## Tecnologias

| Área | Tecnologias |
| --- | --- |
| **Linguagens** | TypeScript, Python, JavaScript, SQL |
| **Front-end** | React 19, Next.js (App Router), interfaces responsivas |
| **Back-end e dados** | Node.js, Python, Supabase (PostgreSQL, Auth, migrações SQL), APIs REST, webhooks, Mercado Pago (Pix, cartão) |
| **Engenharia de IA** | Model Context Protocol (MCP), orquestração de agentes de código, roteamento de modelos (local ↔ avançado ↔ humano), inferência local compatível com Ollama, telemetria de agentes |
| **Segurança** | Verificação OAuth/JWT (RS256, falha fechada), isolamento de credenciais, inspeção de push Git, logs de auditoria encadeados por HMAC, privilégio mínimo |
| **Infraestrutura** | Linux, Docker, Google Cloud Run e Cloud Build, Cloudflare, GitHub Actions, CircleCI |
| **Práticas** | Revisão de pull requests, testes automatizados, staging → produção, migrações reversíveis |

## Exemplo público reproduzível

[**Política de autorização de ferramentas para agentes — Python, testes unitários e CI**](./examples/agent-policy/README.md). Exemplo independente e educacional, sem código extraído do MCP privado.

## Como trabalho

- **Mudanças pequenas e verificáveis:** cada mudança tem escopo claro, critérios de aceite e testes antes de ir para revisão.
- **Integridade de dados em primeiro lugar:** releases e migrações são planejadas para ser reversíveis, e os dados de cada conta ficam isolados.
- **Segurança por padrão:** privilégio mínimo, nenhum segredo no código e aprovação explícita para operações destrutivas.
- **IA com responsabilidade:** agentes aceleram a entrega, e pessoas continuam responsáveis por revisão, release e produção.

## Sobre o acesso ao código

A maior parte do meu trabalho profissional está em repositórios privados. Os estudos de caso acima mostram os problemas, a arquitetura e as decisões de engenharia sem expor código proprietário nem dados de clientes. Em entrevistas técnicas, apresento o código e as decisões de design com prazer.

## Vamos conversar

Estou aberto a oportunidades **CLT, PJ ou contrato internacional** em engenharia de software, desenvolvimento full-stack e engenharia de IA, remotas ou híbridas, no Brasil ou no exterior.

<!-- Adicione aqui seus links de contato, por exemplo:
[LinkedIn](https://www.linkedin.com/in/seu-usuario) · [E-mail](mailto:voce@exemplo.com)
-->
