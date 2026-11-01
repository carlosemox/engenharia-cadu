# Mapa da Engenharia Cadu

Uma fonte por assunto. A biblioteca orienta; o ambiente e os testes demonstram o funcionamento. Os nomes P00–P30 permanecem estáveis.

| Preciso de… | Fonte oficial | Página visual |
|---|---|---|
| Começar do zero | [P01](p/P01.md) e [comando de continuidade](continuar.md) | [Começar no P01](https://carlosemox.github.io/engenharia-cadu/prompts/P01/) |
| Avançar entre prompts | [Continuidade](politicas/CONTINUIDADE.md) e [rotas](orquestracao/rotas.json) | [Fluxo contínuo](https://carlosemox.github.io/engenharia-cadu/guia/continuidade/) |
| Conferir segurança | [Política](politicas/SEGURANCA_ENGENHARIA.md) e [registro de revisão](templates/REVISAO_SEGURANCA.md) | [Segurança e revisão](https://carlosemox.github.io/engenharia-cadu/guia/seguranca/) |
| Proteger arquivos | [Backup](politicas/BACKUP_DRIVE.md) e [recibo](templates/RECIBO_BACKUP.md) | [Backup por projeto](https://carlosemox.github.io/engenharia-cadu/guia/backup/) |
| Saber o que está realmente ativo | [Estado operacional](OPERACAO.md) | [Implantação e limites](https://carlosemox.github.io/engenharia-cadu/guia/operacao/) |
| Organizar projeto existente | [Guia de adoção](https://github.com/carlosemox/engenharia-cadu-adocao/blob/main/GUIA_DE_USO.md) | [Central de adoção](https://carlosemox.github.io/engenharia-cadu-adocao/) |
| Selecionar agentes e skills | [Catálogo](catalogo/README.md), [papéis](agentes/README.md) e [P08](p/P08.md) | [Capacidades](https://carlosemox.github.io/engenharia-cadu/#capacidades) |
| Preparar uma missão prolongada | [P17](p/P17.md), [P18](p/P18.md), [contrato](templates/CONTRATO_MISSAO.md) | [P17](https://carlosemox.github.io/engenharia-cadu/prompts/P17/) |

## Separação dos repositórios
- `engenharia-cadu`: método, comandos, templates, catálogo publicável e site.
- `engenharia-cadu-adocao`: entendimento, retrato e adaptação de aplicativos existentes, preservando trabalho.
- `engenharia-cadu-ops`: perfis e evidências operacionais privadas; não é cofre de senhas.
- Cada aplicativo: seu código, requisitos, dados de configuração não secretos, testes e runbooks.

Relatórios reais, IDs de pastas de backup e recibos detalhados ficam no perfil privado. O site não navega pelo Drive e não executa prompts. Iniciar uma tarefa não autoriza migração, produção ou contratação por implicação.

## Auditoria incremental S01

- [Módulo e marcos](modulos/seguranca/README.md): início, meio, fim e verificação por lote.
- [Comando de entrada](modulos/seguranca/read.md) e [prompt universal integral](modulos/seguranca/PROMPT_UNIVERSAL.md).
- [Hooks e contrato de implantação](modulos/seguranca/hooks/README.md): exemplos separados de controles instalados.
- [Página do módulo](https://carlosemox.github.io/engenharia-cadu/guia/auditoria/).

Atualização das políticas existentes permanece no mesmo arquivo; o módulo novo fica separado em `modulos/seguranca/`. Relatórios reais ficam privados, fora da central.

## Entradas V2.3

- [Comando único](comando.md) e [fábrica](fabrica/README.md).
- [Assumir projeto](comandos/ASSUMIR_PROJETO.md) e [reestruturar](comandos/REESTRUTURAR_PROJETO.md).
- [Memória](politicas/CONTEXTO_E_MEMORIA.md), [índice de contexto](templates/INDICE_CONTEXTO.md) e [case](avaliacoes/CASE_EFICIENCIA.md).
