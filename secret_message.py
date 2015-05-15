__author__ = 'jannie'

import os


def rename_files():
    secret_path = r"C:\Users\abc\PycharmProjects\udacity\secret_message"
    for file_name in os.listdir(secret_path):
        new_name = file_name.translate(None, "0123456789")
        os.rename(os.path.join(secret_path, file_name), os.path.join(secret_path, new_name))

rename_files()
