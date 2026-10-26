# -*- coding: utf-8 -*-
"""Genera las figuras BPMN de la Entrega 4."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from bpmn_lib import (canvas, pool, lane, task, event, gateway, flow, note,
                      save, INK, LANE_TINT, LANE_ALT, FLOW, MSG)
from matplotlib.patches import Circle, FancyBboxPatch, Polygon
from matplotlib.lines import Line2D

OUT = Path(__file__).resolve().parents[1] / "diagramas"
_DOCS = Path(__file__).resolve().parents[1] / "docs" / "01-bpmn"
if _DOCS.is_dir():
    OUT = _DOCS


# ============================================================ FIGURA 2
def figura_facturacion():
    W, H = 23.2, 13.3
    fig, ax = canvas(W, H, (12.2, 7.0))

    # ---- pools
    pool(ax, 0.2, 11.30, 22.8, 1.80, "Cliente\n(actor externo)", external=True)
    pool(ax, 0.2, 0.35, 22.8, 10.75, "Latorre Ascensores")

    # ---- lanes
    lane(ax, 0.82, 9.05, 22.18, 2.05, "Operaciones / Técnico", tint=LANE_TINT,
         fs=7.0)
    lane(ax, 0.82, 3.65, 22.18, 5.40, "Administración", tint=LANE_ALT)
    lane(ax, 0.82, 0.35, 22.18, 3.30, "Sistema / Aplicación", tint=LANE_TINT)

    # ---- cliente
    task(ax, 12.00, 12.20, "Recibir factura y abonar", w=2.4, h=0.78,
         kind="Tarea externa", chars=22)

    # ---- carril operaciones
    event(ax, 2.45, 10.05, "Trabajo\nfinalizado", kind="start", dy=-0.40)
    task(ax, 4.00, 10.05, "Cargar parte digital", w=1.75, h=0.80,
         kind="Tarea de usuario")
    task(ax, 7.95, 10.05, "Corregir y recargar parte", w=1.95, h=0.82,
         kind="Tarea de usuario", chars=19)

    # ---- carril administración: facturación
    task(ax, 5.90, 7.55, "Revisar parte y datos", w=1.95, h=0.82)
    gateway(ax, 7.70, 7.55, "¿Datos completos?", dy=-0.98, chars=18)
    task(ax, 9.75, 7.55, "Registrar comprobante", w=2.0, h=0.82)
    gateway(ax, 11.95, 7.55, "¿Condición de venta?", dx=-0.75, dy=-0.70, chars=13)
    task(ax, 14.15, 8.55, "Registrar cobro e imputar", w=2.0, h=0.82)
    task(ax, 14.15, 6.55, "Sumar importe al saldo", w=2.0, h=0.82)
    gateway(ax, 16.30, 7.55, "", s=0.55)

    # ---- carril administración: cobro
    event(ax, 2.45, 4.80, "Pago\nrecibido", kind="start", dy=-0.40)
    task(ax, 4.00, 4.80, "Registrar e imputar pago", w=1.90, h=0.82)
    gateway(ax, 6.10, 4.80, "¿Pago total?", dy=-1.02, chars=12)
    task(ax, 8.10, 5.55, "Cancelar comprobante", w=1.90, h=0.76)
    task(ax, 8.10, 4.10, "Mantener saldo pendiente", w=1.90, h=0.76, chars=20)
    gateway(ax, 9.55, 4.80, "", s=0.55)

    # ---- convergencia y control
    gateway(ax, 17.40, 4.80, "", s=0.55)
    task(ax, 17.40, 2.00, "Recalcular saldo y evaluar morosidad", w=2.4, h=0.95,
         kind="Tarea de servicio", chars=24)
    gateway(ax, 19.60, 2.00, "¿Deuda vencida?", dy=0.82, chars=17)
    task(ax, 21.35, 2.00, "Emitir alerta y bloquear trabajos no urgentes",
         w=2.1, h=1.00, kind="Tarea de servicio", chars=21)
    event(ax, 22.75, 2.00, "Fin", kind="end", dy=0.32)
    event(ax, 19.60, 0.82, "Cuenta al día", kind="end", dx=0.26, dy=0, ha="left")

    # ---- flujos facturación
    flow(ax, [(2.62, 10.05), (3.125, 10.05)])
    flow(ax, [(4.875, 10.05), (5.90, 10.05), (5.90, 7.96)])
    flow(ax, [(6.875, 7.55), (7.10, 7.55)])
    flow(ax, [(7.70, 8.15), (7.70, 9.64)], label="No", lx=8.02, ly=8.90)
    flow(ax, [(7.95, 10.46), (7.95, 10.70), (4.00, 10.70), (4.00, 10.47)],
         label="reingreso", lx=5.95, ly=10.87)
    flow(ax, [(8.30, 7.55), (8.75, 7.55)], label="Sí", lx=8.52, ly=7.84)
    flow(ax, [(10.75, 7.55), (11.35, 7.55)])
    flow(ax, [(11.95, 8.17), (11.95, 8.55), (13.15, 8.55)],
         label="Contado", lx=12.42, ly=8.76)
    flow(ax, [(11.95, 6.93), (11.95, 6.55), (13.15, 6.55)],
         label="Cuenta corriente", lx=12.10, ly=6.30)
    flow(ax, [(15.15, 8.55), (16.30, 8.55), (16.30, 8.10)])
    flow(ax, [(15.15, 6.55), (16.30, 6.55), (16.30, 7.00)])
    flow(ax, [(16.85, 7.55), (17.40, 7.55), (17.40, 5.35)])

    # ---- flujos cobro
    flow(ax, [(2.62, 4.80), (3.05, 4.80)])
    flow(ax, [(4.95, 4.80), (5.50, 4.80)])
    flow(ax, [(6.10, 5.40), (6.10, 5.55), (7.15, 5.55)],
         label="Sí", lx=6.38, ly=5.72)
    flow(ax, [(6.10, 4.20), (6.10, 4.10), (7.15, 4.10)],
         label="No", lx=6.36, ly=3.99)
    flow(ax, [(9.05, 5.55), (9.55, 5.55), (9.55, 5.35)])
    flow(ax, [(9.05, 4.10), (9.55, 4.10), (9.55, 4.25)])
    flow(ax, [(10.10, 4.80), (16.85, 4.80)],
         label="saldo actualizado", lx=13.30, ly=5.04)
    flow(ax, [(17.40, 4.25), (17.40, 2.48)])

    # ---- control
    flow(ax, [(18.60, 2.00), (19.00, 2.00)])
    flow(ax, [(20.20, 2.00), (20.30, 2.00)])
    flow(ax, [(22.40, 2.00), (22.58, 2.00)])
    flow(ax, [(19.60, 1.40), (19.60, 0.99)], label="No", lx=19.92, ly=1.22)

    # ---- flujos de mensaje
    flow(ax, [(10.20, 7.96), (10.20, 11.66), (11.35, 11.66), (11.35, 11.81)],
         kind="msg", label="factura", lx=9.92, ly=9.55, ha="right")
    flow(ax, [(10.80, 12.20), (1.45, 12.20), (1.45, 4.80), (2.28, 4.80)],
         kind="msg", label="pago del cliente", lx=1.62, ly=8.30, ha="left")

    # ---- notas
    note(ax, 2.55, 6.42, "El cobro puede ser total o parcial;", fs=5.6)
    note(ax, 2.55, 6.08, "el saldo se recalcula en ambos casos.", fs=5.6)

    return save(fig, OUT / "figura-1-4-1-bpmn-facturacion-cobro")


# ============================================================ FIGURA 3
def figura_proveedores():
    W, H = 23.4, 12.2
    fig, ax = canvas(W, H, (11.7, 6.10))

    pool(ax, 0.2, 10.10, 23.0, 1.70, "Proveedor\n(actor externo)", external=True)
    pool(ax, 0.2, 0.35, 23.0, 9.45, "Latorre Ascensores")

    lane(ax, 0.82, 5.30, 22.38, 4.50, "Administración", tint=LANE_TINT)
    lane(ax, 0.82, 3.30, 22.38, 2.00, "Dirección", tint=LANE_ALT)
    lane(ax, 0.82, 0.35, 22.38, 2.95, "Sistema / Aplicación", tint=LANE_TINT)

    task(ax, 11.00, 11.00, "Emitir factura y gestionar cobro", w=5.0, h=0.85,
         kind="Tarea externa", chars=40)

    # ---- administración
    event(ax, 2.35, 8.10, "Factura recibida", kind="start", dy=-0.32)
    task(ax, 4.15, 8.10, "Registrar factura recibida", w=2.2, h=0.85)
    gateway(ax, 6.60, 8.10, "¿Datos válidos?", dy=-0.94, chars=13)
    task(ax, 6.60, 9.35, "Observar y devolver", w=2.1, h=0.72)
    gateway(ax, 8.70, 8.10, "¿Duplicada?", dy=0.82, chars=11)
    task(ax, 8.70, 6.70, "Rechazar y notificar", w=2.0, h=0.72)
    event(ax, 8.70, 5.95, "Factura rechazada", kind="end", dx=0.26, dy=0,
          ha="left")
    gateway(ax, 10.90, 8.10, "¿Condición?", dx=0.58, dy=-1.05, chars=12)
    task(ax, 13.30, 9.00, "Imputar pago inmediato", w=2.2, h=0.78)
    task(ax, 13.30, 6.40, "Sumar al saldo a pagar", w=2.2, h=0.78)
    task(ax, 19.60, 8.10, "Registrar pago al proveedor", w=2.4, h=0.85)

    # ---- dirección
    task(ax, 13.30, 4.30, "Consultar prioridad y saldo", w=2.2, h=0.82)
    gateway(ax, 16.00, 4.30, "¿Crítico?", dx=-0.75, dy=-0.88, chars=10)
    task(ax, 17.70, 4.95, "Priorizar pago", w=1.8, h=0.66)
    task(ax, 17.70, 3.65, "Programar pago", w=1.8, h=0.66)
    gateway(ax, 19.45, 4.30, "", s=0.52)

    # ---- sistema
    task(ax, 18.60, 1.75, "Recalcular saldo a pagar", w=2.3, h=0.85,
         kind="Tarea de servicio", chars=20)
    event(ax, 20.45, 1.75, "Cuenta actualizada", kind="end", dx=0.26, dy=0,
          ha="left")

    # ---- flujos administración
    flow(ax, [(2.52, 8.10), (3.05, 8.10)])
    flow(ax, [(5.25, 8.10), (5.98, 8.10)])
    flow(ax, [(6.60, 8.72), (6.60, 8.99)], label="No", lx=6.92, ly=8.86)
    flow(ax, [(5.55, 9.35), (4.15, 9.35), (4.15, 8.53)],
         label="reingreso", lx=4.85, ly=9.57)
    flow(ax, [(7.22, 8.10), (8.08, 8.10)], label="Sí", lx=7.65, ly=7.83)
    flow(ax, [(8.70, 7.48), (8.70, 7.06)], label="Sí", lx=9.02, ly=7.27)
    flow(ax, [(8.70, 6.34), (8.70, 6.13)])
    flow(ax, [(9.32, 8.10), (10.28, 8.10)], label="No", lx=9.80, ly=7.83)
    flow(ax, [(10.90, 8.72), (10.90, 9.00), (12.20, 9.00)],
         label="Contado", lx=11.55, ly=9.21)
    flow(ax, [(10.90, 7.48), (10.90, 6.40), (12.20, 6.40)],
         label="Cuenta corriente", lx=11.50, ly=6.66)
    flow(ax, [(14.40, 9.00), (19.60, 9.00), (19.60, 8.525)])

    # ---- flujos dirección
    flow(ax, [(13.30, 6.01), (13.30, 4.71)])
    flow(ax, [(14.40, 4.30), (15.42, 4.30)])
    flow(ax, [(16.00, 4.88), (16.00, 4.95), (16.80, 4.95)],
         label="Sí", lx=16.30, ly=5.13)
    flow(ax, [(16.00, 3.72), (16.00, 3.65), (16.80, 3.65)],
         label="No", lx=16.30, ly=3.46)
    flow(ax, [(18.60, 4.95), (19.45, 4.95), (19.45, 4.82)])
    flow(ax, [(18.60, 3.65), (19.45, 3.65), (19.45, 3.78)])
    flow(ax, [(19.97, 4.30), (20.30, 4.30), (20.30, 7.675)])

    # ---- flujos sistema
    flow(ax, [(20.80, 8.10), (21.90, 8.10), (21.90, 2.70),
              (18.60, 2.70), (18.60, 2.175)])
    flow(ax, [(19.75, 1.75), (20.27, 1.75)])

    # ---- mensajes
    flow(ax, [(8.50, 11.15), (2.35, 11.15), (2.35, 8.27)],
         kind="msg", label="factura", lx=5.20, ly=11.36)
    flow(ax, [(6.60, 9.71), (6.60, 10.90), (8.50, 10.90)],
         kind="msg", label="subsanar", lx=7.55, ly=10.72)
    flow(ax, [(20.00, 8.525), (20.00, 9.55), (12.40, 9.55), (12.40, 10.575)],
         kind="msg", label="pago", lx=17.30, ly=9.72)

    # ---- notas
    note(ax, 1.50, 4.55, "En cuenta corriente, Dirección prioriza el pago", fs=5.4)
    note(ax, 1.50, 4.25, "según saldo y criticidad del insumo.", fs=5.4)
    note(ax, 1.50, 2.45, "El saldo a pagar se recalcula al registrar", fs=5.4)
    note(ax, 1.50, 2.15, "cada factura y cada pago al proveedor.", fs=5.4)

    return save(fig, OUT / "figura-1-5-1-bpmn-proveedores-pagos")


# ============================================================ LEYENDA
def leyenda():
    W, H = 9.2, 3.0
    fig, ax = canvas(W, H, (7.0, 2.3))

    columnas = [1.4, 4.6, 7.8]
    fila1, rotulo1 = 2.45, 1.90
    fila2, rotulo2 = 0.95, 0.40

    def rotulo(x, y, texto):
        ax.text(x, y, texto, ha="center", va="center", fontsize=9.0,
                color=INK, linespacing=1.05)

    # ---- fila 1: evento de inicio, tarea, compuerta
    x = columnas[0]
    ax.add_patch(Circle((x, fila1), 0.17, facecolor="white", edgecolor=INK,
                        linewidth=1.1, zorder=5))
    rotulo(x, rotulo1, "Evento de\ninicio")

    x = columnas[1]
    ax.add_patch(FancyBboxPatch((x - 0.50, fila1 - 0.21), 1.00, 0.42,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor="white", edgecolor=INK, linewidth=1.0,
                                zorder=5))
    ax.text(x, fila1, "Tarea", ha="center", va="center", fontsize=8.0,
            color=INK, zorder=6)
    rotulo(x, rotulo1, "Actividad\n(manual o de usuario)")

    x = columnas[2]
    s = 0.25
    ax.add_patch(Polygon([(x, fila1 + s), (x + s, fila1), (x, fila1 - s),
                          (x - s, fila1)], closed=True, facecolor="white",
                         edgecolor=INK, linewidth=1.0, zorder=5))
    ax.text(x, fila1, "×", ha="center", va="center", fontsize=10, color=INK,
            zorder=6)
    rotulo(x, rotulo1, "Compuerta XOR\n(decisión)")

    # ---- fila 2: flujo de secuencia, flujo de mensaje, evento de fin
    x = columnas[0]
    ax.annotate("", xy=(x + 0.50, fila2), xytext=(x - 0.50, fila2),
                arrowprops=dict(arrowstyle="-|>,head_length=0.42,head_width=0.20",
                                color=FLOW, linewidth=1.1), zorder=5)
    rotulo(x, rotulo2, "Flujo de secuencia")

    x = columnas[1]
    ax.add_line(Line2D([x - 0.50, x + 0.50], [fila2, fila2], color=MSG,
                       linewidth=1.1, linestyle=(0, (4, 2.2)), zorder=5))
    ax.annotate("", xy=(x + 0.50, fila2), xytext=(x + 0.30, fila2),
                arrowprops=dict(arrowstyle="-|>,head_length=0.42,head_width=0.20",
                                color=MSG, linewidth=1.1), zorder=6)
    rotulo(x, rotulo2, "Flujo de mensaje")

    x = columnas[2]
    ax.add_patch(Circle((x, fila2), 0.17, facecolor="white", edgecolor=INK,
                        linewidth=2.2, zorder=5))
    rotulo(x, rotulo2, "Evento de fin")

    return save(fig, OUT / "figura-1-3-1-leyenda-bpmn")


if __name__ == "__main__":
    print(leyenda())
    print(figura_facturacion())
    print(figura_proveedores())

