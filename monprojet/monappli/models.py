from django.db import models

# Create your models here.
class Client(models.Model):
      client_ip = models.CharField(max_length=15)


class Page(models.Model):
      page = models.CharField(max_length=50)



class Hit(models.Model):
      timestamp =  models.CharField(max_length=30)
      referer =  models.CharField(max_length=200)
      client = models.ForeignKey(Client, on_delete=models.CASCADE)
      page = models.ForeignKey(Page, on_delete=models.CASCADE)
      




