import pandas as pd
import os
#pip install pandas openyxl

data = {
    "Nombre": ["Ana", "Luis", "Pedro"],
    "Edad": [25, 30, 22]
}

df = pd.DataFrame(data)

#Guardarlo en excel
file = "nuevo_archivo.xlsx"
df.to_excel(file, index=False)
os.startfile(file)