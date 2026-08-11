from django.test import TestCase
from django.urls import reverse

from .models import Note


class NoteModelTests(TestCase):
    def test_str_returns_title(self):
        note = Note.objects.create(title="Hello", body="World")
        self.assertEqual(str(note), "Hello")


class IndexViewTests(TestCase):
    def test_index_returns_ok(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["notes_count"], 0)
