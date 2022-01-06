from django.contrib import admin

from .models import Article, Scope, ScopePositions


class ScopePositionsInline(admin.TabularInline):
    model = ScopePositions


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ['scope_name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopePositionsInline]


