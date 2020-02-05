from functools import wraps


def make_html(element):
    def real_decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            return '<{}>'.format(element) + fn(*args, **kwargs) + "</{}>".format(element)

        return wrapper

    return real_decorator
