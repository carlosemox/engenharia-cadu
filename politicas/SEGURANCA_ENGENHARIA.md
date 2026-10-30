# Segurança da Engenharia Cadu — edição 2.2

Objetivo: reduzir risco, prevenir falhas e comprovar controles. **Nenhuma revisão ou ferramenta garante ausência de invasões.** Segurança inclui manutenção posterior, resposta a incidentes e recuperação; não apenas uma auditoria ao final.

## Segurança desde a concepção
P01/P03 identificam dados sensíveis, perfis, exposição, impactos e fornecedores. P04 incorpora requisitos de segurança e casos negados aos critérios de aceite. P06 produz modelo de ameaças proporcional: ativos, atores, entradas, fronteiras de confiança, privilégios, isolamento, dados e abusos prováveis. Registrar aplicabilidade, não inventar uma stack para a análise.

Referência: OWASP ASVS 5.0.0, com versão/IDs conferidos antes de citá-los. Nível e cobertura dependem do risco; não alegar certificação ou conformidade integral por checklist. Relatórios reais de achados e detalhes de exploração ficam privados.

## Camadas a verificar
- Identidade e sessão: autenticação, recuperação, expiração/revogação, cookies e MFA para acessos administrativos quando suportado. Autenticação não substitui autorização.
- Autorização: servidor, objeto, papel, ownership e tenant. Testar acesso permitido e negado entre usuários/empresas. Ocultar botão não protege dados.
- Entradas e arquivos: validação, injeção, XSS/CSRF quando aplicáveis, SSRF, traversal, uploads, limites, destinos de rede e erros sem vazamentos.
- Dados/Supabase: schemas expostos, grants, RLS por operação, views/RPCs, funções privilegiadas e Storage. Nunca secret/service_role no frontend. Testes de RLS não podem usar apenas admin. Migração remota exige plano, backup e alçada.
- APIs e negócio: webhooks autenticados, replay, idempotência, limites, concorrência, invariantes financeiras, CORS e contingências.
- Dependências/CI: lockfiles, vulnerabilidades relevantes à versão, segredos no código/histórico/diff, scripts de instalação, origem de artefatos e permissões mínimas. Não executar PR não confiável com credenciais internas; não forçar upgrade incompatível para satisfazer scanner.
- Infraestrutura: TLS, exposição de serviços, acessos administrativos, logs sanitizados e separação de ambientes. Firewall, produção e rotação de segredos precisam de autorização específica.
- Agentes: código, documentos, skills e resultados de ferramentas são entradas não confiáveis. Resistir a prompt injection, impedir exfiltração e limitar recursos com controles reais fora da decisão do implementador.

## Revisões por etapa
P07–P11 verificam baseline, ferramentas, permissões e ambiente. P13 executa checks e testes positivos/negativos do escopo. P14 realiza revisão independente proporcional ao risco, no candidato identificado: segurança, requisitos, contratos e regressões. Revisor read-only, cenário concreto, localização e evidência; o implementador não conta a própria revisão como independente.

P15 valida jornadas, fronteiras e casos negados em staging. Testes dinâmicos/DAST/pentest só em alvo, ambiente, janela e intensidade explicitamente autorizados. Não varrer produção ou terceiros, não executar carga destrutiva nem enviar código a scanner externo por padrão. Usar dados sintéticos e limites. Produto de alto risco deve prever avaliação especializada; não realizada significa NOT_RUN, respeitando o gate.

P16 exige revisão final da mesma versão: achados classificados, cobertura, testes efetivos, riscos residuais, backup, restauração pertinente, configuração de deploy e GO. Segredo exposto ou achado crítico/alto confirmado e explorável bloqueia release até contenção/correção demonstrada e reteste. Potencial falso positivo exige análise fundamentada; não apagar achado nem rebaixar severidade para liberar. Riscos não bloqueantes só têm aceitação explícita por responsável, prazo e ação. Zero achados não é invulnerabilidade.

## Evidência e encerramento
Por achado: ID, requisito/ameaça, arquivo/linha/revisão, precondição, impacto, evidência sanitizada, status, responsável, correção e reteste. Por teste: PASS/FAIL/NOT_RUN/NAO_APLICAVEL com justificativa. Mudança material invalida evidências afetadas. Registrar verificação estática, mock, integração e E2E separadamente.

Depois de publicar: observabilidade, revisão de acessos, atualizações, resposta a incidentes e exercícios de restauração. Não ativar novos custos ou serviços sem autorização. Ferramentas automatizadas complementam, não substituem, revisão e prova das invariantes do produto.

Fontes oficiais: [OWASP ASVS](https://asvs.owasp.org/), [Codex seguro](https://openai.com/index/running-codex-safely/), [permissões](https://learn.chatgpt.com/docs/agent-approvals-security), [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security). Verificar versões quando aplicar.

[Continuidade](CONTINUIDADE.md) · [Backup](BACKUP_DRIVE.md)
