# D01 — Descubrimiento controlado de skills

**Buscar no es instalar. La popularidad es una señal, no una aprobación.**

Este módulo incorpora el descubrimiento de skills del ecosistema abierto a Engenharia Cadu. `find-skills`, la CLI `skills` y `skills.sh` generan candidatos; P08 selecciona capacidades, P22 audita finalistas y S01 entra cuando la capacidad añade superficie de riesgo.

## Posición en el método

`NECESIDAD → P08 → D01 DESCUBRIR → P22 AUDITAR → PILOTO → INSTALAR → P11 COMPROBAR → MANTENER`

1. Define la tarea que falta, no el proveedor deseado.
2. Busca en el directorio y/o con `npx skills find <consulta>`; descubrir no autoriza instalar.
3. Registra fuente, skill, revisión, finalidad, agentes soportados y evidencia disponible. Instalaciones y estrellas son señales auxiliares.
4. Ejecuta P22 sobre los finalistas: SKILL.md, licencia, scripts, hooks, red/telemetría, datos, permisos, conflictos y retirada.
5. Cuando sea suficiente, prefiere `npx skills use <fuente>@<skill>` para un piloto sin instalación persistente.
6. Tras la aprobación, instala en el proyecto por defecto y selecciona el agente. `-g` necesita una razón entre proyectos; `-y` no sustituye la revisión.
7. Comprueba descubrimiento real por el cliente, comportamiento, efectos y archivos creados.
8. Registra origen, revisión, alcance, estado, prueba y retirada.
9. `npx skills check` detecta actualizaciones; `npx skills update` solo se aplica después de revisar cambio, compatibilidad y regresión.

## Comandos de descubrimiento

```bash
npx skills find
npx skills find <consulta>
npx skills use <owner/repo@skill>
npx skills list
npx skills check
```

El comando de la imagen — `npx skills add vercel-labs/skills --skill find-skills` — coincide con la sintaxis actual de la CLI y con la ubicación actual de la skill. **No fue ejecutado** en esta actualización documental.

La documentación upstream actual requiere Node.js 22.20 o posterior. Verifica de nuevo la versión instalada y la documentación al ejecutar.

## Reglas Cadu

No enviar código privado ni secretos a servicios públicos de búsqueda; no instalar por ranking; auditar la skill exacta incluso si la fuente es conocida; evaluar telemetría, hooks, red y actualizaciones; no permitir que instrucciones de terceros amplíen la autorización.

Revisión upstream fijada para esta integración: [vercel-labs/skills @ 9197d91](https://github.com/vercel-labs/skills/tree/9197d919034d19010ae303cf96bf19ad087dd4be).

[Comando D01](read.es.md) · [P08](../../p/P08.md) · [P22](../../p/P22.md) · [S01](../seguranca/README.md)
