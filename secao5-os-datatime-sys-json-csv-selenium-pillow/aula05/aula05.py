import os
import shutil

caminho_original = r'C:\Users\Skull\OneDrive\Área de Trabalho\WarRiders'
caminho_novo = r'C:\Users\Skull\OneDrive\Área de Trabalho\WarRiders2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_patch = os.path.join(caminho_novo, file)

        if '.txt' in file:
            os.remove(new_file_patch)


