# Indicadores y estándares de desempeño

Un proceso modelado sin indicadores es una declaración de intenciones. Los indicadores
retoman las metas cuantitativas definidas en la Entrega 2 y las convierten en estándares
verificables: cada uno indica qué se mide, contra qué valor se compara y cómo se obtiene
la evidencia.

## Tabla de indicadores

| Indicador | Estándar esperado | ¿Cómo se verifica? | Frecuencia |
|---|---|---|---|
| Tiempo de registro | Registrar un comprobante en aproximadamente 1 minuto | Cronometrar la carga de varios comprobantes de prueba | Por lote de prueba |
| Velocidad de búsqueda | Encontrar comprobantes por mes y año en menos de 3 segundos | Cronometrar búsquedas con un conjunto de datos de prueba | Por lote de prueba |
| Exactitud de los saldos | El 100 % de los saldos calculados coincide con los movimientos registrados | Comparar el sistema contra el cálculo manual de una muestra | Mensual |
| Trabajos pendientes de facturación | El 100 % de los trabajos terminados sin facturar aparece en el listado | Comparar los trabajos cargados contra el listado de cierre | Mensual |
| Integridad de los datos | No se pierden ni se duplican registros durante las operaciones | Registrar, consultar y modificar datos de prueba y verificar persistencia | Por versión |
| Control de morosidad | El estado de deuda refleja correctamente pagos y saldos pendientes | Probar clientes al día, con deuda y con pagos parciales | Mensual |

Los estándares se eligieron por su relación con el problema diagnosticado. El minuto de
carga responde a la demora actual del registro manual; los tres segundos de búsqueda, a la
imposibilidad de encontrar un comprobante por período sin revisar carpeta por carpeta; y
el 100 % de exactitud, a que un saldo mal calculado tiene consecuencias directas sobre el
cobro o sobre la relación con el proveedor.

## Tipos de prueba

- **Funcionales:** comprobar que se pueden registrar y consultar facturas, comprobantes de
  proveedores y movimientos de cobro y pago.
- **De exactitud:** verificar que los saldos se calculen correctamente, incluyendo pagos
  parciales, ausencia de pagos y cancelación total de una deuda.
- **De rendimiento:** evaluar cuánto tarda el sistema en registrar comprobantes y en
  buscar información.
- **De integridad:** verificar que los datos se conserven al cerrar y volver a abrir el
  programa, y que los errores de carga no produzcan registros inconsistentes.

## Evidencias y plan de auditoría

| Evidencia | Qué demuestra | Dónde se conserva |
|---|---|---|
| Diagramas BPMN en PNG y SVG | Que el proceso fue modelado y versionado | `docs/01-bpmn/` |
| Historial de commits | Que el trabajo se construyó de forma incremental | Repositorio GitHub |
| PR de cada rama con revisión | Que hubo control de calidad sobre lo producido | Repositorio GitHub |
| Tablero con las tres historias | Que el backlog se sigue y se actualiza | Tablero del proyecto |
| Planilla de casos de prueba | Que los indicadores se midieron con datos | `docs/03-control/plan-de-pruebas.md` |
| Documento de la entrega 4 | Que el conjunto es coherente y trazable | `entregas/` |

## Riesgos y acciones preventivas

| Riesgo | Impacto | Acción de control |
|---|---|---|
| Duplicación de comprobantes | Alto: saldos inflados y reclamos | Compuerta de duplicados (RN-02) y control de integridad por versión |
| Trabajos terminados sin facturar | Alto: pérdida de ingresos | Listado de pendientes y control mensual al cierre (RN-01) |
| Error en la imputación de un pago | Medio: saldo incorrecto en una cuenta | Recálculo automático, historial de movimientos y prueba de exactitud |
| Pago a proveedor crítico fuera de plazo | Alto: interrupción del servicio | Compuerta de criticidad y priorización de Dirección (RN-07) |
| Pérdida de información | Alto: imposibilidad de auditar | Pruebas de integridad y respaldo del repositorio |
