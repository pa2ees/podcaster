from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.urls import reverse_lazy

from feedgen.feed import FeedGenerator

from first.models import Item

class IndexView(generic.ListView):
    model = Item
    template_name = 'first/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        return Item.objects.all()

class ItemDetail(generic.DetailView):
    model = Item
    template_name = 'first/item_detail.html'
    context_object_name = 'item'

class NewItem(generic.edit.CreateView):
    model = Item
    fields = ['title', 'description', 'link']
    
class EditItem(generic.edit.UpdateView):
    model = Item
    fields = ['title', 'description', 'link']

class DeleteItem(generic.edit.DeleteView):
    model = Item
    success_url = reverse_lazy('index')

def import_item(request):
    # form for taking a url and scraping the info off it to generate an item
    pass

def confirm_new_item(request):
    #display scraped info for new item, and ask user to confirm
    #possibly allow to change data?
    pass

def feed(request):
    #return HttpResponse("Howdy!")
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.id('dingus.com')
    fg.title('Some Other title')
    fg.author( {'name': 'me of course', 'email': 'blarf@gmail.com'})
    fg.link( href='http://35.224.79.205/first', rel='self')
    #fg.logo('http://www.mormonnewsroom.org/media/960x540/ElderBallard.jpg')
    fg.image(url='http://35.224.79.205/static/frog.jpg',
             title='image title',
             link='http://35.224.79.205',
             width='800',
             height='600')
    fg.description('some description')
    #fg.author({'name': 'why me, of course', 'email':'someemail@gmail.com'})
    # author not actually put in the feed

    for item in Item.objects.all():
        
        fe = fg.add_entry()

        fe.id("{}".format(item.id))
        fe.title(item.title)
        fe.link(href=item.link)
        fe.description(item.description)
        fe.enclosure(item.link, 0, 'audio/mpeg')
        #fe.id('http://media2.ldscdn.org/assets/general-conference/april-2018-general-conference/2018-03-1020-m-russell-ballard-64k-eng.mp3?download=true')
        # fe.id('12345')
        #fe.title('First')
        #fe.link(href='http://35.224.79.205/first')
        #fe.description('This is the description of the first item')
        #fe.enclosure('http://media2.ldscdn.org/assets/general-conference/april-2018-general-conference/2018-03-1020-m-russell-ballard-64k-eng.mp3?download=true', 0, 'audio/mpeg')

    return HttpResponse(fg.rss_str(pretty=False), content_type="text/xml")
