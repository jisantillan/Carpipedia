from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from users.models import User
from .models import Categoria, Post
# Create your tests here.

class PostTests(TestCase):
    def setUp(self):
        # acá se escribe algo en común para todos los tests. Por ejemplo crear objetos
        self.username = "test"
        self.email = "test@test.com"
        self.password = "test"
        user = get_user_model().objects.create_user(username=self.username,  email=self.email, password=self.password)

    def test_cargar_post_con_usuario(self):
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        response = self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        self.assertRedirects(response, "/", fetch_redirect_response=False)
        self.assertEqual(Post.objects.get(titulo="titulo de test") in Post.objects.all(), True)
        self.client.logout()
    
    def test_cargar_post_sin_usuario(self):
        self.client = Client()
        response = self.client.get(
            reverse("post-create")
        )
        self.assertRedirects(response, "/accounts/login/?redirect_to=/crear/", fetch_redirect_response=False)
        self.client.logout()

    def test_no_se_puede_editar_post_de_otro_usuario(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        user2 = get_user_model().objects.create_user(username="test2",  email="user2@test.com", password="test2")
        post=Post.objects.create(titulo="titulo de test", contenido="contenido de test", propietario=user2, slug="titulo-de-test")
        post.categorias.set([Categoria.objects.get(id=3)])
        post.save()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        request = self.client.get(reverse("post-edit", args=[post.slug]))
        self.assertEqual(request.status_code, 403)

    def test_editar_post(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        self.client.post(reverse("post-edit", args=[post.slug]), {"titulo": "titulo de test editado", "contenido": "contenido de test editado", "categorias": [2]})
        self.assertEqual(Post.objects.get(titulo="titulo de test editado") in Post.objects.all(), True)
    
    def test_eliminar_post(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        self.client.post(reverse("post-delete", args=[post.slug]))
        self.assertEqual(Post.objects.filter(titulo="titulo de test").first() in Post.objects.all(), False)

    def test_ver_detalle_post(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        response = self.client.get("/detalle/"+post.slug+"/")
        self.assertEqual(response.status_code, 200)
    
    def test_post_se_ve_en_muro_general(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.titulo)
    
    def test_post_se_ve_en_muro_por_tags(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        response = self.client.get("/?categorias="+str(post.categorias.first().id))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, post.titulo)

    def test_puntuar_post(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        self.client.post(reverse("like_post"), {"slug": post.slug}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(user in post.likes.all(), True)
        self.assertEqual(user in post.dislikes.all(), False)
        self.client.post(reverse("dislike_post"), {"slug": post.slug}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(user in post.likes.all(), False)
        self.assertEqual(user in post.dislikes.all(), True)
        self.client.post(reverse("dislike_post"), {"slug": post.slug}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        self.assertEqual(user in post.likes.all(), False)
        self.assertEqual(user in post.dislikes.all(), False)

    def test_comentar_post(self):
        user = get_user_model().objects.get(username=self.username)
        self.client = Client()
        self.client.post(
            settings.LOGIN_URL, {"login": self.username, "password": self.password}
        )
        self.client.post(
            reverse("post-create"), {"titulo": "titulo de test", "contenido": "contenido de test", "categorias": [3]}
        )
        post = Post.objects.get(titulo="titulo de test")
        self.client.post(reverse("comentar_post"), {"slug": post.slug, "cuerpo": "comentario de test"}, **{'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        comentario = post.comentarios.get(cuerpo="comentario de test")
        self.assertEqual(comentario in post.comentarios.all(), True)
        self.client.post(reverse("comment-delete", args=[comentario.id]))
        post = Post.objects.get(titulo="titulo de test")
        self.assertEqual(comentario in post.comentarios.all(), False)
