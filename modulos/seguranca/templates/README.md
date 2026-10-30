# Templates — todos inativos
[SECURITY-FINDINGS.json](SECURITY-FINDINGS.json) mantém identidade, escopo, achados, cobertura e lotes; null significa desconhecido. Não contém resultados reais.

[GATE_POLICY.json](GATE_POLICY.json) exemplifica eventos/required checks. Não usar em produção nem ativar simplesmente trocando enabled: faltam alçada, collectors, isolamento, política aprovada e testes. Prazos ilustrativos não são SLA ou prescrição universal.

[GATE_RECEIPT.json](GATE_RECEIPT.json) começa sem resultados. Um coletor confiável preenche fatos, nunca inventa PASS. Datas/check IDs/evidências devem corresponder ao evento e snapshot observados.

[CAMPAIGN.md](CAMPAIGN.md) delimita marcos inicial/intermediários/final e eventos contínuos. A autorização de uma campanha não concede permissão de correção, teste ativo ou publicação.

O prompt universal descreve os relatórios Markdown e handoff; gerar artefatos privados por campanha, não preencher esta biblioteca com achados reais. Recibos de segurança não são automaticamente enviados a Drive/backup público.
