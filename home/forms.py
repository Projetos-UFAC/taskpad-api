from django import forms
from ckeditor.fields import RichTextFormField
from lista.models import Lista 
from atividade.models import Atividade
from tarefa.models import Tarefa
from ckeditor.widgets import CKEditorWidget

class ListaForm(forms.ModelForm):
    texto = RichTextFormField(widget=CKEditorWidget())

    class Meta:
        model = Lista
        fields = ['texto']
        widgets = {
            'texto': RichTextFormField(),
        }

class AtividadeForm(forms.ModelForm):
    texto = RichTextFormField()

    class Meta:
        model = Atividade
        fields = '__all__'
        widgets = {
            'texto': RichTextFormField(),
        }

class TarefaForm(forms.ModelForm):
    texto = RichTextFormField()

    class Meta:
        model = Tarefa
        fields = '__all__'
        widgets = {
            'texto': RichTextFormField(),
        }
