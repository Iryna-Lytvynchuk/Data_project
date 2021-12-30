from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Data
from .forms import *
from django.core.files.uploadedfile import SimpleUploadedFile


class DataTests(TestCase):
 
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
 
        self.data = Data.objects.create(
            title='New title',
            cover= SimpleUploadedFile(name = 'test_image.jpg', content = open('media/images/14.jpg', 'rb').read(), content_type = 'image/jpg'),
            result='deer'
        )
 
    def test_string_representation(self):
        data = Data(title='New title')
        self.assertEqual(str(data), data.title)
    
    def test_data_content(self):
        self.assertEqual(f'{self.data.title}', 'New title')
        self.assertEqual(f'{self.data.result}', 'deer')
 
    def test_data_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'deer')
        self.assertTemplateUsed(response, 'home.html')
    
 
    def test_data_delete_view(self):
        response = self.client.post(reverse('image_delete', args='1'))
        self.assertEqual(response.status_code, 302)

class Data_Form_Test(TestCase):

    def test_DataForm_invalid(self):
        form = DataForm(data={'title': "", 'cover': ""})
        self.assertFalse(form.is_valid())