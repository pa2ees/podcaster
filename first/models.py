import logging

log = logging.getLogger(__name__)

from django.db import models
from django.urls import reverse
from django import forms

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

class PodcastNewItemForm(forms.ModelForm):
     

     podcast = forms.IntegerField(required=True, widget=forms.HiddenInput())

     def __init__(self, *args, **kwargs):
          super().__init__(*args, **kwargs)
          items = Item.objects.all()
          
          
          for idx,item in enumerate(items):
               field_name = 'item_{}'.format(item.id)
               self.fields[field_name] = forms.BooleanField(required=False, label=item.title)

     def clean(self):
          log.debug("Cleaning data... ")

          podcast = Podcast.objects.get(pk=self.cleaned_data['podcast'])
          self.cleaned_data['podcast'] = podcast

          checked_items = []

          items = Item.objects.all()
          for item in items:
               cleaned_item = self.cleaned_data.get('item_{}'.format(item.id))
               if cleaned_item:
                    podcast_item = Podcast_Item(podcast=podcast, item=item)
                    checked_items.append(podcast_item)

          self.cleaned_data['checked_items'] = checked_items
          

     def save(self):
          log.debug("Saving data... ")

          for item in self.cleaned_data['checked_items']:
               pk = item.save()
               log.debug("Saved podcast item with id {}".format(pk))

     class Meta:
          model = Podcast_Item
          fields = ['podcast']
