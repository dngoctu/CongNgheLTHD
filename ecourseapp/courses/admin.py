from django.contrib import admin
from courses.models import Category, Course
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# SuperUser
# username:admin
# password:123456


class CourseForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Course
        fields = '__all__'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_date', 'updated_date', 'active']
    list_filter = ['id', 'name', 'created_date']
    search_fields = ['name']
    readonly_fields = ['my_image']
    form = CourseForm

    def my_image(self, course):
        if course.image:
            return mark_safe(f"<img width='200' src='{course.image.url}' />")

    class Media:
        css = {
            'all': ['/static/css/style.css']
        }


admin.site.register(Category)
admin.site.register(Course, CourseAdmin)


