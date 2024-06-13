import pandas as pd
import matplotlib.pyplot as plt
import os

ruta = os.getcwd() + "\\Documents\\"
excel = pd.read_excel(ruta + "Listados Excel.xlsx",
        sheet_name="Primer Semestre", header=0)

meses = ["enero", "febrero", "marzo"]
listado = excel[excel.Mes.isin(meses)]

tabla = pd.crosstab(index=listado.Comercial,
	    columns=listado.Mes, values=listado.Unidades, aggfunc="sum", normalize="index")
print("\nLista de ventas de comerciales normalizada...\n", tabla)

tabla.plot(kind="line")
plt.title("Ventas 1er trimestre Normalizadas")
plt.show()
