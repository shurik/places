from django.conf import settings
from django.contrib.sites.models import Site

def project_context(request):
    return {
        'site': Site.objects.get_current(),
        'app_id': settings.FACEBOOK_API['places']['app_id']
    }
