import os
import pandas as pd
import matplotlib.pyplot as plt

# Указываем папку с моделями
models_folder = os.path.join(os.path.dirname(__file__), 'modelsStressStrain')
results_folder = os.path.join(os.path.dirname(__file__), 'StressStrainCombine')

# Создаем папки, если их нет
os.makedirs(models_folder, exist_ok=True)
os.makedirs(results_folder, exist_ok=True)


def plot_combined_stress_strain(filepaths):
    # Создаем фигуру для графика без фиксированного размера
    plt.figure(figsize=(10, 6))

    # Цвета для разных графиков
    colors = plt.cm.tab10.colors

    # Обрабатываем каждый файл
    for i, filepath in enumerate(filepaths):
        try:
            # Читаем файл с помощью openpyxl
            df = pd.read_excel(filepath, engine='openpyxl')
            filename = os.path.basename(filepath)
            filename_no_ext = os.path.splitext(filename)[0]

            # Проверяем наличие нужных столбцов (с учетом возможных разных регистров)
            df.columns = df.columns.str.lower()  # Приводим к нижнему регистру
            if all(col in df.columns for col in ['деформация', 'напряжение']):
                # Удаляем строки с пустыми значениями
                df = df.dropna(subset=['деформация', 'напряжение'])
                # Рисуем график с подписью (имя файла)
                plt.plot(df['деформация'], df['напряжение'],
                         color=colors[i % len(colors)],
                         linewidth=2,
                         label=filename_no_ext)

        except Exception as e:
            print(f"Ошибка при обработке файла {filepath}: {e}")

    # Настраиваем график
    plt.title('Совмещенная диаграмма напряжение-деформация', fontsize=16)
    plt.xlabel('Деформация (ε)', fontsize=14)
    plt.ylabel('Напряжение (σ), Па', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    # Добавляем легенду только если есть что отображать
    if plt.gca().has_data():
        plt.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')
    else:
        print("Предупреждение: Нет данных для отображения на графике")

    # Автоматическое масштабирование осей
    plt.autoscale(enable=True, axis='both', tight=True)

    # Сохраняем график
    output_path = os.path.join(results_folder, 'combined_stress_strain.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Совмещенный график сохранен как '{output_path}'")


# Проверяем наличие openpyxl
try:
    import openpyxl

    openpyxl_available = True
except ImportError:
    openpyxl_available = False
    print("Ошибка: Необходимо установить библиотеку 'openpyxl'. Выполните команду: pip install openpyxl")

# Собираем все Excel файлы в папке modelsStressStrain
excel_files = []
if openpyxl_available:
    for filename in os.listdir(models_folder):
        if filename.lower().endswith(('.xlsx', '.xls')):
            filepath = os.path.join(models_folder, filename)
            print(f"Найден файл для обработки: {filename}")
            excel_files.append(filepath)

    if excel_files:
        plot_combined_stress_strain(excel_files)
        print("Обработка всех файлов завершена.")
    else:
        print("В папке modelsStressStrain не найдено Excel файлов для обработки.")