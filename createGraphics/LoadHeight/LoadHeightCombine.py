import os
import pandas as pd
import matplotlib.pyplot as plt


project_dir = os.path.dirname(os.path.dirname(__file__))  # Корневая папка проекта

# Corrected path construction - using os.path.join for all parts
source_folder = os.path.join(project_dir, 'LoadHeight', 'modelsLoadHeight')  # Папка с Excel-файлами
output_folder = os.path.join(project_dir, 'LoadHeight', 'LoadHeightCombine')  # Папка для сохранения графика


os.makedirs(output_folder, exist_ok=True)


def plot_combined_load_height():
    plt.figure(figsize=(12, 8))

    # Цвета для графиков (можно изменить)
    colors = ['blue', 'red', 'green', 'purple', 'orange', 'cyan', 'magenta', 'brown']
    line_styles = ['-', '--', '-.', ':']  # Разные стили линий

    # Счётчики для цветов и стилей
    color_idx = 0
    style_idx = 0

    # Перебираем файлы в папке
    for filename in sorted(os.listdir(source_folder)):
        if filename.endswith(('.xlsx', '.xls')):
            filepath = os.path.join(source_folder, filename)
            try:
                df = pd.read_excel(filepath)
                filename_no_ext = os.path.splitext(filename)[0]  # Имя без расширения

                if all(col in df.columns for col in ['Высота', 'Нагрузка']):
                    # Выбираем цвет и стиль линии
                    current_color = colors[color_idx % len(colors)]
                    current_style = line_styles[style_idx % len(line_styles)]

                    # Строим график
                    plt.plot(
                        df['Высота'],
                        abs(df['Нагрузка']),
                        linestyle=current_style,
                        linewidth=2,
                        color=current_color,
                        label=filename_no_ext  # Подпись в легенде
                    )

                    # Переключаем цвет и стиль
                    color_idx += 1
                    if color_idx % len(colors) == 0:
                        style_idx += 1

            except Exception as e:
                print(f"❌ Ошибка в файле {filename}: {e}")

    # Настройки общего графика
    plt.title('Совмещённые графики "Нагрузка-Перемещение"', fontsize=14)
    plt.xlabel('Высота', fontsize=12)
    plt.ylabel('Нагрузка', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=9, bbox_to_anchor=(1.05, 1), loc='upper left')  # Легенда справа

    # Сохраняем в папку LoadHeightCombine
    output_path = os.path.join(output_folder, 'combined_load_height.png')
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()


# Запускаем
if __name__ == "__main__":
    plot_combined_load_height()