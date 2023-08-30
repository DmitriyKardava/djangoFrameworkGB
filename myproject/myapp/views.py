import logging
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class LoggerMixin:
    def get(self, request, *args, **kwargs):
        logger.info(f"{request.path} accessed from {get_client_ip(request)}")
        return super().get(self, request, *args, **kwargs)
        
class IndexView(LoggerMixin, TemplateView):
    template_name = 'myapp/index.html'
    
class AboutView(LoggerMixin, TemplateView):
    template_name = 'myapp/about.html'
