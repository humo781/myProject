# from django.db import models
#
#
# class Book(models.Model):
#     # Kitob nomi (Matnli maydon, maksimal uzunligi 200 ta belgi)
#     title = models.CharField(max_length=200)
#
#     # Muallif ismi (Matnli maydon, maksimal uzunligi 100 ta belgi)
#     author = models.CharField(max_length=100)
#
#     # Nashr etilgan sana (Sana maydoni)
#     published_date = models.DateField()
#
#     # ISBN raqami (Matnli maydon, maksimal uzunligi 13 ta belgi, yagona bo'lishi kerak)
#     isbn = models.CharField(max_length=13, unique=True)
#
#     # Sahifalar soni (Butun sonli maydon)
#     pages = models.IntegerField()
#
#     # Kitob tili (Matnli maydon, maksimal uzunligi 30 ta belgi)
#     language = models.CharField(max_length=30)
#
#     # Kitob janri (Matnli maydon, maksimal uzunligi 50 ta belgi)
#     genre = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.title  # Bu kitob nomini ko'rsatadi

from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Subject(models.Model):
    name = models.CharField(max_length=255)
    kafedra = models.ForeignKey(Kafedra, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
