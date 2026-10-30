# Exemplo de integração inicial — aula ao vivo

**Exemplo proposto, sem escolha de fornecedor, preço, credencial ou piloto realizado.** Serve para preencher o mapa INT no ponto certo, não para prescrever uma API.

## Descoberta

Necessidade informada: lançar a plataforma com aulas ao vivo usando solução externa até uma decisão futura. Perguntas materiais: encontro interativo ou transmissão? Quantas salas/participantes simultâneos? Câmera/microfone do aluno? Gravação? Presença? Quem modera? Aula dentro da interface ou link externo é aceitável?

## Decisão e documentos

P01/P03 registram a jornada e D0: aluno matriculado encontra aula e acesso compreensível. P02/P08 comparam link, interface incorporada e integração por API de fornecedores cujas capacidades serão verificadas. Não chamar link de embed.

PRD descreve comportamento e restrições. TRD concentra fornecedor/contrato por INT-AULA-001. Nossa plataforma governa matrícula, agenda e autorização de acesso; não pressupõe que consegue impedir compartilhamento de link sem recurso compatível do fornecedor.

## INT-AULA-001 — rascunho

Estratégia: INTEGRAR inicialmente, pendente de escolha. Requisito: acesso à aula para matrícula válida. Solução/plano/custo: NÃO VERIFICADOS. Forma de acesso: A_DECIDIR. Ambiente/piloto: NOT_RUN. Dados: minimizar, documentar identificadores enviados e retenção de gravações quando existir.

Contrato desejado somente se suportado: agendar/cancelar, obter acesso, consultar estado e receber eventos. Não transformar esses verbos em promessa de API existente. Concentrar detalhes num módulo simples, sem criar microserviços por hipótese.

## Aceite proposto

Matrícula válida e aula disponível apresentam o acesso definido; usuário sem permissão não recebe acesso pelo nosso backend. Sala indisponível/cancelada apresenta o estado e contingência. Evento repetido não duplica registro quando houver webhook. Gravação e presença só são aceites se pertencem ao escopo e puderem ser comprovadas.

Criação de sala, login e conexão são executados apenas em sandbox autorizado; retorno real é evidência. O teste que só usa mock permanece assim identificado.

## Transição

Reavaliar por custo, limites, experiência e controle. Verificar exportação/preservação de dados e gravações, identificadores internos estáveis e contratos de compatibilidade. Não agendar reescrita obrigatória nem garantir migração sem estudar fornecedor/dados.
