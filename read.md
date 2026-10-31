# Engenharia Cadu — entrada curta

Esta central distribui procedimentos, não autorização irrestrita. Codex coordena; colaboradores só quando úteis, disponíveis e autorizados. O alvo é o aplicativo do usuário, não esta biblioteca.

1. Aproveite a intenção e o contexto disponíveis. Novo produto começa no [P01](p/P01.md); falha em projeto existente no [P20](p/P20.md); retomada no [P18](p/P18.md); acervo no [P22](p/P22.md). Sem trilha clara, [P00](p/P00.md).
2. Resolva a central para uma revisão e registre-a. Leia apenas o procedimento e as fontes pertinentes. Mudança de documento não troca modelo, provedor ou autenticação.
3. Ao iniciar produto do zero, use CONTINUO_SUPERVISIONADO na sessão ativa, conforme [Continuidade](politicas/CONTINUIDADE.md). Se o usuário pediu apenas uma etapa/análise, mantenha ISOLADO. Aplique [Segurança](politicas/SEGURANCA_ENGENHARIA.md) e [Backup](politicas/BACKUP_DRIVE.md).
4. Concluída e verificada a fase, conferir entrega, segurança, backup aplicável, checkpoint, limites e alçada; carregar o próximo prompt pertinente sem exigir nova colagem. O coordenador governa transições; cada prompt continua definindo somente sua fase. Não avançar sobre decisão material, falha ou ação não autorizada.
5. Seguir [rotas](orquestracao/rotas.json) por dependências reais: implementação/revisão repetem por incremento; P17 e especializações não são obrigatórios. Fim do escopo encerra; não inventar trabalho para manter execução.
6. Entrevista permanece interativa. Produção, migrations, gastos, credenciais e publicação conservam gates próprios. Backup obrigatório não verificado bloqueia o que depende dele. Sem runtime/conexão, não simular continuidade fora da sessão, segurança absoluta ou cópia automática.

## Atalho
```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md
Inicie meu produto em CONTINUO_SUPERVISIONADO. Avance somente após aceite, segurança, backup pertinente e autorização, sem me pedir para copiar cada próximo prompt.
```

[Comando e limites](continuar.md) · [Todos os prompts](README.md) · [Contrato comum](politicas/CONTRATO_COMUM.md) · [Método](METODO.md)

## Entrada universal e fábrica — V2.3

Para qualquer projeto, use [CADU — comando único](comando.md). Para anexar estudos e assumir coordenação, use [Assumir projeto](comandos/ASSUMIR_PROJETO.md); para recuperar e reorganizar, [Reestruturar projeto](comandos/REESTRUTURAR_PROJETO.md). A [fábrica](fabrica/README.md) gera o comando do pedido; não executa seu conteúdo.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/comando.md
CADU: recupere o estado do projeto aberto e continue a próxima tarefa autorizada.
```

O coordenador recupera perfil, fontes e checkpoint antes de selecionar a etapa. A aprovação de um lote é preservada; instalação global, efeitos externos e acesso a outros projetos continuam dependentes do escopo real.
