# Fontes e origem do módulo S01

Origem normativa: Universal Security Audit and Remediation Prompt fornecido pelo usuário nesta conversa. O texto integral está em [PROMPT_UNIVERSAL.md](PROMPT_UNIVERSAL.md). Não se atribui autoria desse texto à OWASP, NIST ou a fornecedor de IA. Os complementos Cadu são roteiro, eventos, verificador de recibos, exemplos e templates.

Consulta pública de documentação em 30/10/2026 (somente identificadores públicos):

| Fonte | Uso nesta integração | Limite |
|---|---|---|
| [Git — githooks](https://git-scm.com/docs/githooks) | Eventos Git reais, diretório de execução, parâmetros e possibilidade de bypass | Eventos module-complete e phase-exit são lógicos nossos, não hooks nativos do Git |
| [GitHub — protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | Checks e revisões exigidos no servidor e atenção aos bypasses | Nenhuma proteção de branch foi instalada nesta entrega |
| [OWASP ASVS](https://asvs.owasp.org/) | Requisitos para aplicações web, quando pertinentes; página consultada apresenta 5.0.0 como estável | Não declarar cobertura integral ou certificação por um checklist |
| [NIST SSDF](https://csrc.nist.gov/projects/ssdf) | Segurança integrada ao ciclo de desenvolvimento e resposta a vulnerabilidades | Não auditamos conformidade de aplicativos; revalidar final estável na execução |

O prompt universal contém outros pontos de partida, incluindo WSTG, API Security, FIRST CVSS, CISA KEV, Dependabot e Renovate. Não se afirma que todos foram auditados nesta integração. Versions, flags, CVEs e políticas de suporte precisam de consulta na data e stack do projeto. Nada aqui prova suporte universal de uma ferramenta ou compatibilidade de um hook com todos os clientes.

Não foram consultados dados privados de aplicativos, scanners externos, serviços produtivos ou credenciais para criar o módulo.
