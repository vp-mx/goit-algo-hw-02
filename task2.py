import re
from collections import deque


def is_palindrome(s: str) -> bool:
    """Checks if a string is a palindrome, ignoring case, spaces, and punctuation.

    :param s: Input string.
    :return: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase and remove non-alphanumeric characters
    s = re.sub(r"[^a-zA-Z0-9]", "", s.lower())

    # Create a deque from the characters of the string
    deque_s = deque(s)

    while len(deque_s) > 1:
        if deque_s.popleft() != deque_s.pop():
            return False

    return True


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(is_palindrome("race a car"))  # False
    print(is_palindrome("Madam, I'm Adam"))  # True
