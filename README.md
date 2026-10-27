# TPI Latorre Ascensores · Sistema de facturación y cuentas corrientes

Documentación técnica del Trabajo Práctico Integrador y Progresivo de **Organización
Empresarial** (UTN · TUPAD). El caso de estudio es **Latorre Ascensores**, empresa de
instalación, mantenimiento y reparación de ascensores, y el sistema modelado es la
aplicación que centraliza la **facturación y la gestión de cuentas corrientes** de
clientes y proveedores.

| | |
|---|---|
| **Alumno** | Santiago Dominguez (Comisión 10) |
| **Asignatura** | Organización Empresarial — UTN, TUPAD |
| **Docentes** | Gabriela Martínez · Noemí Andrea Ramos · Guillermo Miguel Carvajal |
| **Entrega** | N° 4 — Procesos, trabajo colaborativo y control integrador |

## Accesos

- **Repositorio:** https://github.com/imsantiagodominguez/tpi-latorre-ascensores
- **Tablero de gestión:** https://github.com/users/imsantiagodominguez/projects/3/views/1
- **Entrega 1 (PDF):** [`entregas/entrega-1-latorre-ascensores.pdf`](entregas/entrega-1-latorre-ascensores.pdf)
- **Entrega 2 (PDF):** [`entregas/entrega-2-latorre-ascensores.pdf`](entregas/entrega-2-latorre-ascensores.pdf)
- **Entrega 3 (PDF):** [`entregas/entrega-3-latorre-ascensores.pdf`](entregas/entrega-3-latorre-ascensores.pdf)
- **Entrega 4 (PDF):** [`entregas/entrega-4-latorre-ascensores.pdf`](entregas/entrega-4-latorre-ascensores.pdf)
- **Entrega Consolidada (PDF):** [`entregas/Entrega consolidada (E1-E2-E3-E4) de OE-version_final.pdf`](entregas/entrega-consolidada-(E1-E2-E3-E4)-de-OE-version_final.pdf)

## Qué contiene este repositorio

El repositorio no es un depósito de archivos: se usa con la misma lógica que un equipo
de desarrollo, con ramas secundarias, mensajes de commit descriptivos, Pull Requests y
revisión. La documentación está separada por consigna para que cualquier decisión se
pueda encontrar sin recorrer todo el historial.

```
tpi-latorre-ascensores/
├── README.md
├── .gitignore
├── docs/
│   ├── 01-bpmn/
│   │   ├── README.md
│   │   ├── figura-1-3-1-leyenda-bpmn.png
│   │   ├── figura-1-3-1-leyenda-bpmn.svg
│   │   ├── figura-1-4-1-bpmn-facturacion-cobro.png
│   │   ├── figura-1-4-1-bpmn-facturacion-cobro.svg
│   │   ├── figura-1-5-1-bpmn-proveedores-pagos.png
│   │   └── figura-1-5-1-bpmn-proveedores-pagos.svg
│   ├── 02-backlog/
│   │   └── historias-de-usuario.md
│   ├── 03-control/
│   │   ├── indicadores.md
│   │   └── plan-de-pruebas.md
│   │── 04-ia/
│   │   └── declaracion-uso-ia.md
│   └── 05-repositorio/
│       └── README.md
└── entregas/
    │── entrega-1-latorre-ascensores.pdf
    │── entrega-2-latorre-ascensores.pdf
    │── entrega-3-latorre-ascensores.pdf
    │── entrega-4-latorre-ascensores.pdf
    └── Entrega consolidada (E1-E2-E3-E4) de OE-version_final
```

Los diagramas se versionan en **PNG** —para insertarlos en el documento— y en **SVG**
—formato vectorial editable—, junto con el script que los genera. Guardar el script
permite reproducir una figura con una corrección mínima en lugar de redibujarla a mano.
El detalle del entorno de trabajo —ramas, commits, PR y tablero— está en
[`docs/05-repositorio/`](docs/05-repositorio/).

## Alcance del sistema

El sistema resuelve el circuito administrativo que hoy se lleva con planillas y
registros dispersos:

- **Clientes:** registrar facturas y recibos, consultar el historial por mes y año,
  calcular saldos pendientes y señalar facturas vencidas.
- **Proveedores:** registrar facturas recibidas, consultar el saldo a pagar y apoyar la
  priorización de pagos.
- **Operaciones:** consultar el estado de morosidad antes de autorizar tareas no urgentes.
- **Dirección:** consultar saldos a cobrar y a pagar, identificar morosidad y priorizar
  proveedores críticos.

No se modela la ejecución técnica del servicio —que se resuelve en el terreno— sino el
circuito documental y financiero que la rodea.

## Modelado de procesos (BPMN)

Los dos procesos se modelaron en BPMN 2.0 con **Pools** para los actores externos
(Cliente y Proveedor) y **Lanes** para los roles internos (Administración, Operaciones y
Dirección). Las excepciones se resolvieron con compuertas XOR etiquetadas.

