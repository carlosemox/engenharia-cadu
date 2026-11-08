# Gate de release

- [ ] Plano/arquitetura pertinentes aprovados e escopo delimitado.
- [ ] Identidade de implementador diferente do revisor, snapshot e evidências conferidos.
- [ ] CI do SHA candidato PASS; check obrigatório configurado separadamente.
- [ ] Dependências, catálogo, licenças e permissões revisadas.
- [ ] Validação visual e acessibilidade quando aplicável.
- [ ] Staging representativo; smoke/health check quando aplicável.
- [ ] Backup, restauração e rollback verificáveis para recursos afetados.
- [ ] Autorização específica de merge/deploy/publicação.

Estado: RELEASE_BLOCKED. Main e site publicados preservados. Para esta mudança documental/código, rollback proposto é revert do commit aprovado; não foi realizado rollback em produção. Dados de aplicativos não foram tocados.
