from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag

class ScopesInlineFormset(BaseInlineFormSet):
    def clean(self):

        tags = []
        has_main = False
        for form in self.forms:
            if form.cleaned_data.get("is_main"):
                if has_main:
                    raise ValidationError('Не может быть более 1ого главного тега')
                has_main = True

            if form.cleaned_data.get("tag") in tags:
                raise ValidationError('Теги не могут повторяться')

            tags.append(form.cleaned_data.get("tag"))

        if not has_main:
            raise ValidationError('Должен быть 1 главный тег')

        return super().clean()

class ScopesInline(admin.TabularInline):
    model = Scope
    formset = ScopesInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
   inlines = [ScopesInline]

@admin.register(Tag)
class ArticleAdmin(admin.ModelAdmin):
    pass
