from django.shortcuts import render

# Create your views here.
from wordle.forms import WordleForm
from wordle.models import Wordle

def index(request):
   wordles = Wordle.objects.all()
   #wordles = Wordle.objects.filter(description__contains='Test').order_by('name')
   return render(request, 'index.html', {
      'wordles': wordles,
   })

def wordle_detail(request, slug):
    wordle = Wordle.objects.get(slug=slug)
    return render(request, 'wordles/wordle_detail.html', {
        'wordle': wordle,
    })
 