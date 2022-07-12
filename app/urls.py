from django.http import JsonResponse
from django.urls import path
from .models import New

def news(request):
    return JsonResponse(
        {
            'data': [
                new.json for new in New.objects.all()
            ]
        }
    )

urlpatterns = [
    path('news', news)
]