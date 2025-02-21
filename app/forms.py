from django.forms import ModelForm
from app.models import MultiUserToDo

class MultiUserToDoForm(ModelForm):
    class Meta:
        model = MultiUserToDo
        fields = ['title','status','priority']

