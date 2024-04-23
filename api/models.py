from django.core.validators import RegexValidator
from django.db import models

from treebeard.mp_tree import MP_Node


class BaseModel(MP_Node):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата обновления', auto_now=True)

    class Meta:
        abstract = True


class UrlModel(BaseModel):
    name = models.CharField(verbose_name='Название страницы', max_length=99)
    slug = models.SlugField(verbose_name='Фрагмент url-адреса', max_length=15, unique=True)
    url = models.CharField(
        verbose_name='Полный url-адрес',
        max_length=199,
        unique=True,
        validators=[
            RegexValidator(
                regex='^[a-z0-9]+/?[a-z0-9]+/$',
                message='Url not valid'
            )
        ]
    )

    def __str__(self):
        return f'{self.name}: {self.url}'
