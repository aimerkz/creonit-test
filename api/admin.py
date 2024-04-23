from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from api.models import Parent


class ParentAdmin(TreeAdmin):
    form = movenodeform_factory(Parent)


admin.site.register(Parent, ParentAdmin)
