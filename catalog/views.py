from django.shortcuts import render
from catalog.models import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage


def category(request, url_pretty):
    category_cur = Category.objects.get(url_pretty=url_pretty)
    products = category_cur.product_set.all()[:5]
    return render(request, 'site/inner.html', locals())


def catalog(request, url_pretty):
    category_cur = Category.objects.get(url_pretty=url_pretty)
    products = category_cur.product_set.all()[:2]
    return render(request, 'site/detail.html', locals())


@csrf_exempt
def load_content(request, url_pretty):
    r = request.POST

    try:
        i = int(r.get('item')) + 1
        product = Category.objects.get(url_pretty=url_pretty).product_set.all()[i]

        return HttpResponse(render(request, 'site/catalog.html', locals()), content_type='text/plain')

    except:

        return JsonResponse(r)


def send_mail(request):
    r = request.POST

    if len(r) != 0:
        name = r.get('name')
        phone = r.get('phone')
        type = r.get('type')
        text = ''
        msg = '{}\nИмя: {}\nТелефон: {}'.format(type, name, phone)
        if 'text' in r and len(r.get('text')) != 0:
            text = r.get('text')
            msg = msg + '\nГород: {}'.format(text)

        email = EmailMessage(type, msg, to=['marukhelin@gmail.com'])
        email.send()

    return JsonResponse(r)


