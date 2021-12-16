from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Катерогия'
        verbose_name_plural = 'Категории'

class Specialization(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Специализация университета'
        verbose_name_plural = 'Специализации университета'

class Country(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class University(models.Model):
    name = models.CharField(max_length=255 ,verbose_name='Название университета')
    country = models.ForeignKey(Country, verbose_name='Страна расположения', on_delete=models.SET_NULL, null = True,
                                    related_name='university_country')
    body = models.CharField(max_length=1000, verbose_name='Краткое описание', null=True)
    images = models.ImageField(verbose_name='Фотография', null=True)
    url = models.URLField(null=True, verbose_name='Ссылка на официальный сайт')
    category = models.ForeignKey(Category, verbose_name='Тип университета', on_delete=models.SET_NULL, null = True,
                                    related_name='university_category')
    specialization = models.ManyToManyField(Specialization, verbose_name='Специализация')
    
    deadline_ed = models.CharField(max_length=100, verbose_name='Окончание приема заявок на early decision', default='-', null=True)
    deadline_rd = models.CharField(max_length=100, verbose_name='Окончание приема заявок на regular decision', default='-', null=True)
    TOEFL = models.PositiveSmallIntegerField(verbose_name='рекомендованый балл по TOEFL', default=0, null=True)
    SAT = models.PositiveIntegerField(verbose_name='рекомендованый балл по SAT', default=0, null=True)
    IELTS = models.FloatField(verbose_name='рекомендованый балл по IELTS', default=0, null=True)
    GPA = models.FloatField(verbose_name='рекомендованый средний балл в школе ', default=0, null=True)
    price = models.PositiveIntegerField(verbose_name=' Стоимость обучения с проживанием', default=0)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовать?')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Университет'
        verbose_name_plural = 'Университеты'
