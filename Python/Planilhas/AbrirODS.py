import pandas as pd

# Pandas lêem a planilha do Excel pelo nome
ler = pd.read_excel('X:/DEV/integraFabric/Python/Planilhas/Tear01.ods', sheet_name="Sheet1")
print(ler)