from django.shortcuts import render

from django.http import HttpResponse

from feedgen.feed import FeedGenerator

def index(request):
    #return HttpResponse("Howdy!")
    fg = FeedGenerator()
    fg.id('dingus.com')
    fg.title('Some Other title')
    fg.author( {'name': 'me of course', 'email': 'blarf@gmail.com'})
    fg.link( href='stoopid.com', rel='self')
    fg.description('some description')
    #fg.publisher('why me, of course')

    

    return HttpResponse(fg.rss_str(pretty=False))
