# Codex + Ollama en Mac

[Português](CODEX_OLLAMA_PILOT.md) · [English](CODEX_OLLAMA_PILOT.en.md) · [Español](CODEX_OLLAMA_PILOT.es.md)

Versión / actualización: **1.2.0 · 2026-11-08T15:45:08-03:00 · America/Sao_Paulo**

**PREPARACIÓN APROBADA — HOMOLOGACIÓN OPERATIVA PENDIENTE.**

Cadu aprobó la preparación, organización, traducción y publicación de este incremento. El Mac fue elegido como ejecutor; está apagado y no está disponible para la instalación. Esta aprobación no convierte las verificaciones documentales en pruebas del modelo.

## Arquitectura y costes

Codex dirige las tareas de programación; Ollama ejecuta un modelo local; el supervisor coordina la cola, los límites, la revisión independiente y las evidencias. Un modelo local no es el modelo OpenAI usado por Codex con ChatGPT.

No se contrató ninguna API ni nueva suscripción. La propuesta anterior de BRL 50,00 queda como alternativa inactiva, sin aprobación de gasto. La inferencia local no cobra tokens de API, pero utiliza hardware, energía y almacenamiento. Sin cambio automático a cloud o API de pago. El modelo, la licencia y la capacidad de usar herramientas requieren validación.

## Evidencias y límites

| Elemento | Estado observado |
| --- | --- |
| Regresión de la preparación | 184 pruebas Python aprobadas |
| Revisión independiente | Preparación revisada; correcciones incorporadas |
| GitHub | Cuenta carlosemox confirmada; la API informó permisos admin/push/pull |
| Codex CLI | Versión 0.167.0 instalada solo en el entorno temporal |
| Inicio de sesión ChatGPT | Credenciales reconocidas; ningún valor secreto exportado |
| Acceso al modelo OpenAI | La llamada mínima agotó el plazo de 60 segundos; acceso y cuota no comprobados |
| Mac | Elegido por el usuario; hardware y macOS sin inspeccionar; dispositivo no conectado |
| Ollama en Mac | Instalación, modelo e integración sin verificar |
| Supervisor fuera de la conversación | No activado ni homologado operativamente |
| Agentes externos | Catalogados; sin homologación individual presumida |

El entorno inspeccionado en esta conversación es Linux temporal, limitado a 8 GiB de RAM y ocho CPU por cuota, con 57,7 GiB libres observados y nvidia-smi no disponible. Estos datos no describen el Mac. Ollama no estaba instalado allí. OPENAI_API_KEY y CODEX_API_KEY estaban ausentes o vacías.

## Instalación posterior en Mac

1. Conectar el Mac y registrar procesador, RAM/VRAM, espacio libre, macOS e instalaciones existentes.
2. Seleccionar versiones verificadas de Codex y Ollama y un modelo local con licencia adecuada, herramientas y digest registrado.
3. Configurar solo loopback, cloud desactivada y contexto compatible con la memoria. La documentación Ollama recomienda al menos 64k tokens para Codex; la máquina debe soportarlos.
4. Validar respuesta local, herramientas, aislamiento, timeout, parada, recuperación y ausencia de efectos duplicados en una fixture sin secretos.
5. Resolver una pequeña corrección en un checkout desechable, ejecutar pruebas y obtener revisión independiente del diff. Medir tiempo y memoria.
6. Integrar con el supervisor y probar persistencia y programación periódica solo después de superar los controles. Este piloto no autoriza autoaprobación, merge/deploy de aplicaciones ni homologación de todo el catálogo.

## Comandos preparados, aún no ejecutados en Mac

Iniciar solo si no existe ya un servidor. Si existe, comprobar su configuración y reiniciar el servicio adecuado sin duplicarlo.

```sh
OLLAMA_NO_CLOUD=1 OLLAMA_HOST=127.0.0.1:11434 OLLAMA_CONTEXT_LENGTH=65536 ollama serve
```

Sustituir MODEL_NAME por el nombre exacto del modelo instalado. El contexto es un objetivo de prueba, no una garantía de memoria suficiente.

```sh
codex exec --oss --local-provider ollama --model MODEL_NAME --sandbox read-only -c 'web_search="disabled"' 'Reply CADU_OLLAMA_OK without using tools.'
```

Ollama local no aísla los comandos del agente. El bloqueo real del sandbox debe probarse en el Mac. No copiar la autenticación personal de ChatGPT al workflow público de CI.

## Verificador de acceso

`python scripts/check_codex_access.py` consulta solo versión y sesión; acepta `--codex-bin` con un ejecutable confiable. No lee auth.json directamente, no exporta salida bruta, no llama al modelo ni inicia servicios. Las credenciales no prueban conexión, cuota, acceso al modelo ni aislamiento. Este diagnóstico cubre la ruta ChatGPT; Ollama local no requiere inicio de sesión OpenAI.

## Próximo hito

**MAC_CONNECTED → HARDWARE_CHECKED → LOCAL_MODEL_TESTED → ISOLATION_VERIFIED → PILOT_REVIEWED.** Publicar esta página completa la preparación aprobada, no la homologación operativa.

## Referencias

- https://learn.chatgpt.com/docs/auth
- https://learn.chatgpt.com/docs/non-interactive-mode
- https://learn.chatgpt.com/docs/cli/reference
- https://docs.ollama.com/integrations/codex
- https://docs.ollama.com/faq
