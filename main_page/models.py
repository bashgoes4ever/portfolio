from django.db import models
from tinymce.models import HTMLField


class Advances(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                             verbose_name=u"Заголовок")
    text = HTMLField(default=None, verbose_name=u"Текст")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Преимущество'
        verbose_name_plural = 'Преимущества'


class Replies(models.Model):
    name = HTMLField(default=None, verbose_name=u"Имя, город")
    text = HTMLField(default=None, verbose_name=u"Отзыв")
    iframe = models.TextField(max_length=1024, blank=True, null=True, default=None,
                              verbose_name=u'Ссылка на видео с ютуба')

    def __str__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class RepliesImg(models.Model):
    reply = models.ForeignKey(Replies, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/stuff', verbose_name=u"Фото отзыва")


