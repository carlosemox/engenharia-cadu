# D01 — Fontes verificadas

Verificação documental realizada em 04/11/2026 (horário de São Paulo) sobre a revisão upstream `9197d919034d19010ae303cf96bf19ad087dd4be`.

| Fonte | Fato utilizado |
|---|---|
| [vercel-labs/skills README](https://github.com/vercel-labs/skills/blob/9197d919034d19010ae303cf96bf19ad087dd4be/README.md) | CLI `npx skills`, Node.js 22.20+, `find`, `list`, `use`, `check`, `update`, `remove`, `init`, escopo de projeto/global e agentes suportados. |
| [find-skills SKILL.md](https://github.com/vercel-labs/skills/blob/9197d919034d19010ae303cf96bf19ad087dd4be/skills/find-skills/SKILL.md) | Descoberta por necessidade, consulta ao leaderboard/diretório, pesquisa por palavra-chave e recomendação de verificar qualidade antes de recomendar. |
| [commands.md](https://github.com/vercel-labs/skills/blob/9197d919034d19010ae303cf96bf19ad087dd4be/docs/commands.md) | Sintaxe de `add`, `--skill`, `-a`, `-g`, `use`, `find`, `check` e `update`. |
| [skills.sh](https://skills.sh/) | Diretório público indicado pelo projeto upstream. |

## Leitura crítica

O material upstream usa installs, reputação da fonte e estrelas como sinais de qualidade. A Engenharia Cadu **não transforma esses sinais em aprovação automática**: P22 continua exigindo leitura da skill específica, licença, permissões, scripts, dados, rede, hooks, telemetria, conflitos e piloto proporcional ao risco.

A sintaxe do comando da imagem foi validada documentalmente. Instalação, busca CLI, piloto e atualização: **NOT_RUN nesta integração**.
