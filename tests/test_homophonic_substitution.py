import pytest

from src.fast_encrypt import HomophonicSubstitution


class TestHomophonicSubstitution:
    def test_when_receives_key_KEY_and_then_encrypts_and_decrypts_Hello_World_returns_HELLO_WORLD(
        self,
    ):
        h_substitution = HomophonicSubstitution('KEY')
        entry = 'Hello World!'

        encrypted_text = h_substitution.encrypt(entry)
        decrypted_text = h_substitution.decrypt(encrypted_text)

        expected = 'HELLO WORLD!'

        assert decrypted_text == expected

    def test_when_receives_key_KEY_and_then_encrypts_and_decrypts_John_Frusciante_returns_JOHN_FRUSCIANTE(
        self,
    ):
        h_substitution = HomophonicSubstitution('KEY')
        entry = 'John Frusciante'

        encrypted_text = h_substitution.encrypt(entry)
        decrypted_text = h_substitution.decrypt(encrypted_text)

        expected = 'JOHN FRUSCIANTE'

        assert decrypted_text == expected

    def test_when_receives_key_KEY_and_then_encrypts_and_decrypts_a_text_returns_the_proper_value(
        self,
    ):
        h_substitution = HomophonicSubstitution('KEY')
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encrypted_text = h_substitution.encrypt(entry)
        decrypted_text = h_substitution.decrypt(encrypted_text)

        expected = 'BRASIL (OFICIALMENTE REPUBLICA FEDERATIVA DO BRASIL), E O MAIOR PAIS DA AMERICA DO SUL E DA REGIAO DA AMERICA LATINA, SENDO O QUINTO MAIOR DO MUNDO EM AREA TERRITORIAL (EQUIVALENTE A 47,3% DO TERRITORIO SUL-AMERICANO), COM 8 510 417,771 KM², E O SETIMO EM POPULACAO (COM 203 MILHOES DE HABITANTES, EM AGOSTO DE 2022).'

        assert decrypted_text == expected

    def test_when_key_receives_nothing_raises_TypeError(self):
        with pytest.raises(TypeError):
            HomophonicSubstitution()

    def test_when_key_receives_None_raises_ValueError(self):
        with pytest.raises(ValueError):
            HomophonicSubstitution(None)

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        h_substitution = HomophonicSubstitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            h_substitution.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        h_substitution = HomophonicSubstitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(TypeError):
            h_substitution.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        h_substitution = HomophonicSubstitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            h_substitution.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        h_substitution = HomophonicSubstitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            h_substitution.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        h_substitution = HomophonicSubstitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(TypeError):
            h_substitution.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        h_substitution = HomophonicSubstitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            h_substitution.decrypt(None)
