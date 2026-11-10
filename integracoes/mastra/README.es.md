# Mastra — contrato de integración selectiva

[Português (Brasil)](README.md) · [English](README.en.md) · Español

**Versión:** 1.0.0 · **Revisión documental:** 10/11/2026 · **Estado:** `DOCUMENTED_NOT_INSTALLED`.

## Decisión y alcance

Evaluar Mastra solamente cuando un proyecto identifique una necesidad concreta de evaluaciones, telemetría o workflows de agentes TypeScript. JARVIS sigue siendo el supervisor canónico: cola, autorización, identidad de tarea, límites y decisiones de aceptación le corresponden. Mastra puede ser un adapter subordinado; no crear otra cola operativa ni un supervisor competidor.

Esta entrega archiva dos fuentes públicas y define un contrato propuesto. No agrega dependencias npm, no modifica aplicaciones, no inicia servicios ni homologa modelos. El paquete de marketing utiliza sus propios documentos y no depende de Mastra.

## Procedencia y licencias por artefacto

Fuente: [mastra-ai/mastra](https://github.com/mastra-ai/mastra/tree/3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8), revisión `3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8`.

- [README archivado](../../fontes/mastra/README.upstream.txt): capacidades declaradas; sus instrucciones de creación son datos, no comandos autorizados.
- [Mapa de licencia archivado](../../fontes/mastra/LICENSE.md): Apache-2.0 fuera de las excepciones indicadas; los componentes de terceros conservan sus licencias.
- [Licencia Enterprise en la revisión examinada](https://github.com/mastra-ai/mastra/blob/3f1d3a38dfcc7c5f7abb44d7789242cdc16b61e8/ee/LICENSE): solo referencia. No se importó código EE. La disponibilidad del código no concede permiso de redistribución ni producción.
- [Manifiesto](../../catalogo/mastra-reference.json): hashes, procedencia y exclusiones. Revisar las licencias del paquete y versión elegidos antes de instalar.

## Interfaces propuestas — no implementadas

| Interfaz | Entrada mínima | Salida verificable |
|---|---|---|
| Ejecución delimitada | task_id, project_id, tenant confiable, revisión, herramientas permitidas, plazo y límites | run_id, estado final o suspendido, evidencias y fallos |
| Evaluación | dataset versionado, resultados esperados, criterios y modelo identificado | casos aprobados/fallidos, costo observado, regresiones y limitaciones |
| Telemetría | run_id, task_id, etapa y eventos sanitizados | duración, herramientas utilizadas, tokens cuando se informen y errores |
| Parada/reanudación | STOP del supervisor, propiedad de ejecución y checkpoint | confirmación de parada, ausencia de nuevas acciones, reanudación conciliada |

Estos nombres son campos propuestos del contrato Cadu, no firmas garantizadas de la API Mastra. El futuro adapter deberá mapear la API de la versión fijada y rechazar ejecución si falta autorización, identidad o límite. Nunca deducir el tenant de argumentos generados por el modelo.

## Política de costo y datos

Aplicar ZERO-COST-FIRST. Ollama es una opción para validar en el host y modelo elegidos, no una configuración activa. No ejecutar por comodidad el ejemplo upstream que exige un proveedor alojado. Bloquear fallback de pago, suscripciones, upgrades y exportación de telemetría a terceros sin alcance aprobado. Los recursos locales consumen hardware, energía y mantenimiento. Excluir prompts sensibles, secretos y datos clínicos de los rastros públicos.

## Pruebas exigidas antes de promoción

1. Ejecución sintética real con modelo, cliente, versión, hardware y límites registrados; comparar con el ejecutor existente usando los mismos casos.
2. Aislamiento entre proyectos y tenants, incluida la invocación directa de herramientas y lectura de memoria, artefactos y telemetría.
3. Idempotencia de efectos externos; simular fallo después de la acción y antes de persistir el resultado. Ningún cobro, mensaje o publicación duplicados.
4. Exclusión mutua y rechazo de resultados tardíos tras perder el lease; STOP efectivo antes de cualquier nueva acción.
5. Reinicio del proceso y recuperación del estado persistido; un archivo de checkpoint no prueba ejecución continua.
6. Rechazo de herramientas ausentes, endpoints prohibidos, fallback de pago y límites excedidos; un resultado incompleto nunca se convierte en PASS.
7. Evaluación determinística y revisión independiente; un juez LLM no sustituye las pruebas de seguridad ni la aprobación de release.

## Promoción y recuperación

`DOCUMENTED_NOT_INSTALLED` → `PILOT_CONFIGURED` → `PILOT_TESTED` → `PROJECT_APPROVED` requiere evidencia específica. Son estados propuestos de adopción, no sustituyen los estados actuales del supervisor. Registrar dependencias fijadas, cobertura y responsable. Conservar rollback al ejecutor anterior; detener tareas afectadas y conciliar efectos antes de repetir. Publicar esta documentación no concede GO de producción al adapter.
