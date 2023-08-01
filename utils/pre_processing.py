import os


def pre_processing(file: str):
    if not os.path.isfile(file):
        with open(file, 'w') as f:
            f.close()
            pass
