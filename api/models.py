from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__ (self):
    	return self.name

    @property
    def question_count (self):
    	return Question.objects.filter(category_id=self.id).count()

    class Meta:
    	verbose_name = "Category"
    	verbose_name_plural = "Categories"

class Question(models.Model):
	name = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
	rows = models.IntegerField(default=1)
	answer = models.TextField()
	sequence = models.IntegerField(default=1)

	class Meta:
		ordering = ["sequence"]

	def __str__ (self):
		return self.name