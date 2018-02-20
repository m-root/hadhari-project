from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from django.core.exceptions import MiddlewareNotUsed


from re import compile

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

# from django.utils.deprecation import MiddlewareMixin

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

REDIRECT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'AFTER_LOGIN_REDIRECT_HOME_URLS'):
    REDIRECT_URLS += [compile(expr) for expr in settings.AFTER_LOGIN_REDIRECT_HOME_URLS]


class AuthRequiredMiddleware(MiddlewareMixin):
    """
    Middleware that requires a user to be authenticated to view any page other
    than LOGIN_URL. Exemptions to this requirement can optionally be specified
    in settings via a list of regular expressions in LOGIN_EXEMPT_URLS (which
    you can copy from your urls.py).
    Requires authentication middleware and template context processors to be
    loaded. You'll get an error if they aren't.
    """

    def process_request(self, request):
        assert_error_message = '''
        The Login Required middleware requires authentication middleware to be installed. 
        Edit your MIDDLEWARE_CLASSES setting to insert 'django.contrib.auth.middleware.AuthenticationMiddleware'. 
        If that doesn't work, 
        ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes 'django.core.context_processors.auth'
        '''

        assert hasattr(request, 'user'), assert_error_message
        path = request.path_info.lstrip('/')

        if not request.user.is_authenticated:
            if not any(m.match(path) for m in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL + ('?next={}'.format(path) if path else ''))
        else:
            if path and any(m.match(path) for m in REDIRECT_URLS):
                return HttpResponseRedirect(settings.INDEX_URL)