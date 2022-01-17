from django.db import models


class Scope(models.Model):

    name = models.CharField(null=True, max_length=50, verbose_name='Название категории')


    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'



class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    all_scopes = models.ManyToManyField(Scope,  related_name='all_tags', through='Relationship')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Relationship(models.Model):

    scope = models.ForeignKey(Scope, on_delete=models.CASCADE, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(verbose_name='Основной')

    class Meta:
        ordering = ['-is_main']