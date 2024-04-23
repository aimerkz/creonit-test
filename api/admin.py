from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from api.models import UrlModel


@admin.register(UrlModel)
class UrlModelAdmin(TreeAdmin):
    form = movenodeform_factory(UrlModel)
