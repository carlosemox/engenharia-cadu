# Aceite restrito do executor local

Versão 0.2.0 — 2026-11-10T14:16:31Z.
Resultado: `INSTALLED_ACTIVE_IDLE / SYNTHETIC_PASS / GENERAL_PROJECTS_NOT_QUALIFIED`.

## Implementação e execução

- Executor SHA-256: `cd72903efd433cc849a987d7cb04e3170c7c3a716ae8016465e6c8d4d8a8f9c5`.
- Instalador SHA-256: `fe14ceb65cf36a7137852281c12a7d853a9888692b9d6063e08fcd74c4db1d4f`.
- Mac arm64, 8 GiB, macOS 26.6.2; Ollama 0.40.15.
- Modelo local `qwen3:4b`, digest `359d7dd4bcdab3d86b87d73ac27966f4dbb9f5efdfcc75d34a8764a09474fae7`.
- O controlador confiável solicita JSON via loopback. Código gerado só executa sob Seatbelt.
- LaunchAgent: `com.engenharia-cadu.local-executor`. Processo observado após retomada: PID 76131.
- Heartbeat após retomada: IDLE; launchctl: running. Recibo concluído permaneceu byte a byte igual.
- Uma única fixture sintética admitida; nenhum projeto de produto cadastrado para execução.

## Resultados observados

| Verificação | Resultado | Evidência |
|---|---|---|
| Ollama real pelo serviço instalado | PASS restrito | Uma tentativa; soma positiva, negativa e zero; 5,65 s; REVIEW_REQUIRED |
| Preservação da fonte | PASS | Fonte mantém subtração; candidato contém soma |
| Leitura/escrita fora da área | PASS | EPERM em canário externo |
| Estado do supervisor e candidato | PASS | Escrita negada; estado inacessível ao teste |
| Symlink de escape e Applications | PASS | Leitura EPERM |
| Rede do teste | PASS | Conexão loopback EPERM |
| Spawn destacado | PASS | Node spawnSync detached recebe EPERM |
| STOP e revogação durante teste | PASS | Cliente interrompido; ausência de escrita tardia |
| Crash do supervisor | PASS | Watchdog encerra teste; processo ausente; sem escrita tardia |
| Recuperação | PASS | RUNNING vira INTERRUPTED; sem replay |
| Supervisor duplicado | PASS | Lock rejeita segunda instância |
| STOP do serviço instalado | PASS | Heartbeat STOPPED; exit 0; sem reinício automático |
| Retomada explícita | PASS | Novo PID, IDLE; recibo inalterado |
| Testes de contrato/repositório | PASS | 212 testes; inclui rejeição de projeto antes de leitura |
| Revisão independente | PASS restrito | Código, instalador e evidências do piloto revisados por agente distinto |
| Projetos reais, design system, MCPs e builds gerais | NOT_RUN | Não admitidos nem homologados por este piloto |
| Disponibilidade contínua 24 h | NOT_RUN | Janela observada curta; nenhuma inferência em repouso |

A revisão independente observou STOPPED durante o teste operacional de parada;
a retomada posterior foi conferida pelo operador e registrada em
`state/service-control-test.json`. Isso não é falha nem execução ininterrupta.

## Organização e integridade

Arquivos privados sob `~/Library/Application Support/Engenharia-Cadu-Agent`:
`installation.json`, `state/receipts/installation-pilot.json`, candidato e logs em
`state/runs/installation-pilot`, testes em `evidence/acceptance-2026-11-10`.
A política `state/model.json` admite somente projeto/raiz sintéticos. Autorizações
são locais, privadas e expiram; não existe autenticação multiusuário nesta versão.

JARVIS não foi integrado nem alterado. O workspace anterior continua referência;
a fila operacional deste modo independente é exclusivamente a instalação acima.
A configuração não dá ferramentas ao modelo nem altera os critérios de release.
A Engenharia-Cadu supervisiona por política e controlador; não se torna um LLM.

## Diagnóstico anterior e incidente preservado

A tentativa anterior pelo Codex CLI local não qualificou o modelo pequeno: houve
timeout e ausência de edição. O novo adaptador não depende dessa integração.
Ao avaliar Docker anteriormente, sua abertura iniciou containers preexistentes.
O Docker foi parado para restaurar a indisponibilidade anterior; nenhum comando
foi executado dentro desses containers. Efeitos internos da inicialização não
foram auditados. O executor instalado não usa Docker. O incidente e os ensaios
anteriores permanecem nos recibos privados da preparação; não foram apagados.

## Limites e próxima promoção

O serviço ativo está ocioso após o piloto, não desenvolvendo produtos. Nenhum
merge, deploy ou liberação irrestrita foi realizado. Uma tarefa real exige admissão
específica, testes compatíveis, revisão independente e validação do projeto.
Sem fork, muitos builds frontend não funcionam neste sandbox; não reduzir isolamento
para fazê-los passar. Memória/threads/espaço agregado não têm quota forte. Tests
confiáveis devem ser independentes do conteúdo editável; resultado verde não substitui
revisão. STOP não comprova cancelamento imediato dentro de Ollama. As verificações
de digest não impedem alteração transitória da tag por outro ator do host.

[Operação PT](LOCAL_EXECUTOR_OPERATION.md) · [EN](LOCAL_EXECUTOR_OPERATION.en.md) · [ES](LOCAL_EXECUTOR_OPERATION.es.md).
