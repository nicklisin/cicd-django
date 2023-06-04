from django.test import TestCase
from .models import Page


class ModelsTest(TestCase):
    def setUp(self) -> None:
        self.page = Page.objects.create(name="TestPage")
        return super().setUp()

    def testPage(self):
        p = self.page
        self.assertTrue(isinstance(p, Page))
        self.assertEqual(str(p), "TestPage")
