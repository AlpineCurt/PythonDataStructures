def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    par_open = 0
    par_close = 0
    for char in parens:
        if char == "(":
            par_open += 1
        elif char == ")":
            par_close += 1
        if par_close > par_open:
            return False

    if par_open == par_close:
        return True
    
    return False


# valid_parentheses("()")
# valid_parentheses("()()")
# valid_parentheses("(()())")
# valid_parentheses(")()")
# valid_parentheses("())")
# valid_parentheses("((())")
# valid_parentheses(")()(")