"""
Defines a class for encrypting and decrypting text using RSA algorithm.
"""

import math
import secrets

_public_key = tuple[int, int]
_private_key = tuple[int, int]


class RSA:
    """
    Class for implementing the RSA algorithm for asymmetric encryption.

    `RSA` is a public-key encryption algorithm widely used in secure data transmission
    and digital signatures. It relies on the practical difficulty of factoring the product
    of two large prime numbers. RSA encryption involves generating a public and private
    key pair, where the public key is used for encryption and the private key for decryption.
    This asymmetric cryptography method ensures secure communication over insecure networks,
    providing confidentiality and authenticity for sensitive information.

    Methods
    -------
    generate_keypair() -> tuple[_public_key, _private_key]:
        Generates the public and private key pair.

    encrypt(public_key: tuple[int, int], text: str) -> str:
        Encrypts text using the specified public key.

    decrypt(private_key: tuple[int, int], cipher_text: str) -> str:
        Decrypts the ciphertext using the specified private key.

    Examples
    --------
    Encrypting a text

    >>> from fast_encrypt import RSA
    >>> rsa = RSA()
    >>> public_key, private_key = rsa.generate_keypair()
    >>> rsa.encrypt(public_key, 'Hello World!')

    The result can be:

    `"7847127900545330234450494651182712418090798037256595068106180662552566637..."`

    Decrypting a text

    >>> rsa.decrypt(
    ...     private_key,
    ...     '7847127900545330234450494651182712418090798037256595068106180662552566637...'
    ... )
    "Hello World!"
    """

    def __init__(self, key_length: int = 1024) -> None:
        """
        Initializes the RSA class with the specified key length (bits qty).

        Parameters
        ----------
        key_length : int, optional
            The RSA key length, by default 1024 (bits qty).

        Raises
        ------
        ValueError
            If the key length is not a valid integer or is less than 1024.
        """

        self._validate_key_length(key_length)
        self._key_length = key_length

    def _validate_key_length(self, key_length: int) -> None:
        if not isinstance(key_length, int):
            raise ValueError('The key_length must be a int.')

        min_key_length = 1024

        if key_length < min_key_length:
            raise ValueError('The key_length must be bigger than 2048.')

    def generate_keypair(self) -> tuple[_public_key, _private_key]:
        """
        Generates a pair of public and private keys.

        Returns
        -------
        tuple[_public_key, _private_key]
            A pair of public and private keys.
        """

        p = self._generate_prime_number()
        q = self._generate_prime_number()
        n = p * q
        phi = (p - 1) * (q - 1)

        e = secrets.randbelow(phi - 1) + 1

        while math.gcd(e, phi) != 1:
            e = secrets.randbelow(phi - 1) + 1

        d = pow(e, -1, phi)

        public_key = e, n
        private_key = d, n

        return public_key, private_key

    def _generate_prime_number(self) -> int:
        p = 4

        while not self._is_prime(p):
            p = self._generate_prime_candidate()

        return p

    def _is_prime(self, number: int) -> bool:
        if number <= 1:
            return False
        if number <= 3:
            return True

        k = 128

        for _ in range(k):
            x = secrets.randbelow(number - 1) + 1
            if pow(x, number - 1, number) != 1:
                return False
        return True

    def _generate_prime_candidate(self) -> int:
        prime_number = secrets.randbits(self._key_length)
        prime_number |= (1 << self._key_length - 1) | 1

        return prime_number

    def encrypt(self, public_key: _public_key, text: str):
        """
        Encrypts the text using the specified public key.

        Parameters
        ----------
        public_key : _public_key
            The public key for encryption.
        text : str
            The text to be encrypted.

        Returns
        -------
        str
            The encrypted text.

        Examples
        --------
        Encrypting a text

        >>> rsa = RSA()
        >>> public_key, private_key = rsa.generate_keypair()
        >>> rsa.encrypt(public_key, 'Hello World!')
        "7847127900545330234450494651182712418090798037256595068106180662552566637..."
        """

        self._validate_key(public_key)
        self._validate_text(text)

        handled_text = self._handle_text(text)

        e, n = public_key

        encrypted_text = [str(pow(ord(char), e, n)) for char in handled_text]

        return ' '.join(encrypted_text)

    def _validate_key(self, key: str) -> None:
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError('The given value must be tuple[int, int].')

        for number in key:
            if not isinstance(number, int):
                raise ValueError('The given value must be tuple[int, int].')

    def _validate_text(self, text: str) -> None:
        if not isinstance(text, str):
            raise ValueError('The given value must be a str.')

    def _handle_text(self, text: str) -> str:
        return text.strip()

    def decrypt(self, private_key: _private_key, cipher_text: str) -> str:
        """
        Decrypts the cipher text using the specified private key.

        Parameters
        ----------
        private_key : _private_key
            The private key for decryption.
        cipher_text : str
            The cipher text to be decrypted.

        Returns
        -------
        str
            The decrypted plaintext.

        Examples
        --------
        Encrypting a text

        >>> rsa = RSA()
        >>> public_key, private_key = rsa.generate_keypair()
        >>> rsa.decrypt(
        ...     private_key,
        ...     '7847127900545330234450494651182712418090798037256595068106180662552566637...'
        ... )
        "Hello World!"
        """

        self._validate_key(private_key)
        self._validate_text(cipher_text)

        handled_text = self._handle_text(cipher_text)

        d, n = private_key

        cipher_list = handled_text.split(' ')

        plain_chars = [chr(pow(int(char), d, n)) for char in cipher_list]

        decrypted_text = ''.join(plain_chars)

        return decrypted_text
