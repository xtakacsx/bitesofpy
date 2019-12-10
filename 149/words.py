def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    # sorted_words = sorted(words, key=str.lower)
    # new_list = []
    # for i, word in enumerate(sorted_words):
    #     if sorted_words[i][0].isnumeric():
    #         new_list.append(word)
    # for x in new_list:
    #     sorted_words.remove(x)
    #
    # return sorted_words + new_list
    return sorted(words, key=lambda x: (x[0].isdigit(), str(x).lower()))
