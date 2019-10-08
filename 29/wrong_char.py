def get_index_different_char(char: list) -> int:
    count_alpha = [index for index, character in enumerate(char) if str.isalnum(str(character))]
    count_nonalpha = [index for index, character in enumerate(char) if not str.isalnum(str(character))]

    if len(count_alpha) < len(count_nonalpha):
        return count_alpha[0]
    else:
        return count_nonalpha[0]
