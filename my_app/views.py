from django.shortcuts import render
from django.http import HttpResponse
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def index(request):
    logger.info("Открыта главная страница сайта")
    html = """
    <h1>Главная</h1>
    <p>Вбейте /about в адресную строку, чтобы узнать всю правду</p>        
            """
    return HttpResponse(html)

def about(request):
    logger.error("Кто-то посмел открыть /about!!!")
    html = """
    <h1>О себе</h1>
    <h2>Меня зовут Саша</h2>
    <p>честное слово</р>
    """
    return HttpResponse(html)
