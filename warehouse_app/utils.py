from datetime import datetime

import pandas as pd
import os
from .models import Device, Place, DeviceUser
import time


def handle_uploaded_file(up_file):
    # if up_file.name ==
    start_time = time.time()
    if ".xlsx" in up_file:
        df = pd.read_excel(up_file, engine="openpyxl", na_filter=False)
        cnt = 0
        for _, row in df.iterrows():
            utente = str(row["UTENTE"])
            ufficio = str(row["UFFICIO"])
            sede = str(row["SEDE"])
            device_status = 1
            user = None
            if "onibile" in utente.lower() or "ninbile" in utente.lower():
                device_status = 0
            else:
                user, created = DeviceUser.objects.update_or_create(
                    name=utente,
                    surname="",
                    email="",
                    role="",
                    defaults={"name": utente, "surname": "", "email": "", "role": ""},
                )

                # if created:
                # print(f"User created with name {utente}")
                # else:
                # print(f"User already in db")

            place, created = Place.objects.update_or_create(
                name=ufficio,
                city=sede,
                address="",
                cap="",
                country="",
                plan="",
                defaults={
                    "name": ufficio,
                    "city": sede,
                    "cap": "",
                    "country": "",
                    "plan": "",
                },
            )
            # if created:
            # print(f"Place created with name {ufficio} and city {sede}")
            # else:
            # print(f"Place already in db")

            contratto = str(row["CONTR"])

            host_name = str(row["HOST_NAME"])
            marca = str(row["MARCA"])
            tipo = str(row["TYPE"])
            matricola = str(row["MATRICOLA"])
            stato = str(row["STATO"])
            note = str(row["MONITOR"])
            test_id = str(row["TEST_ID"])

            history_type = 0
            if stato == "STORICO":
                history_type = 0
            elif stato == "ATTIVO":
                history_type = 1

            dt_scadenza = ""
            dt_rinnovo = ""
            scad = None
            rinn = None
            scadenza = str(row["SCAD"])
            rinnovo = str(row["RINNOVO"])
            if scadenza:
                scad = datetime.strptime(scadenza, "%Y-%m-%d %H:%M:%S")
            else:
                scad = None

            if rinnovo:
                rinn = datetime.strptime(rinnovo, "%Y-%m-%d %H:%M:%S")
            else:
                rinn = None

            # print(f"Device data {matricola} - {contratto} - {host_name} - {marca} - {tipo}")
            # print(scad)

            # print(rinn)

            # bisogna rivdere la get_or_create perchè crea meno records di quelli presente nel file excel.
            device, created = Device.objects.update_or_create(
                serial_number=matricola,
                contract=contratto,
                expiration_date=scad if scad else None,
                renewal_date=rinn if rinn else None,
                host_name=host_name,
                make=marca,
                model=tipo,
                place=place,
                user=user,
                status=device_status,
                history_type=history_type,
                note=note,
                test_id=test_id,
            )

            if created:
                print(
                    f"Device created with data {matricola} - {contratto} - {host_name} - {marca} - {tipo}"
                )
            else:
                print(
                    f"Device already in db {matricola} - {contratto} - {host_name} - {marca} - {tipo}"
                )

            cnt += 1
        end_time = time.time() - start_time
        print(f"Execution time in seconds {end_time}")
    else:
        print(f"Wrong file type! You must upload a .xlsx file")