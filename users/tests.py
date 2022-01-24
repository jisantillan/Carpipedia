from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from posts.models import Post
from .models import User

# Create your tests here.

class UserTests(TestCase):
    def setUp(self):
        # acá se escribe algo en común para todos los tests. Por ejemplo crear objetos
        self.username = "test"
        self.email = "test@test.com"
        self.password = "test"
        user = get_user_model().objects.create_user(username=self.username,  email=self.email, password=self.password)

    def test_login(self):
        self.client = Client()
        response = self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.assertRedirects(response, settings.LOGIN_REDIRECT_URL, fetch_redirect_response=False)
        self.client.logout()
    
    def test_eliminar_usuario(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]})
        post = Post.objects.get(titulo="titulo de test")
        response = self.client.post(reverse("user-delete"))
        self.assertRedirects(response, "/", fetch_redirect_response=False)
        response = self.client.get(reverse("usr-detail", args=[user.id]))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("post-detail", args=[post.slug]))
        self.assertEqual(response.status_code, 404)
        self.client.logout()
    
    def test_cambio_avatar(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        response = self.client.post(reverse("user_update"), {"avatar": 1})
        self.assertRedirects(response, '/accounts/detalle/'+str(user.id), fetch_redirect_response=False)
        response = self.client.post(reverse("user_update"), {"avatar": 2})
        self.assertEqual(2, User.objects.get(username=self.username).avatar.id)
