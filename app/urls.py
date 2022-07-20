from django.http import JsonResponse
from django.urls import path
from .models import New

def news(request):
    news: list[New] = New.objects.all()
    return JsonResponse(
        {
            'data': [
                new.json for new in news
            ]
        }
    )


def new_one(request, pk):
    print(pk, type(pk))
    new:New = New.objects.filter(id=pk).first()
    print(new)
    if new:
        return JsonResponse(
            {
                "ok": True,
                "data": new.json
            }
        )
    else:
        return JsonResponse(
            {
                "ok": False,
                "error": 'not_found'
            }
        )

urlpatterns = [
    path('news', news),
    path('new/<int:pk>', new_one)
]