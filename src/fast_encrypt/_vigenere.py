"""
Defines a class for encrypting and decrypting text using the Vigenère cipher.
"""

from ._simple_encryptor import SimpleEncryptor


class Vigenere(SimpleEncryptor):
    """
    Class for encrypting and decrypting text using the Vigenère cipher.

    This class inherits from `SimpleEncryptor`.

    The `Vigenère cipher` is a polyalphabetic substitution cipher that uses a keyword
    to determine the shift for each letter in the plaintext. It's more secure than simple
    substitution ciphers because it employs multiple Caesar ciphers in succession. The
    keyword determines the order of these ciphers and hence the shifting pattern, making it
    more challenging to decipher without the key. Despite its historical significance, it can
    be vulnerable to cryptanalysis, especially with shorter keys or known plaintext attacks.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using the Vigenère cipher.

    decrypt(cipher_text: str) -> str:
        Decrypts the input cipher text into plaintext.

    Examples
    --------
    Encrypting a text:

    >>> from fast_encrypt import Vigenere
    >>> vigenere_cipher = Vigenere('KEY')
    >>> vigenere_cipher.encrypt('Hello World!')
    "Rijvs Uyvjn!"
    >>> vigenere_cipher.encrypt('Jimmy Page')
    "Tmkwc Nkkc"

    Decrypting a text:

    >>> vigenere_cipher = Vigenere('KEY')
    >>> vigenere_cipher.decrypt('Rijvs Uyvjn!')
    "Hello World!"
    >>> vigenere_cipher.decrypt('Tmkwc Nkkc')
    "Jimmy Page"
    """

    def __init__(self, key: str) -> None:
        """
        Initializes the Vigenère cipher with the given key.

        Parameters
        ----------
        key : str
            The key for encryption and decryption.

        Raises
        ------
        ValueError
            If the key contains non-alphabetic characters.
        """

        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self._validate_key(key)
        self._key = key.strip().upper()

    def _validate_key(self, key: str) -> None:
        if not isinstance(key, str):
            raise ValueError('The key must be a str.')

        if not key:
            raise ValueError('The key must not be an empty str.')

        for char in key.strip():
            if not char.isalpha() or char.upper() not in self._alphabet:
                raise ValueError('The key must contains alphabetic chars.')

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using the Vigenère cipher.

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
        >>> vigenere_cipher = Vigenere('KEY')
        >>> vigenere_cipher.encrypt('Hello World!')
        "Rijvs Uyvjn!"
        >>> vigenere_cipher.encrypt('Jimmy Page')
        "Tmkwc Nkkc"
        """

        self._validate_text(text)

        handled_text = self._handle_text(text)

        encrypted_text = ''

        key_index = 0

        for char in handled_text:
            if char.isalpha():
                shift = ord(self._key[key_index % len(self._key)]) - ord('A')
                encrypted_char = chr((ord(char.upper()) - ord('A') + shift) % 26 + ord('A'))

                encrypted_text += encrypted_char if char.isupper() else encrypted_char.lower()

                key_index += 1
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

        return handled_text

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
        >>> vigenere_cipher = Vigenere('KEY')
        >>> vigenere_cipher.decrypt('Rijvs Uyvjn!')
        "Hello World!"
        >>> vigenere_cipher.decrypt('Tmkwc Nkkc')
        "Jimmy Page"
        """

        self._validate_text(cipher_text)

        handled_cipher_text = self._handle_cipher_text(cipher_text)

        decrypted_text = ''

        key_index = 0

        for char in handled_cipher_text:
            if char.isalpha():
                shift = ord(self._key[key_index % len(self._key)]) - ord('A')
                decrypted_char = chr((ord(char.upper()) - ord('A') - shift + 26) % 26 + ord('A'))

                decrypted_text += decrypted_char if char.isupper() else decrypted_char.lower()

                key_index += 1
            else:
                decrypted_text += char

        return decrypted_text

    def _handle_cipher_text(self, cipher_text: str) -> str:
        return cipher_text.strip()
