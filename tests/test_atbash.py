import pytest

from src.easyencrypt import Atbash


class TestAtbash:
    def test_when_encrypts_Hello_World_returns_Svool_Dliow(self):
        atbash = Atbash()
        entry = 'Hello World!'

        result = atbash.encrypt(entry)
        expected = 'Svool Dliow!'

        assert result == expected

    def test_when_decrypts_Svool_Dliow_returns_Hello_World(self):
        atbash = Atbash()
        entry = 'Svool Dliow!'

        result = atbash.decrypt(entry)
        expected = 'Hello World!'

        assert result == expected

    def test_when_encrypts_and_decrypts_John_Frusciante_returns_the_proper_values(
        self,
    ):
        atbash = Atbash()
        entry = 'John Frusciante'

        encryption_result = atbash.encrypt(entry)
        expected_encryption = 'Qlsm Uifhxrzmgv'

        decryption_result = atbash.decrypt(expected_encryption)
        expected_decryption = 'John Frusciante'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_encrypts_and_decrypts_a_text_returns_the_proper_values(
        self,
    ):
        atbash = Atbash()
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encryption_result = atbash.encrypt(entry)
        expected_encryption = 'Yizhro (lurxrzonvmgv Ivkfyorxz Uvwvizgrez wl Yizhro), v l nzrli kzrh wz Znvirxz wl Hfo v wz ivtrzl wz Znvirxz Ozgrmz, hvmwl l jfrmgl nzrli wl nfmwl vn zivz gviirglirzo (vjfrezovmgv z 47,3% wl gviirglirl hfo-znvirxzml), xln 8 510 417,771 pn², v l hvgrnl vn klkfozxzl (xln 203 nroslvh wv szyrgzmgvh, vn ztlhgl wv 2022).'

        decryption_result = atbash.decrypt(expected_encryption)
        expected_decryption = 'Brasil (oficialmente Republica Federativa do Brasil), e o maior pais da America do Sul e da regiao da America Latina, sendo o quinto maior do mundo em area territorial (equivalente a 47,3% do territorio sul-americano), com 8 510 417,771 km², e o setimo em populacao (com 203 milhoes de habitantes, em agosto de 2022).'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        atbash = Atbash()

        with pytest.raises(ValueError):
            atbash.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        atbash = Atbash()

        with pytest.raises(TypeError):
            atbash.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        atbash = Atbash()

        with pytest.raises(ValueError):
            atbash.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        atbash = Atbash()

        with pytest.raises(ValueError):
            atbash.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        atbash = Atbash()

        with pytest.raises(TypeError):
            atbash.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        atbash = Atbash()

        with pytest.raises(ValueError):
            atbash.decrypt(None)
