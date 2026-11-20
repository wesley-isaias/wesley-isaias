# Federação Sergipana de Surf: plataforma web

[← Voltar ao perfil](../../README.pt-BR.md) · [🇺🇸 English](../fss.md)

| | |
| --- | --- |
| **Cliente** | Federação Sergipana de Surf |
| **Papel** | Desenvolvedor: aplicação web, integração com o back-end e releases |
| **Status** | Em desenvolvimento (repositório privado) |

## Contexto

Uma federação esportiva estadual precisava de presença digital e de ferramentas administrativas para operações que antes eram feitas manualmente.

## Escopo

- Site público e áreas autenticadas
- Fluxos administrativos para a equipe da federação
- Integração entre a aplicação web e o back-end
- Permissões por perfil de usuário

## Práticas de engenharia

- **Ambientes separados:** staging e produção são isolados, e as mudanças são validadas antes da liberação.
- **Controle de acesso:** permissões definidas por perfil, seguindo o princípio do privilégio mínimo.
- **Liberação gradual:** funcionalidades entram em produção por etapas, com revisão de configuração em cada uma.
- **Proteção de dados:** dados institucionais e de associados nunca aparecem em material público.