| Figura | Proceso | Archivos |
|---|---|---|
| 1.3.1 | Leyenda de la notación utilizada | [PNG](docs/01-bpmn/figura-1-3-1-leyenda-bpmn.png) · [SVG](docs/01-bpmn/figura-1-3-1-leyenda-bpmn.svg) |
| 1.4.1 | Facturación y cobro a clientes | [PNG](docs/01-bpmn/figura-1-4-1-bpmn-facturacion-cobro.png) · [SVG](docs/01-bpmn/figura-1-4-1-bpmn-facturacion-cobro.svg) |
| 1.5.1 | Facturación y pago a proveedores | [PNG](docs/01-bpmn/figura-1-5-1-bpmn-proveedores-pagos.png) · [SVG](docs/01-bpmn/figura-1-5-1-bpmn-proveedores-pagos.svg) |

Reglas de negocio modeladas: listado de pendientes de facturación (RN-01), control de
duplicados (RN-02), datos mínimos del comprobante (RN-03), imputación explícita de pagos
(RN-04), recálculo automático del saldo (RN-05), bloqueo solo de trabajos no urgentes
(RN-06), priorización de proveedores críticos por Dirección (RN-07) y auditoría de cambios
(RN-08).

## Backlog ágil

El backlog se gestiona en el [tablero del proyecto](https://github.com/users/imsantiagodominguez/projects/3/views/1)
con las columnas «Por hacer», «En progreso» y «Listo». Las tres historias se desprenden
del proceso modelado: no son funcionalidades inventadas, sino pasos del diagrama que el
sistema debe sostener.

| ID | Historia | Estado |
|---|---|---|
| HU-01 | Registrar y consultar comprobantes | Listo |
| HU-02 | Registrar cobros y actualizar saldos | En progreso |
| HU-03 | Alertas de morosidad y bloqueo de trabajos no urgentes | Por hacer |

El detalle con criterios de aceptación, reglas asociadas y evidencias está en
[`docs/02-backlog/historias-de-usuario.md`](docs/02-backlog/historias-de-usuario.md).

## Control y auditoría

| Indicador | Estándar |
|---|---|
| Tiempo de registro | Registrar un comprobante en ~1 minuto |
| Velocidad de búsqueda | Encontrar comprobantes por mes y año en menos de 3 segundos |
| Exactitud de los saldos | 100% de coincidencia con el cálculo manual |
| Trabajos pendientes de facturación | 100% de los trabajos terminados sin facturar en el listado |
| Integridad de los datos | Sin pérdida ni duplicación de registros entre versiones |
| Control de morosidad | Estado de deuda correcto ante pagos y saldos pendientes |

Indicadores, evidencias y riesgos: [`docs/03-control/indicadores.md`](docs/03-control/indicadores.md).
Casos de prueba y su registro: [`docs/03-control/plan-de-pruebas.md`](docs/03-control/plan-de-pruebas.md).

## Trabajo colaborativo

- **Ramas:** `main` estable; una rama por unidad de trabajo:
  `feature/bpmn-facturacion` (modelado y figuras), `feature/backlog-historias` (tres
  historias de usuario), `docs/indicadores-control` (indicadores y plan de pruebas) y
  `feature/entrega-4` (PDF y documentación del repositorio).
- **Commits:** adaptación de Conventional Commits (`feat`, `fix`, `docs`, `refactor`,
  `chore`), con verbo en infinitivo y objeto concreto. El historial permite reconstruir
  qué se hizo en cada rama y por qué.
- **Pull Request:** las ramas se integran con un PR que describe el cambio, las figuras o
  secciones afectadas, la lista de verificación y el vínculo con la historia o consigna.
  La revisión del PR de BPMN controla que los flujos de mensaje no crucen las etiquetas
  de los eventos, que todos los carriles tengan actividades y que las compuertas estén
  rotuladas. El PR de la entrega verifica enlaces, numeración y correspondencia con el
  PDF. Las observaciones y su resolución quedan registradas en el PR.
- **Tablero:** las tres historias se mueven entre «Por hacer», «En progreso» y «Listo»
  cuando se abre la rama y cuando el PR se integra, para que el estado del tablero y el
  del repositorio no se contradigan.

## Declaración de uso de inteligencia artificial

Se utilizaron asistentes de IA como apoyo para ordenar el trabajo, contrastar alternativas
de modelado y corregir redacción. La asistencia no reemplazó el análisis: cada resultado
fue leído, corregido y, cuando correspondía, descartado.

| Etapa | Herramienta | Uso concreto |
|---|---|---|
| Entregas 1, 2 y 3 | Gemini 3.8 Flash | Revisión de redacción, ordenamiento de ideas y borradores de tablas comparativas. |
| Entrega 4: BPMN | OpenCode con DeepSeek V4.1 Flash | Discusión de pools y carriles, revisión de la lógica de las compuertas y generación del script que dibuja los diagramas. |
| Entrega 4: documentación | OpenCode con DeepSeek V4.1 Flash | Ajuste de estilo, coherencia entre secciones y armado del repositorio y del tablero. |

Correcciones humanas principales: se acotó el bloqueo del cliente moroso a los trabajos
no urgentes (RN-06), se agregó el parte u orden de trabajo como entidad, se reemplazó la
imputación automática de pagos por una imputación explícita y se verificó cada cifra de
los indicadores contra las metas de la Entrega 2.

Prompts, resultados y criterio de uso responsable:
[`docs/04-ia/declaracion-uso-ia.md`](docs/04-ia/declaracion-uso-ia.md).

---

Santiago Dominguez · Comisión 10 · Organización Empresarial · UTN TUPAD · Octubre de 2026