from threading import local
from django.utils.functional import SimpleLazyObject

_thread_locals = local()


def _get_user_lazy(request):
    if request.user is None or request.user.is_anonymous:
        return None
    return request.user


class ThreadLocalMiddleware:
    """Middleware that catches request and current user information for reuse across the application."""

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        _thread_locals.request = request
        # Fix for DRF lazy evaluation: https://stackoverflow.com/a/41281748
        # TODO: Consider django.utils.functional.lazy
        _thread_locals.user = SimpleLazyObject(lambda: _get_user_lazy(request))

        try:
            response = self.get_response(request)
        finally:
            del _thread_locals.request
            del _thread_locals.user
        # Code to be executed for each request/response after
        # the view is called.
        return response
