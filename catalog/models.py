from django.db import models
from tinymce.models import HTMLField
from django.db.models.signals import post_save


class Category(models.Model):
    index_title = models.TextField(max_length=256, blank=True, null=True, default=None,
                                   verbose_name=u"Заголовок на главной")
    first_title = HTMLField(default=None, verbose_name=u"Заголовок первого экрана")
    first_text = HTMLField(default=None, verbose_name=u"Текст на первом экране")
    second_title = models.TextField(max_length=256, blank=True, null=True, default=None,
                                   verbose_name=u"Заголовок второго экрана")
    third_title = models.TextField(max_length=256, blank=True, null=True, default=None,
                                   verbose_name=u"Заголовок экрана с консультацией")
    meta_tags = models.TextField(max_length=256, blank=True, null=True, default=None,
                                   verbose_name=u"Мета теги страницы")
    url_pretty = models.CharField(max_length=256, blank=True, null=True, default=None,
                                   verbose_name=u"URL")
    catalog_url = models.CharField(max_length=556, blank=True, null=True, default=None,
                                   verbose_name=u"Ссылка на каталог")

    def __str__(self):
        return '%s' % self.index_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class CategoryIndexImg(models.Model):
    service = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/categories', verbose_name=u"Фото на главной")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото на главной'
        verbose_name_plural = 'Фото на главной'


class CategoryInnerImg(models.Model):
    service = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/categories', verbose_name=u"Фото на первом экране")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото на первом экране'
        verbose_name_plural = 'Фото на первом экране'


class CategoryCatalogImg(models.Model):
    service = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/categories', verbose_name=u"Фото каталога")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото каталога'
        verbose_name_plural = 'Фото каталога'


class CategoryCatalogText(models.Model):
    service = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField(default=None, verbose_name=u"Пункт каталога")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт каталога'
        verbose_name_plural = 'Пункты каталога'


class CategoryConsImg(models.Model):
    service = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/categories', verbose_name=u"Фото консультация")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото консультация'
        verbose_name_plural = 'Фото консультации'


class CategoryConsText(models.Model):
    service = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE)
    text = HTMLField(default=None, verbose_name=u"Пункт консултации")

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Пункт консултации'
        verbose_name_plural = 'Пункты консультации'


class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, default=None, on_delete=models.CASCADE,
                                 verbose_name=u"Категория")
    date = models.CharField(max_length=126, blank=True, null=True, default=None,
                            verbose_name=u"Дата изготовления")
    title = models.CharField(max_length=256, blank=True, null=True, default=None,
                            verbose_name=u"Заголовок")
    text = HTMLField(default=None, verbose_name=u"Описание")
    type = models.CharField(max_length=10, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImg(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/img/categories', verbose_name=u"Фото изделия")
    type = models.CharField(max_length=10, blank=True, null=True, default=None)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Фото изделия'
        verbose_name_plural = 'Фото изделия'

    def save(self, *args, **kwargs):
        if self.img.width >= self.img.height:
            self.type = '1'
        else:
            self.type = '2'
        super(ProductImg, self).save(*args, **kwargs)


# изменение типа карточки продукта, при разных изображениях
def product_type_post_save(sender, instance, created, **kwargs):
    product = instance.product
    images = ProductImg.objects.filter(product_id=instance.product_id)

    wide = 0
    tall = 0

    for i in images:
        if i.img.width >= i.img.height:
            wide += 1
        elif i.img.width < i.img.height:
            tall += 1

    if wide >= 2 and tall == 0:
        instance.product.type = 1
    elif tall >= 2 and wide == 0:
        instance.product.type = 2
    elif wide >= 2 and tall >= 1:
        instance.product.type = 3
    else:
        instance.product.type = 1

    instance.product.save(force_update=True)


post_save.connect(product_type_post_save, sender=ProductImg)