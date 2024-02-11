"""
Defines a class for encrypting and decrypting text using substitution cipher.
"""

from ._encryptor import Encryptor


class Substitution(Encryptor):
    """
    Class for encrypting and decrypting text using substitution cipher.

    This class inherits from `Encryptor`.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using substitution cipher.

    decrypt(cipher_text: str) -> str:
        Decrypts the input cipher text into plaintext.

    Examples
    --------
    Encrypting a text

    >>> from encrypt import Substitution
    >>> substitution_cipher = Substitution('QWERTYUIOPASDFGHJKLZXCVBNM')
    >>> substitution_cipher.encrypt('Hello World!')
    "Itssg Vgksr!"
    >>> substitution_cipher.encrypt('John Frusciante')
    "Pgif Ykxleoqfzt"

    Decrypting a text

    >>> substitution_cipher.decrypt('Itssg Vgksr!')
    "Hello World!"
    >>> substitution_cipher.decrypt('Pgif Ykxleoqfzt')
    "John Frusciante"
    """

    def __init__(self, key: str) -> None:
        """
        Initializes the Substitution cipher with the given key.

        Parameters
        ----------
        key : str
            The substitution key (with 26 no repeated alpha chars).

        Raises
        ------
        ValueError
            If the key is not a valid substitution key.
        """

        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        self._validate_key(key)
        self._substitution_dict = self._create_substitution_dict(key)

    def _validate_key(self, key: str) -> None:
        if not isinstance(key, str):
            raise ValueError('The key must be a str.')

        key_length = 26

        if len(key) != key_length:
            raise ValueError('The key must contains 26 chars.')

        key_chars = []

        for char in key.strip():
            if not char.isalpha() or char.upper() not in self._alphabet:
                raise ValueError('The key must contains alphabetic chars.')

            if char.upper() in key_chars:
                raise ValueError('The key must not contains repeated chars.')

            key_chars.append(char.upper())

    def _create_substitution_dict(self, key: str) -> dict[str, str]:
        substitution_dict = {}

        for i, _ in enumerate(self._alphabet):
            substitution_dict[self._alphabet[i]] = key[i].upper()

        return substitution_dict

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using substitution cipher.

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
        >>> substitution_cipher = Substitution('QWERTYUIOPASDFGHJKLZXCVBNM')
        >>> substitution_cipher.encrypt('Hello World!')
        "Itssg Vgksr!"
        >>> substitution_cipher.encrypt('John Frusciante')
        "Pgif Ykxleoqfzt"
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
        >>> substitution_cipher = Substitution('QWERTYUIOPASDFGHJKLZXCVBNM')
        >>> substitution_cipher.decrypt('Itssg Vgksr!')
        "Hello World!"
        >>> substitution_cipher.decrypt('Pgif Ykxleoqfzt')
        "John Frusciante"
        """

        self._validate_text(cipher_text)

        handled_cipher_text = self._handle_cipher_text(cipher_text)

        decrypted_text = ''

        for char in handled_cipher_text:
            for original, substitute in self._substitution_dict.items():
                if char.upper() == substitute:
                    decrypted_text += original if char.isupper() else original.lower()
                    break
            else:
                decrypted_text += char

        return decrypted_text

    def _handle_cipher_text(self, cipher_text: str) -> str:
        return cipher_text.strip()
