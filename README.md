<p align="center"><img src="docs/assets/banner.svg" alt="Engenharia Cadu — Da intenção ao software. Com engenharia." width="100%"></p>

<p align="center"><b>Codex principal · Astra econômico · design no briefing · integrações planejadas</b></p>
<p align="center"><a href="https://carlosemox.github.io/engenharia-cadu/"><b>Abrir a central visual</b></a> · <a href="read.md">Comece aqui</a> · <a href="#biblioteca-de-prompts">29 prompts</a> · <a href="catalogo/README.md">Agentes e skills</a></p>

# Engenharia Cadu

Uma metodologia para criar, recuperar e evoluir software com decisões claras, colaboração seletiva e evidências antes da conclusão. Documentação pública; operação específica e credenciais ficam fora deste repositório.

## Atalho principal
Cole na **conversa do agente**, não no shell:

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/read.md e siga a trilha do meu pedido. O alvo é meu projeto, não esta central.
```

| Quero… | Começar em | Atalho |
|---|---|---|
| Criar um produto | [P01](p/P01.md) | `Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md` |
| Recuperar um projeto travado | [P20](p/P20.md) | `Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P20.md` |
| Retomar uma execução | [P18](p/P18.md) | `Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P18.md` |
| Selecionar serviços e APIs | [P08](p/P08.md) | `Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P08.md` |
| Organizar agentes e skills | [P22](p/P22.md) | `Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P22.md` |

`Read` é uma instrução natural. O agente precisa de acesso ao conteúdo e ao projeto. Registre o SHA consultado para missões reproduzíveis. Não carregue a biblioteca inteira a cada tarefa.

## O fluxo
**Ideia → entrevista → briefing com design → PRD → fluxos, arquitetura e dados → seleção de capacidades → bootstrap → preflight → implementação → testes e revisão → staging → release autorizado → operação.**

### Biblioteca de prompts

| ID | Etapa | Quando usar |
|---|---|---|
| [P00](p/P00.md) | Escolher a trilha e a próxima ação | Quando chega uma ideia, um pedido de continuação, uma falha ou um acervo para avaliar. |
| [P01](p/P01.md) | Entrevista de produto, histórico e direção de design | Quando a ideia ainda precisa virar um briefing utilizável. |
| [P02](p/P02.md) | Pesquisa, evidências e viabilidade | Quando hipóteses, serviços ou alternativas ainda podem mudar a decisão de construir. |
| [P03](p/P03.md) | Briefing final, primeira versão e fronteiras | Quando a descoberta deve se transformar em compromisso de produto e limites da versão. |
| [P04](p/P04.md) | PRD com regras e critérios de aceite | Quando o escopo confirmado precisa ser transformado em requisitos implementáveis. |
| [P05](p/P05.md) | Fluxos, experiência e design system | Quando a direção D0 precisa virar experiência especificada e critérios para implementação. |
| [P06](p/P06.md) | TRD, dados, segurança e arquitetura | Quando o produto e as dependências precisam virar uma solução técnica proporcional. |
| [P07](p/P07.md) | Inventariar e preparar a máquina, contas e clientes | Antes de configurar um projeto; repetir apenas quando o ambiente mudar ou houver evidência de problema. |
| [P08](p/P08.md) | Selecionar agentes, ferramentas, serviços e APIs | Antes de fechar decisões dependentes de fornecedor e antes de instalar capacidades. |
| [P09](p/P09.md) | Preparar repositório e base do projeto novo | Após definir o próximo incremento e sua arquitetura; projeto existente segue P20/P21. |
| [P10](p/P10.md) | Preparar ambientes, CI e integrações aprovadas | Quando as decisões técnicas e de serviços precisam virar configurações verificáveis. |
| [P11](p/P11.md) | Comprovar prontidão antes da execução | Antes de iniciar desenvolvimento, CI, staging, missão prolongada ou release. |
| [P12](p/P12.md) | Transformar especificações em tarefas executáveis | Quando a versão está especificada e precisamos organizar execução sem decisões implícitas. |
| [P13](p/P13.md) | Implementar uma tarefa com verificação | Quando há uma tarefa delimitada, entradas suficientes e autorização de implementação. |
| [P14](p/P14.md) | SENTINEL — revisão independente por risco e evidência | Após uma implementação, antes da integração de mudanças que exigem revisão. |
| [P15](p/P15.md) | Staging, jornada real e homologação | Quando um incremento revisado precisa ser verificado no ambiente representativo de homologação. |
| [P16](p/P16.md) | Release, migração e operação inicial | Quando há candidato homologado e necessidade de preparar ou executar publicação. |
| [P17](p/P17.md) | Executar missão prolongada com limites e recuperação | Somente depois de comprovar supervisor e prontidão para execução não assistida. |
| [P18](p/P18.md) | Retomar trabalho sem duplicação ou perda | Após erro de sessão, reinício do host, falha de worker ou interrupção do controlador. |
| [P19](p/P19.md) | Priorizar projetos em andamento ou parados | Quando há vários projetos e é necessário escolher uma recuperação ou entrega-piloto. |
| [P20](p/P20.md) | Diagnosticar projeto travado sem reescrever | Quando já há código e o funcionamento ou desenvolvimento não avança. |
| [P21](p/P21.md) | Corrigir e adotar o padrão incrementalmente | Após um diagnóstico ou plano de recuperação aprovado para o projeto existente. |
| [P22](p/P22.md) | Auditar agentes, skills e pacotes | Antes de instalar um acervo ou ativar capacidades de terceiros. |
| [P23](p/P23.md) | Transformar capacidade em módulo reutilizável | Quando uma função pode atender mais de um produto sem copiar a aplicação inteira. |
| [P24](p/P24.md) | Medir e melhorar o harness sem enfraquecer controles | Após mudança material de instruções/ferramentas ou diante de falha recorrente comprovada. |
| [P25](p/P25.md) | Projetar e construir módulo financeiro auditável | Quando o produto precisa de capacidade financeira, conciliação ou análise gerencial. |
| [P26](p/P26.md) | Conteúdo, Instagram e publicação com controle | Quando a capacidade de criação de conteúdo precisa virar um processo rastreável por marca. |
| [P27](p/P27.md) | Vídeo programático como capacidade reutilizável | Quando o produto precisa gerar, editar ou renderizar vídeos a partir de contratos repetíveis. |
| [P28](p/P28.md) | Engenharia, quantitativos e gestão de obras | Quando um produto precisa de capacidades de orçamento, planejamento, compras ou acompanhamento de obras. |

## Explorar a engenharia

| Seção | O que você encontra |
|---|---|
| [Método](METODO.md) | Filosofia e fluxo do início à operação. |
| [Papéis](agentes/README.md) | 10 responsabilidades documentadas, não uma equipe instalada. |
| [Skills e catálogos](catalogo/README.md) | 120 identificadores de referência, 57 papéis operacionais e matriz Matheus. |
| [Política de economia](politicas/ECONOMIA_ASTRA.md) | Contexto, esforço, delegação e medição sem promessas fictícias. |
| [Contrato comum](politicas/CONTRATO_COMUM.md) | Escopo, autoridade, preservação e evidências. |
| [Templates](templates/README.md) | Briefing, PRD, design, arquitetura, missão, tarefa e APIs. |
| [Integração dos clientes](integracoes/CLIENTES.md) | Codex, Antigravity, Gemini e OpenCode; especificação, não instalação. |
| [Avaliações](avaliacoes/CENARIOS.md) | Casos a homologar em clientes/projetos. |
| [Licenciamento](LICENCIAMENTO.md) | Direitos, atribuição e restrições de terceiros. |

## O que esta publicação não afirma
Não instala CLIs, conecta contas, implementa supervisor de 24 horas ou certifica os prompts. `NOT_RUN` continua sendo teste não executado. Menos texto não comprova redução proporcional da fatura. Publicação documental não autoriza publicar seus aplicativos.

## Referências e atribuição
Inspirado no [Vibe Coding Toolkit de Matheus Gomes](https://github.com/soumatheusgomes/vibe-coding-toolkit), revisão `790a895304e0c08b70a5b215c9d334f1c86b816c`. Aviso MIT preservado. [Mapa de adaptação](fontes/MATRIZ_MATHEUS_CADU.md). Sem afiliação ou endosso presumido.

## Manutenção
`p/` e documentos são canônicos. Site e downloads são derivados. Leia [guia do site](site-src/README.md). Atualizações do método não alteram projetos em execução automaticamente.
