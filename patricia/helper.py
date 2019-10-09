def get_intersection(word_one, word_two):

    """
    Buca o ponto onde duas strings de diferenciam
    :param str word_one:
    :param str word_two:
    :return int:
    """
    for i in range(len(word_one)):

        if len(word_two) > i:

            if word_one[i] != word_two[i]: return i