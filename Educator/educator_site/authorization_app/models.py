# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model, login
from django.conf import settings

#User = get_user_model()

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EducationPrograms(models.Model):
    id_program = models.AutoField(primary_key=True, verbose_name='ID программы')
    title_of_programm = models.CharField(verbose_name='Наименование программы')
    year = models.CharField(verbose_name='Год')

    class Meta:
        managed = False
        db_table = 'education_programs'
        verbose_name = 'Образовательная программа'
        verbose_name_plural = 'Образовательные программы'
    
    def __str__(self):
        return f'{self.title_of_programm}'


class Educator(models.Model):
    id_educator = models.AutoField(primary_key=True, verbose_name='ID преподавателя')
    surname = models.CharField(verbose_name='Фамилия')
    name = models.CharField(verbose_name='Имя')
    patronymic = models.CharField(blank=True, null=True, verbose_name='Отчество')
    rank = models.CharField(blank=True, null=True, verbose_name='Звание')
    academic_degree = models.CharField(blank=True, null=True, verbose_name='Степень')
    position = models.CharField(verbose_name='Должность')
    departmen = models.CharField(verbose_name='Кафедра')
    start_work_specialty = models.DateField(blank=True, null=True, verbose_name='Дата начала работы по специальности')
    work_experience = models.IntegerField(blank=True, null=True, verbose_name='Опыт работы по специальности')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        managed = False
        db_table = 'educator'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        
    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class RefresherCourse(models.Model):
    id_course = models.AutoField(primary_key=True)
    id_educ = models.ForeignKey(Educator, on_delete=models.CASCADE, db_column='id_educ', verbose_name='ID преподавателя')
    type_of_document = models.CharField(verbose_name='Вид документа')
    title_of_document = models.CharField(verbose_name='Название')
    date_completion = models.DateField(verbose_name='Дата прохождения')
    place_of_completion = models.CharField(verbose_name='Место прохождения')
    city_of_completion = models.CharField(blank=True, null=True, verbose_name='Город прохождения')
    link_doc = models.CharField(verbose_name='Ссылка на документ')

    class Meta:
        managed = False
        db_table = 'refresher_course'
        verbose_name = 'Курсы повышения квалификации'
        verbose_name_plural = 'Курсы повышения квалификации'

    def __str__(self):
        return f'{self.id_educ} {self.type_of_document} {self.title_of_document}'


class ScientificWorks(models.Model):
    id_work = models.AutoField(primary_key=True, verbose_name='ID работы')
    id_educ = models.ForeignKey(Educator, on_delete=models.CASCADE, db_column='id_educ', verbose_name='ID преподавателя')
    type_of_work = models.CharField(verbose_name='Тип работы')
    subtype_of_work = models.CharField(blank=True, null=True, verbose_name='Подтип работы')
    title_of_work = models.CharField(verbose_name='Название работы')
    output_data = models.CharField(verbose_name='Выходные данные')

    class Meta:
        managed = False
        db_table = 'scientific_works'
        verbose_name = 'Научные работы'
        verbose_name_plural = 'Научные работы'

    def __str__(self):
        return f'{self.id_educ} {self.type_of_work} {self.title_of_work}'


class Subjects(models.Model):
    id_subject = models.AutoField(primary_key=True, verbose_name='ID дисциплины')
    id_prog = models.ForeignKey(EducationPrograms, on_delete=models.CASCADE, db_column='id_prog', verbose_name='ID образовательной программы')
    code_subject = models.IntegerField(unique=True, verbose_name='Код дисциплины')
    title_of_subject = models.CharField(verbose_name='Название дисциплины')
    course = models.CharField(verbose_name='Курс')

    class Meta:
        managed = False
        db_table = 'subjects'
        verbose_name = 'Дисциплины'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return self.title_of_subject


class Umkd(models.Model):
    id_umkd = models.AutoField(primary_key=True, verbose_name='ID УМКД')
    code_umkd = models.ForeignKey(Subjects, on_delete=models.CASCADE, db_column='code_umkd', to_field='code_subject', verbose_name='Код УМКД')
    title_of_file = models.CharField(verbose_name='Название файла')
    link_file = models.CharField(verbose_name='Ссылка на файл')

    class Meta:
        managed = False
        db_table = 'umkd'
        verbose_name = 'УМКД'
        verbose_name_plural = 'УМКД'

    def __str__(self):
        return f'{self.code_umkd} {self.title_of_file} {self.link_file}'


class WhoIsLeading(models.Model):
    id_subj = models.ForeignKey(Subjects, on_delete=models.CASCADE, db_column='id_subj', verbose_name='ID дисциплины')
    type_of_lesson = models.CharField(verbose_name='Тип занятия')
    id_educ = models.ForeignKey(Educator, on_delete=models.CASCADE, db_column='id_educ', verbose_name='ID преподавателя')

    class Meta:
        managed = False
        db_table = 'who_is_leading'
        verbose_name = 'Кто что ведёт'
        verbose_name_plural = 'Кто что ведёт'
    
    def __str__(self):
        return f'{self.id_subj} {self.type_of_lesson} {self.id_educ}'
