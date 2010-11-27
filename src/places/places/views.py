import logging
from django.conf import settings
from django.contrib.csrf.middleware import csrf_exempt
from django.shortcuts import render_to_response
from django.template import RequestContext
import facebook

@csrf_exempt
def homepage(request):
    logging.info(request)
    user = facebook.get_user_from_cookie(request.COOKIES,
        settings.FACEBOOK_API['places']['app_id'],
        settings.FACEBOOK_API['places']['secret_key'])
    logging.error(user)
    if user is not None:
        graph = facebook.GraphAPI(user.get('access_token', None))
        logging.error(graph)
        user = graph.get_object("me")
        logging.error(user)
        friends = graph.get_connections(user["id"], "friends")
        logging.error(friends)
        friends_info = graph.get_objects([
            n['id'] for n in friends['data']
        ])
        logging.error(friends_info)
    return render_to_response('homepage.html', {
        
    }, context_instance=RequestContext(request))