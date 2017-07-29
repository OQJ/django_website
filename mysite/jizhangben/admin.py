from django.contrib import admin
from .models import  Question,Choice
# Register your models here.


class Choiceinline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [('问题',{'fields':['question_text']}),
                 ('日期',{'fields':['pub_date']})]
    inlines = [Choiceinline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
admin.site.register(Question,QuestionAdmin)