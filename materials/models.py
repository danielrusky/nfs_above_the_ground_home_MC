from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Material(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    body = models.TextField(verbose_name='содержимое')

    views_count = models.IntegerField(default=0, verbose_name='Просмотры')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'

# class Material(models.Model):
#     title = models.CharField(max_length=100, verbose_name='Заголовок')
#     slug = models.CharField(max_length=100, verbose_name='slug')
#     text = models.TextField(verbose_name='Содержимое')
#     image = models.ImageField(upload_to='blog/', verbose_name='Изображeние', **NULLABLE)
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
#     to_publish = models.BooleanField(default=True, verbose_name='Признак публикации')
#     views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')
