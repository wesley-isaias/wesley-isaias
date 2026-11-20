# Deny-by-default tool authorization for AI agents

[← Back to profile](../../README.md) · [Português abaixo](#português)

A small, dependency-free example of the first rule behind [Zayuni DevWS](../../projects/mcp.md), my MCP server for AI agents: **before any tool runs, a policy decides, and the default answer is no.**

This is independent, educational code. It does not contain code, configuration or rules from the production MCP server.

## What it does

`authorize(action, path)` returns a `Decision(allowed, reason)`. It never touches the filesystem and never runs commands.

| Request | Decision | Reason |
| --- | --- | --- |
| `read_file /workspace/src/main.py` | allowed | `policy_allowed` |
| `run_tests /workspace/tests` | allowed | `policy_allowed` |
| `write_file /workspace/src` | denied | `action_not_allowed` |
| `read_file /etc/passwd` | denied | `outside_workspace` |
| `read_file /workspace/.env` | denied | `sensitive_or_traversal_path` |
| `read_file /workspace/../etc` | denied | `sensitive_or_traversal_path` |
| `run_tests /workspace/src` | denied | `tests_directory_only` |

## Run it

```bash
cd examples/agent-policy
python -m unittest discover -v
```

No dependencies, no credentials, no network. The same tests run in [GitHub Actions](../../.github/workflows/public-example-tests.yml) on every change.

## Limits

- **This is not a production security boundary.** Symlinks, path normalization, TOCTOU races and filesystem differences are out of scope here.
- A real system also needs identity-based authorization, OS-level isolation, checks on the resolved target, audit logging and adversarial tests. In Zayuni DevWS those live in separate services: an OAuth proxy, an isolated workspace, a Git gateway and an audit log.
- Executing a tool is a separate step that happens only after the policy decision.

---

## Português

Exemplo pequeno e sem dependências da primeira regra do [Zayuni DevWS](../../projects/pt-br/mcp.md), meu servidor MCP para agentes de IA: **antes de qualquer ferramenta executar, uma política decide, e a resposta padrão é não.**

É um código independente e educacional. Não contém código, configuração nem regras do servidor MCP de produção.

- `authorize(action, path)` devolve `Decision(allowed, reason)`, sem acessar arquivos nem executar comandos.
- Permite apenas leitura, listagem e testes dentro de `/workspace`. Escrita, caminhos sensíveis (`.env`, `.git`, `secrets`), saída do workspace e `..` são negados.
- Para rodar: `python -m unittest discover -v` dentro de `examples/agent-policy`.
- **Não é uma fronteira de segurança de produção.** Um sistema real precisa de autorização por identidade, isolamento no sistema operacional, validação do destino resolvido, auditoria e testes adversariais.
