# Recibo de backup — template inativo e privado

Estado inicial: PLANEJADO. Usar ENVIADO somente após confirmação do serviço; VERIFICADO requer integridade; RESTAURACAO_TESTADA exige prova separada. Não colocar IDs reais ou links de acesso privado no repositório público.

## Origem e cobertura
Projeto, revisão/snapshot, data UTC, escritores reconciliados e alcance. Descrever arquivos versionados, staged/unstaged/untracked úteis, assets, histórico Git/refs, banco, Storage/volumes e segredos protegidos. Registrar inclusões, exclusões e pendências por classe. ZIP de revisão não equivale a toda a recuperação.

## Geração e destino
Nome único, pasta-pai e ID privado verificados, nome do projeto, pacote/manifesto, número e tamanho dos arquivos, SHA-256 do pacote e hashes individuais. Verificar acesso restrito. Chave de criptografia nunca no mesmo backup. Não sobrescrever geração anterior.

## Envio e leitura de volta
ID retornado pelo serviço, tamanho remoto, checksum disponível ou SHA-256 após novo download, resultado da comparação, falhas e referência da evidência. Um nome de pasta ou boolean no JSON não prova backup.

## Restauração
Testes de restauração: destino vazio/isolado, comparação dos arquivos, testes de recuperação executados, versão/ambiente e limitações. Integridade do ZIP não comprova consistência de banco nem funcionamento do aplicativo. Não restaurar por cima de um workspace ativo.

## Disposição
Status por classe, cobertura completa ou parcial, bloqueios que impedem a próxima ação, próxima verificação e responsável. Retenção sem limpeza automática até decisão específica.

[Política de backup](../politicas/BACKUP_DRIVE.md)
