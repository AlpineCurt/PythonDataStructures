def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    
    char_list = [char for char in phrase]
    char_list.reverse()
    txt = ''
    for char in char_list:
        txt += char
    return txt