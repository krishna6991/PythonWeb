from django.test import TestCase

from ..models import Puppy

class PuppyTest(TestCase):

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=5, breed='Bull Dog', color='Brown')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
