'''
`fast-encrypt`
============

fast-encrypt is a comprehensive Python library that offers a
variety of cryptographic methods to protect sensitive data simply and effectively.

Github link https://github.com/Alberto-Frigatto/fast-encrypt
PyPi link https://pypi.org/project/fast-encrypt/
'''

from ._atbash import Atbash
from ._caesars_cipher import CaesarsCipher
from ._homophonic_substitution import HomophonicSubstitution
from ._morse_code import MorseCode
from ._pipeline import Pipeline
from ._rsa import RSA
from ._substitution import Substitution
from ._vigenere import Vigenere

__author__ = 'Alberto Frigatto de Andrade Ferreira'
__contact__ = 'albertofrigatto.comercial@gmail.com'
__copyright__ = 'Copyright 2024, Alberto Frigatto'
__date__ = '2024/02/13'
__deprecated__ = False
__email__ = 'albertofrigatto.comercial@gmail.com'
__license__ = 'MIT'
__maintainer__ = 'Alberto Frigatto'
__status__ = 'Production'
__version__ = '0.0.1'
