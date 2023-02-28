from datetime import datetime

import pandas as pd
import os
from .models import Device, Place, DeviceUser


def handle_uploaded_file(up_file):
    # if up_file.name ==
    df = pd.read_excel(up_file, engine='openpyxl', na_filter = False)
    cnt = 0
    for _, row in df.iterrows():
        UTENTE = str(row['UTENTE'])
        # UTENTE = UTENTE[:-1]
        UFFICIO = str(row['UFFICIO'])
        # UFFICIO = UFFICIO[:-1]
        SEDE = str(row['SEDE'])
        # SEDE = SEDE[:-1]
        # user = DeviceUser(
        #    name=row['UTENTE'],
        #    surname='',
        #    email='',
        #    role=''
        # )
        # user.save()
        user, created = DeviceUser.objects.get_or_create(
            name=UTENTE,
            surname='',
            email='',
            role='')

        if created:
            print(f"User created with name {UTENTE}")
        else:
            print(f"User already in db")

        place, created = Place.objects.get_or_create(
            name=UFFICIO,
            city=SEDE,
            address='',
            cap='',
            country='',
            plan=''
        )
        if created:
            print(f"Place created with name {UFFICIO} and city {SEDE}")
        else:
            print(f"Place already in db")

        CONTRATTO = str(row['CONTR'])
        # CONTRATTO = CONTRATTO[:-1]
        # SCADENZA = str(row['SCAD'])
        # SCADENZA = SCADENZA[:-1]
        # RINNOVO = str(row['RINNOVO'])
        # RINNOVO = RINNOVO[:-1]
        HOST_NAME = str(row['HOST_NAME'])
        # HOST_NAME = HOST_NAME[:-1]
        MARCA = str(row['MARCA'])
        # MARCA = MARCA[:-1]
        TIPO = str(row['TYPE'])
        # PROVA = PROVA[:-1]
        MATRICOLA = str(row['MATRICOLA'])
        # MATRICOLA = MATRICOLA[:-1]
        STATO = str(row['STATO'])
        NOTE = str(row['MONITOR'])
        # STATO = STATO[:-1]

        # DESC = str(row['DESC'])
        # DESC = DESC[:-1]
        # DISPONIBILE = str(row['DISPONIBILE'])
        # DISPONIBILE = DISPONIBILE[:-1]
        real_disp = 0
        if STATO == 'STORICO':
            real_disp = 1
        elif STATO == 'ATTIVO':
            real_disp = 0
        else:
            STATO = 2

        #if UTENTE == 'DISPONIBILE':
            #real_disp = 2
        #elif UTENTE == 'na' or UTENTE == 'nan':
            real_disp = 1
        #else:
            #real_disp = 0
        dt_scadenza = ''
        dt_rinnovo = ''
        scad = None
        rinn = None
        scadenza = str(row['SCAD'])
        rinnovo = str(row['RINNOVO'])
        if scadenza:
            scad = datetime.strptime(scadenza, '%Y-%m-%d %H:%M:%S')
        else:
            scad = None

        if rinnovo:
            rinn = datetime.strptime(scadenza, '%Y-%m-%d %H:%M:%S')
        else:
            rinn = None

        print(f"Device data {MATRICOLA} - {CONTRATTO} - {HOST_NAME} - {MARCA} - {TIPO}")
        print(scad)

        print(rinn)

        device, created = Device.objects.get_or_create(
            serial_number=MATRICOLA,
            contract=CONTRATTO,
            expiration_date=scad if scad else None,
            renewal_date=rinn if rinn else None,
            host_name=HOST_NAME,
            make=MARCA,
            model=TIPO,
            place=place,
            user=user,
            status=real_disp,
            note=NOTE
        )

        if created:
            print(f"Device created with data {MATRICOLA} - {CONTRATTO} - {HOST_NAME} - {MARCA} - {TIPO}")
        else:
            print(f"Device already in db")

        cnt += 1

        # place = Place(
        #    name=row['UFFICIO'],
        #    city=row['SEDE'],
        #    address='',
        #    cap='',
        #    country='',
        #    plan=''
        # )
        # place.save()
