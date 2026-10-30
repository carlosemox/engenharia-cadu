# Hooks e verificador de recibos

## Arquivos e limites
`security_gate.py`: Python 3.10+, biblioteca padrão, somente leitura. Confere política, projeto, evento, snapshot, idade individual dos checks, resultado PASS, cobertura e disposições de achados. Eventos podem exigir revisão independente e backup. Sem scanners, modelos, subprocessos, rede, instalações ou mudanças no aplicativo. Saída JSON curta. Exit 0 = recibo aceito; 1 = bloqueado; 2 = entrada/contexto inválido.

**Não é um scanner nem um autenticador.** O gate não abre evidências, não verifica assinaturas/proveniência e não confirma a veracidade de um JSON. O implementador não pode escrever PASS para aprovar a própria mudança. Recibos, política/digest e snapshot vêm de serviço/job confiável, com controles externos e permissões próprias. IDs de dois revisores em um JSON não provam revisão independente.

`entrypoint.sh.example` e os wrappers de eventos são exemplos POSIX inativos. Não estão em `.git/hooks`, não configuram clientes e não ativam CI. Windows nativo pode chamar o Python por adaptador revisado. Variáveis exigidas vêm de configuração privada confiável; não são segredos. Não usar valores deste template como evidência real.

## Ativação mínima no projeto (FIX explícito)
1. Inventariar stack, ferramentas, hooks e CI existentes; preservar o que funciona.
2. Selecionar checks aplicáveis, revisar scripts/efeitos, versões/flags e capacidade de redigir saídas. Não instalar scanner silenciosamente nem consultar nomes privados em serviço externo.
3. Implementar coletores/adaptadores reais em ambiente isolado sem produção. Capturar exit, timeout, crash, estado da base de advisories, versão e evidências. Sem ferramenta ou check requerido, bloquear; não registrar PASS.
4. Configurar cópia privada da política fora do projeto e aprovar seu digest; escolher validade por evento e risco, sem adotar o prazo de exemplo como universal.
5. Associar evento → escopo → snapshot → checks → recibo → gate. Tratar Git index vs working tree; um SHA HEAD sozinho não cobre alterações locais. Pre-push exige lidar com as refs reais fornecidas pelo Git, inclusive múltiplas refs, tags e exclusões.
6. Instalar por mecanismo real do cliente/supervisor e/ou CI autorizado. Não mudar core.hooksPath global, sobrescrever hook anterior ou criar exceção automática. Os wrappers lógicos **não** devem ser instalados literalmente como hook Git esperando descoberta automática do contexto.
7. Provar invocação, PASS e falhas em cópia isolada. Configurar checks essenciais no CI e controle de merge/release quando suportados; conferir bypass de administradores, scripts modificáveis e origem do verificador/política. Sem esse controle, o hook é só feedback local.
8. Revisar rollout e recuperação; registrar o que foi instalado e o que ainda está NOT_RUN. Publicar esta biblioteca não realiza esses passos.

## Chamada do verificador
```text
python /caminho/fixado/security_gate.py --policy /privado/policy.json --receipt /privado/receipt.json --event module-complete --snapshot <snapshot-observado> --project-root /projeto --expected-policy-sha256 <digest-aprovado>
```
Substituir caminhos. O CLI rejeita política/recibo dentro da árvore do projeto; o gate atual exige destino externo, mais restritivo que a opção de pasta ignorada permitida para os relatórios de auditoria. O snapshot é calculado pelo executor, não lido do próprio recibo.

O digest da política usa `policy_hash`: SHA-256 do JSON canônico, UTF-8, chaves ordenadas, sem espaços separadores, sem números não finitos. Não é o hash dos bytes de um arquivo JSON formatado. Digest é referência aprovada, não assinatura. Eventuais mudanças na política exigem nova revisão/digest; o recebedor não aprova automaticamente por calcular o próprio hash.

## Política de evidências
Required checks não vazios, únicos e atuais. NOT_RUN/ERROR/SKIPPED/TIMEOUT/N/A não satisfazem um required check. Retirar requisito como não aplicável requer justificativa aprovada, não ocultar falha. Data do recibo não renova a idade do scan. Relatórios de outro snapshot/evento/projeto são recusados. Não existe opção skip/force para passar no gate.

Somente as lacunas obrigatórias do escopo do evento entram em `coverage_gaps`; áreas futuras continuam no handoff, sem sumir do total da campanha. Antes de release, cobertura global requerida precisa estar concluída ou explicitamente tratada conforme política, nunca extrapolada de amostra.

Achados High/Critical não resolvidos bloqueiam, e candidatos graves aguardam triagem; não contam como confirmados automaticamente. Risco aceito de menor gravidade exige owner, motivo, referência e expiração. No evento pre-release, achados não informativos ainda abertos exigem correção verificada ou disposição válida; não desaparecem sob uma classificação menor. PASS do gate não é GO de produção. Checks legítimos/negados, restauração e configuração de deploy têm provas próprias.

## CI e agendamento
[CI.md](CI.md) descreve contrato de integração; não há workflow ativo neste módulo. Nenhum webhook GitHub, bot, scheduler ou hook do terminal foi instalado. Dependabot/Renovate são opções conforme suporte real; updates como PRs revisáveis, automerge desativado por padrão. Hooks não atualizam versões no momento do commit.

[Eventos](EVENTOS.json) · [Política inativa](../templates/GATE_POLICY.json) · [Recibo inativo](../templates/GATE_RECEIPT.json) · [Módulo](../README.md)
