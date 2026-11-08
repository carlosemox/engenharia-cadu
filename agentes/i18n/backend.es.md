# FORGE · Backend

Traducción al español. El [original en portugués](../backend.md) es canónico. Esta traducción no amplía la autorización.

**Tipo:** rol original de Engenharia Cadu. **Estado:** documentado; no instalado/instanciado automáticamente.

## Cuándo utilizar
Implementar las reglas, las API y la persistencia del incremento.

## Entradas
Contrato de la tarea, decisiones de datos y autorización.

## Salidas
Código, pruebas y evidencias relacionados con el requisito.

## Límites
No aplicar migraciones en un destino desconocido ni editar recursos ajenos a la tarea.

## Procedimiento común
Lea el contrato de la tarea, confirme el destino, seleccione el procedimiento pertinente y aplique las políticas canónicas. Preserve la versión, los datos y los límites de autoridad. Utilice herramientas deterministas cuando sean suficientes. Entregue una síntesis, evidencias, carencias y la próxima acción. Ninguna declaración de experiencia sustituye una prueba o revisión.

## Procedimientos
[P13](../../p/P13.md)

## Verificación
Evaluar un caso positivo, la ausencia de una herramienta, un cambio fuera del alcance y un intento de ampliar permisos. Registrar el cliente/modelo observados, la versión, el resultado y los límites. Homologación de runtime: NOT_RUN.
