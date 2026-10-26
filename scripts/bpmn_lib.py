# -*- coding: utf-8 -*-
"""Utilidades mínimas para dibujar diagramas BPMN 2.0 con matplotlib."""

import textwrap
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Rectangle
from matplotlib.lines import Line2D
from matplotlib import font_manager

# ---------------------------------------------------------------- tipografía
ARIAL = Path(r"C:\Windows\Fonts\arial.ttf")
if ARIAL.exists():
    font_manager.fontManager.addfont(str(ARIAL))
    FAMILY = "Arial"
else:  # respaldo
    FAMILY = "DejaVu Sans"

plt.rcParams.update({
    "font.family": FAMILY,
    "font.size": 7,
    "svg.fonttype": "none",
})

# ---------------------------------------------------------------- paleta
INK = "#1f2933"
MUTED = "#5b6770"
LANE_TINT = "#f5f7fa"
LANE_ALT = "#eef2f7"
POOL_EXT = "#e9edf2"
POOL_INT = "#ffffff"
TASK_FILL = "#ffffff"
ACCENT = "#1f4e79"
FLOW = "#2f3b45"
MSG = "#6b7785"

# ---------------------------------------------------------------- lienzo


def canvas(w, h, figsize, dpi=300):
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    ax.set_xlim(0, w)
    ax.set_ylim(0, h)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.subplots_adjust(left=0.005, right=0.995, top=0.995, bottom=0.005)
    return fig, ax


def _wrap(text, width):
    return "\n".join(textwrap.wrap(text, width=width)) if text else ""


# ---------------------------------------------------------------- pools y lanes


def pool(ax, x, y, w, h, label, external=False, header=0.62, fs=8.2):
    face = POOL_EXT if external else POOL_INT
    ax.add_patch(Rectangle((x, y), w, h, facecolor=face, edgecolor=INK,
                           linewidth=1.15, zorder=1))
    ax.add_patch(Rectangle((x, y), header, h, facecolor="#dbe3ec" if not external else "#d3dae3",
                           edgecolor=INK, linewidth=1.15, zorder=2))
    ax.text(x + header / 2, y + h / 2, label, rotation=90, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=INK, zorder=3)


def lane(ax, x, y, w, h, label, tint=None, fs=7.6):
    if tint:
        ax.add_patch(Rectangle((x, y), w, h, facecolor=tint, edgecolor="none", zorder=0.5))
    ax.plot([x, x + w], [y, y], color=INK, linewidth=0.8, zorder=2)
    ax.plot([x, x + w], [y + h, y + h], color=INK, linewidth=0.8, zorder=2)
    ax.text(x + 0.30, y + h / 2, label, rotation=90, ha="center", va="center",
            fontsize=fs, color=MUTED, zorder=3)


# ---------------------------------------------------------------- elementos


def task(ax, cx, cy, label, w=1.8, h=0.82, kind="Tarea", fs=7.0, chars=21):
    ax.add_patch(FancyBboxPatch((cx - w / 2, cy - h / 2), w, h,
                                boxstyle="round,pad=0.02,rounding_size=0.10",
                                facecolor=TASK_FILL, edgecolor=INK, linewidth=1.0, zorder=4))
    ax.text(cx, cy + 0.11, _wrap(label, chars), ha="center", va="center",
            fontsize=fs, color=INK, zorder=5, linespacing=1.05)
    ax.text(cx, cy - h / 2 + 0.09, kind, ha="center", va="center",
            fontsize=4.4, color=MUTED, style="italic", zorder=5)


def event(ax, cx, cy, label, kind="start", r=0.17, fs=6.0, dx=0.0, dy=-0.30, ha="center"):
    lw = 2.2 if kind == "end" else 1.15
    ax.add_patch(Circle((cx, cy), r, facecolor="white", edgecolor=INK,
                        linewidth=lw, zorder=5))
    if kind == "message":
        # sobre (evento de mensaje)
        ax.add_patch(Rectangle((cx - r * 0.62, cy - r * 0.42), r * 1.24, r * 0.84,
                               facecolor="none", edgecolor=INK, linewidth=0.8, zorder=6))
        ax.plot([cx - r * 0.62, cx, cx + r * 0.62],
                [cy + r * 0.42, cy - r * 0.05, cy + r * 0.42],
                color=INK, linewidth=0.8, zorder=6)
    if label:
        ax.text(cx + dx, cy + dy, label, ha=ha, va="center", fontsize=fs,
                color=INK, zorder=7, linespacing=1.02)


def gateway(ax, cx, cy, label, s=0.60, fs=5.9, chars=17, dy=-0.86, dx=0.0):
    pts = [(cx, cy + s), (cx + s, cy), (cx, cy - s), (cx - s, cy)]
    ax.add_patch(Polygon(pts, closed=True, facecolor="white", edgecolor=INK,
                         linewidth=1.0, zorder=4))
    ax.text(cx, cy, "×", ha="center", va="center", fontsize=11, color=INK, zorder=5)
    ax.text(cx + dx, cy + dy, _wrap(label, chars), ha="center", va="center",
            fontsize=fs, color=INK, zorder=5, linespacing=1.02)


def _arrowhead(ax, p0, p1, color, lw):
    ax.annotate("", xy=p1, xytext=p0,
                arrowprops=dict(arrowstyle="-|>,head_length=0.42,head_width=0.20",
                                color=color, linewidth=lw, shrinkA=0, shrinkB=0),
                zorder=6)


def flow(ax, pts, label=None, kind="seq", lw=1.0, fs=5.7, lx=None, ly=None, ha="center"):
    color = FLOW if kind == "seq" else MSG
    style = (0, (4, 2.2)) if kind == "msg" else "solid"
    for a, b in zip(pts[:-1], pts[1:]):
        ax.add_line(Line2D([a[0], b[0]], [a[1], b[1]], color=color, linewidth=lw,
                           linestyle=style, solid_capstyle="butt", zorder=3.5))
    _arrowhead(ax, pts[-2], pts[-1], color, lw)
    if label:
        if lx is None or ly is None:
            a, b = pts[0], pts[1]
            lx = (a[0] + b[0]) / 2
            ly = (a[1] + b[1]) / 2
        ax.text(lx, ly, label, ha=ha, va="center", fontsize=fs, color=color,
                bbox=dict(boxstyle="round,pad=0.15", facecolor="white",
                          edgecolor="none", alpha=0.92), zorder=7)


def note(ax, x, y, text, fs=5.8, w=None):
    ax.text(x, y, text, ha="left", va="center", fontsize=fs, color=MUTED,
            style="italic", zorder=7, linespacing=1.1)


def save(fig, base):
    base = Path(base)
    base.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(base.with_suffix(".png"), dpi=300, facecolor="white",
                bbox_inches="tight", pad_inches=0.04)
    fig.savefig(base.with_suffix(".svg"), facecolor="white",
                bbox_inches="tight", pad_inches=0.04)
    plt.close(fig)
    return base.with_suffix(".png")
