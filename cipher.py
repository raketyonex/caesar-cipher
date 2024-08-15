def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            result += char
    return result