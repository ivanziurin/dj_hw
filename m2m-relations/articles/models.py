from django.db import models


class Scope(models.Model):

    scope_name = models.CharField(null=True, max_length=50, verbose_name='Название категории')


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Scope, through='ScopePositions')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class ScopePositions(models.Model):

    scope = models.ForeignKey(Scope, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    general = models.BooleanField(verbose_name='Основной?')