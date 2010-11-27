import logging
from django.conf import settings
from django.contrib.csrf.middleware import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
import facebook

@csrf_exempt
def homepage(request):
    logging.info(request)
    user = facebook.get_user_from_cookie(settings.FACEBOOK_API['places']['app_id'],
        settings.FACEBOOK_API['places']['secret_key'])
    graph = facebook.GraphAPI(user.get('access_token', None))
    logging.info(graph)
    user = graph.get_object("me")
    logging.info(user)
    friends = graph.get_connections(user["id"], "friends")
    logging.info(friends)
    return render_to_response('homepage.html', {
        
    }, context_instance=RequestContext(request))