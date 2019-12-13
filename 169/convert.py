def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if isinstance(value, (int, float)):
        pass
    else:
        raise TypeError

    if fmt.lower() in ("cm", "in"):
        units = fmt.lower()
    else:
        raise ValueError

    if units == "cm":
        return round(value * 2.54, 4)
    elif units == "in":
        return round(value / 2.54, 4)
