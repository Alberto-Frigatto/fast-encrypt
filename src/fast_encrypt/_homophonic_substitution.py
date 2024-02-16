"""
Defines a class for encrypting and decrypting text using the homophonic substitution cipher.
"""

import random

from ._simple_encryptor import SimpleEncryptor


class HomophonicSubstitution(SimpleEncryptor):
    """
    Class for encrypting and decrypting text using the Homophonic Substitution cipher.

    This class inherits from `SimpleEncryptor`.

    The `homophonic substitution` cipher replaces each plaintext character with multiple
    cipher characters to create ambiguity and increase security. This technique, used in
    cryptographic systems, assigns more than one ciphertext symbol to certain plaintext
    symbols, making frequency analysis and decryption more challenging.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using the Homophonic Substitution cipher.

    decrypt(cipher_text: str) -> str:
        Decrypts the input cipher text into plaintext.

    Examples
    --------
    Encrypting a text:

    >>> from fast_encrypt import HomophonicSubstitution
    >>> homophonic_cipher = HomophonicSubstitution('KEY')
    >>> homophonic_cipher.encrypt('Saul Hudson')

    The result can be:

    - `"iEL- ps@i<1"`
    - `"kl_% Ms@i<3"`
    - `"im_% M_[k:v"`
    - `"ilL- M_@kPv"`
    - `...`

    Decrypting a text:

    >>> homophonic_cipher = HomophonicSubstitution('KEY')
    >>> homophonic_cipher.decrypt("iEL- ps@i<1")
    "SAUL HUDSON"
    >>> homophonic_cipher.decrypt("im_% M_[k:v")
    "SAUL HUDSON"
    """

    def __init__(self, key: int | str) -> None:
        """
        Initializes the Homophonic Substitution cipher with the given key.

        Parameters
        ----------
        key : int | str
            The key for encryption and decryption.
        """

        self._validate_key(key)
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._substitution_dict = self._create_substitution_dict(key)

    def _validate_key(self, key: int | str) -> None:
        if not isinstance(key, (int, str)):
            raise ValueError('The given value must be an int or str.')

    def _create_substitution_dict(self, key: int | str) -> dict[str, list]:
        substitute_chars = [chr(i) for i in range(33, 127)]

        random_generator = random.Random(key)

        substitution_dict = {}

        for char in self._alphabet:
            chosen_substitute_chars = {}

            for i in range(3):
                random_char = random_generator.choice(substitute_chars)
                substitute_chars.remove(random_char)
                chosen_substitute_chars[i] = random_char

            substitution_dict[char] = list(chosen_substitute_chars.values())

        return substitution_dict

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using the Homophonic Substitution cipher.

        Parameters
        ----------
        text : str
            The plaintext to be encrypted.

        Returns
        -------
        str
            The encrypted cipher text.

        Examples
        --------
        Encrypting a text:

        >>> homophonic_cipher = HomophonicSubstitution('KEY')
        >>> homophonic_cipher.encrypt('Saul Hudson')

        The result can be:

        - `"iEL- ps@i<1"`
        - `"kl_% Ms@i<3"`
        - `"im_% M_[k:v"`
        - `"ilL- M_@kPv"`
        - `...`
        """

        self._validate_text(text)

        handled_text = self._handle_text(text)

        encrypted_text = ''

        random_generator = random.Random()

        for char in handled_text:
            for original, substitute_chars in self._substitution_dict.items():
                if char.upper() == original:
                    encrypted_text += random_generator.choice(substitute_chars)
                    break
            else:
                encrypted_text += char

        return encrypted_text

    def _validate_text(self, text: str) -> None:
        if not isinstance(text, str):
            raise ValueError('The given value must be a str.')

    def _handle_text(self, text: str) -> str:
        handled_text = text.strip()

        substitute_letters = {
            'A': ('Á', 'À', 'Ã', 'Â', 'Ä'),
            'E': ('É', 'È', 'Ê', 'Ë'),
            'I': ('Í', 'Ì', 'Î', 'Ï'),
            'O': ('Ò', 'Ó', 'Ô', 'Õ', 'Ö'),
            'U': ('Ú', 'Ù', 'Û', 'Ü'),
            'C': ('Ç',),
        }

        for key, letters in substitute_letters.items():
            for letter in letters:
                if letter in handled_text.upper():
                    handled_text = handled_text.replace(letter, key)
                    handled_text = handled_text.replace(letter.lower(), key.lower())

        prepared_text = ''

        for char in handled_text:
            if char != ' ' and char.upper() not in self._alphabet:
                prepared_text += f'\0{char}'
            else:
                prepared_text += char

        return prepared_text

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the input cipher text into plaintext.

        Parameters
        ----------
        cipher_text : str
            The cipher text to be decrypted.

        Returns
        -------
        str
            The decrypted plaintext.

        Examples
        --------
        >>> homophonic_cipher = HomophonicSubstitution('KEY')
        >>> homophonic_cipher.decrypt("iEL- ps@i<1")
        "SAUL HUDSON"
        >>> homophonic_cipher.decrypt("im_% M_[k:v")
        "SAUL HUDSON"
        """

        self._validate_text(cipher_text)

        handled_cipher_text = self._handle_cipher_text(cipher_text)

        decrypted_text = ''

        is_special_char = False

        for char in handled_cipher_text:
            for original, substitute_chars in self._substitution_dict.items():
                if is_special_char:
                    decrypted_text += char
                    is_special_char = False
                    break

                if char in substitute_chars:
                    decrypted_text += original
                    break
            else:
                if char == '\0':
                    is_special_char = True
                else:
                    decrypted_text += char

        return decrypted_text

    def _handle_cipher_text(self, cipher_text: str) -> str:
        return cipher_text.strip()
