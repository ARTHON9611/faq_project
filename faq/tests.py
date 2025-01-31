from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python-based web framework."
        )

    def test_translation(self):
        translated = self.faq.get_translation('hi')
        self.assertIsNotNone(translated['question'])
