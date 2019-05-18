def is_palindrome(phrase):
    stripped = list(phrase.replace(" ", ""))
    cont = True
    while cont and len(stripped) > 0:
        if len(stripped) == 1:
            break
        if stripped[0] != stripped[-1]:
            cont = False
        stripped.pop(0)
        stripped.pop(-1)

    return cont


print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('amanaplanacanalpanama'))  # True
