import os
import shutil
caminho_novo = str("C:/Riot Games/League/pasta_new")
try:
    os.makedirs(caminho_novo)
except FileExistsError:
    print("O arquivo já existe")
    print(caminho_novo)

