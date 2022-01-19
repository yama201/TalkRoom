from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpResponseServerError



def index(request):
    # chat/templates/chat/index.html をビューとして返す
    return render(request, 'talkroom/index.html')

def room(request, room_name):
    return render(request, 'talkroom/room.html', {
        'room_name': room_name
    })
    
    
@requires_csrf_token
def my_customized_server_error(request, template_name='500.html'):
    import sys
    from django.views import debug
    error_html = debug.technical_500_response(request, *sys.exc_info()).content
    return HttpResponseServerError(error_html)