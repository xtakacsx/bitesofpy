from functools import wraps

known_users = ["bob", "julian", "mike", "carmen", "sue"]
loggedin_users = ["mike", "sue"]


def login_required(func):
    @wraps(func)
    def inner(arg):
        if arg not in known_users:
            return "please create an account"
        if arg not in loggedin_users:
            return "please login"

        return func(arg)

    return inner


@login_required
def welcome(user):
    """Return a welcome message if logged in"""
    return f"welcome back {user}"
