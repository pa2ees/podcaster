from django.db import models
from django.urls import reverse

class Podcast(models.Model):
     title = models.CharField(max_length=200)
     guid = models.CharField(max_length=200)
     link = models.CharField(max_length=200)
     description = models.CharField(max_length=1000)
     summary = models.CharField(max_length=1000)
     author = models.CharField(max_length=200)
     cover = models.CharField(max_length=1000)

     def get_absolute_url(self):
          return reverse('podcast_list', kwargs={'pk': self.pk})
    

class Item(models.Model):
     title = models.CharField(max_length=200)
     #pub_date = models.DateTimeField
     description = models.CharField(max_length=1000)
     link = models.CharField(max_length=200)
     #item_type = models.CharField(max_length=200)

     def get_absolute_url(self):
          return reverse('detail', kwargs={'pk': self.pk})

class Podcast_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    # title
    # publish date
    # description
    # itunes summary
    # media file enclosure
    # duration
    # file size
    # explicit rating
