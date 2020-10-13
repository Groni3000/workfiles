from django.shortcuts import render
from .models import stories, paintforcar
from django.views.generic import View
from .forms import result_of_search_page as res #TODO That's something for future ideas? Don't need it right now.
from .services import check_criterion, data_for_pagination, data_for_presentation_on_page
from .services import next_and_prev_urls_for_paginator, Exception_catcher


#from django.db.models import Q

# Create your views here.
@Exception_catcher
def index(request):
    ''' Главная страничка. Пустая, контент для неё ещё не придуман. '''
    return render(request, 'mainpages/index.html')

@Exception_catcher
def show_completed_stories(request):
    """ Страничка, где перечислены все завершенные истории из БД. """
    #TODO Посмотреть как правильно вводить данные в БД. То есть, как правильно вводить из cleaned_data.
    context={
        'completed_stories': stories.storytitles.all(),
    }
    return render(request, 'mainpages/completed_stories.html', context)

@Exception_catcher
def result_of_search_page(request):
    ''' Страничка с выводом результата поиска. 
    ------------------------------------------------------------------------------------------------------
    check_criterion(criterion, search_query) 
    Тут выполняется проверка критерия поиска, считывание поискового запроса;
    ------------------------------------------------------------------------------------------------------
    выбирается НУЖНАЯ таблица из БД, формирование ответа на поисковый запрос;
    ------------------------------------------------------------------------------------------------------
    формируем странички с использованием пагинатора, считаем количество объектов в результате поиска, и 
    в переменную is_paginated=True|False — нужно ли выводить пагинацию;
    ------------------------------------------------------------------------------------------------------
    выборка нужных строчек для показа информации;
    формирование url для пагинации. '''

    #Получаем данные для поиска (критерий поиска, поисковой запрос).
    criterion=request.GET.get('criterion','Я не нашел критерий')
    search_query=request.GET.get('search', "")

    # Выбираем таблицу из базы данных (согласно критерию поиска) и формируем ответ на поисковой запрос
    result_of_search, table = check_criterion(criterion, search_query)
    
    # Формируем страницу, используя пагинацию, узнаем количество объектов результата поиска,
    # узнаем "нужно ли пагинировать"
    page, number_of_objects, is_paginated = data_for_pagination(result_of_search, request, 16)

    #
    result_for_html_blank = data_for_presentation_on_page(search_query, page, table, (0,1))

    #
    next_url, prev_url = next_and_prev_urls_for_paginator(page, criterion, search_query)


    context={
        "number_of_objects" : number_of_objects,
        "page" : page,
        "search_quary": search_query,
        "is_paginated": is_paginated,
        "next_page_url": next_url,
        "prev_page_url": prev_url,
        "criterion": criterion,
        "result_of_search": result_of_search,
        "result": result_for_html_blank,
    }
    return render(request, 'mainpages/result_of_search.html', context)








