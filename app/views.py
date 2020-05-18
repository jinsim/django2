from django.shortcuts import render, redirect
from .models import Article
# Create your views here.
def index_defined_in_view(request):
    movie_articles = Article.objects.filter(category = "movie").count()
    drama_articles = Article.objects.filter(category = "drama").count()
    entertain_articles = Article.objects.filter(category = "entertain").count()
    return render(request, 'index_in_templates.html', 
    {'movie_i_will_use_in_html':movie_articles,'drama_i_will_use_in_html':drama_articles,'entertain_i_will_use_in_html':entertain_articles})
    
def detail_defined_in_view(request, primary_key_of_the_article_that_i_clicked):
    article = Article.objects.get(pk=primary_key_of_the_article_that_i_clicked) 
    return render(request, 'detail_in_templates.html', {'an_article_i_will_use_in_html':article})

def new_defined_in_view(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category']
        )
        return redirect('detail_in_html', primary_key_of_the_article_that_i_clicked=new_article.pk)
    else:
        return render(request, 'new_in_templates.html')

def movie_defined_in_view(request):
    movie_article = Article.objects.filter(category = "movie")
    return render(request, 'movie_in_templates.html', {'movie_i_will_use_in_html':movie_article})

def drama_defined_in_view(request):
    drama_article = Article.objects.filter(category = "drama")
    return render(request, 'drama_in_templates.html', {'drama_i_will_use_in_html':drama_article})

def entertain_defined_in_view(request):
    entertain_article = Article.objects.filter(category = "entertain")
    return render(request, 'entertain_in_templates.html', {'entertain_i_will_use_in_html':entertain_article})
