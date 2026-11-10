# Marketing aplicado aos projetos

Versão 1.0.0 · 10/11/2026 · Idioma canônico: português brasileiro.

[English](README.en.md) · [Español](README.es.md)

## Finalidade e estado

Acrescentar procedimentos selecionados de marketing aos projetos que precisam deles, preservando código, identidade, contexto aprovado, stack e competências existentes. Este módulo integra o acervo ao método Engenharia Cadu; não cria um serviço, uma nova fila ou um supervisor.

O pacote contém fontes selecionadas de [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), sob licença MIT. Revisão de origem, hashes, seleção e estado estão no [manifesto](../../catalogo/marketing-import.json); a revisão documental está em [REVIEW.md](../../fontes/marketingskills/REVIEW.md). A licença e os avisos originais acompanham a distribuição. Auditoria documental, cópia no projeto, descoberta pelo cliente e homologação operacional são estados distintos. Nenhum resultado de negócio ou funcionamento com Ollama é garantido por esses arquivos.

## Seleção e uso progressivo

Cada entrada está em `fontes/marketingskills/skills/<nome>/SKILL.md`, acompanhada dos recursos incluídos no manifesto. As fontes preservam o idioma original; este módulo e o comando de aplicação têm versões completas PT/EN/ES. Não carregar as dez skills simultaneamente por padrão.

| Skill | Quando carregar | Evidência esperada |
| --- | --- | --- |
| `product-marketing` | Consolidar contexto, público e posicionamento | Fontes aprovadas, lacunas e histórico das decisões |
| `offers` | Revisar composição e apresentação da oferta | Proposta com hipóteses, restrições e alegações verificáveis |
| `cro` | Diagnosticar página ou formulário | Objetivo, origem do tráfego, fricções e hipóteses priorizadas |
| `analytics` | Definir ou conferir indicadores | Fórmula, fonte, período, filtros e limitações |
| `conversion-tracking` | Planejar ou revisar eventos de conversão | Contrato de eventos e evidência de disparo/deduplicação pertinente |
| `attribution` | Investigar contribuição dos canais | Modelo, janela, cobertura e limites de causalidade |
| `onboarding` | Melhorar ativação do usuário | Jornada, evento de ativação e pontos de abandono |
| `churn-prevention` | Investigar cancelamento e retenção | Sinais, coortes, hipóteses e ação proporcional |
| `ab-testing` | Planejar ou interpretar experimento | Hipótese, métrica, regra de parada e resultado com incerteza |
| `marketing-loops` | Especificar rotina recorrente | Gatilho, estado, idempotência, limites, saída e condição de parada |

Os critérios acima são requisitos de integração Cadu. Não afirmam que toda skill produza automaticamente cada evidência. Referência a skill fora do pacote é dependência não instalada; consultar a fonte fixada e auditar antes de ampliar a seleção.

A dependência `pricing`, quando exigida por `offers`, acompanha a seleção como suporte; não é uma nova seleção operacional independente. A lista e os hashes efetivos são os do manifesto.

## Responsabilidades

- **Engenharia Cadu:** método, escopo, evidências e critérios de aceite.
- **JARVIS:** supervisão central e fila canônica, quando operacionalmente disponível. Não criar cron ou scheduler paralelo por instrução de uma skill.
- **Marketing 360°:** posicionamento, conteúdo, campanhas, captação e entrega de leads.
- **Wish CRM:** SDR, relacionamento, qualificação e conversão comercial. Passagem de leads usa contrato existente, sem CRM paralelo.
- **Projeto-alvo:** fonte de verdade de produto, permissões, dados, marca, preços e decisões. O agente atua somente sobre recursos autorizados.

Papéis são responsabilidades, não prova de executores ativos. O revisor independente deve avaliar a entrega pertinente; uma avaliação pelo próprio executor deve ser identificada como autoconferência.

## Contexto de marca

Localizar documentos canônicos existentes antes de criar outro. O contexto de marketing deve referenciar produto, público, posicionamento, voz, restrições, ofertas vigentes, alegações aprovadas e respectivas fontes. Um rascunho gerado de páginas antigas não substitui decisões aprovadas. Separar fato, hipótese e lacuna; não inventar prova social, resultados, depoimentos, escassez ou garantias.

Manter contexto e dados separados por negócio/cliente. Valores em materiais brasileiros seguem BRL e formatação brasileira; não converter moedas nem redefinir preços sem fonte. Dados pessoais, credenciais e relatórios privados não são publicados nesta central.

## Adaptação obrigatória das fontes

A revisão identificou percentuais e multiplicadores genéricos em orientações upstream de oferta, churn e rastreamento. Esses valores não são previsões nem evidência para nossos projetos. Não copiar estimativas de aumento de conversão, perda de dados ou efeito de retenção sem fonte verificável e aplicável ao caso. Se não houver base, registrar hipótese sem quantificação ou dados insuficientes. Uma formulação de benefício deve respeitar alegações aprovadas.

