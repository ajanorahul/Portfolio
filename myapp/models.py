from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    discription = models.TextField()
    img = models.ImageField(upload_to ='pics')

    def __str__(self):
        return self.title

class CategoryName(models.Model):
    title = models.CharField(max_length=100)
    create_at =models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title


class portfolio(models.Model):
    category = models.ForeignKey(CategoryName, on_delete =models.CASCADE)
    portfolio_title = models.CharField(max_length=100)
    portfolio_image = models.ImageField(upload_to ='pics1')
    href = models.CharField(max_length=150)

    def __str__(self):
        return self.portfolio_title

class Services(models.Model):
    icon = models.ImageField(upload_to ='pics2')
    title = models.CharField(max_length=150)
    disc = models.TextField()

    def __str__(self):
        return self.title
