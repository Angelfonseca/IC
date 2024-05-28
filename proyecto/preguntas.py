import tkinter as tk
from tkinter import ttk
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def crear_sistema():
    # Crear el sistema de control
    humidity_range = np.arange(0, 101, 1)
    soilHum_range = np.arange(0, 101, 1)
    temperature_range = np.arange(0, 43, 1)
    output_range = np.arange(0, 101, 1)
    precipitation_range = np.arange(0, 101, 1)

    # Crear variables difusas para la humedad, la humedad del suelo y la temperatura
    humidity = ctrl.Antecedent(humidity_range, 'Humidity')
    humidity['Alta'] = fuzz.trimf(humidity_range, [70, 100, 100])
    humidity['Media'] = fuzz.trimf(humidity_range, [30, 50, 70])
    humidity['Baja'] = fuzz.trimf(humidity_range, [0, 0, 30])

    soilHum = ctrl.Antecedent(soilHum_range, 'SoilHumidity')
    soilHum['Alta'] = fuzz.trimf(soilHum_range, [70, 100, 100])
    soilHum['Media'] = fuzz.trimf(soilHum_range, [30, 50, 70])
    soilHum['Baja'] = fuzz.trimf(soilHum_range, [0, 0, 30])

    temperature = ctrl.Antecedent(temperature_range, 'Temperature')
    temperature['Alta'] = fuzz.trimf(temperature_range, [25, 43, 43])
    temperature['Media'] = fuzz.trimf(temperature_range, [9, 25, 43])
    temperature['Baja'] = fuzz.trimf(temperature_range, [0, 9, 25])

    precipitation = ctrl.Antecedent(precipitation_range, 'Precipitation')
    precipitation['Sin lluvia'] = fuzz.trimf(precipitation_range, [0, 0, 50])
    precipitation['Lluvia leve'] = fuzz.trimf(precipitation_range, [25, 44, 73])
    precipitation['Lluvia intensa'] = fuzz.trimf(precipitation_range, [50, 70, 100])

    # Crear la variable de salida para el riego
    output = ctrl.Consequent(output_range, 'Riego')
    output['No regar'] = fuzz.trimf(output_range, [0, 0, 50])
    output['Poco riego'] = fuzz.trimf(output_range, [25, 50, 75])
    output['Riego normal'] = fuzz.trimf(output_range, [50, 100, 100])

    rule1 = ctrl.Rule(precipitation['Lluvia leve'] | precipitation['Lluvia intensa'], output['No regar'])
    rule2 = ctrl.Rule(humidity['Alta'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Sin lluvia'], output['No regar'])
    rule3 = ctrl.Rule(humidity['Alta'] & soilHum['Media'] & temperature['Alta'] & precipitation['Sin lluvia'], output['No regar'])
    rule4 = ctrl.Rule(humidity['Alta'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Sin lluvia'], output['No regar'])
    rule5 = ctrl.Rule(humidity['Alta'] & soilHum['Alta'] & temperature['Media'] & precipitation['Sin lluvia'], output['No regar'])
    rule6 = ctrl.Rule(humidity['Alta'] & soilHum['Media'] & temperature['Media'] & precipitation['Sin lluvia'], output['No regar'])
    rule7 = ctrl.Rule(humidity['Alta'] & soilHum['Baja'] & temperature['Media'] & precipitation['Sin lluvia'], output['No regar'])
    rule8 = ctrl.Rule(humidity['Alta'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Sin lluvia'], output['No regar'])
    rule9 = ctrl.Rule(humidity['Alta'] & soilHum['Media'] & temperature['Baja'] & precipitation['Sin lluvia'], output['No regar'])
    rule10 = ctrl.Rule(humidity['Alta'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Sin lluvia'], output['No regar'])
    rule11 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule12 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Alta'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule13 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule14 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Media'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule15 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Media'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule16 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Media'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule17 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule18 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Baja'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule19 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Sin lluvia'], output['Poco riego'])
    rule20 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule21 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Alta'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule22 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule23 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Media'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule24 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Media'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule25 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Media'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule26 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule27 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Baja'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule28 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Sin lluvia'], output['Riego normal'])
    rule29 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule30 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule31 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule32 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule33 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule34 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule35 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule36 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule37 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule38 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule39 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule40 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule41 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule42 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule43 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule44 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule45 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule46 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule47 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule48 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule49 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule50 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule51 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule52 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule53 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule54 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule55 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule56 = ctrl.Rule(humidity['Alta'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule57 = ctrl.Rule(humidity['Alta'] & soilHum['Media'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule58 = ctrl.Rule(humidity['Alta'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Lluvia intensa'], output['No regar'])
    rule59 = ctrl.Rule(humidity['Alta'] & soilHum['Alta'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule60 = ctrl.Rule(humidity['Alta'] & soilHum['Media'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule61 = ctrl.Rule(humidity['Alta'] & soilHum['Baja'] & temperature['Media'] & precipitation['Lluvia intensa'], output['No regar'])
    rule62 = ctrl.Rule(humidity['Alta'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule63 = ctrl.Rule(humidity['Alta'] & soilHum['Media'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule64 = ctrl.Rule(humidity['Alta'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Lluvia intensa'], output['No regar'])
    rule65 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule66 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule67 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule68 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule69 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule70 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule71 = ctrl.Rule(humidity['Media'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule72 = ctrl.Rule(humidity['Media'] & soilHum['Media'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule73 = ctrl.Rule(humidity['Media'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule74 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule75 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule76 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Alta'] & precipitation['Lluvia leve'], output['No regar'])
    rule77 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule78 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule79 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Media'] & precipitation['Lluvia leve'], output['No regar'])
    rule80 = ctrl.Rule(humidity['Baja'] & soilHum['Alta'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule81 = ctrl.Rule(humidity['Baja'] & soilHum['Media'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])
    rule82 = ctrl.Rule(humidity['Baja'] & soilHum['Baja'] & temperature['Baja'] & precipitation['Lluvia leve'], output['No regar'])

    system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20, rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30, rule31, rule32, rule33, rule34, rule35, rule36, rule37, rule38, rule39, rule40, rule41, rule42, rule43, rule44, rule45, rule46, rule47, rule48, rule49, rule50, rule51, rule52, rule53, rule54, rule55, rule56, rule57, rule58, rule59, rule60, rule61, rule62, rule63, rule64, rule65, rule66, rule67, rule68, rule69, rule70, rule71, rule72, rule73, rule74, rule75, rule76, rule77, rule78, rule79, rule80, rule81, rule82])
    return ctrl.ControlSystemSimulation(system)

def analizar_datos():
    controller = crear_sistema()
    try:
        controller.input['Humidity'] = float(entry_humidity.get())
        controller.input['SoilHumidity'] = float(entry_soilHum.get())
        controller.input['Temperature'] = float(entry_temperature.get())
        controller.input['Precipitation'] = float(entry_precipitation.get())
        controller.compute()
        result = controller.output['Riego']
        if result < 50:
            decision = "No regar"
        else:
            decision = "Regar"
        result_label.config(text=f"Resultado: {decision}")
    except ValueError as e:
        result_label.config(text="Error: Verifica que todos los campos sean números válidos.")
    except KeyError as e:
        result_label.config(text=f"Error: {e}")

root = tk.Tk()
root.title("Formulario de Análisis Difuso")

# Campos de entrada
ttk.Label(root, text="Humedad:").grid(column=0, row=0, padx=10, pady=10)
entry_humidity = ttk.Entry(root)
entry_humidity.grid(column=1, row=0, padx=10, pady=10)

ttk.Label(root, text="Humedad del suelo:").grid(column=0, row=1, padx=10, pady=10)
entry_soilHum = ttk.Entry(root)
entry_soilHum.grid(column=1, row=1, padx=10, pady=10)

ttk.Label(root, text="Temperatura:").grid(column=0, row=2, padx=10, pady=10)
entry_temperature = ttk.Entry(root)
entry_temperature.grid(column=1, row=2, padx=10, pady=10)

ttk.Label(root, text="Precipitación:").grid(column=0, row=3, padx=10, pady=10)
entry_precipitation = ttk.Entry(root)
entry_precipitation.grid(column=1, row=3, padx=10, pady=10)

# Botón para analizar los datos
analyze_button = ttk.Button(root, text="Analizar", command=analizar_datos)
analyze_button.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

# Etiqueta para mostrar el resultado
result_label = ttk.Label(root, text="Resultado: ")
result_label.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

root.mainloop()