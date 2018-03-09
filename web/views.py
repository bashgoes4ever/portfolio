from django.shortcuts import render
from main_page.models import *
from catalog.models import *


def site(request):
    advances = Advances.objects.filter(is_active=True)
    replies = RepliesImg.objects.all()
    categories = Category.objects.all()
    return render(request, 'site/index.html', locals())


