"""
Defines a class for encrypting and decrypting text using Morse code.
"""

from ._simple_encryptor import SimpleEncryptor


class MorseCode(SimpleEncryptor):
    """
    Class for encrypting and decrypting text using Morse code.

    This class inherits from `SimpleEncryptor`.

    The `Morse code` is a method of encoding text characters as sequences
    of two different signal durations called dots and dashes. It's widely
    used for transmitting telegraphic information where long and short signals
    represent letters and numbers.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using Morse code.

    decrypt(morse_code: str) -> str:
        Decrypts the input Morse code into plaintext.

    Examples
    --------
    Encrypting a text

    >>> from fast_encrypt import MorseCode
    >>> morse = MorseCode()
    >>> morse.encrypt('Hello World!')
    ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
    >>> morse.encrypt('Jimi Hendrix')
    ".--- .. -- .. .... . -. -.. .-. .. -..-"

    Decrypting a text

    >>> morse.decrypt('.... . .-.. .-.. --- .-- --- .-. .-.. -..')
    "HELLOWORLD"
    >>> morse.decrypt('.--- .. -- .. .... . -. -.. .-. .. -..-')
    "JIMIHENDRIX"
    """

    _chars_morse = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
    }

    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text using Morse code.

        Parameters
        ----------
        text : str
            The plaintext to be encrypted.

        Returns
        -------
        str
            The encrypted Morse code.

        Examples
        --------
        >>> morse = MorseCode()
        >>> morse.encrypt('Hello World!')
        ".... . .-.. .-.. --- .-- --- .-. .-.. -.."
        >>> morse.encrypt('Jimi Hendrix')
        ".--- .. -- .. .... . -. -.. .-. .. -..-"
        """

        self._validate_text(text)

        encrypted_text = self._handle_text(text)

        for char, m_code in self._chars_morse.items():
            if char in encrypted_text:
                encrypted_text = encrypted_text.replace(char, m_code)

        return encrypted_text

    def _validate_text(self, text: str) -> None:
        if not isinstance(text, str):
            raise ValueError('The given value must be a str.')

    def _handle_text(self, text: str) -> str:
        handled_text = text.strip().upper().replace(' ', '')

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
                if letter in handled_text:
                    handled_text = handled_text.replace(letter, key)

        chars = list(handled_text)

        i = 0

        while True:
            if i == len(chars):
                break

            if chars[i] not in self._chars_morse:
                chars.pop(i)
                continue

            i += 1

        handled_text = ' '.join(chars)

        return handled_text

    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the input Morse code into plaintext.

        Parameters
        ----------
        cipher_text : str
            The Morse code to be decrypted.

        Returns
        -------
        str
            The decrypted plaintext.

        Examples
        --------
        >>> morse = MorseCode()
        >>> morse.decrypt('.... . .-.. .-.. --- .-- --- .-. .-.. -..')
        "HELLOWORLD"
        >>> morse.decrypt('.--- .. -- .. .... . -. -.. .-. .. -..-')
        "JIMIHENDRIX"
        """

        self._validate_cipher_text(cipher_text)

        handled_m_code = self._handle_cipher_text(cipher_text)

        chars = handled_m_code.split()

        for i, m_char in enumerate(chars):
            for char, m_code in self._chars_morse.items():
                if m_char == m_code:
                    chars[i] = char

        decrypted_m_code = ''.join(chars)

        return decrypted_m_code

    def _validate_cipher_text(self, cipher_text: str) -> None:
        if not isinstance(cipher_text, str):
            raise ValueError('The given value must be a str.')

        m_c_chars = cipher_text.strip().split()

        for char in m_c_chars:
            if char not in self._chars_morse.values():
                raise ValueError('The given value has invalid morse chars.')

    def _handle_cipher_text(self, cipher_text: str) -> str:
        return cipher_text.strip()
