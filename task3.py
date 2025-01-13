def check_delimiters(s: str) -> str:
    """Checks if the delimiters in the string are symmetric.

    :param s: Input string containing delimiters.
    :return: 'Symmetric' if delimiters are symmetric, 'Not symmetric' otherwise.
    """
    brackets = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return "Not symmetric"

    return "Symmetric" if not stack else "Not symmetric"


if __name__ == "__main__":
    assert check_delimiters("(( ){[ 1 ]( 1 + 3 )( ){ }})") == "Symmetric"
    assert check_delimiters("( 23 ( 2 - 3);") == "Not symmetric"
    assert check_delimiters("( 11 }") == "Not symmetric"
