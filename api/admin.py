from django.contrib import admin
from .models import Question, Category
# Register your models here.


class QuestionAdminInline(admin.TabularInline):
	model = Question
	extra = 0

class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name", "question_count")
	inlines = [
		QuestionAdminInline
	]

class QuestionAdmin(admin.ModelAdmin):
	list_display = ("name", "category", "sequence",)
	list_filter = ('category',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)