import pytest

from src.easyencrypt import CaesarsCipher


class TestCaesarsCipher:
    def test_when_receives_shift_3_and_then_encrypts_Hello_World_returns_Khoor_Zruog(self):
        caesars = CaesarsCipher(3)
        entry = 'Hello World!'

        result = caesars.encrypt(entry)
        expected = 'Khoor Zruog!'

        assert result == expected

    def test_when_receives_shift_3_and_then_decrypts_Khoor_Zruog_returns_Hello_World(self):
        caesars = CaesarsCipher(3)
        entry = 'Khoor Zruog!'

        result = caesars.decrypt(entry)
        expected = 'Hello World!'

        assert result == expected

    def test_when_receives_shift_15_and_then_encrypts_and_decrypts_John_Frusciante_returns_the_proper_values(
        self,
    ):
        caesars = CaesarsCipher(15)
        entry = 'John Frusciante'

        encryption_result = caesars.encrypt(entry)
        expected_encryption = 'Ydwc Ugjhrxpcit'

        decryption_result = caesars.decrypt(expected_encryption)
        expected_decryption = 'John Frusciante'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_receives_shift_21_and_then_encrypts_and_decrypts_a_text_returns_the_proper_values(
        self,
    ):
        caesars = CaesarsCipher(21)
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encryption_result = caesars.encrypt(entry)
        expected_encryption = 'Wmvndg (jadxdvghzioz Mzkpwgdxv Azyzmvodqv yj Wmvndg), z j hvdjm kvdn yv Vhzmdxv yj Npg z yv mzbdvj yv Vhzmdxv Gvodiv, nziyj j lpdioj hvdjm yj hpiyj zh vmzv ozmmdojmdvg (zlpdqvgzioz v 47,3% yj ozmmdojmdj npg-vhzmdxvij), xjh 8 510 417,771 fh², z j nzodhj zh kjkpgvxvj (xjh 203 hdgcjzn yz cvwdoviozn, zh vbjnoj yz 2022).'

        decryption_result = caesars.decrypt(expected_encryption)
        expected_decryption = 'Brasil (oficialmente Republica Federativa do Brasil), e o maior pais da America do Sul e da regiao da America Latina, sendo o quinto maior do mundo em area territorial (equivalente a 47,3% do territorio sul-americano), com 8 510 417,771 km², e o setimo em populacao (com 203 milhoes de habitantes, em agosto de 2022).'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_shift_receives_0_raises_ValueError(self):
        with pytest.raises(ValueError):
            CaesarsCipher(0)

    def test_when_shift_receives_minus_1_raises_ValueError(self):
        with pytest.raises(ValueError):
            CaesarsCipher(-1)

    def test_when_shift_receives_26_raises_ValueError(self):
        with pytest.raises(ValueError):
            CaesarsCipher(27)

    def test_when_shift_receives_abc_raises_ValueError(self):
        with pytest.raises(ValueError):
            CaesarsCipher('abc')

    def test_when_shift_receives_nothing_raises_TypeError(self):
        with pytest.raises(TypeError):
            CaesarsCipher()

    def test_when_shift_receives_None_raises_ValueError(self):
        with pytest.raises(ValueError):
            CaesarsCipher(None)

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        caesars = CaesarsCipher(1)

        with pytest.raises(ValueError):
            caesars.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        caesars = CaesarsCipher(1)

        with pytest.raises(TypeError):
            caesars.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        caesars = CaesarsCipher(1)

        with pytest.raises(ValueError):
            caesars.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        caesars = CaesarsCipher(1)

        with pytest.raises(ValueError):
            caesars.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        caesars = CaesarsCipher(1)

        with pytest.raises(TypeError):
            caesars.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        caesars = CaesarsCipher(1)

        with pytest.raises(ValueError):
            caesars.decrypt(None)
