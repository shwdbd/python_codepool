import os


def list_files(file_folder: str) -> list:
    """ 列出文件夹下所有文件名 """
    for f in os.listdir(file_folder):
        print(f)


if __name__ == "__main__":
    dir_path = 'D:/000 软件开发'
    list_files(dir_path)