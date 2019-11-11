from django.db import models
from autoslug import AutoSlugField
# Create your models here.


class Post(models.Model):
    title = models.CharField(
        verbose_name='Назва',
        null=False,
        blank=False,
        max_length=255
    )

    image = models.ImageField(
        verbose_name='зображення',
        upload_to='cards',
        null=True,
        blank=True
    )

    text = models.TextField(
        verbose_name='Текст',
        null=False,
        blank=False,
    )

    slug = AutoSlugField(
        populate_from='title',
        null=True,
        unique=True,
        allow_unicode=True
    )

    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата оновлення'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата створення'
    )

    @classmethod
    def get_posts_count(cls):
        return cls.objects.all().count()

    @property
    def comments_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def short_text(self):
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text

    def __str__(self):
        return f"{self.title}, {self.updated.date()}"

    class Meta:
        verbose_name = 'Публікацію'
        verbose_name_plural = 'Публікації'

    def save(self, *args, **kwargs):
        self.slug = None
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='Публікація')

    username = models.CharField(
        max_length=255,
        verbose_name='Коментатор',
    )

    text = models.TextField(
        verbose_name='Текст',
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата створення',
    )

    @property
    def short_text(self):
        return f"{self.text[:50]}..." if len(self.text) > 50 else self.text

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
