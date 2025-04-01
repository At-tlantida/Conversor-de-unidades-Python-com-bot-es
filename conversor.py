import tkinter as tk
from tkinter import ttk

# Função de conversão de unidades
def convert():
    try:
        value = float(entry_value.get())
        conversion = conversion_type.get()
        result = conversions[conversion](value)
        label_result.config(text=f"Resultado: {result:.4f}")
    except ValueError:
        label_result.config(text="Digite um valor válido")

# Conversões por categoria
conversion_categories = {
    "Peso": {
        "kg → lb": lambda x: x * 2.20462,
        "lb → kg": lambda x: x / 2.20462,
    },
    "Distância": {
        "m → in": lambda x: x * 39.3701,
        "in → m": lambda x: x / 39.3701,
        "cm → in": lambda x: x / 2.54,
        "in → cm": lambda x: x * 2.54,
        "km → mi": lambda x: x * 0.621371,
        "mi → km": lambda x: x / 0.621371,
    },
    "Volume": {
        "L → gal (US)": lambda x: x * 0.264172,
        "gal (US) → L": lambda x: x / 0.264172,
        "m³ → gal (US)": lambda x: x * 264.172,
        "gal (US) → m³": lambda x: x / 264.172,
    },
    "Temperatura": {
        "°C → °F": lambda x: (x * 9/5) + 32,
        "°F → °C": lambda x: (x - 32) * 5/9,
    },
    "Força": {
        "N → lbf": lambda x: x * 0.224809,
        "lbf → N": lambda x: x / 0.224809,
    },
    "Energia": {
        "J → cal": lambda x: x / 4.184,
        "cal → J": lambda x: x * 4.184,
    },
    "Área": {
        "m² → ft²": lambda x: x * 10.7639,
        "ft² → m²": lambda x: x / 10.7639,
    },
}

# Unificando todas as conversões
conversions = {k: v for cat in conversion_categories.values() for k, v in cat.items()}

# Atualiza as opções do combobox conforme a categoria
def update_options(category):
    options = list(conversion_categories[category].keys())
    conversion_type.config(values=options)
    conversion_type.set(options[0])

# Interface Gráfica
root = tk.Tk()
root.title("Conversor de Unidades do Jão")
root.geometry("800x360")
root.config(bg="#f7f4ea")

frame = tk.Frame(root, bg="#f7f4ea")
frame.pack(pady=10)

tk.Label(frame, text="Valor:", bg="#f7f4ea").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_value = tk.Entry(frame, width=20)
entry_value.grid(row=0, column=1, padx=10, pady=5)

# Categoria de conversão
category_frame = tk.Frame(root, bg="#f7f4ea")
category_frame.pack(pady=5)
tk.Label(category_frame, text="Categoria:", bg="#f7f4ea").pack(side="left", padx=5)

for category in conversion_categories.keys():
    tk.Button(category_frame, text=category, command=lambda c=category: update_options(c), bg="#ccc", width=10).pack(side="left", padx=2)

# Tipo de conversão
tk.Label(root, text="Conversão:", bg="#f7f4ea").pack(pady=(10,0))
conversion_type = ttk.Combobox(root, values=[], state="readonly", width=35)
conversion_type.pack(pady=5)
update_options("Peso")  # Inicializa com a categoria Peso

# Botão converter
convert_button = tk.Button(root, text="Converter", command=convert, bg="#928686", fg="white", width=20)
convert_button.pack(pady=10)

# Resultado
label_result = tk.Label(root, text="Resultado: ", font=("Arial", 14), bg="#f7f4ea")
label_result.pack(pady=10)

root.mainloop()
