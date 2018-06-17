from django.db import models

# class Podcast(models.Model):
#     title (SHALL) (monson talks, chron of narnia, etc)
#     guid  (SHOULD) what is it usually?
#     link (SHALL) URL of the podcasts website
#     description (SHALL) 
#     update frequency? (RECOMMENDED)
#     generator? (SHOULD)
#     payment url? (RECOMMENDED)
#     language (SHOULD)
#     summary (should) (short version of the description, I think)
#     author (SHOULD)
#     image/cover (RECOMMENDED) url of image
#     copyright and license ? (RECOMMENDED)
#     categorization
    

class Item(models.Model):
     title = models.CharField(max_length=200)
     #pub_date = models.DateTimeField
     description = models.CharField(max_length=1000)
     link = models.CharField(max_length=200)
     #item_type = models.CharField(max_length=200)


# class Feed_Item(models.Model):
#     item = models.ForeignKey(Item, on_delete=models.CASCADE)
#     podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE)
#     title
#     publish date
#     description
#     itunes summary
#     media file enclosure
#     duration
#     file size
#     explicit rating
