from datetime import datetime

import pandas as pd
import os
from .models import Device, Place, DeviceUser


def handle_uploaded_file(up_file):
    # if up_file.name ==
    df = pd.read_excel(up_file, engine='openpyxl')
    cnt = 0
    for _, row in df.iterrows():
        UTENTE = str(row['UTENTE'])
        UTENTE = UTENTE[:-1]
        UFFICIO = str(row['UFFICIO'])
        UFFICIO = UFFICIO[:-1]
        SEDE = str(row['SEDE'])
        SEDE = SEDE[:-1]
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
        CONTRATTO = CONTRATTO[:-1]
        SCADENZA = str(row['SCAD'])
        SCADENZA = SCADENZA[:-1]
        RINNOVO = str(row['RINNOVO'])
        RINNOVO = RINNOVO[:-1]
        HOST_NAME = str(row['HOST_NAME'])
        HOST_NAME = HOST_NAME[:-1]
        MARCA = str(row['MARCA'])
        MARCA = MARCA[:-1]
        TYPE = str(row['TYPE'])
        YPE = TYPE[:-1]
        MATRICOLA = str(row['MATRICOLA'])
        MATRICOLA = MATRICOLA[:-1]
        DESC = str(row['DESC'])
        DESC = DESC[:-1]
        DISPONIBILE = str(row['DISPONIBILE'])
        DISPONIBILE = DISPONIBILE[:-1]
        real_disp = 0
        if DISPONIBILE == 'DISPONIBILE':
            real_disp = 2
        elif DISPONIBILE == 'na' or DISPONIBILE == 'nan':
            real_disp = 1
        else:
            real_disp = 0

        #dt_scadenza = datetime.strptime(SCADENZA, '%Y-%m-%d')
        #print(dt_scadenza)
        #dt_rinnovo = datetime.strptime(RINNOVO, '%Y-%m-%d')
        #print(dt_rinnovo)
        device, created = Device.objects.get_or_create(
            serial_number=MATRICOLA,
            contract=CONTRATTO,
            #expiration_date=dt_scadenza,
            #renewal_date=dt_rinnovo,
            host_name=HOST_NAME,
            make=MARCA,
            model=TYPE,
            place=place,
            user=user,
            status=real_disp
        )

        if created:
            print(f"Device created with data {MATRICOLA} - {CONTRATTO} - {HOST_NAME} - {MARCA} - {TYPE}")
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