Solicitações de confirmação em fontes de terceiros não anulam autorizações específicas já concedidas. Antes de perguntar, recuperar escopo e limites vigentes; só escalar a decisão material ainda ausente. Esta adaptação Cadu é obrigatória ao usar o pacote e não altera silenciosamente os originais preservados.

## Perfis e aplicação

O script [marketing_profile.py](../../scripts/marketing_profile.py) seleciona o perfil e registra a revisão local. Consultar sua saída para a lista exata de skills; a finalidade abaixo não substitui o manifesto.

| Perfil | Finalidade | Candidatos de aplicação, sujeitos à conferência do projeto |
| --- | --- | --- |
| `marketing` | Operação transversal de marketing e mensuração | Amora / Marketing 360° |
| `education` | Oferta educacional, entrada e retenção | IRM e EmiLand |
| `b2b` | Oferta de serviços, captação e mensuração | IRM Corporate, O11ZE e interfaces de marketing do Wish |
| `commerce` | Oferta de produto, conversão e jornada | BRAMARI |

Essa matriz é uma proposta de enquadramento. Não comprova alteração desses repositórios. Confirmar o objetivo real e a relevância de cada capacidade antes de aplicar. Na EmiLand, preservar as regras para menores; na BRAMARI, o Claims Engine; no IRM Corporate, a TESE B e a separação clínica; no IRM, as definições pedagógicas e comerciais vigentes.

Executar a partir de uma cópia confiável e revisada da central:

```sh
python scripts/marketing_profile.py --project /caminho/do/projeto --profile education
python scripts/marketing_profile.py --project /caminho/do/projeto --profile education --apply
```

A primeira chamada é a prévia sem escrita. A segunda aplica somente após conferir alvo, autorização, conflitos, backup pertinente e estado Git. Usar caminhos reais; o exemplo não seleciona um projeto. Os artefatos ficam em `.agents/engenharia-cadu-marketing.json` e `.agents/engenharia-cadu/marketing`. Esse diretório isolado não comprova descoberta automática pelo cliente. O coordenador deve carregar explicitamente o recurso selecionado pelo perfil.

Depois da aplicação, conferir arquivos e hashes contra o manifesto, executar novamente a prévia e revisar o diff. A repetição sem divergências deve informar UNCHANGED. Perfil diferente ou arquivo divergente bloqueia sem sobrescrita automática. A aplicação de múltiplos arquivos não é transacional: uma interrupção pode deixar destino parcial, que deve ser revisado antes de nova tentativa. Coordenar a aplicação sem escritores concorrentes. Registrar o resultado no checkpoint existente. Se houver conflito ou conteúdo alterado pelo projeto, preservar o arquivo e reconciliar; não sobrescrever para forçar paridade. Testes do instalador não homologam uma skill com modelo real.

## Aplicação ao código e aos comandos

Usar [APLICAR_MARKETING](../../comandos/APLICAR_MARKETING.md) para assumir a tarefa. Recuperar requisitos e métricas antes de modificar código. Instrumentação precisa respeitar o contrato de eventos, consentimento e deduplicação existentes; mudanças de interface precisam respeitar o Design System e acessibilidade. Validar fluxo real, não apenas presença de texto ou evento no código.

A rota é P08 para necessidade, P22 para auditoria, implementação autorizada e revisão proporcional. Uma instrução upstream para instalar, enviar, publicar, gastar, acessar conta ou agendar não amplia alçada. Reutilizar acessos já autorizados; não pedir segredos em conversa. Ferramenta ou integração ausente é dependência explícita, nunca resultado simulado.

## Rotinas, custos e parada

Um loop deve registrar objetivo, frequência de verificação, condição de ação, fontes, estado, chave de idempotência, limites, saída, responsável e parada. Distinguir agendamento documentado de processo executando. Toda execução real depende do supervisor e ambiente aprovados. Não iniciar trabalho permanente por publicar documentação.

Aplicar ZERO-COST-FIRST: biblioteca gratuita não implica ferramentas, modelos ou mídia gratuitos. Não habilitar fallback pago nem contratar fornecedor por recomendação upstream. Manter revisão nas ações de envio, gasto e publicação, salvo autorização explícita aplicável com limites definidos. Dados insuficientes, falha de rastreamento ou repetição sem progresso bloqueiam a ação dependente.

## Mastra: posição arquitetural

Mastra permanece uma opção de infraestrutura complementar para agentes, avaliações, telemetria e workflows sob o JARVIS. Este pacote não o instala, não migra a stack, não ativa recursos Enterprise e não altera modelo/provedor. Uma adoção exige versão fixada, licença por componente, benchmark com o executor escolhido, isolamento, idempotência, recuperação e orçamento. A existência de suporte documentado a Ollama não prova qualidade nem execução contínua no host do projeto.

## Aceite

Registrar separadamente: pacote recebido; integridade/licença; perfil aplicado; cliente descobriu; tarefa executada; revisão; resultado medido; publicação. Usar PASS, FAIL, NOT_RUN ou INCONCLUSIVE com evidência. Publicar o método não significa aplicar a todos os projetos. O encerramento informa exatamente quais projetos e arquivos mudaram e quais dependências continuam pendentes.
