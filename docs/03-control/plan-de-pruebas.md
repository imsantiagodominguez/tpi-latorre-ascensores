# Plan de pruebas y registro de evidencias

Los casos se ejecutan sobre un conjunto de datos de prueba (un cliente al día, uno con
deuda vencida, uno con pago parcial, un proveedor común y un proveedor crítico). Cada caso
se registra con su resultado para que el indicador se pueda auditar sin depender de la
memoria de quien hizo la prueba.

## Casos de prueba

| ID | Caso | Datos de entrada | Resultado esperado | Indicador asociado |
|---|---|---|---|---|
| CP-01 | Alta de comprobante de cliente | Cliente, período, importe, condición «cuenta corriente» | El comprobante queda asociado a la cuenta y suma al saldo | Tiempo de registro |
| CP-02 | Alta de comprobante duplicado | Mismo cliente, mismo período e importe que CP-01 | El sistema rechaza el registro e informa el duplicado | Integridad de los datos |
| CP-03 | Búsqueda por período | Mes y año con comprobantes cargados | El listado aparece en menos de 3 segundos | Velocidad de búsqueda |
| CP-04 | Pago total de un comprobante | Recibo por el importe exacto del comprobante | El comprobante queda cancelado y el saldo en cero | Exactitud de los saldos |
| CP-05 | Pago parcial | Recibo por el 50 % del comprobante | El comprobante mantiene saldo pendiente y el historial registra el movimiento | Exactitud de los saldos |
| CP-06 | Imputación de un pago a dos comprobantes | Recibo por la suma de dos comprobantes | El importe se distribuye y ambos saldos se recalculan | Exactitud de los saldos |
| CP-07 | Trabajo terminado sin facturar | Parte cerrado por el técnico, sin comprobante | El trabajo aparece en el listado de pendientes al cierre | Trabajos pendientes de facturación |
| CP-08 | Cliente con deuda vencida | Cliente con comprobante vencido impago | La consulta muestra el estado en mora en menos de 3 segundos | Control de morosidad |
| CP-09 | Bloqueo de trabajo urgente | Cliente en mora, trabajo marcado como urgente | El sistema permite la ejecución y deja registro de la excepción (RN-06) | Control de morosidad |
| CP-10 | Cancelación de la deuda | Pago total de la deuda vencida | La alerta se retira y la cuenta vuelve a estado al día | Control de morosidad |
| CP-11 | Persistencia de datos | Cierre y reapertura del sistema | Los registros cargados se conservan sin duplicarse | Integridad de los datos |
| CP-12 | Priorización de proveedor crítico | Factura de proveedor crítico en cuenta corriente | Dirección define la prioridad y el pago se registra en el circuito priorizado (RN-07) | Control de morosidad / integridad |

## Registro de ejecución

| Fecha | Caso | Resultado | Observaciones | Responsable |
|---|---|---|---|---|
| — | CP-01 | Pendiente de ejecución formal | Validado en la prueba de alta durante el modelado | S. Dominguez |
| — | CP-02 | Pendiente de ejecución formal | La regla está modelada en la compuerta «¿Duplicada?» | S. Dominguez |
| — | CP-03 | Pendiente de ejecución formal | Requiere el conjunto de datos de prueba completo | S. Dominguez |
| — | CP-04 a CP-06 | Pendiente de ejecución formal | Base de la HU-02, en progreso | S. Dominguez |
| — | CP-07 | Pendiente de ejecución formal | Depende del alta de partes de trabajo | S. Dominguez |
| — | CP-08 a CP-10 | Pendiente de ejecución formal | Base de la HU-03, por hacer | S. Dominguez |
| — | CP-11 y CP-12 | Pendiente de ejecución formal | Se ejecutan al cierre de cada versión | S. Dominguez |

## Criterio de aceptación del plan

Una versión se considera aceptada cuando todos los casos funcionales y de exactitud
resultan conformes, no se registra ninguna pérdida ni duplicación de datos y los tiempos
medidos en CP-01 y CP-03 respetan los estándares de 1 minuto y 3 segundos. Los casos que
no se hayan ejecutado se informan como pendientes: no se reemplazan por una estimación.
