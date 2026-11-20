<div align="center">

# Wesley Isaias

[![Public example tests](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml/badge.svg)](https://github.com/wesley-isaias/wesley-isaias/actions/workflows/public-example-tests.yml)

**Desenvolvedor de Software · Produtos Digitais · Engenharia de IA e MCP**

Brasil (UTC−3) · Aberto a oportunidades remotas no Brasil e no exterior

[LinkedIn](https://www.linkedin.com/in/wesley-isaias) · [A história](https://wesley-isaias.github.io/wesley-isaias/) · [Projetos](#projetos-em-destaque) · [Tecnologias](#tecnologias) · [Zayuni](https://app.zayuni.com) · [🇺🇸 English version](./README.md)

</div>

---

**O Zayuni é o produto: um SaaS de saúde com usuários reais, que fundei e desenvolvo com agentes de IA dentro de um processo de entrega rígido.** Toda mudança começa de uma issue aprovada, passa por testes, CI e revisão, e só chega à produção por uma promoção explícita. Para que isso seja seguro, construí e opero o **Zayuni DevWS**, meu próprio servidor MCP: o ChatGPT e o Claude trabalham nos meus repositórios por um workspace isolado e sem credenciais, com cada push inspecionado e cada ação auditada.

**[▶ Leia a história: um passeio pelo sistema inteiro, rolando a página](https://wesley-isaias.github.io/wesley-isaias/)**

Atuo de ponta a ponta: requisitos, modelagem de dados, interface, integrações, testes e entregas controladas. Integridade de dados, segurança e privacidade são requisitos centrais em todo esse processo.

## Projetos em destaque

### 1 · O produto

#### Zayuni: gestão de consultório para profissionais de saúde · *fundador*
Agenda, pacientes, histórico de atendimentos e financeiro num app para celular, tablet e computador. Agendamentos sincronizados com Google Calendar e iCloud, cobranças Pix como BR Code e comprovantes lidos por OCR no próprio aparelho, sem que o comprovante saia do celular. Cada registro fica restrito à sua conta por row-level security.
<br>`Expo` `React Native Web` `Python` `FastAPI` `Supabase` `PostgreSQL RLS` `Cloud Run` · **425 testes no backend · 51 migrações SQL · 442 commits**
<br>**[Estudo de caso](./projects/pt-br/zayuni.md)** · **[Produto](https://app.zayuni.com)**

### 2 · A infraestrutura de IA por trás dele

#### Zayuni DevWS: meu próprio servidor MCP para agentes de IA
*Onde os agentes trabalham.* Em uso diário desde novembro de 2026, inclusive pelo ChatGPT no celular. Sete serviços Docker: OAuth com MFA e checagem JWT que falha fechada, um workspace sem credenciais, um gateway Git que guarda o token e recusa push na `main`, um proxy de saída e um log de auditoria encadeado por HMAC, ancorado num bucket travado contra alteração.
<br>`MCP` `Python` `Node.js` `OAuth/JWT` `Docker Compose` `Cloudflare` · **81 testes do gateway · branch → push → PR pelo celular, PC desligado**
<br>**[Estudo de caso](./projects/pt-br/mcp.md)**

### 3 · A mesma disciplina, para um cliente

#### Federação Sergipana de Surf: plataforma de atletas e competições (em desenvolvimento)
Site público e plataforma do atleta para uma federação esportiva estadual, em desenvolvimento no ambiente de homologação: cadastro, filiações, inscrições em etapas, pagamentos por Pix e cartão com webhooks, ranking importado do LiveHeats e área administrativa.
<br>`Next.js 16` `React 19` `TypeScript` `Supabase` `Mercado Pago` `Google Cloud Run` · **49 testes · 21 migrações SQL · lint e typecheck na CI**
<br>**[Estudo de caso](./projects/pt-br/fss.md)**

### Laboratório

#### DevCore: protótipo de motor para tarefas de código com IA
Um experimento de outubro de 2026: o modelo só propõe ações por ferramentas permitidas, um roteador escolhe a rota mais barata capaz de resolver (sem modelo, modelo local, modelo mais forte ou humano), e as verificações rodam num executor isolado antes de abrir um pull request. Não faz parte do fluxo de produção.
<br>`Python` `Roteamento de LLMs` `Inferência local compatível com Ollama` `Docker` · **141 testes automatizados**
<br>**[Notas](./projects/pt-br/devcore.md)**

## Tecnologias

| Área | Tecnologias |
| --- | --- |
| **Linguagens** | TypeScript, Python, JavaScript, SQL |
| **Front-end** | React 19, Next.js (App Router), Expo / React Native Web, PWA, interfaces responsivas |
| **Back-end e dados** | Python (FastAPI), Node.js, Supabase (PostgreSQL, Auth, row-level security, migrações SQL), APIs REST, webhooks, Pix (BR Code, Mercado Pago), Google Calendar e CalDAV |
| **Engenharia de IA** | Servidores Model Context Protocol (MCP), desenvolvimento com agentes de código (Claude, ChatGPT), segurança de agentes: isolamento de credenciais, ferramentas delimitadas, auditoria · *laboratório:* roteamento de modelos e LLMs locais |
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

**[Fale comigo no LinkedIn](https://www.linkedin.com/in/wesley-isaias)** · **E-mail:** [wesley_isaias@hotmail.com](mailto:wesley_isaias@hotmail.com) · **[Leia a história](https://wesley-isaias.github.io/wesley-isaias/)**
