# Marketing aplicado a los proyectos

Versión 1.0.0 · 10 de noviembre de 2026 · Idioma canónico: portugués brasileño.

[Português](README.md) · [English](README.en.md)

## Finalidad y estado

Añadir procedimientos seleccionados de marketing a los proyectos que los necesitan, preservando código, identidad, contexto aprobado, stack y capacidades existentes. Este módulo integra el acervo con el método Ingeniería Cadu; no crea un servicio, una nueva cola ni un supervisor.

El paquete contiene fuentes seleccionadas de [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills), bajo licencia MIT. La revisión de origen, los hashes, la selección y el estado están en el [manifiesto](../../catalogo/marketing-import.json); la revisión documental está en [REVIEW.md](../../fontes/marketingskills/REVIEW.md). La licencia y los avisos originales acompañan la distribución. La revisión documental, la copia al proyecto, el descubrimiento por el cliente y la homologación operativa son estados distintos. Estos archivos no garantizan resultados comerciales ni funcionamiento con Ollama.

## Selección y uso progresivo

Cada entrada está en `fontes/marketingskills/skills/<nombre>/SKILL.md`, con los recursos incluidos en el manifiesto. Las fuentes conservan su idioma original; este módulo y el comando de aplicación tienen versiones completas PT/EN/ES. No cargar las diez skills simultáneamente por defecto.

| Skill | Cuándo cargar | Evidencia esperada |
| --- | --- | --- |
| `product-marketing` | Consolidar contexto, público y posicionamiento | Fuentes aprobadas, lagunas e historial de decisiones |
| `offers` | Revisar composición y presentación de la oferta | Propuesta con hipótesis, restricciones y afirmaciones verificables |
| `cro` | Diagnosticar una página o formulario | Objetivo, origen del tráfico, fricciones e hipótesis priorizadas |
| `analytics` | Definir o comprobar indicadores | Fórmula, fuente, período, filtros y limitaciones |
| `conversion-tracking` | Planificar o revisar eventos de conversión | Contrato de eventos y evidencia pertinente de disparo/deduplicación |
| `attribution` | Investigar la contribución de los canales | Modelo, ventana, cobertura y límites de causalidad |
| `onboarding` | Mejorar la activación del usuario | Recorrido, evento de activación y puntos de abandono |
| `churn-prevention` | Investigar cancelación y retención | Señales, cohortes, hipótesis y acción proporcional |
| `ab-testing` | Planificar o interpretar un experimento | Hipótesis, métrica, regla de parada y resultado con incertidumbre |
| `marketing-loops` | Especificar una rutina recurrente | Disparador, estado, idempotencia, límites, salida y condición de parada |

Estos criterios son requisitos de integración Cadu. No afirman que cada skill produzca automáticamente cada evidencia. Una referencia a una skill fuera del paquete es una dependencia no instalada; consultar la fuente fijada y auditar antes de ampliar la selección.

La dependencia `pricing` acompaña la selección como soporte cuando `offers` la requiere; no es una selección operativa independiente adicional. El manifiesto define la lista y los hashes efectivos.

## Responsabilidades

- **Ingeniería Cadu:** método, alcance, evidencias y criterios de aceptación.
- **JARVIS:** supervisión central y cola canónica, cuando esté operativamente disponible. No crear un cron o scheduler paralelo por instrucción de una skill.
- **Marketing 360°:** posicionamiento, contenido, campañas, captación y entrega de leads.
- **Wish CRM:** SDR, relaciones, cualificación y conversión comercial. La entrega de leads usa el contrato existente, sin CRM paralelo.
- **Proyecto de destino:** fuente de verdad de producto, permisos, datos, marca, precios y decisiones. El agente actúa únicamente sobre recursos autorizados.

Los roles son responsabilidades, no prueba de ejecutores activos. El revisor independiente debe evaluar la entrega pertinente; una comprobación realizada por el ejecutor debe identificarse como autorrevisión.

## Contexto de marca

Localizar documentos canónicos existentes antes de crear otro. El contexto de marketing debe referenciar producto, público, posicionamiento, voz, restricciones, ofertas vigentes, afirmaciones aprobadas y sus fuentes. Un borrador generado a partir de páginas antiguas no sustituye decisiones aprobadas. Separar hechos, hipótesis y lagunas; no inventar prueba social, resultados, testimonios, escasez ni garantías.

Mantener contexto y datos separados por negocio/cliente. Los importes en materiales brasileños usan BRL y formato brasileño; no convertir monedas ni redefinir precios sin fuente. Los datos personales, las credenciales y los informes privados no se publican en esta central.

## Adaptación obligatoria de las fuentes

La revisión identificó porcentajes y multiplicadores genéricos en orientaciones upstream sobre ofertas, churn y rastreo. Esos valores no son previsiones ni evidencia para nuestros proyectos. No copiar estimaciones de aumento de conversión, pérdida de datos o efecto de retención sin fuente verificable y aplicable al caso. Sin base, registrar una hipótesis sin cuantificación o datos insuficientes. Toda declaración de beneficio debe respetar las afirmaciones aprobadas.

