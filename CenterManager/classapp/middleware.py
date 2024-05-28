from django.conf import settings
from django.http import HttpResponseForbidden

def api_key_required(view_func):
    def _wrapped_view_func(viewset, request, *args, **kwargs):
        api_key = request.headers.get('Authorization')
        print(api_key)
        if api_key != settings.API_KEY:
            return HttpResponseForbidden("Invalid API key")
        return view_func(viewset, request, *args, **kwargs)
    return _wrapped_view_func