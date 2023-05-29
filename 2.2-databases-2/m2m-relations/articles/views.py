from django.shortcuts import render

from .models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.order_by('-published_at')
    # for article in object_list:
    #     for scope in article.scopes.all:
    #         print(scope.tag.name)
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)

