# Declaración de uso de inteligencia artificial

En línea con la declaración de transparencia de la cátedra, se explicita qué asistentes de
inteligencia artificial se utilizaron, con qué propósito y qué decisiones se tomaron sobre
sus resultados. La asistencia no reemplazó el análisis: se usó para ordenar el trabajo,
contrastar alternativas de modelado y corregir redacción, y cada resultado fue revisado y
ajustado antes de incorporarlo.

## Herramientas utilizadas

| Etapa | Herramienta | Uso concreto |
|---|---|---|
| Entregas 1, 2 y 3 | Gemini 3.8 Flash | Revisión de redacción, ordenamiento de ideas para el análisis sistémico y generación de borradores de tablas comparativas. |
| Entrega 4: BPMN | OpenCode con DeepSeek V4.1 Flash | Discusión de la estructura de pools y carriles, revisión de la lógica de las compuertas y generación del script que dibuja los diagramas. |
| Entrega 4: documentación | OpenCode con DeepSeek V4.1 Flash | Ajuste de estilo, control de coherencia entre secciones y armado del repositorio y del tablero. |

## Prompts representativos y resultado obtenido

| Objetivo | Prompt (síntesis) | Resultado y ajuste humano |
|---|---|---|
| Estructurar el modelado BPMN | «Armá un diagrama BPMN con pools y lanes para un sistema de facturación y cuentas corrientes de una empresa de ascensores; incluí compuertas para excepciones». | El asistente propuso un flujo lineal sin devoluciones. Se agregaron la compuerta de datos incompletos, el reingreso del parte y el bloqueo solo de trabajos no urgentes, que son reglas reales de la empresa. |
| Definir el diccionario de datos | «¿Qué entidades necesita un sistema de facturación y cuentas corrientes para sostener el proceso?». | Sugirió cuatro entidades. Se detectó que faltaba el parte u orden de trabajo y se incorporó como quinta entidad, con el campo de facturado. |
| Redactar las historias de usuario | «Escribí tres historias de usuario en formato Como/quiero/para con criterios de aceptación medibles». | Las historias eran genéricas. Se reescribieron tomando como referencia las metas cuantitativas de la Entrega 2 (1 minuto, 3 segundos, 100 %). |
| Organizar el repositorio | «Proponé una estructura de carpetas y una convención de commits para un TPI individual». | La propuesta era adecuada, pero se simplificó: se eliminaron ramas de release y se dejó una rama por consigna, acorde al tamaño del proyecto. |
| Revisar los diagramas | «Revisá este diagrama BPMN y señalá errores de notación o de legibilidad». | Detectó que un flujo de mensaje cruzaba las etiquetas de los eventos y que un carril no tenía actividades. Ambas correcciones se aplicaron y se registraron en el Pull Request. |

## Correcciones humanas efectuadas

Las correcciones más relevantes no fueron de estilo sino de contenido, y surgieron de
contrastar la propuesta del asistente con el funcionamiento real de la empresa:

- Se descartó el bloqueo total del cliente moroso propuesto por el asistente: en la empresa
  los trabajos urgentes se realizan igual, porque está en juego la seguridad de los
  usuarios. La regla quedó acotada a los trabajos no urgentes (RN-06).
- Se agregó el parte u orden de trabajo como entidad, sin la cual el control de trabajos
  sin facturar no tiene origen de datos.
- Se reemplazó la imputación automática de pagos a la factura más antigua por una
  imputación explícita, porque en la práctica el cliente suele indicar a qué comprobante
  corresponde el pago.
- Se corrigieron las etiquetas y la ubicación de los flujos en los diagramas para evitar
  cruces y textos superpuestos.
- Se verificó cada cifra de los indicadores contra las metas de la Entrega 2, en lugar de
  aceptar los valores propuestos por el modelo.

## Criterio de uso responsable

El uso de asistentes de IA se limitó a tareas de estructuración, contraste y redacción. Las
decisiones de modelado, la definición de las reglas de negocio y la validación de los
datos son propias: responden al conocimiento del circuito administrativo real de Latorre
Ascensores. Todo resultado generado fue leído, corregido y, cuando correspondía,
descartado. Asumo la responsabilidad intelectual sobre la totalidad del contenido de esta
entrega.

---

Santiago Dominguez · Comisión 10 · Organización Empresarial · UTN TUPAD
