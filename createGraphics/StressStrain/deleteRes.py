import os
import shutil


def clear_res_folders():
    folders_to_clear = [
        os.path.join(os.path.dirname(__file__), 'modelsStressStrain'),
        os.path.join(os.path.dirname(__file__), 'StressStrainCombine')
    ]

    for folder in folders_to_clear:
        if not os.path.exists(folder):
            print(f"Папка {folder} не существует.")
            continue

        try:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print(f"Не удалось удалить {file_path}. Причина: {e}")

            print(f"Содержимое папки {folder} успешно удалено.")
        except Exception as e:
            print(f"Произошла ошибка при очистке папки {folder}: {e}")


if __name__ == "__main__":
    clear_res_folders()