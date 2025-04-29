import pandas as pd
from pathlib import Path

project_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
res_dir = project_dir / "res"

txt_files = list(res_dir.glob("*.txt"))
if not txt_files:
    raise FileNotFoundError(f"В папке {res_dir} не найдено файлов .txt")

input_file = txt_files[0]
print(f"Используем файл: {input_file}")

# Получаем имя файла без расширения и добавляем '_processed_data.xlsx'
output_filename = f"{input_file.stem}_processed_data.xlsx"
output_file = res_dir / output_filename

df = pd.read_csv(input_file, sep='\s+', skiprows=3, engine='python')

selected_columns = df.iloc[:, [1, 3, 8]]
selected_columns.columns = ['CAREA', 'Y_Coordinate', 'Нагрузка']

def process_column(column):
    return pd.to_numeric(column[column != 'NoValue'], errors='coerce')

for col in selected_columns.columns:
    selected_columns[col] = process_column(selected_columns[col])

print("Укажите начальное значение высоты в м (пример 1м = 0.001):\n")
initial_height = float(input())
selected_columns['Высота'] = initial_height + selected_columns['Y_Coordinate']

selected_columns.dropna(how='all', inplace=True)

for col in selected_columns.columns:
    non_nan_values = selected_columns[col].dropna().values
    selected_columns[col] = pd.Series(non_nan_values)

selected_columns.dropna(how='all', inplace=True)

selected_columns.to_excel(output_file, index=False, header=True)

print(f"Данные сохранены в {output_filename}")
