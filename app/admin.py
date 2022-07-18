from django.contrib import admin

from app.models import Img, New

# Register your models here.



class ImgInline(admin.TabularInline):
    # model = New.images.through
    model = Img
    


class NewsModelAdmin(admin.ModelAdmin):
    inlines = [ImgInline]
    class Meta:
        model = New

admin.site.register(New, NewsModelAdmin)





