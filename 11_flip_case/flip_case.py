def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    text = ''
    if to_swap.islower():
        for char in phrase:
            if char == to_swap:
                text += char.upper()
            elif char == to_swap.upper():
                text += char.lower()
            else:
                text += char
    elif to_swap.isupper():
        for char in phrase:
            if char == to_swap:
                text += char.lower()
            elif char == to_swap.lower():
                text += char.upper()
            else:
                text += char
    return text