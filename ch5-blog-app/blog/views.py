import os
import random
import time

from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect



# class BlogListView(ListView):
#     model = Post
#     template_name = 'home.html'
#
#
# class BlogDetailView(DetailView):
#     model = Post
#     template_name = 'post_detail.html'



def search(request):
    print(os.getcwd())
    if request.method == "POST":
        start_time = time.time()
        user_id = str(dict(request.POST)['id_user'][0])
        link = dict(request.POST)['link']
        if len(dict(request.FILES)) != 0:
            if str(dict(request.FILES).get("file")[0]) != '':
                print('ФОТОГРАФИЯ ЗАГРУЖЕНА')
                path = 'static/download/' + user_id
                if not os.path.exists(path):
                    os.mkdir(path)
                    print("Успешно создана директория для тестового пользователя %s " % path)
                id_user_photo = str(random.randint(10000, 99999))

                if not os.path.exists(path + '/-6'):
                    os.mkdir(path + '/-6')
                # os.chdir(path + '\\-6')
                name_photo = str(dict(request.FILES).get("file")[0])
                with open('static/download/' + user_id + '/-6/' + str(dict(request.FILES).get("file")[0]),
                          'wb+') as destination:
                    for chunk in request.FILES['file'].chunks():
                        destination.write(chunk)
            print(time.time() - start_time, "НАЧАЛО ДЕТЕКТИРОВАНИЯ ФОТОГРАФИИ")
        print('not POST search', dict(request.POST))
        date_result = [
            {'city': 'Москва', 'country': 'Россия', 'gender': 'Man', 'photo': '1637030543194610984836_0',
             'percent': '0.0', 'user': 'https://vk.com/id102441', 'name': 'Александр', 'surname': 'Кастыкин',
             'path': 'clear_photos1\\102441\\-6\\1637030543194610984836\\1637030543194610984836_0.jpg'},
            {'city': 'Москва', 'country': 'Россия', 'gender': 'Man', 'photo': '163705322315397319325_0',
             'percent': '0.48737136', 'user': 'https://vk.com/id102441', 'name': 'Александр',
             'surname': 'Кастыкин',
             'path': 'clear_photos1\\102441\\-6\\163705322315397319325\\163705322315397319325_0.jpg'},
            {'city': 'Москва', 'country': 'Россия', 'gender': 'Man', 'photo': '163706756665995114388_0',
             'percent': '0.6068278', 'user': 'https://vk.com/id102441', 'name': 'Александр',
             'surname': 'Кастыкин',
             'path': 'clear_photos1\\102441\\-6\\163706756665995114388\\163706756665995114388_0.jpg'},
            {'city': 'Санкт-Петербург', 'country': 'Россия', 'gender': 'Man',
             'photo': '383166471619717481828_0', 'percent': '0.6756211', 'user': 'https://vk.com/id100175',
             'name': 'Дмитрий', 'surname': 'Борисов',
             'path': 'clear_photos1\\100175\\-6\\383166471619717481828\\383166471619717481828_0.jpg'},
            {'city': 'Санкт-Петербург', 'country': 'Россия', 'gender': 'Woman',
             'photo': '758815785422851135222_0', 'percent': '0.8921693', 'user': 'https://vk.com/id101638',
             'name': 'Алена', 'surname': 'Захаренко',
             'path': 'clear_photos1\\101638\\-6\\758815785422851135222\\758815785422851135222_0.jpg'},
            {'city': 'Санкт-Петербург', 'country': 'Россия', 'gender': 'Woman',
             'photo': '700287073500611994569_1', 'percent': '0.94780666', 'user': 'https://vk.com/id100193',
             'name': 'Кристи', 'surname': 'Григорьева',
             'path': 'clear_photos1\\100193\\-6\\700287073500611994569\\700287073500611994569_1.jpg'},
            {'city': 'Москва', 'country': 'Россия', 'gender': 'Man', 'photo': '5337126847165403156725_0',
             'percent': '0.9491468', 'user': 'https://vk.com/id101363', 'name': 'Владимир',
             'surname': 'Внук',
             'path': 'clear_photos1\\101363\\-6\\5337126847165403156725\\5337126847165403156725_0.jpg'},
            {'city': 'Санкт-Петербург', 'country': 'Россия', 'gender': 'Man',
             'photo': '554133363735494185588_1', 'percent': '0.9897469', 'user': 'https://vk.com/id102022',
             'name': 'Denis', 'surname': 'Krasnyy',
             'path': 'clear_photos1\\102022\\-6\\554133363735494185588\\554133363735494185588_1.jpg'}]

        most = [{'city': 'Москва', 'country': 'Россия', 'gender': 'Man', 'photo': '1637030543194610984836_0',
                 'percent': '0.0', 'user': 'https://vk.com/id102441', 'name': 'Александр', 'surname': 'Кастыкин',
                 'path': 'clear_photos1\\102441\\-6\\1637030543194610984836\\1637030543194610984836_0.jpg'},
                {'city': 'Москва', 'country': 'Россия', 'gender': 'Man', 'photo': '163705322315397319325_0',
                 'percent': '0.48737136', 'user': 'https://vk.com/id102441', 'name': 'Александр',
                 'surname': 'Кастыкин',
                 'path': 'clear_photos1\\102441\\-6\\163705322315397319325\\163705322315397319325_0.jpg'}]
        post = [{'path': 'clear_photos1\\102441\\-6\\1637030543194610984836\\1637030543194610984836_0.jpg',
                 'value': '1637030543194610984836_0.json'}]
        return render(request, "search_result.html", {'vk': date_result,
                                                             'most': most,
                                                             'post': post})
    return render(request, "search.html", { "paaath": str(os.listdir('static/download/')) + 'patttt' })


def home(request):
    print(dict(request.POST))
    return render(request, 'home.html', {"paaath": os.listdir(os.getcwd()) })
