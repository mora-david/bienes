from BienesApp.models import CustomUSer, Bienes
from BienesApp.serializer import CustomUserSerializer

import pandas as pd

#exec(open('BienesApp/importar_bienes.py').read())



user = {'usuario':'userAdmin', 'nombre':'usuario1','password':'$#Pass12EAbc&'}

def first_user_bienes(user):
    if CustomUSer.objects.filter(usuario=user['usuario'],nombre=user['nombre']):
        print('el usuario ya existe')
    else:
        serializer = CustomUserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        userdb = serializer.save()

        df = pd.read_csv('bienes/bienes_to_DB.csv')

        for index, row in df.iterrows():
            Bienes.objects.create(id=row['id'],articulo=row['articulo'], descripcion=row['descripcion'], usuario_id=userdb)

first_user_bienes(user)
