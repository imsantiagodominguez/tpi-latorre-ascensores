# Backlog ágil — Historias de usuario

Las tres historias se desprenden del proceso modelado: no son funcionalidades inventadas,
sino pasos del diagrama BPMN que el sistema debe sostener. Se gestionan en el
[tablero del proyecto](https://github.com/users/imsantiagodominguez/projects/1) con las
columnas «Por hacer», «En progreso» y «Listo».

| ID | Historia | Estado | Evidencia |
|---|---|---|---|
| HU-01 | Registrar y consultar comprobantes | Listo | `feature/bpmn-facturacion`, su PR, Figura 1.4.1 |
| HU-02 | Registrar cobros y actualizar saldos | En progreso | `feature/bpmn-facturacion`, plan de pruebas |
| HU-03 | Alertas de morosidad y bloqueo | Por hacer | `docs/indicadores-control`, Tabla de indicadores |

Una tarjeta pasa a «En progreso» cuando se abre la rama y a «Listo» cuando el Pull Request
se integra. De este modo, el estado del tablero y el del repositorio nunca se contradicen.

---

## HU-01 · Registrar y consultar comprobantes

**Historia.** Como auxiliar administrativo, quiero registrar comprobantes de clientes y
proveedores asociándolos a su cuenta y período, para dejar de duplicar la información en
planillas.

**Valor.** Reduce el tiempo de carga y elimina la doble registración.

**Criterios de aceptación**

1. El comprobante se guarda con período, importe y condición de venta o compra.
2. Queda asociado a un cliente o proveedor existente.
3. El sistema impide el registro duplicado del mismo comprobante para el mismo tercero y
   período.
4. El registro completo demanda alrededor de un minuto.

**Reglas de negocio:** RN-02 y RN-03.

**Evidencia:** Figura 1.4.1, rama `feature/bpmn-facturacion` y su PR.

**Tareas**

- [x] Definir los campos mínimos del comprobante.
- [x] Modelar la compuerta de duplicados.
- [x] Vincular el comprobante con el parte u orden de trabajo.
- [x] Verificar el alta contra un cliente y un proveedor de prueba.

---

## HU-02 · Registrar cobros y actualizar saldos

**Historia.** Como responsable administrativo, quiero registrar cobros y pagos e
imputarlos a los comprobantes, para que el saldo de cada cuenta se actualice
automáticamente.

**Valor.** Elimina el cálculo manual y reduce los errores de saldo.

**Criterios de aceptación**

1. El pago se imputa a uno o más comprobantes.
2. Se admiten pagos parciales.
3. El saldo se recalcula sin edición manual.
4. El historial muestra el movimiento con fecha, importe y usuario.
5. El saldo calculado coincide con el control manual en el 100 % de los casos de prueba.

**Reglas de negocio:** RN-04 y RN-05.

**Evidencia:** plan de pruebas en `docs/03-control/` y Figura 1.4.1.

**Tareas**

- [x] Definir la imputación explícita del pago.
- [x] Modelar el recálculo como tarea de servicio.
- [ ] Completar la planilla de casos de prueba con pagos parciales.
- [ ] Comparar el saldo del sistema contra el cálculo manual en la muestra mensual.

---

## HU-03 · Alertas de morosidad y bloqueo

**Historia.** Como responsable de Operaciones, quiero consultar el estado de morosidad de
un cliente antes de autorizar un trabajo no urgente, para no seguir prestando servicios a
cuentas vencidas.

**Valor.** Protege la liquidez sin afectar la seguridad de los usuarios.

**Criterios de aceptación**

1. La consulta muestra el estado de la cuenta y la deuda vencida.
2. La respuesta demora menos de tres segundos.
3. El bloqueo solo afecta trabajos no urgentes.
4. La alerta se retira automáticamente cuando la deuda vencida se cancela.

**Reglas de negocio:** RN-06.

**Evidencia:** Figura 1.4.1 e indicadores de control.

**Tareas**

- [x] Acotar el bloqueo a los trabajos no urgentes.
- [ ] Definir el indicador de morosidad y su frecuencia de cálculo.
- [ ] Modelar la consulta desde el carril de Operaciones.
- [ ] Probar la baja automática de la alerta al cancelarse la deuda.

---

## Trazabilidad entre historias, procesos y artefactos

| Historia | Paso del proceso | Entidades | Rama / artefacto |
|---|---|---|---|
| HU-01 | Registrar comprobante (Figuras 1.4.1 y 1.5.1) | Comprobante; Parte/Orden de Trabajo | `feature/bpmn-facturacion` |
| HU-02 | Imputar cobro y recalcular saldo (Figura 1.4.1) | Pago/Recibo; Comprobante; Cliente | `feature/bpmn-facturacion` |
| HU-03 | Evaluar morosidad y bloquear trabajos (Figura 1.4.1) | Cliente; Comprobante | `docs/indicadores-control` |
