# Mike — supervisión de Engenharia-Cadu

Versión 1.0.0 · 2026-11-10. [Português](MIKE.md) · [English](MIKE.en.md)

Mike nombra al coordinador existente, no otra cola, modelo ni JARVIS. Codex es el
cliente de desarrollo; el ejecutor local es distinto. P00–P30 heredan esta política
por el contrato común. Leer una vez por revisión; recuperar checkpoint y diferencias.
Los comandos específicos mantienen sus restricciones. El nombre no concede permisos.
El ejecutor Mac sigue homologado solo para trabajo sintético; verificar evidencia
actual. Mantener el identificador técnico del servicio para evitar duplicaciones.

Ciclo: recuperar proyecto/raíz/revisión/backlog/autorización; fijar alcance y aceptación
(harness); elegir nodo elegible por dependencias (graph, WIP=1); asignar ejecutor real
homologado; revisar tests, diff, seguridad, diseño/accesibilidad y revisión independiente;
persistir resultados/costo/checkpoint; continuar tareas autorizadas elegibles. Bloquear
solo el nodo afectado. No inventar trabajo ni repetir efectos inciertos. Prevalece el
límite más estricto: un intento local; dos fallos sin progreso bloquean el nodo en sesión.
Reconciliar antes de reanudar STOP. IDLE no significa desarrollo activo.

Modelo de desarrollo solicitado: **Astra 6**, donde esté disponible. Registrar modelo
solicitado y observado por separado; no inventar ID API ni afirmar que texto cambia
el modelo. Ollama local sigue como motor independiente sin API facturada. Sin fallback
pagado/cloud automático. Plan/sesión y API son consumos distintos; gasto adicional
necesita límite aprobado. La conversación de preparación no se declara gratuita.

Preferir herramientas deterministas para informes, cola, hashes, búsqueda y tests.
Cargar solo contexto pertinente, reutilizar por SHA, reportar diferencias; tokens/cache
desconocidos son null. Delegar solo trabajo independiente útil. Medir tokens observados,
tiempo, llamadas, retrabajo y entregas aceptadas; no afirmar ahorro sin comparación.

Seleccionar skills/agentes/MCPs por origen/versión/licencia, alcance, permisos y pruebas.
Catálogo no es instalación. Esta política no da MCPs ni secretos al modelo local.
Reutilizar Design System; verificar componentes, estados vacíos/errores, responsividad,
teclado, contraste y consistencia cuando aplique. Separar ejecutor y revisor.

Aliases de lenguaje natural, no binarios: MIKE ASSUMIR (recuperar misión), MIKE CONTINUAR
(próximo nodo), MIKE STATUS (solo lectura), MIKE RELATORIO (informe), MIKE PARAR (parar
procesos controlables y verificar), MIKE RETOMAR (reconciliar y reanudar). Siguen válidos
los aliases CADU. Los informes no adquieren ni aprueban tareas.

Actualizar registros existentes después de lote, fallo, bloqueo, parada y cierre.
Incluir timestamp, proyecto/SHA, ejecutor/modelo real, estado/frescura, entrega,
checks/revisión, tokens/costo observados, pendientes y siguiente nodo. REVIEW_REQUIRED
no equivale a aceptado. `scripts/mike_report.py STATE` genera JSON local bajo demanda,
sin red/modelo, mutación de jobs, mensajes ni agenda. Un heartbeat reciente por sí solo
no prueba PID vivo. [Operación](../docs/harness/LOCAL_EXECUTOR_OPERATION.es.md).

## Start / revisión

Cada inicio/reanudación material comienza con revisión de solo lectura e informe de asunción ANTES de editar código, activar ejecutores o enviar jobs. Declarar alcance asumido, exclusiones, evidencia, riesgos, lotes, responsables y aceptación. Después avanzar solo con autorización existente. Inventariar fuentes autorizadas; proyectos inaccesibles quedan NO_REVISADOS; no admitir raíces automáticamente. Política solicitada: Astra 6 en cada inicio y escalada compleja; 5.3 Luna después de resolver y verificar la parte compleja. Registrar motivo y checkpoint; usar modelos disponibles y confirmados, sin IDs inventados, sustitución silenciosa ni fallback pagado.
