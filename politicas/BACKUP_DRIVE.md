# Backup no Drive por projeto — edição 2.2

Destino: **Projetos 2026 / Backup / <nome-do-projeto>**. IDs e configuração de acesso ficam no perfil privado. Resolver pai e filho, verificar duplicatas e permissões; nomes não identificam unicamente uma pasta. Não publicar relatórios reais, credenciais ou cópias de aplicativos na central pública.

## Quando copiar
Antes de modificar projeto existente; ao fechar etapa com artefatos novos/alterados; após lote de implementação aceito; antes de refatoração relevante, migração, operação destrutiva e release; ao parar/retomar uma missão quando mudou o estado. Evitar duplicar conteúdo idêntico sem perder gerações anteriores.

Fechar etapa → verificar entrega → capturar estado pertinente → enviar → conferir integridade → registrar recibo → avançar. Ação de alto risco exige backup do estado anterior e prova de recuperação pertinente ANTES da mudança. Falha de upload bloqueia a ação dependente, não autoriza contornar proteção. Análise independente pode continuar. Sem conexão/adapter/runtime, não afirmar backup automático ativo.

## Todos os arquivos: cobertura explícita
Inventariar código, docs, designs, assets, scripts, testes, migrations, configs não secretas e alterações staged/unstaged/untracked úteis. O manifesto registra inclusões, exclusões e pendências. Não omitir conteúdo e chamar a cópia de completa.

Separar classes de recuperação:
1. Arquivos de trabalho e artefatos fora do Git.
2. Histórico Git/refs por bundle ou mirror seguro quando acessível/autorizado. ZIP de uma revisão não preserva automaticamente histórico, outras branches, submódulos, LFS, releases, issues, settings ou alterações locais.
3. Banco, objetos Storage/uploads, volumes e configurações de serviços: exportação e teste de restauração próprios. Backup de código não é backup de dados; backup de banco Supabase não inclui automaticamente objetos do Storage.
4. Segredos/dados sensíveis: nunca em ZIP comum nem logs. Cofre ou arquivo criptografado por mecanismo aprovado, chave controlada pelo responsável e fora do backup. Sem mecanismo adequado, declarar a classe PENDENTE e impedir ação dependente; não inventar criptografia, não enviar `.env`, chaves ou tokens em texto aberto.

Caches, dependências instaladas e saídas reconstruíveis só podem ser excluídos por política explícita, com manifesto e instruções de reconstrução. Assets únicos não são cache. `.env.example` exige verificação de ausência de segredo real. Histórico Git também pode conter segredos e precisa ser avaliado antes da transferência.

## Integridade e destino
Criar geração nova, sem sobrescrever: `<projeto>__<timestamp-UTC>__<revisao>__<classe>.zip`. Incluir manifesto por arquivo com caminho, tamanho e SHA-256, revisão/estado, escopo, exclusões e instruções de restauração.

Congelar ou reconciliar escritores. Se arquivos mudarem durante captura, refazer a unidade ou declarar INCONSISTENTE. Não guardar o pacote dentro do diretório capturado. Não seguir links para fora do alvo nem executar scripts ao extrair; conferir caminhos seguros.

Depois do upload: confirmar ID, nome, pasta-pai, tamanho e acesso restrito. Comparar checksum oferecido pelo Drive quando disponível; caso contrário baixar novamente e comparar SHA-256. Não colocar links temporários autenticados em relatórios públicos.

Estados: PLANEJADO → CAPTURADO → ENVIADO → VERIFICADO. RESTAURACAO_TESTADA é outra evidência: extrair em local vazio e descartável, comparar arquivos e testar o necessário. ZIP íntegro não prova cobertura completa ou recuperação do aplicativo. Recibo privado registra IDs, revisão, manifesto, checksums e limitações; um boolean não cria prova.

## Retenção e recuperação
Preservar gerações antigas. Nenhuma limpeza/expiração automática foi autorizada nesta configuração. Política futura de retenção deve considerar custo e recuperação. Drive é cópia adicional, não armazenamento imutável nem proteção única contra comprometimento da conta. Cópia independente/offline ou imutável requer estratégia e autorização próprias quando o risco exigir.

Para restaurar: selecionar geração → conferir hash/manifesto → extrair em destino vazio/isolado → comparar estado → testar sem produção → revisar diferenças → aprovar alteração no alvo. Não sobrepor workspace ativo automaticamente.

## Limites operacionais
Uma pasta criada não prova automação instalada. Cada computador/supervisor precisa de acesso Drive observado e integração testada; conexão desta conversa não se transfere ao Codex. Esta política não instala credenciais nem agendamentos.

Fontes: [Drive/checksums](https://developers.google.com/workspace/drive/api/reference/rest/v3/files), [Supabase backups](https://supabase.com/docs/guides/platform/backups), [NIST — backups e recuperação](https://csrc.nist.gov/pubs/other/2020/04/24/protecting-data-from-ransomware-and-other-data-los/final).

[Continuidade](CONTINUIDADE.md) · [Segurança](SEGURANCA_ENGENHARIA.md)
