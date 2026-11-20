<div align="center">

# Wesley Isaias

[![Public example tests](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml/badge.svg)](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml)

**Desenvolvedor de Software · Produtos Digitais · Engenharia de IA e MCP**

Brasil (UTC−3) · Aberto a oportunidades remotas no Brasil e no exterior

[A história](https://wesley-isaias.github.io/wesley-isaias/) · [Projetos](#projetos-em-destaque) · [Tecnologias](#tecnologias) · [Zayuni](https://app.zayuni.com) · [🇺🇸 English version](./README.md)

</div>

---

**O Zayuni é o produto: um SaaS de saúde. Para desenvolvê-lo rápido, com equipe pequena, sem arriscar dados de pacientes nem a produção, construí a infraestrutura em volta dos agentes de IA que ajudam a desenvolvê-lo:** o **workspace MCP** controla *onde* os agentes trabalham e *o que* podem acessar, e o **DevCore** controla *como* as tarefas são executadas e *como* o resultado é verificado.

**[▶ Leia a história: um passeio pelo sistema inteiro, rolando a página](https://wesley-isaias.github.io/wesley-isaias/)**

Atuo de ponta a ponta: requisitos, modelagem de dados, interface, integrações, testes e entregas controladas. Integridade de dados, segurança e privacidade são requisitos centrais em todo esse processo.

## Projetos em destaque

### 1 · O produto

#### Zayuni: gestão de consultório para profissionais de saúde
Agenda, pacientes, histórico de atendimentos e financeiro num app para celular, tablet e computador. Agendamentos sincronizados com Google Calendar e iCloud, cobranças Pix como BR Code e comprovantes lidos por OCR no próprio aparelho, sem que o comprovante saia do celular. Cada registro fica restrito à sua conta por row-level security.
<br>`Expo` `React Native Web` `Python` `FastAPI` `Supabase` `PostgreSQL RLS` `Cloud Run` · **425 testes no backend · 51 migrações SQL · 442 commits**
<br>**[Estudo de caso](./projects/pt-br/zayuni.md)** · **[Produto](https://app.zayuni.com)**

### 2 · A infraestrutura de IA por trás dele

#### Zayuni Dev Workspace: acesso MCP seguro para agentes de IA
*Onde os agentes trabalham.* ChatGPT e Claude se conectam por MCP a um contêiner isolado, sem credenciais. Um gateway Git inspeciona cada push e mantém o token do GitHub fora do workspace, um verificador JWT protege o endpoint MCP, e um log de auditoria à prova de adulteração registra cada ação.
<br>`MCP` `Python` `Node.js` `OAuth/JWT` `Docker` `Cloudflare Access` · **81 testes do gateway + checks de segurança offline na CI**
<br>**[Estudo de caso](./projects/pt-br/mcp.md)**

#### DevCore: motor de execução para agentes de código
*Como as tarefas rodam.* O modelo só propõe ações por ferramentas permitidas. Um roteador escolhe a rota mais barata capaz de resolver (sem modelo, modelo local, modelo mais forte ou humano), as verificações rodam num executor isolado, e cada tarefa termina em um único pull request revisável.
<br>`Python` `Roteamento de LLMs` `Inferência local compatível com Ollama` `Docker` `API do GitHub` · **141 testes automatizados**
<br>**[Estudo de caso](./projects/pt-br/devcore.md)**

### 3 · A mesma disciplina, para um cliente

#### Federação Sergipana de Surf: plataforma de atletas e competições
Site público e plataforma do atleta para uma federação esportiva estadual: cadastro, filiações, inscrições em etapas, pagamentos por Pix e cartão com webhooks, ranking importado do LiveHeats e área administrativa.
<br>`Next.js 16` `React 19` `TypeScript` `Supabase` `Mercado Pago` `Google Cloud Run` · **49 testes · 21 migrações SQL · lint e typecheck na CI**
<br>**[Estudo de caso](./projects/pt-br/fss.md)**

## Tecnologias

| Área | Tecnologias |
| --- | --- |
| **Linguagens** | TypeScript, Python, JavaScript, SQL |
| **Front-end** | React 19, Next.js (App Router), Expo / React Native Web, PWA, interfaces responsivas |
| **Back-end e dados** | Python (FastAPI), Node.js, Supabase (PostgreSQL, Auth, row-level security, migrações SQL), APIs REST, webhooks, Pix (BR Code, Mercado Pago), Google Calendar e CalDAV |
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

Estou aberto a oportunidades **CLT, PJ ou contrato internacional** em desenvolvimento de software, desenvolvimento full-stack e engenharia de IA, remotas ou híbridas, no Brasil ou no exterior.

<!-- Adicione aqui seus links de contato, por exemplo:
[LinkedIn](https://www.linkedin.com/in/seu-usuario) · [E-mail](mailto:voce@exemplo.com)
-->
