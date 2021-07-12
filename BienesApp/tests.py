from django.test import TestCase
from .importar_bienes import first_user_bienes
from .models import Bienes
from BienesApp.models import CustomUSer, Bienes
from rest_framework_simplejwt.tokens import RefreshToken




class LoadBienesAndFirstUser(TestCase):
    def test_load(self):
        user = {'usuario':'userAdminxddd1', 'nombre':'usuario1','password':'$#Pass12EAbc&'}
        first_user_bienes(user)
        self.assertEqual(Bienes.objects.get(id=17309).descripcion,'MADERA VINO')
        self.assertEqual(CustomUSer.objects.last().usuario,'userAdminxddd1')

class CreateUserTest(TestCase):
    def test_register_users(self):
        user = CustomUSer.objects.create(usuario='user1',nombre='gabriel',password='$#Pass12EAbc&')
        token = str(RefreshToken.for_user(user).access_token)
        
        url = '/api/Register/'

        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + token,
            'content_type': 'application/json'
        }

        data_register = {'usuario':'miguel', 'nombre':'usuario2','password':'$#Pass12EAbc&'}
        r = self.client.post(url, data_register, **headers)
        self.assertEqual(r.status_code, 201)

class BienesTest(TestCase):
    url = '/api/Bienes/'
    def setUp(self) -> None:
        user = {'usuario':'userAdminxddd1', 'nombre':'usuario1','password':'$#Pass12EAbc&'}
        first_user_bienes(user)

    def test_getBienes(self):
        token = str(RefreshToken.for_user(CustomUSer.objects.last()).access_token)
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + token,
            'content_type': 'application/json'
        }
        r = self.client.get(self.url, **headers)
        self.assertEqual(r.status_code, 200)

    def test_postBienes(self):
        token = str(RefreshToken.for_user(CustomUSer.objects.last()).access_token)
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + token,
            'content_type': 'application/json'
        }

        data = {'articulo':'silla de madera','descripcion':'silla chica', 'usuario_id':CustomUSer.objects.last().id}

        r = self.client.post(self.url,data,**headers)
        self.assertEqual(r.status_code, 201)
        

    def test_getBulkBienes(self):
        base_url = '/BienesBulk/'
        ids = '56024&66472&63355&732176&54547/'
        user = {'usuario':'userAdminxddd1', 'nombre':'usuario1','password':'$#Pass12EAbc&'}
        first_user_bienes(user)

        token = str(RefreshToken.for_user(CustomUSer.objects.last()).access_token)
        headers = {
            'HTTP_AUTHORIZATION': 'Bearer ' + token,
            'content_type': 'application/json'
        }
        r = self.client.get(base_url+ids, **headers)
        self.assertEqual(r.status_code, 200)
                










