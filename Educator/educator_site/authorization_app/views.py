from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Educator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import EducatorUpdateForm, RefresherCourseForm, ScienceWorkForm, AddSubjectForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Educator, ScientificWorks, RefresherCourse, EducationPrograms, Subjects, Umkd, WhoIsLeading
from django.db.models import Prefetch
from django.contrib.auth import logout

def educator_registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Educator.objects.create(user=user)
            login(request, user)
            return redirect('educator_profile')
    else:
        form = UserCreationForm()
    return render(request, 'authorization/educator_profile.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile_page'))
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль')
    else:
        form = AuthenticationForm()
    return render(request, 'authorization/login.html', {'form': form})

@login_required
def educator_profile(request):
    educator = Educator.objects.get(user=request.user)
    if request.method == 'POST':
        form = EducatorUpdateForm(request.POST, instance=educator)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        form = EducatorUpdateForm(instance=educator)
    return render(request, 'educator/profile.html', {'form': form})

def main_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile_page'))
            else:
                # В случае, если пользователь не найден, создаём нового
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    Educator.objects.create(user=user)
                    login(request, user)
                    return redirect('educator_profile')
    else:
        form = AuthenticationForm()
    return render(request, 'base.html', {'form': form})


@login_required
def profile_page(request):
    educator = Educator.objects.get(user=request.user)

    courses = RefresherCourse.objects.filter(id_educ=educator)
    works = ScientificWorks.objects.filter(id_educ=educator)
    wil = WhoIsLeading.objects.filter(id_educ=educator)
    subjects = Subjects.objects.filter(whoisleading__id_educ=educator)
    
    subjects_umkd = Subjects.objects.filter(whoisleading__id_educ=educator.id_educator) \
                              .prefetch_related(
                                  Prefetch('umkd_set', queryset=Umkd.objects.all())
                              )

    wil_dict = {wil.id_subj: wil for wil in wil}
    join_data = zip(subjects, wil_dict.values())
    join_list = list(join_data)

    context = {
        'educator': educator,
        'courses': courses,
        'scientific_works': works,
        'who_is_leding': wil,
        'subjects_umkd': subjects_umkd,
        'join_list': join_list
    }
    return render(request, 'educator/educator_cart.html', context)

def logout_view(request):
    logout(request)
    return redirect('main_page') 

@login_required
def add_refresher_course(request):
    if request.method == 'POST':
        form = RefresherCourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        educator = Educator.objects.get(user=request.user)
        form = RefresherCourseForm(initial={'id_educ': educator.id_educator})
    return render(request, 'educator/add_course.html', {'form': form})

@login_required
def add_science_work(request):
    if request.method == 'POST':
        form = ScienceWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    else:
        # Получение объекта Educator, связанного с текущим пользователем
        educator = Educator.objects.get(user=request.user)
        # Передача начального значения для поля id_educ
        form = ScienceWorkForm(initial={'id_educ': educator.id_educator})
    return render(request, 'educator/add_science_work.html', {'form': form})

def delete_science_work(request, pk):
    science_work = get_object_or_404(ScientificWorks, pk=pk)
    science_work.delete()
    return redirect('profile_page')

def delete_refresher_course(request, pk):
    refresher_course = get_object_or_404(RefresherCourse, pk=pk)
    refresher_course.delete()
    return redirect('profile_page')

@login_required
def add_subject_to_educator(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject_id = form.cleaned_data['subject_id']
            lesson_type = form.cleaned_data['type_of_lesson']
            
            educator = Educator.objects.get(user=request.user)
            
            WhoIsLeading.objects.create(id_subj=subject_id, type_of_lesson=lesson_type, id_educ=educator)
            
            return redirect('profile_page')
    else:
        form = AddSubjectForm()
    
    return render(request, 'educator/add_subject.html', {'form': form})
