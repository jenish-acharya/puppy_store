from django.test import TestCase
from puppies.models import Puppy


class PuppyTest(TestCase):
    """
    Test module for Puppy model
    """

    def setUp(self) -> None:
        Puppy.objects.create(name="Casper", age=3, breed="Bull Dog", color="Brown")
        Puppy.objects.create(name="Muffin", age=1, breed="Muffin", color="Black")

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name="Casper")
        puppy_muffin = Puppy.objects.get(name="Muffin")
        self.assertEqual(puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(puppy_muffin.get_breed(), "Muffin belongs to Muffin breed.")