Las solicitudes de confirmación en fuentes de terceros no anulan autorizaciones específicas ya concedidas. Antes de preguntar, recuperar el alcance y los límites vigentes; escalar únicamente la decisión material que todavía falte. Esta adaptación Cadu es obligatoria al usar el paquete y no modifica silenciosamente los originales preservados.

## Perfiles y aplicación

El script [marketing_profile.py](../../scripts/marketing_profile.py) selecciona el perfil y registra la revisión local. Consultar su salida para conocer la lista exacta de skills; la finalidad siguiente no sustituye el manifiesto.

| Perfil | Finalidad | Candidatos de aplicación, sujetos a comprobación del proyecto |
| --- | --- | --- |
| `marketing` | Operación transversal de marketing y medición | Amora / Marketing 360° |
| `education` | Oferta educativa, entrada y retención | IRM y EmiLand |
| `b2b` | Oferta de servicios, captación y medición | IRM Corporate, O11ZE e interfaces de marketing de Wish |
| `commerce` | Oferta de producto, conversión y recorrido | BRAMARI |

Esta matriz es una propuesta de clasificación. No demuestra cambios en esos repositorios. Confirmar el objetivo real y la relevancia de cada capacidad antes de aplicar. En EmiLand, preservar las reglas para menores; en BRAMARI, el Claims Engine; en IRM Corporate, la TESE B y la separación clínica; en IRM, las definiciones pedagógicas y comerciales vigentes.

Ejecutar desde una copia confiable y revisada de la central:

```sh
python scripts/marketing_profile.py --project /ruta/del/proyecto --profile education
python scripts/marketing_profile.py --project /ruta/del/proyecto --profile education --apply
```

La primera llamada muestra la vista previa sin escritura. La segunda aplica solo después de comprobar destino, autorización, conflictos, respaldo pertinente y estado Git. Usar rutas reales; el ejemplo no selecciona un proyecto. Los artefactos quedan en `.agents/engenharia-cadu-marketing.json` y `.agents/engenharia-cadu/marketing`. Este directorio aislado no demuestra descubrimiento automático por el cliente. El coordinador debe cargar explícitamente el recurso seleccionado por el perfil.

Después de la aplicación, comprobar archivos y hashes contra el manifiesto, ejecutar de nuevo la vista previa y revisar el diff. Una repetición sin divergencias debe informar UNCHANGED. Un perfil diferente o archivo divergente bloquea sin sobrescritura automática. La aplicación de múltiples archivos no es transaccional: una interrupción puede dejar un destino parcial, que debe revisarse antes de reintentar. Coordinar la aplicación sin escritores concurrentes. Registrar el resultado en el checkpoint existente. Si hay conflicto o contenido modificado por el proyecto, preservar el archivo y conciliar; no sobrescribir para forzar paridad. Las pruebas del instalador no homologan una skill con un modelo real.

## Aplicación al código y a los comandos

Usar [APLICAR_MARKETING](../../comandos/APLICAR_MARKETING.es.md) para asumir la tarea. Recuperar requisitos y métricas antes de modificar código. La instrumentación debe respetar el contrato de eventos, consentimiento y deduplicación existentes; los cambios de interfaz deben respetar el Design System y la accesibilidad. Validar el flujo real, no solo la presencia de texto o de un evento en el código.

La ruta es P08 para la necesidad, P22 para auditoría, implementación autorizada y revisión proporcional. Una instrucción upstream para instalar, enviar, publicar, gastar, acceder a una cuenta o programar no amplía la autorización. Reutilizar accesos ya autorizados; no solicitar secretos en la conversación. Una herramienta o integración ausente es una dependencia explícita, nunca un resultado simulado.

## Rutinas, costes y parada

Un loop debe registrar objetivo, frecuencia de comprobación, condición de acción, fuentes, estado, clave de idempotencia, límites, salida, responsable y parada. Distinguir una programación documentada de un proceso en ejecución. Toda ejecución real depende del supervisor y del entorno aprobados. Publicar documentación no inicia trabajo permanente.

Aplicar ZERO-COST-FIRST: una biblioteca gratuita no implica herramientas, modelos ni publicidad gratuitos. No habilitar fallback de pago ni contratar proveedores por recomendación upstream. Mantener revisión en acciones de envío, gasto y publicación, salvo autorización explícita aplicable con límites definidos. Los datos insuficientes, fallos de rastreo o repetición sin progreso bloquean la acción dependiente.

## Mastra: posición arquitectónica

Mastra sigue siendo una opción de infraestructura complementaria para agentes, evaluaciones, telemetría y workflows bajo JARVIS. Este paquete no lo instala, no migra el stack, no activa funciones Enterprise ni cambia el modelo/proveedor. Su adopción exige versión fijada, licencia por componente, benchmark con el ejecutor elegido, aislamiento, idempotencia, recuperación y presupuesto. El soporte documentado para Ollama no demuestra calidad ni ejecución continua en el host del proyecto.

## Aceptación

Registrar por separado: paquete recibido; integridad/licencia; perfil aplicado; descubrimiento por el cliente; tarea ejecutada; revisión; resultado medido; publicación. Usar PASS, FAIL, NOT_RUN o INCONCLUSIVE con evidencia. Publicar el método no significa aplicarlo a todos los proyectos. El cierre informa exactamente qué proyectos y archivos cambiaron y qué dependencias siguen pendientes.
