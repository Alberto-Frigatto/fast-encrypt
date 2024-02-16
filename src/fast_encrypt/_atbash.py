"""
Defines a class for encrypting and decrypting text using the Atbash cipher.
"""

from ._simple_encryptor import SimpleEncryptor


class Atbash(SimpleEncryptor):
    """
    Class for encrypting and decrypting text using the Atbash cipher.

    This class inherits from `SimpleEncryptor`.

    The `Atbash cipher` is a basic encryption method dating back to biblical times.
    It substitutes each letter of the alphabet with its inverse counterpart, such that
    `"A"` is replaced by `"Z"` and vice versa. While easily reversible and lacking substantial
    security, it serves well for simple message encoding and decoding purposes.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using the Atbash cipher.

    decrypt(cipher_text: str) -> str:
        Decrypts the input cipher text into plaintext.

    Examples
    --------
    Encrypting a text:

    >>> from fast_encrypt import Atbash
    >>> atbash_cipher = Atbash()
    >>> atbash_cipher.encrypt('Hello World!')
    "Svool Dliow!"
    >>> atbash_cipher.encrypt('Billie Joe Armstrong')
    "Yroorv Qlv Zinhgilmt"

    Decrypting a text:

    >>> atbash_cipher = Atbash()
    >>> atbash_cipher.decrypt('Svool Dliow!')
    "Hello World!"
    >>> atbash_cipher.decrypt('Yroorv Qlv Zinhgilmt')
    "Billie Joe Armstrong"
    """

    def __init__(self) -> None:
        """
        Initializes the Atbash cipher.
        """

        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self._substitution_dict = self._create_substitution_dict()

    def _create_substitution_dict(self) -> dict[str, str]:
        alphabet_chars = list(self._alphabet)
        alphabet_chars.reverse()
        reverse_alphabet = ''.join(alphabet_chars)

        substitution_dict = {}

        for i, _ in enumerate(self._alphabet):
            substitution_dict[self._alphabet[i]] = reverse_alphabet[i]

        return substitution_dict

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using the Atbash cipher.

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
        >>> atbash_cipher = Atbash()
        >>> atbash_cipher.encrypt('Hello World!')
        "Svool Dliow!"
        >>> atbash_cipher.encrypt('Billie Joe Armstrong')
        "Yroorv Qlv Zinhgilmt"
        """

        self._validate_text(text)

        handled_text = self._handle_text(text)

        encrypted_text = ''

        for char in handled_text:
            for original, substitute in self._substitution_dict.items():
                if char.upper() == original:
                    encrypted_text += substitute if char.isupper() else substitute.lower()
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
        >>> atbash_cipher = Atbash()
        >>> atbash_cipher.decrypt('Svool Dliow!')
        "Hello World!"
        >>> atbash_cipher.decrypt('Yroorv Qlv Zinhgilmt')
        "Billie Joe Armstrong"
        """
        return self.encrypt(cipher_text)
