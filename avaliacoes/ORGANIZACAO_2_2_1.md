# Organização da central e do site — 2.2.1

Registro de 30/10/2026. Escopo: navegação, guias, fontes, templates e documentação dos repositórios. Nenhum aplicativo, banco, servidor, conta de executor ou workflow foi alterado.

## Revisões examinadas
- Central e site: `0d01db8df3efc103ac586e2c4d830023b11931c7`.
- Adoção: `0ae85da1b79210c5ab84a6af55e8d38ba87e5eec`.
- Operação privada: `cf21a3c4c1372edb2a49e82331e1d02dbda45628` (sem dados privados reproduzidos aqui).

## Conferências realizadas
- 27 testes automatizados passaram (contratos documentais, organização e importador); oito casos de organização falharam antes da implementação e passaram depois.
- 29 prompts preservados; 39 páginas HTML; 1.833 referências locais verificadas sem erro.
- 207 arquivos do candidato central comparados aos blobs Git, sem divergência.
- 42 páginas/recursos da central responderam HTTP 200, com bytes iguais aos arquivos preparados.
- Página de adoção respondeu HTTP 200 e correspondeu ao arquivo preparado.
- Sintaxe JavaScript aprovada; geração editorial repetida sem mudanças adicionais.
- [Publicação da central](https://github.com/carlosemox/engenharia-cadu/actions/runs/41043106965): concluída com sucesso.
- [Publicação da adoção](https://github.com/carlosemox/engenharia-cadu-adocao/actions/runs/41043330063): concluída com sucesso.

Os números descrevem o candidato acima, antes de acrescentar este registro e atualizar seu manifesto. Essa última alteração é somente de documentação de evidências.

## Limitações
A inspeção visual/interativa do artefato publicado foi tentada com Chromium/Playwright, mas a navegação local foi bloqueada por `ERR_BLOCKED_BY_ADMINISTRATOR`. Não houve tentativa de contornar a política. Layout em navegador, menu móvel e área de transferência não receberam PASS por inferência; permanecem não verificados por execução interativa.

Testes de agentes em aplicativos reais, auditoria de segurança dos aplicativos, implantação de backup automático e supervisor de 24 horas: **NOT_RUN / NÃO IMPLANTADO por esta atualização**. A verificação estática e o deploy do site não substituem essas provas.

## Conteúdo entregue
[Mapa](../MAPA_DA_CENTRAL.md), [continuidade](../politicas/CONTINUIDADE.md), [segurança](../politicas/SEGURANCA_ENGENHARIA.md), [backup](../politicas/BACKUP_DRIVE.md), [estado operacional](../OPERACAO.md), [revisão de segurança](../templates/REVISAO_SEGURANCA.md) e [recibo de backup](../templates/RECIBO_BACKUP.md).
