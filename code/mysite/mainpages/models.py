from django.db import models
from datetime import datetime, date
from django.utils.timezone import now
from django.shortcuts import reverse
from django.utils.translation import gettext_lazy as readable_name

# Create your models here.


#Модель истрии

class stories(models.Model):
    id = models.AutoField(primary_key=True)
    UserId=models.IntegerField(name='UserId',unique=False, default=1)
    title=models.CharField(name="title", max_length=300, help_text='Напишите название истории!',default="title")
    titleId=models.IntegerField(name='titleId', unique=True, default=1)
    pub_time=models.DateTimeField(name='pub_time', auto_now_add=True)
    text=models.CharField(max_length=300,default='TEXT')

    search_field='title'

    result_title_and_descrition=('title', 'text')

    storytitles = models.Manager()

    #def get_absolute_url(self):
        #return reverse()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Историю"
        verbose_name_plural="Истории"
        ordering=['-pub_time']


#Модель краски

class paintforcar(models.Model):
    id = models.AutoField(primary_key=True)
    nameofpaint=models.CharField(name='nameofpaint', max_length=300, unique=False, default='', help_text='Введите наименование краски')
    vendor_code=models.CharField(name="vendor_code", max_length=300, help_text='Введите артикул краски',default="")
    colour=models.CharField(name='colour', max_length=300, unique=False, default='', help_text='Введите цвет краски')
    pub_time=models.DateTimeField(name='pub_time', auto_now_add=True)
    description=models.CharField(max_length=300,default='Описание краски')

    search_field='vendor_code'

    result_title_and_descrition=('nameofpaint', 'vendor_code')

    allcolours = models.Manager()

    #def get_absolute_url(self):
        #return reverse()

    def __str__(self):
        return self.nameofpaint

    class Meta:
        verbose_name="Краску"
        verbose_name_plural="Краски"
        ordering=['-pub_time']

#Модель категорий

class categories(models.Model):
    id=models.AutoField(primary_key=True)
    category=models.CharField(name='category', max_length=300, unique= True, default='', help_text='Введите название категории')

    allcategories = models.Manager()

    #def get_absolute_url(self):
        #return reverse()

    def __str__(self):
        return self.category

    class Meta:
        verbose_name="Категорию"
        verbose_name_plural="Категории"

#Модель телефона

class mobile_phone(models.Model):
    class Resolution(models.TextChoices):
        HD= '1280x720', readable_name('HD, 1280x720p')
        FullHD= '1920x1080', readable_name('FullHD, 1920x1080p')
        QuadHD= '2560x1440', readable_name('QuadHD, 2560x1440p')

    class Display(models.IntegerChoices):
        inch= 5.1 , readable_name('5.1 дюймов')
        cm=   12.954, readable_name('12.954 сантиметров')

    id=models.AutoField(primary_key=True)
    mobile_name=models.CharField(name='mobile_name', max_length=300, unique=True, help_text='Введите наименование мобильного телефона')
    description=models.TextField(name='descriprion', )
    display=models.IntegerField(choices=Display.choices, default=Display.inch,)
    resolution=models.CharField(max_length=300, choices=Resolution.choices, default=Resolution.FullHD,)
    specifications=[
        display,
        resolution,
    ]

    phones = models.Manager()

    #def get_absolute_url(self):
        #return reverse()

    def __str__(self):
        return self.mobile_name

    class Meta:
        verbose_name="Телефон"
        verbose_name_plural="Телефоны"
    
    