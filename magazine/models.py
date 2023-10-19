from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Marka(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Autocar(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(verbose_name='Изображение', upload_to='img/', **NULLABLE)
    marka = models.ForeignKey(Marka, verbose_name='Категория', on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    data_created = models.DateTimeField(verbose_name='Дата последнего изменения', auto_now_add=True)

    def __str__(self):
        return f"{self.marka}"

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'