from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError

from .models import Article, Scope, ScopePositions


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            print(form.cleaned_data)
            if form.cleaned_data['general'] == True:
                counter += 1
            print(form.cleaned_data['general'])
        if counter > 1:
            raise ValidationError('Основным может быть только один раздел')
            return super().clean()




class ScopePositionsInline(admin.TabularInline):
    model = ScopePositions
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopePositionsInline,]


