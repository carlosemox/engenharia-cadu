# Começar no P01 e continuar entre etapas

Cole na conversa do Codex, não no shell:

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md

Quero iniciar um produto do zero em CONTINUO_SUPERVISIONADO.
Ao concluir e verificar cada etapa, leia e execute o próximo prompt
pertinente da mesma revisão, sem me pedir para copiar outro comando.
Preserve minhas decisões, permissões e limites; pare apenas para
informação/aprovação material, falha ou bloqueio real.
Inclua segurança durante o fluxo, revisão antes de release e backup
privado em Projetos 2026/Backup/<nome-do-projeto>.
Não publique, migre dados, aumente gastos ou inicie 24 horas
sem a autorização e a prontidão correspondentes.
```

O coordenador carrega [Continuidade](politicas/CONTINUIDADE.md), [Segurança](politicas/SEGURANCA_ENGENHARIA.md) e [Backup](politicas/BACKUP_DRIVE.md) uma vez por revisão e usa somente as seções pertinentes. Referências externas são instruções subordinadas ao pedido e às permissões efetivas.

## O percurso
P01 entrevista → P02 pesquisa quando necessária → P03 briefing/escopo → P04 PRD → P05 fluxos/design → P06 arquitetura → P07 ambiente → P08 capacidades/serviços → P09 bootstrap → P10 integrações → P11 preflight → P12 tarefas → P13 implementar → P14 revisar → P15 homologar → P16 preparar/publicar conforme alçada.

A sequência adapta dependências reais. Mais tarefas repetem o ciclo de implementação/revisão, não a entrevista. P17/P18 são supervisão e retomada; demais especializações somente quando aplicáveis. Antes de uma ação dependente, rever decisões que mudaram.

## O que é automático e o que exige decisão
O próximo procedimento é lido e conduzido na sessão ativa quando suas condições e alçada estão atendidas. Você continua respondendo à entrevista e decide escopo, arquitetura relevante e publicação. Uma decisão pode cobrir vários itens claramente apresentados; o agente não pergunta por cada arquivo.

Não há promessa de continuar com o computador desligado, sessão encerrada ou quota esgotada. Supervisor persistente e integração Drive do computador têm de ser configurados/testados separadamente. Instruções no GitHub não instalam CLIs ou conectores.

## Resultado de cada etapa
Entrega + teste/evidência + revisão pertinente + backup verificado dos novos artefatos + checkpoint + próxima etapa. Falha bloqueia a dependência; não vira aprovação automática. Referências a backup, gasto e aprovação no estado precisam de comprovação, não apenas campos preenchidos.

## Segurança final
Não existe garantia de segurança total contra invasões. O gate de release exige revisão e testes proporcionais, sem achados bloqueantes abertos, cobertura documentada, recuperação e GO. Depois do lançamento, manutenção e resposta a incidentes continuam necessárias.

[Índice](README.md) · [Retomada](p/P18.md) · [Missão prolongada](p/P17.md)
