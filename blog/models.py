from django.db import models
from django.urls import reverse


class Blog(models.Model):
	title = models.CharField(max_length=50)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to="images/")

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:140]

	def get_absolute_url(self):
		return reverse('blog:blog_detail', args=[str(self.id)])
