# Modelado de procesos (BPMN 2.0)

Los dos procesos del sistema de facturación y cuentas corrientes se modelaron en
**BPMN 2.0** con la estructura solicitada por la cátedra: **Pools** para las
organizaciones y los actores externos, **Lanes** para los roles internos y para el
comportamiento automatizado del sistema, y **compuertas lógicas** para las excepciones.

## Archivos

| Figura | Contenido | Formatos |
|---|---|---|
| 1.3.1 | Leyenda de la notación utilizada | `figura-1-3-1-leyenda-bpmn.png` · `.svg` |
| 1.4.1 | Facturación y cobro a clientes | `figura-1-4-1-bpmn-facturacion-cobro.png` · `.svg` |
| 1.5.1 | Facturación y pago a proveedores | `figura-1-5-1-bpmn-proveedores-pagos.png` · `.svg` |

Los PNG se usan para insertar las figuras en el documento (300 dpi); los SVG son la
versión vectorial editable. Ambos se generan con `scripts/make_diagrams.py`, de modo que
una corrección se hace sobre el script y no redibujando la figura.

## Convenciones de notación

- **Pool «Latorre Ascensores»:** agrupa los carriles internos (Administración, Dirección,
  Sistema/Aplicación y, en el proceso de clientes, Operaciones/Técnico).
- **Pools externos:** Cliente y Proveedor. La comunicación con ellos se representa con
  **flujos de mensaje** (línea punteada), nunca con flujos de secuencia.
- **Compuertas exclusivas (XOR):** cada decisión habilita un único camino. Se usan para
  validar datos, detectar duplicados, resolver la condición de venta o compra y evaluar
  morosidad o criticidad.
- **Eventos:** de inicio (simple o de mensaje), de fin y de fin alternativo (factura
  rechazada, cuenta al día, cuenta actualizada).
- **Tareas:** de usuario (carga manual con apoyo del sistema), externas (del cliente o del
  proveedor) y de servicio (ejecutadas automáticamente por la aplicación).
- **Convergencia:** se usa una XOR de convergencia porque solo uno de los caminos puede
  estar activo; si pudieran activarse en paralelo, correspondería una AND.

## Proceso de facturación y cobro a clientes (Figura 1.4.1)

Cubre el circuito de ingreso: desde que un técnico termina un trabajo hasta que el sistema
recalcula el saldo y evalúa la morosidad. Intervienen el pool del cliente, el carril de
Operaciones/Técnico, el de Administración y el del Sistema/Aplicación.

1. **Cierre técnico.** Al finalizar un mantenimiento, una reparación o una instalación, el técnico carga el parte digital. Ese registro actúa como disparador del control de facturación.
2. **Revisión.** Administración consulta la lista de trabajos terminados que todavía no fueron facturados y selecciona el que corresponde procesar.
3. **Validación.** Se verifica el cliente, el servicio prestado y el importe a facturar. Si faltan datos, el parte vuelve al técnico para su corrección y reingresa al circuito.
4. **Registro del comprobante.** Administración ingresa el comprobante y lo vincula al cliente y al período correspondiente.
5. **Condición de venta.** Si la operación es al contado, se registra la factura y el cobro correspondiente una sola vez. Si es a cuenta corriente, el importe de la factura se incorpora al saldo pendiente del cliente.
6. **Emisión y envío.** El comprobante se emite y se envía al cliente. En las operaciones al contado, el pago ya queda registrado junto con la operación; en las operaciones a cuenta corriente, el cliente puede abonarlo posteriormente.
7. **Registro del cobro.** Cuando el cliente realiza un pago de una operación a cuenta corriente, Administración registra el recibo o movimiento de cobro y lo vincula con uno o más comprobantes pendientes.
8. **Imputación.** El sistema aplica el importe recibido a los comprobantes vinculados, verificando los datos del movimiento y evitando imputaciones duplicadas.
9. **Recálculo.** El sistema calcula el saldo que queda pendiente, contempla los pagos completos o parciales y determina si existen facturas vencidas.
10. **Control y alerta.** Si persiste deuda vencida, se genera una alerta y se restringe la autorización de trabajos no urgentes. Si no existe deuda vencida, la cuenta se considera al día. Las situaciones urgentes se atienden de acuerdo con los criterios de seguridad establecidos.

