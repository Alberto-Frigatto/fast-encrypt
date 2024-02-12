import pytest

from src.easyencrypt import RSA


class TestRSA:
    def test_when_encrypts_and_decrypts_Hello_World_returns_Hello_World(
        self,
    ):
        rsa = RSA()
        entry = 'Hello World!'

        public_key, private_key = rsa.generate_keypair()

        encrypted_text = rsa.encrypt(public_key, entry)
        decrypted_text = rsa.decrypt(private_key, encrypted_text)

        expected = entry

        assert decrypted_text == expected

    def test_when_encrypts_and_decrypts_John_Frusciante_returns_John_Frusciante(
        self,
    ):
        rsa = RSA()
        entry = 'John_Frusciante'

        public_key, private_key = rsa.generate_keypair()

        encrypted_text = rsa.encrypt(public_key, entry)
        decrypted_text = rsa.decrypt(private_key, encrypted_text)

        expected = entry

        assert decrypted_text == expected

    def test_when_encrypts_and_decrypts_a_text_returns_the_proper_value(
        self,
    ):
        rsa = RSA()
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        public_key, private_key = rsa.generate_keypair()

        encrypted_text = rsa.encrypt(public_key, entry)
        decrypted_text = rsa.decrypt(private_key, encrypted_text)

        expected = entry

        assert decrypted_text == expected

    def test_when_key_length_receives_None_raises_ValueError(self):
        with pytest.raises(ValueError):
            RSA(None)

    def test_when_key_length_receives_1023_raises_ValueError(self):
        with pytest.raises(ValueError):
            RSA(1023)

    def test_when_key_length_receives_abc_raises_ValueError(self):
        with pytest.raises(ValueError):
            RSA('abc')

    def test_when_the_encrypt_method_receives_public_key_as_int_raises_ValueError(self):
        rsa = RSA()

        with pytest.raises(ValueError):
            rsa.encrypt(1, 'abc')

    def test_when_the_encrypt_method_receives_public_key_as_str_raises_ValueError(self):
        rsa = RSA()

        with pytest.raises(ValueError):
            rsa.encrypt('abc', 'abc')

    def test_when_the_encrypt_method_receives_public_key_as_None_raises_ValueError(self):
        rsa = RSA()

        with pytest.raises(ValueError):
            rsa.encrypt(None, 'abc')

    def test_when_the_encrypt_method_receives_public_key_as_list_int_raises_ValueError(self):
        rsa = RSA()

        with pytest.raises(ValueError):
            rsa.encrypt([1, 2], 'abc')

    def test_when_the_encrypt_method_receives_public_key_as_tuple_int_str_raises_ValueError(self):
        rsa = RSA()

        with pytest.raises(ValueError):
            rsa.encrypt((1, 'abc'), 'abc')

    def test_when_the_encrypt_method_receives_text_as_int_raises_ValueError(self):
        rsa = RSA()
        public_key, private_key = rsa.generate_keypair()

        with pytest.raises(ValueError):
            rsa.encrypt(public_key, 1)

    def test_when_the_encrypt_method_receives_text_as_None_raises_ValueError(self):
        rsa = RSA()
        public_key, private_key = rsa.generate_keypair()

        with pytest.raises(ValueError):
            rsa.encrypt(public_key, None)

    def test_when_the_decrypt_method_receives_cipher_text_int_raises_ValueError(self):
        rsa = RSA()
        public_key, private_key = rsa.generate_keypair()

        with pytest.raises(ValueError):
            rsa.decrypt(private_key, 1)

    def test_when_the_decrypt_method_receives_cipher_text_None_raises_ValueError(self):
        rsa = RSA()
        public_key, private_key = rsa.generate_keypair()

        with pytest.raises(ValueError):
            rsa.decrypt(private_key, None)
