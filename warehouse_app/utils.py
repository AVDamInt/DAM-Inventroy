from datetime import datetime
import time
import pandas as pd
import os
from .models import Device, Place, DeviceUser, Department, Office, Company


def handle_uploaded_file(up_file):
    # if up_file.name ==ù
    print(up_file)
    start_time = time.time()
    df = pd.read_excel(up_file, engine="openpyxl", na_filter=False)
    cnt = 0
    for _, row in df.iterrows():
        utente = str(row["UTENTE"])
        ufficio = str(row["UFFICIO"])
        sede = str(row["SEDE"])
        dipartimento = str(row["DIREZIONE"])

        company = str(row["COMPANY"])

        department_create, created = Department.objects.update_or_create(
            name=dipartimento
        )

        office_create, created = Office.objects.update_or_create(
            name=ufficio
        )

        company_create, created = Company.objects.update_or_create(
            name=company
        )

        device_status = 1
        user = None

        if 'spedito' in utente.lower():
            print("Found spedito")

        # split on space or underscore
        if "onibile" in utente.lower() or "ninbile" in utente.lower():
            device_status = 0
        else:
            device_stats = 1
        splitted_user = ''
        user_final = ''
        if '_' in utente:
            name = ''
            surname = ''
            splitted_user = utente.split('_')
            if len(splitted_user) > 2:
                name = splitted_user[0]
                surname = splitted_user[1] + ' ' + splitted_user[2]
            else:
                name = splitted_user[0]
                surname = splitted_user[1]
            user, created = DeviceUser.objects.update_or_create(
                name=name,
                surname=surname,
                email="",
            )
        elif ' ' in utente:
            splitted_user = utente.split(' ')
            if len(splitted_user) > 2:
                name = splitted_user[0]
                surname = splitted_user[1] + ' ' +  splitted_user[2]
            else:
                name = splitted_user[0]
                surname = splitted_user[1]
            user, created = DeviceUser.objects.update_or_create(
                name=name,
                surname=surname,
                email="",
            )
        else:
            name = utente
            user, created = DeviceUser.objects.update_or_create(
                name=name,
                surname='',
                email="",
            )

            # if created:

            # print(f"User created with name {utente}")
            # else:
            # print(f"User already in db")

        place, created = Place.objects.update_or_create(
            city=sede,
            address="",
            cap="",
            country="",
            plan=""
        )
        # if created:
        # print(f"Place created with name {ufficio} and city {sede}")
        # else:
        # print(f"Place already in db")

        contratto = str(row["CONTR"])

        host_name = str(row["HOST_NAME"])
        make = str(row["MARCA"])
        model = str(row["TYPE"])
        matricola = str(row["MATRICOLA"])
        stato = str(row["STATO"])
        note = str(row["MONITOR"])
        #test_id = str(row["TEST_ID"])

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
            company=company_create,
            serial_number=matricola,
            contract=contratto,
            expiration_date=scad if scad else None,
            renewal_date=rinn if rinn else None,
            host_name=host_name,
            make=make,
            model=model,
            place=place,
            user=user,
            status=device_status,
            history_type=history_type,
            note=note,
            department=department_create,
            office=office_create
            #test_id=test_id,
        )

        if created:
            print(
                f"Device created with data {matricola} - {contratto} - {host_name} - {make} - {model}"
            )
        else:
            print(
                f"Device already in db {matricola} - {contratto} - {host_name} - {make} - {model}"
            )

        cnt += 1
    end_time = time.time() - start_time
    print(f"Execution time in seconds {end_time}")
