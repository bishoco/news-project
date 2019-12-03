from datetime import datetime
import random

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.html import strip_tags

from .models import Article, Comment
from .utils import *

def index(request):
    slug = "10-promise" #move this slug to db config table
    sub_article_count = 3 #number of articles listed at the bottom of the main page

    article_list = get_articles_from_api()
    main_article = get_main_article (article_list, slug);
    sub_article_list = get_sub_articles(article_list, sub_article_count, main_article.uuid)

    context = {'main_article': main_article, 'sub_article_list': sub_article_list}
    return render(request, 'articles/index.html', context)

def detail(request, uuid):
    article_list = get_articles_from_api()
    raw_article = get_article_by_uuid(article_list, uuid)
    instruments = raw_article.get("instruments")
    
    article = convert_raw_article_to_article(raw_article)

    stock_list = get_stocks_from_api()
    stock_list = filter_stock_list_by_instruments(stock_list, instruments)

    comment_list = Comment.objects.filter(article_uuid=uuid).order_by('-comment_date')
    print(comment_list)

    context = {'article': article, "stock_list": stock_list, "comment_list": comment_list}
    return render(request, 'articles/detail.html', context)

def comment(request, uuid):
    comment = Comment(
        article_uuid = uuid,
        # Added strip tags to prevent people injecting HTML
        comment_text = strip_tags(request.POST['comment_text'])
    )
    comment.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(uuid,)))




