from django.forms import ModelForm
from wordle.models import Wordle

class WordleForm(ModelForm):
    class Meta:
        model = Wordle
        fields = ('name', 'description', 'word', 'score', 'board',)