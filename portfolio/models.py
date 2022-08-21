from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return self.name

class Project_info(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name= 'projects')
    client = models.CharField(max_length= 50)
    project_url = models.URLField()
    project_date = models.DateField(auto_now_add= True)
    details = models.TextField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()

    def __str__(self):
        return self.client

    def get_absolute_url(self):
        return reverse('portfolio:portfoliodetails', kwargs={
            'id': self.id,
            'title': self.title
        })
