from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data['is_main'] == True:
                counter += 1
            print(form.cleaned_data['is_main'])
        if counter > 1:
            raise ValidationError('Основным может быть только один раздел')
            return super().clean()




class RelationshipInline(admin.TabularInline):
    model = Relationship
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline,]


