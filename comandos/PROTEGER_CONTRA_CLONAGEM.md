# Comando — Proteger projeto contra exposição e clonagem

Leia:
https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/read.md

Leia também:
https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P29.md
https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P22.md
https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P14.md

Audite este projeto contra exposição de código, segredos, regras comerciais, modelos, prompts, integrações, sourcemaps e clonagem de artefatos.

Não instale globalmente ferramentas, MCPs, skills ou hooks. Não altere produção. Não trate uma ferramenta de hardening como garantia de invulnerabilidade.

Reconstrua o estado real e classifique cada achado como confirmado, provável, não verificado ou falso positivo. Verifique frontend, backend, banco, build, CI/CD, variáveis públicas, dependências, endpoints, autorização, rate limiting, logs, sourcemaps e artefatos publicados.

Mantenha lógica crítica, segredos, autorização e cálculos estratégicos no servidor. Avalie BLA somente como piloto reversível para artefatos próprios, com versão fixada, backup, cópia separada, verificação funcional, teste de desempenho e rollback.

Entregue:
- inventário de exposição;
- matriz de risco;
- correções por prioridade;
- arquivos que podem ser alterados;
- testes antes e depois;
- evidências;
- riscos residuais;
- decisão de release;
- checkpoint e próximo passo.

Resultado sem evidência deve ser marcado como NOT_VERIFIED.
