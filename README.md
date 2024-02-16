<h1 align="center">
    <img src="./docs/img/logo.png" width="200"/>
    <br/>
    <p style="font-size: 30px">fast-encrypt</p>
</h1>
<p align="center">
    <a href="https://pypi.org/project/fast-encrypt/">
        <img src="https://img.shields.io/badge/PyPi-v1.0.0-blue.svg"/>
    </a>
    <a href="https://docs.python.org/3.10/">
        <img src="https://img.shields.io/badge/Python->=%20v3.10-blue.svg"/>
    </a>
    <img src="https://img.shields.io/badge/Coverage-97%25-grren.svg"/>
    <a href="./LICENSE.md">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg"/>
    </a>
    <a href="https://black.readthedocs.io/en/stable/">
        <img src="https://img.shields.io/badge/Code%20style-black-000000.svg"/>
    </a>
</p>

<p align="center">
    <b>fast-encrypt</b> is a comprehensive Python library that offers a variety of cryptographic methods to protect sensitive data simply and effectively.
</p>

# Table of contents

- [Installation](#installation)
- [Docs](#docs)
- [Examples](#examples)
  - [Caesar's cipher](#caesars-cipher)
  - [Morse code](#morse-code)
  - [Substitution cipher](#substitution-cipher)
  - [Pipeline](#pipeline)
  - [RSA](#rsa)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

# Installation

Using pip:

```bash
pip install fast-encrypt
```

# Docs

See our [Docs](./docs/md/docs.md) for comprehensive and detailed documentation on **fast-encrypt**. In the documentation, you will find in-depth explanations, usage examples, and additional resources to help you maximize your experience with **fast-encrypt**.

This package offers classes for:

- <a href="./docs/md/docs.md#Atbash">Atbash cipher</a>
- <a href="./docs/md/docs.md#CaesarsCipher">Caesar's cipher</a>
- <a href="./docs/md/docs.md#HomophonicSubstitution">Homophonic substitution</a>
- <a href="./docs/md/docs.md#MorseCode">Morse code</a>
- <a href="./docs/md/docs.md#Pipeline">Pipeline of simple encryptors</a>
- <a href="./docs/md/docs.md#RSA">RSA cryptosystem</a>
- <a href="./docs/md/docs.md#Substitution">Substitution cipher</a>
- <a href="./docs/md/docs.md#Vigenere">Vigenère cipher</a>

# Examples

## Caesar's cipher

To encrypt some text using **Caesar's cipher**, fist of all, you need import and instantiate the `CaesarsCipher` class providing the shift for chars.

```python
from fast_encrypt import CaesarsCipher


encryptor = CaesarsCipher(1) # shift = 1
```

Then, you'll be able to encrypt a text.

```python
plaintext = 'Hello World!'

encrypted_text = encryptor.encrypt(plaintext)

print(encrypted_text)
```

The `encrypted_text` will be:

```
Ifmmp Xpsme!
```

To decrypt it's very simple.

```python
decrypted_text = encryptor.decrypt(encrypted_text)

print(decrypted_text)
```

The `decrypted_text` will be:

```
Hello World!
```

## Morse code

To encrypt some text using **Morse code**, fist of all, you need import and instantiate the `MorseCode` class.

```python
from fast_encrypt import MorseCode


encryptor = MorseCode()
```

Then, you'll be able to encrypt a text.

```python
plaintext = 'Hello World!'

encrypted_text = encryptor.encrypt(plaintext)

print(encrypted_text)
```

The `encrypted_text` will be:

```
.... . .-.. .-.. --- .-- --- .-. .-.. -..
```

To decrypt it's very simple.

```python
decrypted_text = encryptor.decrypt(encrypted_text)

print(decrypted_text)
```

The `decrypted_text` will be:

```
HELLOWORLD
```

## Substitution cipher

To encrypt some text using **substitution cipher**, fist of all, you need import and instantiate the `Substitution` class providing the alphabet for substitution.

```python
from fast_encrypt import Substitution


encryptor = Substitution('poiuytrewqlkjhgfdsamnbvcxz') # the alphabet for substitution
```

Then, you'll be able to encrypt a text.

```python
plaintext = 'Hello World!'

encrypted_text = encryptor.encrypt(plaintext)

print(encrypted_text)
```

The `encrypted_text` will be:

```
Eykkg Vgsku!
```

To decrypt it's very simple.

```python
decrypted_text = encryptor.decrypt(encrypted_text)

print(decrypted_text)
```

The `decrypted_text` will be:

```
Hello World!
```

## Pipeline

You can create a pipeline of simple encryptors, fist of all, you need import and instantiate the `Pipeline` class providing the list of simple encryptors.

```python
from fast_encrypt import (
    Pipeline,
    CaesarsCipher,
    Substitution,
    MorseCode
)


pipeline = Pipeline([
    CaesarsCipher(3),
    Substitution('mnbvcxzlkjhgfdsapoiuytrewq'),
    MorseCode()
])
```

Then, you'll be able to encrypt a text.

```python
plaintext = 'Hello World!'

encrypted_text = pipeline.encrypt(plaintext)

print(encrypted_text)
```

The `encrypted_text` will be:

```
.... .-.. ... ... --- --.- --- -.-- ... --..
```

To decrypt it's very simple.

```python
decrypted_text = pipeline.decrypt(encrypted_text)

print(decrypted_text)
```

The `decrypted_text` will be:

```
HELLOWORLD
```

## RSA

For a more complex and secure way to encrypt your data, you can use our `RSA` class for the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)).

To encrypt some text using , fist of all, you need import and instantiate the `RSA` class providing the key length in bits (default = 1024).

```python
from fast_encrypt import RSA


encryptor = RSA() # default key length = 1024
```

Then, you must generate the public and private key (public key is used for encrypt a text, private is used for decrypt)

```python
public_key, private_key = encryptor.generate_keypair()
```

Then, you'll be able to encrypt a text.

```python
plaintext = 'Hello World!'

encrypted_text = encryptor.encrypt(public_key, plaintext)

print(encrypted_text)
```

The `encrypted_text` will can be:

```
1485228768820288706400698504222851526198153333611564433069219712708655679297610713312684847266463375809614570944...
```

> The three dots means the result own more numbers.

To decrypt it's very simple.

```python
decrypted_text = encryptor.decrypt(private_key, encrypted_text)

print(decrypted_text)
```

The `decrypted_text` will be:

```
Hello World!
```

# Contributing

You may contribute in several ways like creating new features, fixing bugs, improving documentation and examples or translating any document here to your language. Find more information in [CONTRIBUTING.md](./docs/md/CONTRIBUTING.md).

# License

[MIT](./LICENSE.md) - Alberto Frigatto, 2024
