import pandas as pd
import numpy as np
import os
from pathlib import Path

project_root = os.path.dirname(os.path.abspath(__file__))
res_folder = os.path.join(project_root, 'res')

# Ищем все txt файлы в папке 'res'
txt_files = list(Path(res_folder).glob('*.txt'))

if not txt_files:
    raise FileNotFoundError(
        f"Не найдены txt файлы в папке {res_folder}."
    )

# Берем первый txt файл и формируем имя обработанного файла
base_name = txt_files[0].stem  # Имя txt файла без расширения
processed_file_name = f"{base_name}_processed_data.xlsx"
input_file = Path(res_folder) / processed_file_name

if not input_file.exists():
    raise FileNotFoundError(
        f"Не найден файл {input_file}. "
        "Убедитесь, что первая программа отработала корректно."
    )

print(f"Используем файл: {input_file}")

df = pd.read_excel(input_file)

# Проверяем наличие нужных столбцов
required_columns = ['Нагрузка', 'CAREA', 'Высота']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"Отсутствуют столбцы: {missing_columns}")

# Вычисляем деформацию и напряжение
H0 = df['Высота'].iloc[0]
df['деформация'] = np.log(H0 / df['Высота'])
df = df.iloc[1:]  # Удаляем первую строку (исходная высота)
df['напряжение'] = np.abs(df['Нагрузка'] / df['CAREA'])

# Формируем имя выходного файла
output_file_name = f"{base_name}_deformation_results.xlsx"
output_file = os.path.join(res_folder, output_file_name)

# Сохраняем результаты в новый файл
df[['деформация', 'напряжение']].to_excel(output_file, index=False)
print(f"Файл успешно сохранён: {output_file}")