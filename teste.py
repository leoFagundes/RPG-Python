itensBossDG1 = {"Armadura Bad Wolfão (lendário)": [2, 2, 2],
                "Espada Bad Wolfiado (lendário)": [0, 0, 0],
                "Adaga de presa de lobo (raro)": [0, 0, 0],
                "Espada quebrada (comum)": [0, 0, 0],
                "Armadura furada (comum)": [0, 0, 0]}

inventario = {
            "espada": 
                {},
            "aramdura": 
                {},
            "elmo": 
                {}
             }

print(inventario["espada"])

inventario["espada"] = itensBossDG1["Adaga de presa de lobo (raro)"]

print(inventario["espada"])

inventario["espada"] = itensBossDG1["Armadura Bad Wolfão (lendário)"]

print(inventario["espada"])

