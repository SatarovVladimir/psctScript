# import os
# import pandas as pd
# import matplotlib.pyplot as plt
#
# res_folder = os.path.join(os.path.dirname(__file__), 'res')
#
# if not os.path.exists(res_folder):
#     os.makedirs(res_folder)
#
# def process_excel_file(filepath):
#     try:
#         df = pd.read_excel(filepath)
#         filename = os.path.basename(filepath)
#         filename_no_ext = os.path.splitext(filename)[0]
#
#         if all(col in df.columns for col in ['деформация', 'напряжение']):
#             plt.figure(figsize=(10, 6))
#             plt.plot(df['деформация'], df['напряжение'], 'b-', linewidth=2)
#             plt.title('Диаграмма напряжение-деформация', fontsize=14)
#             plt.xlabel('Деформация (ε)', fontsize=12)
#             plt.ylabel('Напряжение (σ), Па', fontsize=12)
#
#             # Устанавливаем пределы и шаг для оси OX
#             plt.xlim(0, 0.35)
#             plt.xticks([x / 100 for x in range(0, 36, 5)])  # 0.00, 0.05, 0.10, ..., 0.35
#             plt.grid(True, linestyle='--', alpha=0.7)
#
#             output_path = os.path.join(res_folder, f'{filename_no_ext}_stress_strain.png')
#             plt.savefig(output_path, dpi=300, bbox_inches='tight')
#             plt.close()
#             print(f"График сохранен как '{output_path}'")
#
#         if all(col in df.columns for col in ['Высота', 'Нагрузка']):
#             plt.figure(figsize=(10, 6))
#             plt.plot(df['Высота'], abs(df['Нагрузка']), 'b-', linewidth=2)
#             plt.title('Диаграмма нагрузка-перемещение', fontsize=14)
#             plt.ylabel('Нагрузка', fontsize=12)
#             plt.xlabel('Высота', fontsize=12)
#             plt.grid(True, linestyle='--', alpha=0.7)
#
#             output_path = os.path.join(res_folder, f'{filename_no_ext}_load_height.png')
#             plt.savefig(output_path, dpi=300, bbox_inches='tight')
#             plt.close()
#             print(f"График сохранен как '{output_path}'")
#
#     except Exception as e:
#         print(f"Ошибка при обработке файла {filepath}: {e}")
#
#
# for filename in os.listdir(res_folder):
#     if filename.endswith(('.xlsx', '.xls')):
#         filepath = os.path.join(res_folder, filename)
#         print(f"Обработка файла: {filename}")
#         process_excel_file(filepath)
#
# print("Обработка всех файлов завершена.")

import os
import pandas as pd
import matplotlib.pyplot as plt

# Определяем пути к папкам
project_dir = os.path.dirname(os.path.dirname(__file__))  # Получаем путь к папке 'проект'
source_folder = os.path.join(project_dir, 'modelsGraphic')  # Папка с исходными Excel-файлами
output_folder = os.path.join(project_dir, 'resultGraphic')  # Папка для графиков

# Создаем папку для результатов, если ее нет
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def process_excel_file(filepath):
    try:
        df = pd.read_excel(filepath)
        filename = os.path.basename(filepath)
        filename_no_ext = os.path.splitext(filename)[0]

        if all(col in df.columns for col in ['деформация', 'напряжение']):
            plt.figure(figsize=(10, 6))
            plt.plot(df['деформация'], df['напряжение'], 'b-', linewidth=2)
            plt.title('Диаграмма напряжение-деформация', fontsize=14)
            plt.xlabel('Деформация (ε)', fontsize=12)
            plt.ylabel('Напряжение (σ), Па', fontsize=12)

            # Устанавливаем пределы и шаг для оси OX
            plt.xlim(0, 0.35)
            plt.xticks([x / 100 for x in range(0, 36, 5)])  # 0.00, 0.05, 0.10, ..., 0.35
            plt.grid(True, linestyle='--', alpha=0.7)

            output_path = os.path.join(output_folder, f'{filename_no_ext}_stress_strain.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"График сохранен как '{output_path}'")

        if all(col in df.columns for col in ['Высота', 'Нагрузка']):
            plt.figure(figsize=(10, 6))
            plt.plot(df['Высота'], abs(df['Нагрузка']), 'b-', linewidth=2)
            plt.title('Диаграмма нагрузка-перемещение', fontsize=14)
            plt.ylabel('Нагрузка', fontsize=12)
            plt.xlabel('Высота', fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.7)

            output_path = os.path.join(output_folder, f'{filename_no_ext}_load_height.png')
            plt.savefig(output_path, dpi=300, bbox_inches='tight')
            plt.close()
            print(f"График сохранен как '{output_path}'")

    except Exception as e:
        print(f"Ошибка при обработке файла {filepath}: {e}")

# Обрабатываем все Excel файлы в исходной папке
for filename in os.listdir(source_folder):
    if filename.endswith(('.xlsx', '.xls')):
        filepath = os.path.join(source_folder, filename)
        print(f"Обработка файла: {filename}")
        process_excel_file(filepath)

print("Обработка всех файлов завершена.")