# coding=utf-8

import argparse
import math

ALPHABET = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
            'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ALPHABET_ENG = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']


def decrypt(text, keyWord):
    """
    >>> decrypt('ucv rmom zjossax', 'angel')
    too many secrets
    """
    keyText = keyWord * math.ceil((len(text) / len(keyWord)))
    result = ''
    textWithoutSpases = ''.join([l for l in text if l.isalpha()]).lower()

    for index, letter in enumerate(textWithoutSpases):
        alphabet = getAlphabet(letter)
        result += alphabet[(letterIndex(letter, alphabet) - letterIndex(keyText[index], alphabet))-1]

    return restoreText(text, result)


def encrypt(text, keyWord):
    """

    :param text: text for cipher
    :param keyWord: keyword
    :param alphabet: Using alphabet
    :return: coded message
    >>> encrypt('too many secrets', 'angel')
    ucv rmom zjossax
    """
    keyText = keyWord * math.ceil((len(text) / len(keyWord)))
    result = ''
    textWithoutSpases = ''.join([l for l in text if l.isalpha()]).lower()
    for index, letter in enumerate(textWithoutSpases):
        alphabet = getAlphabet(letter)
        alphabetIndex = (letterIndex(letter, alphabet) + letterIndex(keyText[index], alphabet))-1
        if alphabetIndex >= len(alphabet):
            alphabetIndex = alphabetIndex - len(alphabet)
        result += alphabet[alphabetIndex]

    return restoreText(text, result)


def getAlphabet(letter):
    if letter in ALPHABET_ENG:
        alphabet = ALPHABET_ENG
    elif letter in ALPHABET:
        alphabet = ALPHABET
    else:
        raise Exception('Letter %s is not in latin or kyrilic letter')
    return alphabet


def restoreText(origText, cipferText):
    result = cipferText
    upperIndexes = []
    for index, letter in enumerate(origText):
        if not letter.isalpha():
            result = result[:index] + letter + result[index:]
        if letter.isupper():
            upperIndexes.append(index)

    result = "".join(c.upper() if i in upperIndexes else c for i, c in enumerate(result))
    return result


def letterIndex(letter, alphabet=None):
    if not alphabet:
        alphabet = ALPHABET
    return alphabet.index(letter) + 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Welcome to MM7Deshifr.')
    parser.add_argument(
        'message',
        metavar='--m',
        help='Message'
    )
    parser.add_argument(
        'key',
        help='encrypt key'
    )
    parser.add_argument('--encrypt', help='flag for encryption and decryption', action="store_true")
    args = parser.parse_args()
    if args.encrypt:
        print(encrypt(args.message, args.key))
    else:
        print(decrypt(args.message, args.key))
