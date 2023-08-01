import os

TMP_DIR = os.path.join(os.getcwd(), "tmp")
if not os.path.exists(TMP_DIR):
    os.makedirs(TMP_DIR)
