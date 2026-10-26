# Entorno de trabajo colaborativo

Este documento describe cómo se organizó el repositorio, qué ramas se usaron, con qué
criterio se escribieron los commits y cómo se gestionó el Pull Request y el tablero. Es la
evidencia de la consigna de trabajo colaborativo y el respaldo de la sección 2 del
documento de la Entrega 4.

## Repositorio

- **URL:** https://github.com/imsantiagodominguez/tpi-latorre-ascensores
- **Rama estable:** `main`
- **Pull Requests:** https://github.com/imsantiagodominguez/tpi-latorre-ascensores/pulls
- **Tablero:** https://github.com/users/imsantiagodominguez/projects/3/views/1

El repositorio es público y contiene la documentación técnica, las figuras en PNG y SVG,
los scripts que las generan y el PDF de la entrega. La rama `main` es la versión estable:
no recibe commits directos de trabajo, sino integraciones revisadas.

## Estructura

```
tpi-latorre-ascensores/
├── README.md                     presentación, alcance y declaración de IA
├── docs/
│   ├── 01-bpmn/                  modelado, figuras y reglas de negocio
│   ├── 02-backlog/               tres historias de usuario
│   ├── 03-control/               indicadores y plan de pruebas
│   ├── 04-ia/                    declaración ampliada de uso de IA
│   └── 05-repositorio/           este documento
├── scripts/                      generación reproducible de las figuras
└── entregas/                     PDF de la Entrega 4
```

Cada carpeta de `docs/` corresponde a una unidad de trabajo y a una rama. Así, el
historial del repositorio permite reconstruir qué se hizo, en qué orden y con qué
justificación.

## Estrategia de ramas

| Rama | Contenido | Integración |
|---|---|---|
| `main` | Versión estable: README, `.gitignore` y declaración de IA | Base del repositorio |
| `feature/bpmn-facturacion` | `docs/01-bpmn/` y `scripts/` | PR de BPMN |
| `feature/backlog-historias` | `docs/02-backlog/` | PR de backlog |
| `docs/indicadores-control` | `docs/03-control/` | PR de control |
| `feature/entrega-4` | PDF de la entrega y esta documentación | PR de entrega |

Cada rama parte de `main`, agrupa una sola unidad de trabajo y se integra mediante un
Pull Request. La rama de BPMN es la principal porque concentra el modelado, las figuras y
la revisión de notación; las demás agregan el backlog, el control y el cierre documental.

| PR | Rama | Contenido | Estado |
|---|---|---|---|
| #4 | `feature/bpmn-facturacion` | BPMN, figuras PNG/SVG y script reproducible | Abierto; revisión de pares pendiente |
| #5 | `feature/backlog-historias` | Tres historias de usuario y trazabilidad | Mergeado |
| #6 | `docs/indicadores-control` | Indicadores y plan de pruebas | Mergeado |
| #7 | `feature/entrega-4` | PDF de la entrega y esta documentación | Mergeado |

## Convención de commits

Se usa una adaptación de Conventional Commits: tipo, alcance entre paréntesis y un objeto
concreto en infinitivo. El mensaje explica qué cambia, no solo qué archivo se tocó.

| Tipo | Uso | Ejemplo |
|---|---|---|
| `docs` | Documentación, figuras y README | `docs(bpmn): agrega criterios de modelado y leyenda de notación` |
| `fix` | Corrección de un error de contenido o de notación | `fix(bpmn): corrige el cruce de un flujo de mensaje` |
| `build` | Scripts y herramientas de generación | `build: agrega script reproducible de diagramas` |
| `chore` | Mantenimiento del repositorio | `chore: actualiza .gitignore` |

Commits principales del historial:

1. `docs(bpmn): agrega criterios de modelado y leyenda de notación`
2. `docs(bpmn): incorpora diagramas de facturación y pago a proveedores`
3. `build: agrega script reproducible de diagramas`
4. `docs(backlog): incorpora las tres historias de usuario`
5. `docs(control): define indicadores y estándares de desempeño`
6. `docs(control): agrega plan de pruebas y registro de evidencias`
7. `docs(entrega): agrega el PDF de la Entrega 4`
8. `docs(repositorio): documenta ramas, commits, PR y tablero`

## Pull Request y revisión

El circuito es: rama → commits → push → Pull Request → revisión → merge. El PR describe
el alcance, las figuras o secciones afectadas, la lista de verificación y el vínculo con
la consigna. La revisión se registra como comentario en el PR, no por fuera del
repositorio.

Lista de verificación usada en la revisión:

- [ ] La rama parte de `main` y no mezcla unidades de trabajo.
- [ ] Los mensajes de commit describen el cambio.
- [ ] Los enlaces, figuras y tablas se visualizan correctamente.
- [ ] La numeración coincide con el documento de la Entrega 4.
- [ ] Las reglas de negocio citadas existen en `docs/01-bpmn/`.
- [ ] El estado del tablero coincide con el estado del PR.

La revisión de pares del PR de BPMN se realiza en la conversación del PR. La lista de
verificación incluye dos controles concretos: que ningún flujo de mensaje cruce las
etiquetas de los eventos y que todos los carriles —incluido el de Dirección— tengan al
menos una actividad. Al cierre de esta versión, el PR #4 permanece abierto para esa
revisión; las observaciones se resolverán en commits de la misma rama, de modo que la
revisión modifica el artefacto y queda registrada en el historial.

## Tablero

El tablero tiene tres columnas —«Por hacer», «En progreso» y «Listo»— y una tarjeta por
historia de usuario. La tarjeta se mueve cuando se abre la rama y cuando el PR se integra.

| Tarjeta | Estado | Criterio de salida | Evidencia |
|---|---|---|---|
| HU-01 · Registrar y consultar comprobantes | Listo | Alta y consulta con control de duplicados | Issue #1; PR #5; Figura 1.4.1 |
| HU-02 · Registrar cobros y actualizar saldos | En progreso | Imputación y recálculo verificados | Issue #2; PR #5; CP-04 a CP-06 |
| HU-03 · Alertas de morosidad y bloqueo | Por hacer | Consulta en menos de 3 segundos y bloqueo solo de trabajos no urgentes | Issue #3; indicadores y CP-08 a CP-10 |

Cada tarjeta incluye la historia en formato Como/quiero/para, sus criterios de aceptación,
la rama asociada y el enlace a la evidencia. El tablero es público para que la revisión
pueda hacerse sin pedir acceso.

## Declaración de uso de IA

La declaración completa está en el [README](../../README.md#declaración-de-uso-de-inteligencia-artificial)
y se amplía en [`docs/04-ia/declaracion-uso-ia.md`](../04-ia/declaracion-uso-ia.md). Resume
qué herramientas se usaron, para qué, qué prompts fueron representativos y qué
correcciones humanas se aplicaron. La IA se usó como apoyo de estructuración y redacción;
las decisiones de modelado y las reglas de negocio son propias.

## Trazabilidad de la Entrega 4

| Consigna | Artefacto | Dónde se verifica |
|---|---|---|
| 1. BPMN | Pools, lanes, compuertas y diccionario | `docs/01-bpmn/` y figuras 1.3.1 a 1.5.1 |
| 2. Repositorio | Ramas, commits, PR y tablero | Este documento y la pestaña Pull Requests |
| 3. Backlog | Tres historias con criterios de aceptación | `docs/02-backlog/` |
| 4. Control | Indicadores, pruebas y evidencias | `docs/03-control/` |

---

Santiago Dominguez · Comisión 10 · Organización Empresarial · UTN TUPAD
