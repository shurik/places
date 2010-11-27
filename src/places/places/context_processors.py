from django.conf import settings

def project_context(request):
    return {
        'app_id': settings.FACEBOOK_API['places']['app_id']
    }