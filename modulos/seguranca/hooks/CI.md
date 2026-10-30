# Contrato de integração com CI — inativo

Independente de fornecedor: usar o pipeline existente, seu mecanismo de evidência e configuração de acesso mínimo. Esta página não é um workflow instalado. Não mover arquivo de exemplo para `.github/workflows` sem autorização específica.

Job de seleção: identificar candidato, arquivos/contratos e controles requeridos a partir de política confiável. Checks obrigatórios têm nomes estáveis/inequívocos. Se houver merge queue, testar o candidato de integração apropriado; não depender de um scan de outro SHA.

Jobs executores: somente ferramentas revisadas, ambiente isolado, sem segredos de produção; não executar código de PR externo em runner privilegiado. Erros/timeouts/skips e bases desatualizadas precisam de estado explícito. Não usar continue-on-error ou `|| true` para disfarçar falha. Configurar limitações de rede conforme o teste/advisory autorizado.

Agregador: deve rodar mesmo quando job requerido falha/não roda, representar as ausências, não confiar no recibo que vem no diff do PR e não receber credenciais desnecessárias. Emitir recibo privado e chamar gate confiável/pinado com projeto/evento/snapshot/digest esperados fora do controle do autor.

Controles de merge/publicação: exigir o resultado pertinente, conferir bypass e quem pode mudar política/workflows/allowlists/exceções. Um job pode ser alterado para retornar sucesso; checks no servidor precisam considerar confiança da origem e revisão desses arquivos. O gate não resolve isso sozinho.

Agendamento: definir frequência, repositório/branch e fontes de advisories em tarefa própria aprovada. Não inferir que hook de commit detecta advisory publicado depois do último commit. Configurar duração, concorrência e canal privado de triagem. Nenhum agendamento é criado por ler esta receita.

Homologação: fixture sintética para provar que falha, ausência de ferramenta, timeout, snapshot divergente, bypass e revisão pendente realmente impedem a transição. Não produzir ataque contra terceiros. Rollout/correção do CI com alçada e rollback; manter separação AUDIT/PLAN/FIX/VERIFY.
