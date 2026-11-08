# Contrato do Design System

Contrato existente preservado: docs/assets/factory.css para a fábrica e os estilos existentes da central. Nenhuma paleta, fonte ou sistema visual novo. Templates em templates/DESIGN_SYSTEM.md continuam a orientar aplicativos.

FRAME e squads landing/dashboard só recebem caminhos visuais explicitamente aprovados. Não podem alterar migrations, auth, APIs ou banco por inferência. Um prefixo no JSON é gate de escopo, não uma sandbox de sistema operacional. Bloquear executor real até implementar sandbox e conferir diff, renames e symlinks.

Para cada projeto registrar versão do DS, tokens e componentes permitidos, estados vazio/loading/erro/acesso negado e critérios de acessibilidade. Sem contrato local verificado: BLOCKED para alteração visual material. Validação visual deste lote: NOT_RUN; não há alteração de estilos.
