"""
Defines the abstract base class for encryptors.
"""

from abc import ABCMeta, abstractmethod


class SimpleEncryptor(metaclass=ABCMeta):
    """
    Abstract base class for encryptors.

    Methods
    -------
    encrypt(text: str) -> str:
        Encrypts the input text.

    decrypt(cipher_text: str) -> str:
        Decrypts the input cipher text.
    """

    @abstractmethod
    def encrypt(self, text: str) -> str:
        """
        Encrypts the input text.

        Parameters
        ----------
        text : str
            The plaintext to be encrypted.

        Returns
        -------
        str
            The encrypted cipher text.
        """

    @abstractmethod
    def decrypt(self, cipher_text: str) -> str:
        """
        Decrypts the input cipher text.

        Parameters
        ----------
        cipher_text : str
            The cipher text to be decrypted.

        Returns
        -------
        str
            The decrypted plaintext.
        """
