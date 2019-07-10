def filter_dots(string):
    """Function that filter string from dots
    :param string: string to be filtered from dots
    :return: string that does not contains dots
    """
    return ''.join(char for char in string if char != '.')
