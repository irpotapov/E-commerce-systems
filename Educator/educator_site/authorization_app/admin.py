from django.contrib import admin
from django.utils.html import format_html
from .models import Educator, ScientificWorks, RefresherCourse, EducationPrograms, Subjects, Umkd, WhoIsLeading

@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
    list_display = ('id_educator', 'surname', 'name', 'patronymic', 'rank', 'academic_degree', 'position', 'departmen', 'start_work_specialty', 'work_experience', 'user')
    search_fields = ('surname', 'name', 'patronymic', 'rank', 'academic_degree', 'position', 'departmen', 'start_work_specialty')

@admin.register(ScientificWorks)
class ScientificWorksAdmin(admin.ModelAdmin):
    list_display = ('id_educ', 'type_of_work', 'title_of_work', 'output_data')

@admin.register(RefresherCourse)
class RefresherCourseAdmin(admin.ModelAdmin):
    list_display = ('id_educ', 'type_of_document', 'title_of_document', 'date_completion', 'place_of_completion', 'city_of_completion', 'link_doc', 'link_doc_link')
    def link_doc_link(self, obj):
        return format_html('<a href="{}">Ссылка на документ</a>', obj.link_doc)
    link_doc_link.short_description = 'Кликабельная ссылка'
    link_doc_link.allow_tags = True

@admin.register(EducationPrograms)
class EducationProgramsAdmin(admin.ModelAdmin):
    list_display = ('id_program', 'title_of_programm', 'year')

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id_subject', 'id_prog', 'code_subject', 'title_of_subject', 'course')
    search_fields = ('code_subject', 'title_of_subject', 'course')

@admin.register(Umkd)
class UmkdAdmin(admin.ModelAdmin):
    list_display = ('id_umkd', 'code_umkd', 'title_of_file', 'link_file', 'link_file_link')
    def link_file_link(self, obj):
        return format_html('<a href="{}">Ссылка на файл</a>', obj.link_file)
    link_file_link.short_description = 'Кликабельная ссылка'
    link_file_link.allow_tags = True

@admin.register(WhoIsLeading)
class WhoIsLeadingAdmin(admin.ModelAdmin):
    list_display = ('id_subj', 'type_of_lesson', 'id_educ')

