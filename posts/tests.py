from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="ClaveSegura123!")
        self.post = Post.objects.create(
            titulo="Post de prueba",
            contenido="Contenido de prueba",
            autor="Tester",
            estado=Post.Estado.PUBLICADO,
        )

    def test_inicio_es_publico(self):
        response = self.client.get(reverse("posts:inicio"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.titulo)

    def test_detalle_es_publico(self):
        response = self.client.get(reverse("posts:detalle", args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.post.contenido)

    def test_crear_post_requiere_login(self):
        response = self.client.get(reverse("posts:crear"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response.url)

    def test_usuario_autenticado_puede_crear_post(self):
        self.client.login(username="tester", password="ClaveSegura123!")
        response = self.client.post(
            reverse("posts:crear"),
            {
                "titulo": "Nuevo post",
                "contenido": "Creado desde test",
                "autor": "Tester",
                "estado": Post.Estado.BORRADOR,
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(titulo="Nuevo post").exists())
