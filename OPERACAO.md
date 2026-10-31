# Estado operacional e implantação

**Esta página é um registro documental de escopo, não um painel conectado aos seus computadores.** Atualização editorial: 30/10/2026. Conferir evidências do projeto antes de qualquer operação.

## O que está disponível e o que ainda precisa de implantação

| Capacidade | Situação desta entrega | O que permite afirmar funcionamento |
|---|---|---|
| Biblioteca P00–P28 | Documentos publicados | Leitura da mesma revisão pelo executor |
| Continuidade começando no P01 | Procedimento documentado | Pilotar transições na sessão real, com entradas, aceite e alçadas |
| Revisão de segurança | Política e template publicados | Avaliação do candidato e ambiente específicos; testes dos aplicativos: NOT_RUN nesta entrega |
| Backup no Drive por projeto | Política publicada; cópias históricas não equivalem ao estado atual | Captura completa do escopo, envio, conferência de integridade e recibo |
| Backup automático no host do Codex | NÃO IMPLANTADO por esta publicação | Autenticação de acesso restrito, upload/download, destino privado e restauração testados no host |
| Supervisor de 24 horas | NÃO IMPLANTADO por esta publicação | Runtime real, exclusividade, limites, retomada, parada e missão autorizada |
| Agentes e skills | Catálogo para seleção | Procedência, licença, descoberta pelo cliente e piloto funcional |

A situação de um aplicativo real pode ser diferente. O agente deve inspecioná-lo e registrar a evidência, não presumir que os estados desta biblioteca sejam os do produto.

## Começar sem perder os limites

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md
Inicie meu produto em CONTINUO_SUPERVISIONADO. Avance para a próxima etapa autorizada após verificar entrega, segurança, backup pertinente e checkpoint. Mantenha decisões materiais comigo.
```

A sessão ativa conduz as etapas, mas não continua por conta própria após encerramento, suspensão do computador ou esgotamento de quota. Instruções e templates não concedem credenciais nem ativam um serviço persistente.

## Checklist de implantação por projeto

1. Identificar o projeto, sua revisão, escopo, orçamento e autorizações.
2. Preparar o cliente real e conferir comandos, testes e ambiente, sem presumir que conexões desta conversa existem no terminal.
3. Configurar a pasta privada `Projetos 2026/Backup/<nome-do-projeto>`; registrar IDs somente no perfil privado.
4. Capturar os arquivos e classes de dados realmente incluídos; declarar exclusões, segredos protegidos e pendências.
5. Testar envio, download e restauração em destino isolado; registrar o recibo, não apenas o nome da pasta.
6. Executar um incremento pequeno e conferir transição, revisão, falha, retomada e limites.
7. Só ampliar autonomia após comprovar o supervisor, as proteções e a missão específica. Produção mantém aprovação própria.

## Revisão e proteção

Segurança é verificada durante o processo e novamente antes de release. Não se promete proteção total contra invasões. Falhas bloqueantes, credenciais expostas ou testes indispensáveis ausentes impedem o avanço dependente. Evidência de outra revisão não aprova automaticamente o candidato novo.

Cópias históricas já realizadas são registradas privadamente. Elas não demonstram backup atualizado de todo o portfólio, histórico Git completo, arquivos locais ou bancos. Não foi ativada exclusão automática de gerações antigas.

[Continuidade](politicas/CONTINUIDADE.md) · [Segurança](politicas/SEGURANCA_ENGENHARIA.md) · [Backup](politicas/BACKUP_DRIVE.md) · [Mapa](MAPA_DA_CENTRAL.md)

## Auditoria S01 e hooks

[Módulo S01](modulos/seguranca/README.md) acrescenta início, marcos intermediários e revisão final, além de eventos durante a execução. Procedimentos, templates e verificador de recibos são uma entrega da biblioteca. **Hooks/scanners/CI dos aplicativos: NÃO IMPLANTADOS por esta publicação.** Auditorias de aplicativos: NOT_RUN. A campanha de projeto deve ligar os checks e produtores de evidência reais ao mecanismo de controle e comprovar bloqueios; os exemplos não fazem isso sozinhos.

## Estado V2.3

Fábrica determinística e comandos de assumir/reestruturar são capacidades desta central. Não configuram agentes no computador do usuário, não auditam automaticamente aplicativos e não instalam candidatos de terceiros. O índice de contexto e o checkpoint devem ser adotados em cada projeto autorizado. O case possui protocolo, sem resultados operacionais declarados.
