from django.db import models


class Book(models.Model):
    # Kitob nomi (Matnli maydon, maksimal uzunligi 200 ta belgi)
    title = models.CharField(max_length=200)

    # Muallif ismi (Matnli maydon, maksimal uzunligi 100 ta belgi)
    author = models.CharField(max_length=100)

    # Nashr etilgan sana (Sana maydoni)
    published_date = models.DateField()

    # ISBN raqami (Matnli maydon, maksimal uzunligi 13 ta belgi, yagona bo'lishi kerak)
    isbn = models.CharField(max_length=13, unique=True)

    # Sahifalar soni (Butun sonli maydon)
    pages = models.IntegerField()

    # Kitob tili (Matnli maydon, maksimal uzunligi 30 ta belgi)
    language = models.CharField(max_length=30)

    # Kitob janri (Matnli maydon, maksimal uzunligi 50 ta belgi)
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title  # Bu kitob nomini ko'rsatadi

