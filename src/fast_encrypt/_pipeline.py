"""
Defines a class for creating a pipeline of encryption and decryption steps.
"""

from ._homophonic_substitution import HomophonicSubstitution
from ._morse_code import MorseCode
from ._simple_encryptor import SimpleEncryptor


class Pipeline:
    """
    Class for creating a pipeline of encryption and decryption steps.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text using the pipeline of encryption steps.

    decrypt(text: str) -> str:
        Decrypts the input text using the pipeline of decryption steps.

    Examples
    --------
    Encrypting a text using a pipeline:

    >>> from encrypt import Pipeline, CaesarsCipher, MorseCode, Vigenere
    >>> pipeline = Pipeline([CaesarsCipher(3), Vigenere('KEY'), MorseCode()])
    >>> pipeline.encrypt('Hello World!')
    "..- .-.. -- -.-- ...- -..- -... -.-- -- --.-"
    >>> pipeline.encrypt('Josh Klinghoffer')
    ".-- ...- - ..- .-. -- ...- ..- .... ..- ...- --. ... .-.. ..."

    Decrypting a text using a pipeline:

    >>> pipeline.decrypt('..- .-.. -- -.-- ...- -..- -... -.-- -- --.-')
    "HELLOWORLD"
    >>> pipeline.decrypt('.-- ...- - ..- .-. -- ...- ..- .... ..- ...- --. ... .-.. ...')
    "JOSHKLINGHOFFER"
    """

    def __init__(self, steps: list[SimpleEncryptor]) -> None:
        """
        Initializes the pipeline with the given encryption steps.

        Parameters
        ----------
        steps : list[Encryptor]
            A list of encryption steps to be applied sequentially.

        Raises
        ------
        ValueError
            If the steps list is not valid.
        """

        self._validate_steps(steps)
        self._steps = steps

    def _validate_steps(self, steps: list[SimpleEncryptor]) -> None:
        if not isinstance(steps, list):
            raise ValueError('The given value must be a list[Encryptor].')

        morse_encryptors = 0
        homophonic_substitution_encryptors = 0

        for step in steps:
            if not isinstance(step, SimpleEncryptor):
                raise ValueError('The given value must be a list[Encryptor].')

            if isinstance(step, MorseCode):
                morse_encryptors += 1

            if isinstance(step, HomophonicSubstitution):
                homophonic_substitution_encryptors += 1

            if morse_encryptors > 1:
                raise ValueError('The given list can only have one MorseCode.')

            if homophonic_substitution_encryptors > 1:
                raise ValueError('The given list can only have one HomophonicSubstitution.')

        if morse_encryptors and not isinstance(steps[-1], MorseCode):
            raise ValueError('The MorseCode must be in list last position.')

        if morse_encryptors and homophonic_substitution_encryptors:
            raise ValueError(
                'The list cannot contain a HomophonicSubstitution and a MorseCode at the same time.'
            )

    def encrypt(self, text: str):
        """
        Encrypts the input text using the pipeline of encryption steps.

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
        >>> pipeline = Pipeline([CaesarsCipher(3), Vigenere('KEY'), MorseCode()])
        >>> pipeline.encrypt('Hello World!')
        "..- .-.. -- -.-- ...- -..- -... -.-- -- --.-"
        >>> pipeline.encrypt('Josh Klinghoffer')
        ".-- ...- - ..- .-. -- ...- ..- .... ..- ...- --. ... .-.. ..."
        """

        encrypted_text = ''

        for i, step in enumerate(self._steps):
            if i == 0:
                encrypted_text = step.encrypt(text)
            else:
                encrypted_text = step.encrypt(encrypted_text)

        return encrypted_text

    def decrypt(self, text: str):
        """
        Decrypts the input text using the pipeline of reverse decryption steps.

        Parameters
        ----------
        text : str
            The cipher text to be decrypted.

        Returns
        -------
        str
            The decrypted plaintext.

        Examples
        --------
        >>> pipeline = Pipeline([CaesarsCipher(3), Vigenere('KEY'), MorseCode()])
        >>> pipeline.decrypt('..- .-.. -- -.-- ...- -..- -... -.-- -- --.-')
        "HELLOWORLD"
        >>> pipeline.decrypt('.-- ...- - ..- .-. -- ...- ..- .... ..- ...- --. ... .-.. ...')
        "JOSHKLINGHOFFER"
        """

        decrypted_text = ''

        reverse_steps = self._steps.copy()
        reverse_steps.reverse()

        for i, step in enumerate(reverse_steps):
            if i == 0:
                decrypted_text = step.decrypt(text)
            else:
                decrypted_text = step.decrypt(decrypted_text)

        return decrypted_text
