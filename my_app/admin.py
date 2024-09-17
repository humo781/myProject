# # from django.contrib import admin
# # from .models import Book  # Modelingizni import qiling
# #
# # # Book modelini admin panelga qo'shish
# # admin.site.register(Book)
#
# from django.contrib import admin
# from .models import Book
#
# class BookAdmin(admin.ModelAdmin):
#     # Admin panelda ko'rsatiladigan maydonlar
#     list_display = ('title', 'author', 'published_date', 'isbn', 'pages', 'language')
#     # Qidirish maydoni
#     search_fields = ('title', 'author', 'isbn')
#
#
# # Modelni admin panelga ro'yxatdan o'tkazish
# admin.site.register(Book, BookAdmin)


from django.contrib import admin
from .models import Faculty, Group, Kafedra, Student, Subject, Teacher

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')

@admin.register(Kafedra)
class KafedraAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'kafedra', 'group')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'kafedra')

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'subject')
