# Exemplo público — autorização de ferramentas para agentes

Este exemplo é **independente e educacional**. Não contém código, configuração nem regras internas do Zayuni Dev Workspace MCP.

## Problema
Um agente pode solicitar ações fora do escopo. Antes de qualquer ferramenta executar, a aplicação deve aplicar políticas de autorização com **negação por padrão**.

## Demonstração
O módulo `agent_policy.py` recebe uma ação e um caminho e retorna uma decisão. Ele **não acessa arquivos, não executa comandos e não fornece sandbox**.

A política de exemplo permite somente leitura, listagem e uma ação simbólica de testes, com restrições de diretório. Escrita, deploy e exclusão são negados.

```bash
cd examples/agent-policy
python -m unittest discover -v
```

## Limitações importantes
- **Não é uma fronteira de segurança de produção.** Há riscos de symlinks, normalização, TOCTOU e diferenças de filesystem.
- Um sistema real exige autorização por identidade, isolamento no sistema operacional, validação do destino resolvido, logging e testes adversariais.
- A execução de ferramentas precisa de um mecanismo separado, após a decisão de política.

## Evidência verificável
Os testes unitários e o workflow de CI deste repositório executam o exemplo público sem credenciais e sem serviços externos.

[← Portfólio](../../README.md)
