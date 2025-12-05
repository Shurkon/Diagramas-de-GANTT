#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- Config ---
inicio = datetime(2025, 11, 10)

# --- Tareas ---
tareas = [
    ("Fase 1: Preparación y planificación", None),
    ("Análisis de seguridad en la zona del Ciber", 2),
    ("Diseño de red y segmentación por VLANs", 1),
    ("Seleccion de equipamiento necesario", 3),

    ("Fase 2: Implementación de seguridad", None),
    ("Configuración de firewalls y reglas", 5),
    ("Aplicación de la estructura de VLANs", 1),
    ("Implementación de panel de monitoreo", 4),
    ("Manual de actuación ante incidentes", 2),

    ("Fase 3: Automatización de usuarios", None),
    ("Implementación del dominio AD", 2),
    ("Automatización con N8N", 2),

    ("Fase 4: Web y reservas", None),
    ("Desarrollo de la web de reservas", 3),
    ("Integración de web con sistema de usuarios", 2),

    ("Fase 5: Funciones adicionales", None),
    ("Sistema de recompensas por logros", 3),
]

# --- Calcular fechas ---
fechas = []
current = inicio

for nombre, dur in tareas:
    if dur is not None:
        start = current
        end = start + timedelta(days=dur)
        fechas.append([nombre, start, end])
        current = end
    else:
        fechas.append([nombre, None, None])

df = pd.DataFrame(fechas, columns=["Tarea", "Inicio", "Fin"])
df = df.dropna(subset=["Inicio"])

# --- Gráfico Gantt ---
plt.figure(figsize=(12, 8))

y_positions = range(len(df))

for i, row in enumerate(df.itertuples()):
    duracion = (row.Fin - row.Inicio).days
    plt.barh(i, duracion, left=row.Inicio, color="#4C72B0")
    # Línea que añadía la fecha → comentada
    # plt.text(row.Inicio + timedelta(hours=12), i, row.Inicio.strftime("%d-%b"), va='center', color='white')

# Ocultar fechas del eje X si quieres que no aparezcan abajo también:
# plt.gca().set_xticks([])
# plt.gca().set_xticklabels([])

plt.yticks(y_positions, df["Tarea"])
plt.title("Diagrama de Gantt - Proyecto Ciber", fontsize=14)
plt.tight_layout()
plt.show()

