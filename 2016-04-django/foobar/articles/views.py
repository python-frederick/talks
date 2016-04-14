from django.shortcuts import render
from articles.models import Article


def homepage(request):
    article_list = Article.objects.all()

    return render(
        request,
        "homepage.html",
        {
            'article_list': article_list,
        })