Las excepciones están modeladas de forma explícita: la compuerta «¿Datos completos?»
devuelve el parte a Operaciones antes de facturar; «¿Pago total?» distingue entre cancelar
el comprobante y mantener el saldo pendiente, porque un pago parcial no cierra la deuda; y
«¿Deuda vencida?» separa la cuenta al día de la cuenta en mora. Esta última decisión
conecta el circuito administrativo con la operación: el bloqueo alcanza únicamente a los
trabajos no urgentes, porque los urgentes se ejecutan igual para no afectar la seguridad
de los usuarios.

## Proceso de facturación y pago a proveedores (Figura 1.5.1)

Cubre el circuito de egreso. Comparte la lógica del anterior, pero invierte el sentido del
flujo: el comprobante llega desde afuera y la decisión de pagar involucra a Dirección, que
prioriza según el saldo y la criticidad del insumo o servicio.

1. **Recepción.** El proveedor emite la factura y la envía; el proceso se inicia con el
   evento de mensaje «Factura recibida».
2. **Registro.** Administración selecciona el proveedor y carga comprobante, período,
   importe y condición de compra.
3. **Validación de datos.** Si los datos son incompletos u observables, la factura se
   devuelve al proveedor y reingresa al circuito.
4. **Control de duplicados.** Si la factura ya fue registrada se rechaza y se notifica; el
   proceso finaliza en «Factura rechazada».
5. **Condición de compra.** Si es al contado se imputa el pago inmediato; si es a cuenta
   corriente, el importe se suma al saldo a pagar.
6. **Priorización.** Dirección consulta el saldo y la criticidad del insumo y decide si el
   pago se prioriza o se programa.
7. **Registro del pago.** Administración registra el pago y lo asocia a la factura; el
   sistema descuenta el importe.
8. **Recálculo y cierre.** El sistema recalcula el saldo a pagar y deja la cuenta
   actualizada.

La separación entre «Priorizar pago» y «Programar pago» expresa la regla de que un
proveedor crítico —por ejemplo, el que suministra repuestos de seguridad— no puede esperar
el calendario ordinario de pagos sin poner en riesgo la operación.

## Diccionario de datos mínimo

| Entidad | Campos definidos | Campos recomendados |
|---|---|---|
| Cliente | ID_Cliente; Razón_Social; Saldo_Pendiente; Estado_Morosidad | Datos de contacto; condición y vencimiento por comprobante; pagos imputados |
| Proveedor | ID_Proveedor; Nombre_Proveedor; Saldo_A_Pagar; Prioridad_Pago | Datos de contacto; vencimiento por factura; fecha y referencia de cada pago |
| Comprobante | ID_Comprobante; Periodo_Facturacion; Monto_Total; Condicion_Venta | Tipo; tercero; fecha de emisión y vencimiento; estado de cancelación |
| Pago / Recibo | ID_Pago; Importe; Fecha | Comprobantes a los que se imputa; tercero; medio o referencia |
| Parte / Orden de Trabajo | ID_Parte; ID_Cliente; Fecha; Tipo_Servicio | Estado; importe estimado; indicador de facturado; ID_Comprobante; técnico |

La entidad **Parte / Orden de Trabajo** es la que faltaba en el borrador previo y la que
hace posible el control de la Entrega 2: sin ella, el listado de trabajos terminados sin
facturar no tendría de dónde obtener los datos.

## Reglas de negocio y su punto de aplicación

| Código | Regla | Dónde se aplica |
|---|---|---|
| RN-01 | Todo trabajo finalizado sin comprobante debe figurar en el listado de pendientes de facturación. | Carril Operaciones/Técnico y revisión de Administración (Fig. 1.4.1) |
| RN-02 | Un comprobante no puede registrarse dos veces para el mismo tercero y período. | Compuerta «¿Duplicada?» (Fig. 1.5.1) |
| RN-03 | Los datos mínimos son período, importe y condición de venta o compra. | Compuertas «¿Datos completos?» y «¿Datos válidos?» |
| RN-04 | Un pago puede imputarse a uno o más comprobantes, pero nunca superar el saldo impago. | Imputación del cobro y del pago |
| RN-05 | El saldo se recalcula en cada movimiento, sin edición manual. | Tareas de servicio «Recalcular saldo» |
| RN-06 | El bloqueo por morosidad alcanza solo a los trabajos no urgentes. | Compuerta «¿Deuda vencida?» (Fig. 1.4.1) |
| RN-07 | En cuenta corriente, el pago a proveedor requiere la prioridad definida por Dirección. | Compuerta «¿Crítico?» (Fig. 1.5.1) |
| RN-08 | Toda modificación de un comprobante queda registrada con usuario y fecha. | Auditoría transversal del sistema |
