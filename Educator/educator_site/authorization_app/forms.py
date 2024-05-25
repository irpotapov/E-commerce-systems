from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Educator, RefresherCourse, ScientificWorks, WhoIsLeading, Subjects

class EducatorUpdateForm(forms.ModelForm):
    class Meta:
        model = Educator
        fields = ['surname', 'name', 'patronymic', 'rank', 'academic_degree', 'position', 'departmen', 'start_work_specialty']

class RefresherCourseForm(forms.ModelForm):
    class Meta:
        model = RefresherCourse
        fields = ['id_educ', 'type_of_document', 'title_of_document', 'date_completion', 'place_of_completion', 'city_of_completion', 'link_doc']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'initial' in kwargs:
            initial = kwargs.pop('initial')
            self.fields['id_educ'].initial = initial.get('id_educ')

class ScienceWorkForm(forms.ModelForm):
    class Meta:
        model = ScientificWorks
        fields = ['id_educ', 'type_of_work', 'subtype_of_work', 'title_of_work', 'output_data']

class AddSubjectForm(forms.ModelForm):
    subject_id = forms.ModelChoiceField(queryset=Subjects.objects.all(), empty_label="Выберите дисциплину", widget=forms.Select(attrs={'onchange':'this.form.submit();'}))
    type_of_lesson = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Введите тип занятия'}))

    class Meta:
        model = WhoIsLeading
        fields = ['subject_id', 'type_of_lesson']