from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return '%s' % self.name

class Question(models.Model):
	label = models.CharField(max_length=200)
	rows = models.IntegerField(default=1)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	def __init__(self, arg):
		super(Question, self).__init__()
		self.arg = arg




		
