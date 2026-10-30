[English](README.en.md) · [Português (Brasil)](../README.md) · **Español**

# Engenharia Cadu

**De la idea a la entrega. Sin perder el rumbo.**

Convierte tu visión de negocio en un producto que puedas comprender, revisar y mejorar. Una forma de trabajar con agentes de IA: decisiones antes de implementar, contexto que sobrevive a la sesión y evidencia antes de dar algo por terminado.

Tú aportas el problema, el briefing y las referencias. El método organiza la siguiente decisión. El agente ejecuta dentro del alcance autorizado. El proyecto conserva los requisitos, el código y las pruebas de lo realizado.

[INICIAR UN PRODUCTO →](../p/P01.md) · [ORGANIZAR UN PROYECTO EXISTENTE](https://github.com/carlosemox/engenharia-cadu-adocao) · [PREPARAR EL ENTORNO](../p/P07.md) · [ABRIR EL SITIO](https://carlosemox.github.io/engenharia-cadu/es/)

Codex como principal · colaboración selectiva · diseño desde el briefing · economía de contexto · seguridad por etapas.

> La presentación está disponible en tres idiomas. El portugués de Brasil es la base editorial de Engenharia Cadu. Los procedimientos y las guías conservan sus idiomas actuales; el prompt universal de seguridad S01 está en inglés. Elegir un idioma aquí no traduce ni modifica automáticamente los comandos.

<!-- section:historia -->
## 00 / Una idea no debería perderse entre conversaciones

El proyecto empieza con una visión clara. Después llegan referencias, pantallas, bibliotecas, integraciones y nuevas decisiones. El código crece. Pero cuando termina la sesión o toma el relevo otra herramienta, vuelve la pregunta: **¿qué está decidido, qué funciona realmente y por dónde seguimos?**

Engenharia Cadu se estructura para afrontar ese problema: dar un lugar a las decisiones y un camino al desarrollo. No te pide que descartes lo que ya construiste. Pide comprender la intención, delimitar los cambios y poder comprobar cada entrega.

La propuesta no consiste en producir documentos por obligación. Consiste en convertir conversaciones en conocimiento útil, ideas en requisitos y tareas en resultados verificables. Una misma filosofía para empezar de cero, recuperar proyectos y desarrollar capacidades reutilizables.

**Tu negocio define el producto. La ingeniería organiza el trabajo. La herramienta no decide por sí sola qué debe ser tu empresa.**

<!-- section:comecar -->
## 01 / Empieza donde estás

| Tu situación | Entrada | Primer resultado |
|---|---|---|
| Tengo una idea o un briefing | [P01 — Descubrimiento del producto](../p/P01.md) | Entendimiento compartido, carencias relevantes y dirección para la primera versión. |
| Ya existe una aplicación | [Adopción de proyectos](https://github.com/carlosemox/engenharia-cadu-adocao/blob/main/read.md) | Diagnóstico del proyecto y plan revisable antes de cambiar código, estructura o datos. |
| Necesito preparar el equipo | [P07 — Entorno y capacidades](../p/P07.md) | Inventario de lo disponible y configuración de lo autorizado. |
| Necesito una tarea específica | [P00 — Elegir el camino](../p/P00.md) | El procedimiento pertinente, sin ejecutar toda la metodología. |

### Proyecto nuevo: el briefing es un punto de partida, no trabajo perdido

Pega el texto en la conversación del agente y describe el producto en la segunda línea. Si ya tienes un briefing, incorpora su texto o archivo en esa misma conversación.

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P01.md
Proyecto: [nombre, problema, público, recorrido principal y restricciones]. Aprovecha mi briefing, valida solo las carencias y conduce las siguientes etapas autorizadas en CONTINUO_SUPERVISIONADO. Responde en español.
```

Empezar por P01 no significa repetir todas las preguntas. El agente aprovecha decisiones e investigaciones válidas, aclara lo que falta y encamina el trabajo. No omite el descubrimiento solo porque encuentra un archivo llamado briefing.

### Proyecto existente: primero comprender, después cambiar

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu-adocao/main/read.md
Comprende este proyecto, concilia briefing, PRD, TRD y flujos, y presenta el Diagnóstico del Proyecto y el Plan de Adopción antes de modificar código, archivos o bases de datos. Responde en español.
```

Debes poder ver qué pretende hacer el producto, qué está implementado, qué se ha comprobado y qué sigue siendo desconocido. Se preservan la arquitectura útil, la identidad, los contratos y el trabajo local. Una reescritura o migración no debe disfrazarse de organización.

### Entorno: configurar no es suponer

```text
Read https://raw.githubusercontent.com/carlosemox/engenharia-cadu/main/p/P07.md
Haz un inventario del entorno y prepara solo las configuraciones autorizadas para mi proyecto. Distingue instalado, configurado, accesible y verificado. Responde en español.
```

Estos textos son instrucciones para un agente, no comandos del shell. La lectura, la edición y la ejecución dependen de las herramientas y los permisos disponibles. Ninguno de estos accesos publica automáticamente tu aplicación.

<!-- section:metodo -->
## 02 / Da forma al producto antes de ampliar el código

La ingeniería parte de la pregunta que importa al negocio: **¿quién necesita hacer qué, en qué situación y con qué resultado?** La respuesta orienta el alcance, la interfaz, los datos y la operación.

| Entregable | Para qué sirve |
|---|---|
| Briefing y alcance | Definir problema, público, valor, primera versión, restricciones y exclusiones. |
| PRD — requisitos del producto | Especificar comportamientos, reglas, permisos, excepciones y criterios de aceptación. |
| Flujos y sistema de diseño | Definir recorridos coherentes, componentes, respuesta de la interfaz y accesibilidad. |
| TRD — diseño técnico | Delimitar arquitectura, datos, contratos, integraciones y recuperación. |
| Plan por incrementos | Elegir unidades útiles, dependencias, responsables y verificaciones. |

**El diseño no es decoración añadida al final.** La dirección comienza en el briefing (D0), se convierte en reglas y componentes durante la especificación (D1) y se comprueba en la interfaz implementada (D2). Una pantalla atractiva que no resuelve el recorrido aún no completa la tarea.

Las referencias del mercado ayudan a decidir; no aprueban funcionalidades automáticamente. Estudiar un producto, integrar su API y reutilizar código con licencia son decisiones distintas. Registra fuentes y limitaciones, y construye una propuesta propia, adecuada a tu operación.

<!-- section:integracoes -->
## 03 / Elige las dependencias antes de depender de ellas

Clases en directo, pagos, autenticación, mensajes y almacenamiento no deben aparecer como sorpresas a mitad de la implementación. Primero definimos la capacidad necesaria. Después comparamos **construir, reutilizar, contratar, integrar o posponer**.

El [P08](../p/P08.md) separa las herramientas de desarrollo de los servicios que forman parte del producto. Para cada servicio: requisitos, contrato, datos compartidos, acceso, coste verificado o pendiente, límites, alternativa ante fallos y condiciones de sustitución.

Por ejemplo, una plataforma educativa puede gestionar matrículas y agenda mientras un servicio externo realiza la clase. La integración puede ser la solución inicial o seguir siendo la mejor opción. Tener infraestructura propia no es un destino obligatorio.

Supabase puede formar parte de la arquitectura cuando se elija. Eso no autoriza sustituir la autenticación, recrear bases de datos ni migrar información existente. El framework, la base de datos y el ORM responden a las necesidades y decisiones del proyecto, no a una tecnología impuesta por la biblioteca.

<!-- section:agentes -->
## 04 / Un coordinador. Colaboración con responsabilidad.

**Codex es el ejecutor principal del método.** Antigravity, Gemini CLI y OpenCode son colaboradores posibles, elegidos según la tarea y las capacidades realmente disponibles. No es obligatorio abrir cuatro agentes para resolver un cambio sencillo.

Cada delegación lleva un objetivo, contexto suficiente, archivos y recursos permitidos, dependencias, criterios de aceptación y formato de respuesta. Los recursos compartidos tienen un responsable. Los revisores trabajan en lectura; el coordinador comprueba la integración.

Producto, arquitectura, diseño, frontend, backend, calidad, GUARDIAN, SENTINEL y release son responsabilidades documentadas, no un equipo instalado automáticamente. Una skill incluida en un catálogo todavía necesita procedencia, licencia, compatibilidad y una prueba en el cliente elegido.

[Conocer los roles](../agentes/README.md) · [Seleccionar capacidades](../catalogo/README.md) · [Entender los clientes](../integracoes/CLIENTES.md)

<!-- section:continuidade -->
## 05 / La siguiente etapa no necesita otro comando pegado

En **CONTINUO_SUPERVISIONADO**, el coordinador termina la fase, verifica la entrega, la seguridad y el backup pertinente, registra el estado y carga el siguiente procedimiento autorizado. La entrevista sigue siendo interactiva. Las decisiones importantes siguen en tus manos.

```text
Comprender → especificar → preparar → implementar → probar → revisar → validar
                          ↑                           ↓
                          └──── corregir y verificar ─┘
```

P13, P14 y P15 forman ciclos por incremento. P17 contempla una misión prolongada cuando existe un supervisor y se han comprobado sus condiciones; no es una etapa obligatoria después de cada entrega. Las especializaciones se activan por necesidad, no por su número en la lista.

Un fallo bloqueante, una decisión pendiente, un riesgo grave, una protección indispensable ausente o un límite alcanzado detienen la acción dependiente. El trabajo independiente ya autorizado puede continuar. El agente no inventa tareas para mantener ocupada la sesión.

**Un prompt no mantiene el equipo trabajando después de cerrar la sesión.** La autonomía prolongada requiere un proceso real, cola de tareas, límites, exclusividad, puntos de control, parada y recuperación probadas. [Reglas de continuidad](../politicas/CONTINUIDADE.md).

<!-- section:documentos -->
## 06 / Haz que el conocimiento sobreviva a la sesión

En nuestro método, harness engineering significa organizar el entorno de trabajo del agente: instrucciones localizables, fuentes claras, herramientas accesibles y resultados que puedan verificarse. El conocimiento importante permanece en el proyecto, no solo en la memoria de una conversación.

| Información | Dónde mantenerla |
|---|---|
| Cómo iniciar y ejecutar | README de la aplicación. |
| Qué debe hacer el producto | Briefing y PRD canónicos. |
| Cómo se conectan las partes | TRD, contratos y decisiones de arquitectura. |
| Cómo se utiliza el producto | Flujos y sistema de diseño. |
| Cómo debe trabajar el agente | AGENTS.md breve, con referencias a los detalles. |
| Qué cambió y cómo continuar | Evidencias, decisiones y traspaso de contexto pertinente. |

No es una estructura de carpetas obligatoria. En un proyecto existente, preserva documentos equivalentes y registra su correspondencia. Un cambio de comportamiento, esquema o comando debe actualizar su fuente responsable. No conviertas AGENTS.md en una enciclopedia.

El método público guarda recetas. Cada aplicación guarda su producto. La operación privada guarda perfiles y registros internos, nunca contraseñas o tokens en archivos Git. [Explorar las plantillas](../templates/README.md).

<!-- section:auditoria -->
## 07 / Seguridad al inicio, durante y antes de publicar

Una auditoría al final no sustituye las buenas decisiones del comienzo. La ingeniería incluye requisitos y amenazas desde el diseño, verificaciones durante los lotes y revisión del candidato antes de cada publicación.

| Hito | Qué debe examinarse |
|---|---|
| Inicio | Datos, identidad, permisos, exposición, límites de confianza y controles necesarios. |
| Durante | Cambios, componentes consumidores, secretos, dependencias, regresiones y usos permitidos y denegados. |
| Integración | Aislamiento entre módulos o clientes, reglas compartidas y efectos externos. |
| Antes de publicar | Hallazgos, cobertura, revisión, configuración y recuperación de la misma versión candidata. |

El **[S01](../modulos/seguranca/README.md)** conserva el prompt universal de auditoría. Sus modos son distintos: AUDIT examina; PLAN organiza las correcciones; FIX modifica solo el lote autorizado; VERIFY vuelve a comprobar. La campaña avanzada requiere una solicitud expresa. Las pruebas activas y producción tienen autorización propia.

Los ejemplos de hooks cubren inicio, cierre de módulo, salida de fase, integración, commit, push, pull request, pre-release y mantenimiento periódico. **Son ejemplos publicados, no hooks instalados en las aplicaciones.** El verificador de recibos comprueba registros; no es un escáner ni demuestra la veracidad de los resultados aportados.

Ninguna herramienta garantiza la ausencia de intrusiones. Una prueba ausente, un error, un timeout o evidencia antigua no son una aprobación. Los controles esenciales necesitan implementación real, revisión y mantenimiento. [Hooks y límites](../modulos/seguranca/hooks/README.md) · [Política de seguridad](../politicas/SEGURANCA_ENGENHARIA.md).

<!-- section:backup -->
## 08 / Preserva el trabajo. Demuestra que puedes recuperarlo.

El destino definido es `Projetos 2026/Backup/<nombre-del-proyecto>`. Proteger exige más que crear una carpeta: cobertura explícita, generaciones identificadas, integridad comprobada y recuperación probada para el alcance pertinente.

Archivos de trabajo y cambios locales, historial Git, bases de datos, uploads y secretos son clases distintas. Un ZIP del código no demuestra que todas estén protegidas. Las credenciales requieren protección específica; no deben incluirse en un archivo común. El método no autoriza eliminar automáticamente generaciones anteriores.

El backup debe preceder a cambios arriesgados y acompañar entregas con nuevos artefactos. Si la protección indispensable no está comprobada, la acción dependiente no avanza. **La integración automática con Drive debe configurarse y probarse en cada entorno; publicar esta página no la activa.** [Política y cobertura](../politicas/BACKUP_DRIVE.md).

<!-- section:economia -->
## 09 / Ahorra contexto, no criterio

La política de economía en Astra es una disciplina de trabajo: cargar solo lo que exige la tarea, reutilizar decisiones válidas, usar scripts para verificaciones repetitivas y delegar cuando exista un beneficio concreto.

El detalle sigue disponible en la fuente. Quien implementa recibe los requisitos y contratos pertinentes, no todos los documentos. Quien revisa recibe el candidato y su contexto, no el historial completo. Esperar al CI no requiere llamadas sucesivas al modelo.

No prometemos un porcentaje de ahorro. Tokens, coste y retrabajo deben medirse cuando sean observables. No hay cambios silenciosos de modelo, proveedor, autenticación o facturación. El objetivo es **menor coste por entrega aceptada**, incluidas las pruebas y correcciones necesarias. [Política de economía](../politicas/ECONOMIA_ASTRA.md).

[Biblioteca interactiva en portugués](https://carlosemox.github.io/engenharia-cadu/biblioteca.html)

<!-- section:prompts -->
## 10 / Un comando para cada responsabilidad

Utiliza la biblioteca completa como mapa, no como un texto para pegar entero. Los identificadores permanecen estables; cada procedimiento indica finalidad, entradas, límites, entregable y criterios de conclusión.

| Prompt | Responsabilidad |
|---|---|
| [P00](../p/P00.md) | Elegir el camino y la siguiente acción. |
| [P01](../p/P01.md) | Comprender el producto y validar el briefing inicial. |
| [P02](../p/P02.md) | Investigar hipótesis, referencias y viabilidad. |
| [P03](../p/P03.md) | Consolidar primera versión, alcance y exclusiones. |
| [P04](../p/P04.md) | Definir requisitos, reglas y criterios de aceptación. |
| [P05](../p/P05.md) | Especificar flujos, experiencia y sistema de diseño. |
| [P06](../p/P06.md) | Definir arquitectura, datos, contratos y seguridad. |
| [P07](../p/P07.md) | Inventariar y preparar equipo, cuentas y clientes. |
| [P08](../p/P08.md) | Seleccionar agentes, herramientas, servicios y API. |
| [P09](../p/P09.md) | Preparar la base y el repositorio del producto nuevo. |
| [P10](../p/P10.md) | Configurar entornos, CI e integraciones aprobadas. |
| [P11](../p/P11.md) | Comprobar las condiciones para el siguiente trabajo. |
| [P12](../p/P12.md) | Convertir requisitos en tareas delimitadas. |
| [P13](../p/P13.md) | Implementar y verificar una tarea. |
| [P14](../p/P14.md) | Revisar de forma independiente según riesgo y evidencia. |
| [P15](../p/P15.md) | Validar recorridos e integraciones en staging. |
| [P16](../p/P16.md) | Preparar o ejecutar una publicación autorizada. |
| [P17](../p/P17.md) | Conducir una misión prolongada con supervisor comprobado. |
| [P18](../p/P18.md) | Retomar sin perder ni duplicar trabajo. |
| [P19](../p/P19.md) | Priorizar proyectos activos o detenidos. |
| [P20](../p/P20.md) | Diagnosticar un proyecto sin reescribirlo. |
| [P21](../p/P21.md) | Corregir y adoptar el método de forma incremental. |
| [P22](../p/P22.md) | Auditar agentes, skills y paquetes antes de activarlos. |
| [P23](../p/P23.md) | Estructurar módulos reutilizables con consumidores reales. |
| [P24](../p/P24.md) | Evaluar mejoras del harness sin debilitar controles. |
| [P25](../p/P25.md) | Desarrollar capacidades financieras auditables. |
| [P26](../p/P26.md) | Organizar contenido y publicación por marca. |
| [P27](../p/P27.md) | Crear capacidades de vídeo programático. |
| [P28](../p/P28.md) | Estructurar capacidades de ingeniería y obras. |

<!-- section:capacidades -->
## 11 / Adopta lo necesario. Preserva lo que funciona.

El catálogo reúne posibilidades; no es una instalación masiva. Cada skill, biblioteca o integración debe elegirse por necesidad, procedencia, licencia, compatibilidad, coste y validación. Consultar documentación actual no autoriza enviar código o información privada a terceros.

| Lugar | Responsabilidad |
|---|---|
| Equipo y cliente | Runtime, herramientas, autenticación e integraciones globales autorizadas. |
| Aplicación | Código, dependencias, lockfiles, documentación, pruebas y configuración específica. |
| Central pública | Método, procedimientos, plantillas y referencias publicables. |
| Operación privada | Perfiles, autorizaciones, destinos y evidencias internas, sin secretos en Git. |

Los proyectos existentes preservan sus tecnologías, base de datos, contratos y equivalentes funcionales. Los cambios incompatibles requieren una decisión propia. Los monorepos necesitan inventariar límites y recursos compartidos. Los servicios nuevos solo entran cuando tienen una función concreta en el producto.

<!-- section:operacao -->
## 12 / Distingue lo publicado de lo que necesita comprobarse

**Un documento disponible no equivale a una instalación concluida. Una prueba local no equivale a una integración en producción.** Esta central ofrece recetas, plantillas y ejemplos; cada entorno debe demostrar su funcionamiento.

| Capacidad | Estado y condición |
|---|---|
| P00–P28 y S01 | Biblioteca publicada; su eficacia en tu proyecto requiere ejecución y evaluación. |
| Continuidad entre etapas | Instrucción del coordinador; depende de sesión, contexto y autorizaciones. |
| Hooks y controles de seguridad | Ejemplos y políticas; instalación y bloqueos reales deben probarse. |
| Backup automático | Política definida; conexión, cobertura y restauración requieren implantación. |
| Misión de 24 horas | Requiere supervisor, límites, recursos y recuperación comprobados. |
| Presentación trilingüe | Presentación traducida; guías y comandos enlazados conservan sus idiomas actuales. |

Sin acceso al entorno, el agente puede explicar y especificar, pero no comprobar una configuración. Los informes deben distinguir PASS, FAIL, NOT_RUN y no aplicable, con justificación. Seguridad no significa prometer invulnerabilidad.

[Estado operativo](../OPERACAO.md) · [Mapa de la central](../MAPA_DA_CENTRAL.md) · [Escenarios de evaluación](../avaliacoes/CENARIOS.md) · [Validación S01](../modulos/seguranca/validacao/RESULTADOS.md)

<!-- section:evolucao -->
## 13 / Construye una base capaz de evolucionar

Cuando un proyecto revela una mejora, extrae la parte reutilizable, elimina los datos internos, comprueba la licencia y revisa antes de incorporarla al método público. Las actualizaciones permanecen en sus fuentes oficiales; los temas nuevos reciben un lugar propio. La operación privada no se replica automáticamente.

Engenharia Cadu se inspira en la organización de **[Vibe Coding Toolkit, de Matheus Gomes](https://github.com/soumatheusgomes/vibe-coding-toolkit)** y adapta esa referencia a las decisiones de esta central. No se presume afiliación ni respaldo. Se conserva el aviso de licencia del toolkit; los demás componentes mantienen sus propios términos. La central no hereda automáticamente una licencia MIT para todo su contenido. [Licencias y atribuciones](../LICENCIAMENTO.md).

El mejor punto de partida es el siguiente resultado útil: comprender el producto, recuperar un recorrido o preparar una base verificable. Elige la entrada, aporta tu contexto y mantén visibles las decisiones importantes.

**Define con intención. Construye con contexto. Evoluciona con evidencia.**

[EMPEZAR POR P01 →](../p/P01.md) · [RECUPERAR UN PROYECTO](https://github.com/carlosemox/engenharia-cadu-adocao) · [REPORTAR UN PROBLEMA](https://github.com/carlosemox/engenharia-cadu/issues)
