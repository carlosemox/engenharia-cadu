# Entornos y agentes de desarrollo — V1

## Puerta obligatoria

Recupere el entorno autorizado y compárelo con el ejecutor actual. Pregunte solo si el destino es ambiguo o hay un conflicto. Entornos previstos:

1. **Terminal** — CLI, Git, scripts y pruebas directas.
2. **Aplicación del ordenador/Mac** — IDE o aplicación local con edición interactiva y revisión visual.
3. **Cloud Code** — VS Code, IntelliJ/JetBrains o Cloud Shell, especialmente para Cloud Run, Kubernetes, GKE, APIs y recursos de Google Cloud.

Registre el entorno elegido en el estado o checkpoint del proyecto antes de escribir código.

## Funciones

| Capacidad | Uso principal | Límite |
|---|---|---|
| Codex | Coordinar la misión, integrar cambios, revisar evidencias y decidir el siguiente nodo | No asumir que otro agente ejecutó algo sin evidencias |
| Cloud Code | Desarrollar, ejecutar y depurar aplicaciones cloud-native; configurar Cloud Run/Kubernetes/GKE y servicios de Google Cloud | No autoriza despliegue, cambios de proyecto, facturación ni producción |
| Gemini Code Assist/Gemini CLI | Pair programming, explicaciones, generación asistida, revisión localizada y tareas del ecosistema Google | No debe editar la misma rama simultáneamente con otro agente |
| Antigravity | Tareas agentic de varios pasos, navegador, UI, artefactos, ejecución asíncrona y agentes paralelos | Usar proyecto/rama/worktree aislado; revisar diff y artefactos antes de integrar |

Cloud Code es un entorno y una capa de integración; no es otro agente cuando se usa Gemini Code Assist dentro de él.

## Regla de coordinación

Usar todas las herramientas juntas solo con funciones diferenciadas:

- un coordinador mantiene el objetivo, el grafo y la rama de integración;
- un único ejecutor escribe cada archivo o funcionalidad;
- los revisores trabajan en modo lectura o en un worktree/rama separada;
- cada entrega devuelve diff, pruebas, riesgos y evidencias;
- integrar solo después de revisar y verificar.

Nunca permitir que dos agentes escriban simultáneamente en el mismo archivo o rama.

## Enrutamiento práctico

- **Producto, dominio, contratos e integración general:** Codex coordina; terminal o aplicación local ejecuta.
- **Cloud Run, Kubernetes, GKE, Skaffold y APIs de Google Cloud:** Cloud Code es el entorno preferido; Gemini puede ayudar dentro del IDE.
- **Investigación de código, segunda opinión o revisión de una función:** Gemini en modo revisión, sin autoridad de integración.
- **UI, navegador, capturas y flujos completos:** Antigravity en rama/worktree aislado, con artefactos verificables.
- **Release, producción, migraciones y secretos:** solo después de una puerta explícita, revisión independiente y evidencias operativas.

## Secuencia recomendada

`IDENTIFICAR → ELEGIR ENTORNO → DEFINIR RESPONSABLE → EJECUTAR → PROBAR → REVISAR → INTEGRAR`

Referencias oficiales: [Cloud Code](https://cloud.google.com/code), [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/use-agentic-chat-pair-programmer), [Google Antigravity](https://www.antigravity.google/docs).
