from app.users.middlewares import _thread_locals


def get_current_request():
    """Returns the current request from thread-local storage."""
    return getattr(_thread_locals, "request", None)


def get_current_user():
    """Returns the current request from thread-local storage."""
    return getattr(_thread_locals, "user", None)
