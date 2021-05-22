from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class TestPost(TestCase):
    def setUp(self):
        test_user = User.objects.create(username='dannyreigns', password='12345')
        test_user.save()

        test_post = Post.objects.create(author=test_user, title='Things fall apart', body='Test Lorem ipsum dolor sit amet.')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = 'dannyreigns'
        title = 'Things fall apart'
        body='Test Lorem ipsum dolor sit amet.'
        self.assertEqual(post.author.username, author)
        self.assertEqual(post.title, title)
        self.assertEqual(post.body, body)