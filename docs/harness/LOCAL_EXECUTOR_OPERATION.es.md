# Ejecutor local — operación restringida

Versión 0.2.0 · 2026-11-10 · [Português](LOCAL_EXECUTOR_OPERATION.md) · [English](LOCAL_EXECUTOR_OPERATION.en.md)

## Estado y finalidad

`com.engenharia-cadu.local-executor` está instalado en el Mac bajo el método
Engenharia-Cadu. Usa Ollama local `qwen3:4b`, sin clave API, descarga ni fallback de
pago. Corrigió una suma sintética, superó tres aserciones y guardó el candidato como
`REVIEW_REQUIRED`. Esto no homologa un programador generalista ni proyectos reales.

Base: `~/Library/Application Support/Engenharia-Cadu-Agent`.
Código: `scripts/local_executor.py`; instalador: `scripts/install_local_executor.py`.
El instalador rechaza sobrescrituras. El LaunchAgent requiere el Mac encendido y la
sesión iniciada. No funciona con el Mac apagado; no se comprobó disponibilidad de 24 horas.

## Política efectiva

- Un supervisor y una tarea simultánea, bloqueo exclusivo, heartbeat cada cinco segundos en reposo.
- Un intento por ID; límites de tarea/cliente de inferencia/test: 240/90/20 segundos.
- Hasta ocho archivos existentes, 64 KiB cada uno y 256 KiB en total.
- Proyecto y raíz canónica deben coincidir con `state/model.json` antes de leer fuentes.
- Jobs en `state/jobs/` incluyen alcance, instrucción, checks confiables, revisión y autorización que vence en un máximo de 24 horas.
- Solo está admitido `synthetic-acceptance`; la cola contiene únicamente el piloto concluido.
- El modelo devuelve datos JSON; no recibe shell, credenciales, herramientas ni MCPs.
- Las fuentes quedan intactas; candidatos en `state/runs/<id>/work`.
- Los tests reciben candidatos de solo lectura y un temporal privado escribible, sin red ni creación de procesos.
- STOP, cambios de autorización/política y plazos detienen el cliente; no se repiten fallos automáticamente.
- El reinicio marca recibos RUNNING como INTERRUPTED sin repetir efectos inciertos.
- Sin merge/deploy automático, autorrevisión ni activación de agentes externos.

## Operación

Para el operador o conector autorizado en el Mac; no es necesario repetir estos comandos para mantener el servicio activo.

```sh
# Estado del servicio
launchctl print "gui/$(id -u)/com.engenharia-cadu.local-executor"
# Cola/tarea actual
cat "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/heartbeat.json"
# Parada cooperativa; esperar STOPPED
touch "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/STOP_REQUESTED"
# Reanudación explícita después de revisar recibos; quitar STOP no reinicia por sí solo
rm -f "$HOME/Library/Application Support/Engenharia-Cadu-Agent/state/STOP_REQUESTED"
launchctl kickstart "gui/$(id -u)/com.engenharia-cadu.local-executor"
# Descargar servicio; conservar archivos y evidencias
launchctl bootout "gui/$(id -u)/com.engenharia-cadu.local-executor"
```

Para desactivar el inicio en la siguiente sesión, después de bootout mover
`~/Library/LaunchAgents/com.engenharia-cadu.local-executor.plist` fuera de LaunchAgents.
No borrar recibos para repetir tareas.

## Adopción por proyectos y capacidades

Usar `CADU HOMOLOGAR AGENTE LOCAL`. Recuperar backlog y reglas del proyecto, fijar la
revisión del método, elegir una tarea pequeña, definir tests independientes del
contenido editable y persistir autorización. Validar compatibilidad con el sandbox
antes de admitir la raíz. Builds que requieren subprocessos o red no están homologados.

El supervisor selecciona skills, agentes, MCPs y design systems por proyecto, con origen,
versión, permisos y validación. Catálogo no significa instalación ni homologación.
Esta versión no instala esas integraciones ni concede acceso; el worker recibe solo
instrucciones y archivos permitidos. Diseño, accesibilidad, tests de interfaz y revisión
independiente conservan sus gates; tests unitarios no sustituyen requisitos visuales.

## Evidencia y límites

Los probes denegaron lectura/escritura externa, estado, symlinks, Xcode, red y spawn
desvinculado. No prueban confinamiento absoluto de macOS: se permite leer bibliotecas
del sistema y metadatos. Cada archivo temporal tiene límite de 8 MiB; disco agregado,
memoria y threads carecen de cuota fuerte. STOP no demuestra cancelación instantánea
dentro de Ollama. Verificar digest antes/después no hace la tag atómicamente inmutable.
La autorización usa archivos privados del operador, sin autenticar usuarios externos.

La inferencia procesa tokens localmente sin API facturada. Hardware, energía y esta
conversación de preparación no están incluidos en una afirmación de costo cero.

Evidencia privada: `evidence/acceptance-2026-11-10` bajo la base instalada.
[Recibo técnico](LOCAL_EXECUTOR_ACCEPTANCE_2026-11-10.md).
