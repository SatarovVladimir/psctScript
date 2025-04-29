import os
import shutil


def clear_res_folder():
    res_folder = os.path.join(os.path.dirname(__file__), 'res')

    if not os.path.exists(res_folder):
        print(f"Папка {res_folder} не существует.")
        return

    try:
        for filename in os.listdir(res_folder):
            file_path = os.path.join(res_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Не удалось удалить {file_path}. Причина: {e}")

        print(f"Содержимое папки {res_folder} успешно удалено.")
    except Exception as e:
        print(f"Произошла ошибка при очистке папки: {e}")


if __name__ == "__main__":
    clear_res_folder()