# from django.contrib import admin
# from .models import Book  # Modelingizni import qiling
#
# # Book modelini admin panelga qo'shish
# admin.site.register(Book)

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Admin panelda ko'rsatiladigan maydonlar
    list_display = ('title', 'author', 'published_date', 'isbn', 'pages', 'language')
    # Qidirish maydoni
    search_fields = ('title', 'author', 'isbn')


# Modelni admin panelga ro'yxatdan o'tkazish
admin.site.register(Book, BookAdmin)
