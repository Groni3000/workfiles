import importlib
from django.core.paginator import Paginator
import datetime, functools, inspect, json, traceback
from django.db import transaction
from django.http import JsonResponse
from django.views import View
from mysite import settings

'''
----------------------------------------------------------------------------------------------------------------
Начало блока обработки ошибок
----------------------------------------------------------------------------------------------------------------
'''
JSON_DUMPS_PARAMS={
    'ensure_ascii':False
}

def ret(json_object, status=200):
    '''Отдаёт JSON с правильными HTTP заголовками и в читаемом в браузере виде в случае с кириллицей'''
    return JsonResponse(
        json_object,
        status=status,
        safe= not isinstance(json_object,list),
        json_dumps_params=JSON_DUMPS_PARAMS,
    )

def error_response(exception):
    '''Форматирует HTTP ответ с описанием ошибки и Traceback'ом'''
    if settings.DEBUG == True:
        res={
            'errorMessage': str(exception),
            'traceback': traceback.format_exc()
    }
    else:
        res={
            'errorMessage': str(exception),
            'traceback': 'Sorry, DEBUG=False and there is no traceback for you'
    }
    return ret(res, status=400)

def Exception_catcher(func):
    '''Декоратор для обработки исключений всех вьюшек'''
    @functools.wraps(func)
    def inner(request, *args, **kwargs):
        try:
            with transaction.atomic():
                return func(request, *args, **kwargs)
        except Exception as err:
            return error_response(err)
    return inner

'''
----------------------------------------------------------------------------------------------------------------
Конец блока обработки ошибок
----------------------------------------------------------------------------------------------------------------
'''

def check_criterion(criterion, search_query):
    if criterion=='Я не нашел критерий':
        result_of_search=''
        table=None
    else:
        table = getattr(importlib.import_module('.models','mainpages'), criterion)
        if search_query:
            result_of_search=table._base_manager.filter(**{table.search_field+'__icontains': search_query})
        else:
            result_of_search=''
    return result_of_search, table


def data_for_pagination(result_of_search, request, n):
    number_of_objects=len(result_of_search) #просто для вывода количества объектов-результатов поиска
    paginator=Paginator(result_of_search, n) #делаю слайсы из результата поиска по n штук
    page_numb=request.GET.get('page', 1) # получаю номер страницы
    page=paginator.get_page(page_numb) #пагинатор делает страницу со слайсами из резульата поиска
    is_paginated=page.has_other_pages
    return page, number_of_objects, is_paginated

def data_for_presentation_on_page(search_query, page, table, fields):
    result_for_html_blank=''
    if search_query and page.object_list:
        fields_for_presenting_result_on_html_page=tuple(
            getattr(table, 'result_title_and_descrition')[fields[i]] 
            for i in range(len(fields))
            )
        result_for_html_blank=tuple(
            (page.object_list[i],
            
            tuple(getattr(page.object_list[i], fields_for_presenting_result_on_html_page[j]) 

            for j in range(len(fields_for_presenting_result_on_html_page)))) 

            for i in range(len(page.object_list))
            )
    return result_for_html_blank

def next_and_prev_urls_for_paginator(page, criterion, search_query):
    #For now this function defined ONLY FOR result_of_search_page!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #TODO think how can I form a part of url for paginator just using parametrs for this function
    # fun({'?'+**{param1:value1+"&",
    # param2:value2+"&",
    # param3=value3+"&" and so on ...})= fun('?param1=value1&param2=value2&...')
    if page.has_previous():
        prev_url='?criterion={}&search={}&page={}'.format(criterion,search_query, page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url='?criterion={}&search={}&page={}'.format(criterion,search_query,page.next_page_number())
    else:
        next_url=''
    return next_url, prev_url