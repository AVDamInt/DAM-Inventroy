import pandas as porco_demonio
import os


def handle_uploaded_file(up_file):
    # df = porco_demonio.read_excel(f)
    if up_file.name == 'places.xlsx':
        print("Uploading places!")
    elif up_file.name == 'users.xlsx':
        print("Uploading users!")
    elif up_file.name == 'devices.xlsx':
        print("Uploading devices!")
