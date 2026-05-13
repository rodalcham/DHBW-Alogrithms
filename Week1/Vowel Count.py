def count_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    text = text.lower()
    for char in text:
        if char in vowels:
            count += 1

    return count
