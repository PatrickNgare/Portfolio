from django.test import TestCase
from .models import Tag,Portifolio


class PortifolioTestClass(TestCase):
    


    def setUp(self):
        self.moveisIP=Portifolio(title='movies libary app',details='module This class inherits from the TestCase class. We then create a setUp method that allows',giturl='https://github.com/PatrickNgare/landingPage',deployedurl='www.example.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.moveisIP,Portifolio))

def test_save_method(self):
    self.moveisIP.save_editor()
    portifolio=Portifolio.objects.all()
    self.assertTrue(len(portifolio)>0)