# MIKE — Untangle Codebase y Claude Code por Slices · V1.0
Revisión: 2026-11-17 · [Português](UNTANGLE_CLAUDE_SLICES.md) · [English](UNTANGLE_CLAUDE_SLICES.en.md)

## Origen y gobernanza
Adaptación gobernada de `caldoai/skills/skills/untangle-codebase/SKILL.md` (commit `bd73b2ea5eb854ab8f0553fb41f77c8786f28f82`, blob `102ff57803e504876f6eb9b412e4eb0f6c576350`, MIT, copyright 2026 Maze). No ejecuta el mandato original sin límites de «corregir todo». Es una guía para agentes, no un sandbox ni auditor automático.

Cadu aprueba producto, alcance, presupuesto y publicación. **MIKE** supervisa el desarrollo bajo sus órdenes, separado de JARVIS: cola canónica, leases, responsables, evidencias y checkpoints. La documentación no demuestra un daemon permanente. Codex permanece como coordinador técnico en proyectos ya configurados; Claude Code es ejecutor opcional, sin segundo supervisor. Deny by default, privilegio mínimo, RBAC/ABAC/RLS cuando corresponda, MFA/passkey, auditoría y rollback.

**Correspondencia de etapas:** Untangle U01–U08 no equivale a CADU P00–P30; P06 es arquitectura, P13 implementación, P14 revisión y P24 medición.

## Procedimiento obligatorio
1. **Harness:** comprobar repositorio, HEAD/SHA, rama, entorno autorizado anteriormente, decisiones, tests, permisos, estado y worktrees; conservar el trabajo existente.
2. **Untangle selectivo y de solo lectura:** inspeccionar módulos afectados al iniciar/retomar, planificar épicas, revisar PR relevantes o tras incidentes estructurales. Registrar vínculos ocultos, vínculos innecesarios, redundancias demostradas y excepciones válidas; grafo y evidencia archivo:línea/SHA. Conservar reintentos y controles de seguridad justificados.
3. **Slices verticales:** cada slice tiene resultado medible, interfaces, tests positivos/negativos, dependencias, propietario exclusivo de archivos/esquemas/lockfiles/recursos, coste estimado, límite aprobado y rollback. Usar `templates/MIKE_SLICE_CONTRACT.json`.
4. **Graph:** ejecutar READY solo con dependencias PASSED; un ejecutor por defecto. Paralelismo únicamente entre recursos separados y ramas/worktrees realmente aislados.
5. **Gate de implementação antes de P13:** todo cambio requiere autorización específica, worker aislado y permisos comprobados. Eliminar comentarios/tests exige autorización adicional. La skill diagnóstica no concede escritura.
6. **Loop:** OBJETIVO → ACCIÓN MÍNIMA → OBSERVACIÓN → VERIFICACIÓN → DECISIÓN; máximo tres ciclos por nodo; detenerse antes por riesgo, secretos, regresión o coste.
7. **P13/P14:** verificaciones autorizadas y revisión independiente de solo lectura sobre contratos, diff, evidencia y rollback. Sin merge, push, despliegue, producción, migración destructiva, gasto o publicación automáticos.
8. **Checkpoint:** MIKE concilia pruebas reales diff/commit/PR, PASS/FAIL/NOT_RUN/INCONCLUSIVE, costes observados, riesgos y próximo nodo; una afirmación del agente no es evidencia.

## Modelos y costes
Primero herramientas deterministas; Haiku 5.5 para búsqueda; Sonnet 5.5 para planificación, **un worker por slice aprobado** y revisión independiente. Opus 5.5/Fable 5.2 únicamente con justificación y presupuesto aprobados. IDs: `claude-haiku-5-5`, `claude-sonnet-5-5`, `claude-opus-5-5`, `claude-fable-5-2`. Confirmar acceso real. Medir **coste total por slice aceptado**, incluidos tests/revisiones/reintentos; cuotas de suscripción, API y Ollama no son equivalentes. ZERO-COST-FIRST; prohibido eludir cuotas o crear costes sin autorización.

## Implantación Claude Code
La central contiene `CLAUDE.md`, `.claude/skills/cadu-untangle/SKILL.md` y `.claude/agents/`: scout Haiku solo lectura, arquitecto Sonnet lectura, builder Sonnet 5.5 en aislamiento autorizado, revisor Sonnet 5.5 lectura. Permisos plan/default, nunca bypass por defecto. Agent teams experimentales desactivados salvo autorización y valor demostrado; no reemplazan a MIKE. Cada otro repositorio necesita adopción y SHA verificables; esta actualización no lo instala allí. No se crea polling LLM programado.

Comandos: [MIKE Claude Slices](../comandos/MIKE_CLAUDE_SLICES.es.md). Contrato: [plantilla JSON](../templates/MIKE_SLICE_CONTRACT.json). **Estado:** SPEC_CREATED; runtime y despliegue externo NOT_RUN.
