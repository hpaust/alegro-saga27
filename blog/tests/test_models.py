from django.test import TestCase
from blog.models import Post, Comment

class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title='TestTitle',body='TestBody TestBody')
        self.assertEqual(post.title,'TestTitle')
        self.assertEqual(post.body,'TestBody TestBody')

class CommentTestCase(TestCase):
    def testComment(self):
        comment = Comment(body='Comment test',author = 'TestAuthor')
        self.assertEqual(comment.body,'Comment test')
        self.assertEqual(comment.author,'TestAuthor')
