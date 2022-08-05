def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    sep = phrase.split(' ')
    out_str = ''

    for word in sep:
        out_str += f'{word.capitalize()} '

    out_str = out_str.strip()

    return out_str

    # of course python has a built in method for this...