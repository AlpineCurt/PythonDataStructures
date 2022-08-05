def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    all_chars = list(s)
    vowel_indices = []
    vowel_list = []
    
    for i, char in enumerate(all_chars):
        if char in vowels:
            vowel_indices.append(i)
            vowel_list.append(char)
            all_chars[i] = ''
    vowel_list.reverse()
    for i, vowel in enumerate(vowel_list):
        all_chars[vowel_indices[i]] = vowel

    out_string = ''

    for char in all_chars:
        out_string += char
    
    return out_string