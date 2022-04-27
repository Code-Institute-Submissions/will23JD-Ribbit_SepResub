from django.test import TestCase
from .models import Discussion, Categorys


class TestViews(TestCase):

    def test_get_discussion_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_discussion_cat_list(self):
        response = self.client.get('/category_list/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cat_list.html')

    def test_get_discussion_by_cat(self):
        cats = Categorys.objects.create(name='coding')
        response = self.client.get(f'category/{str(cats)}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_by_cats.html')
