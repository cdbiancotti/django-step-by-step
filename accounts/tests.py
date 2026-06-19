from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Perfil


class AccountsFlowTests(TestCase):
    def test_registro_crea_usuario_y_perfil(self):
        response = self.client.post(
            reverse("accounts:registro"),
            {
                "username": "nuevo_usuario",
                "first_name": "Nuevo",
                "last_name": "Usuario",
                "email": "nuevo@example.com",
                "password1": "ClaveSegura123!",
                "password2": "ClaveSegura123!",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="nuevo_usuario").exists())
        self.assertTrue(Perfil.objects.filter(usuario__username="nuevo_usuario").exists())

    def test_perfil_requiere_login(self):
        response = self.client.get(reverse("accounts:perfil"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response.url)

    def test_login_y_logout_funcionan(self):
        User.objects.create_user(username="tester", password="ClaveSegura123!")
        login_response = self.client.post(
            reverse("accounts:login"),
            {"username": "tester", "password": "ClaveSegura123!"},
        )
        self.assertEqual(login_response.status_code, 302)

        perfil_response = self.client.get(reverse("accounts:perfil"))
        self.assertEqual(perfil_response.status_code, 200)

        logout_response = self.client.post(reverse("accounts:logout"))
        self.assertEqual(logout_response.status_code, 302)
