import os


def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError as e:
        print(e)