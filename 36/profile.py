def get_profile(name: str, age: int, *args, **kwargs):
    if len(list(args)) > 5:
        raise ValueError
    if not isinstance(age, int):
        raise ValueError

    profile = dict(name=name, age=age,)
    if args:
        profile.update(sports=sorted(list(args)))
    if kwargs:
        profile.update(awards=kwargs)
    return profile


print(get_profile("tim", 36, "tennis", "basketball", champ="helped out team in crisis"))
