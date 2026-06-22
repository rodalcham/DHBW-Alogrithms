def reverse_string(text):
    stack = []

    for char in text:
        stack.append(char)

    reversed_text = ""

    while stack:
        reversed_text += stack.pop()

    return reversed_text


# Example
print(reverse_string("hello")) 