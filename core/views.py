from django.http import JsonResponse

from .models import Note


def index(request):
    return JsonResponse(
        {
            "project": "Django_python",
            "branch": "PYTHON_3.9",
            "notes_count": Note.objects.count(),
        }
    )
