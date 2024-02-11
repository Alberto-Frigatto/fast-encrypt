"""
Defines a class for encrypting and decrypting text using Caesar's cipher.
"""

from ._simple_encryptor import SimpleEncryptor


class CaesarsCipher(SimpleEncryptor):
    """
    Class for encrypting and decrypting text using Caesar's cipher.

    This class inherits from `SimpleEncryptor`.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using Caesar's cipher.

    decrypt(cipher_text: str) -> str:
        Decrypts the input cipher text into plaintext.

    Examples
    --------
    Encrypting a text

    >>> from encrypt import CaesarsCipher
    >>> caesar_cipher = CaesarsCipher(17)
    >>> caesar_cipher.encrypt('Hello World!')
    "Yvccf Nficu!"
    >>> caesar_cipher.encrypt('David Gilmour')
    "Urmzu Xzcdfli"

    Decrypting a text

    >>> caesar_cipher = CaesarsCipher(17)
    >>> caesar_cipher.decrypt('Yvccf Nficu!')
    "Hello World!"
    >>> caesar_cipher.decrypt('Urmzu Xzcdfli')
    "David Gilmour"
    """

    def __init__(self, shift: int) -> None:
        """
        Initializes the Caesar's cipher with the given shift.

        Parameters
        ----------
        shift : int
            The shift value for encryption and decryption (must be 0 < shift < 26).

        Raises
        ------
        ValueError
            If the shift is not a valid integer between 1 and 25.
        """

        self._validate_shift(shift)
        self._shift = shift
        self._alphabetic_limits = ord('A'), ord('Z')

    def _validate_shift(self, shift: int) -> None:
        if not isinstance(shift, int):
            raise ValueError('The given value must be a int.')

        if shift < 1 or shift > 25:
            raise ValueError('The given value must be >= 1 and < 26.')

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using Caesar's cipher.

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
        >>> caesar_cipher = CaesarsCipher(17)
        >>> caesar_cipher.encrypt('Hello World!')
        "Yvccf Nficu!"
        >>> caesar_cipher.encrypt('David Gilmour')
        "Urmzu Xzcdfli"
        """

        self._validate_text(text)

        handled_text = self._handle_text(text)

        encrypted_text = ''

        for char in handled_text:
            if char.isalpha():
                shifted_char_index = ord(char.upper()) + self._shift

                upper_limit = self._alphabetic_limits[1]

                if shifted_char_index > upper_limit:
                    shifted_char_index -= 26

                encrypted_text += (
                    chr(shifted_char_index) if char.isupper() else chr(shifted_char_index).lower()
                )
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
        >>> caesar_cipher = CaesarsCipher(17)
        >>> caesar_cipher.decrypt('Yvccf Nficu!')
        "Hello World!"
        >>> caesar_cipher.decrypt('Urmzu Xzcdfli')
        "David Gilmour"
        """

        self._validate_text(cipher_text)

        handled_cipher_text = self._handle_cipher_text(cipher_text)

        decrypted_text = ''

        for char in handled_cipher_text:
            if char.isalpha():
                original_char_index = ord(char.upper()) - self._shift

                lower_limit = self._alphabetic_limits[0]

                if original_char_index < lower_limit:
                    original_char_index += 26

                decrypted_text += (
                    chr(original_char_index) if char.isupper() else chr(original_char_index).lower()
                )
            else:
                decrypted_text += char

        return decrypted_text

    def _handle_cipher_text(self, cipher_text: str) -> str:
        return cipher_text.strip()
