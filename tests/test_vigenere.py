import pytest

from src.easyencrypt import Vigenere


class TestVigenere:
    def test_when_receives_key_KEY_and_then_encrypts_Hello_World_returns_Rijvs_Uyvjn(
        self,
    ):
        vigenere = Vigenere('KEY')
        entry = 'Hello World!'

        result = vigenere.encrypt(entry)
        expected = 'Rijvs Uyvjn!'

        assert result == expected

    def test_when_receives_key_KEY_and_then_decrypts_Rijvs_Uyvjn_returns_Hello_World(
        self,
    ):
        vigenere = Vigenere('KEY')
        entry = 'Rijvs Uyvjn!'

        result = vigenere.decrypt(entry)
        expected = 'Hello World!'

        assert result == expected

    def test_when_receives_key_californication_and_then_encrypts_and_decrypts_John_Frusciante_returns_the_proper_values(
        self,
    ):
        vigenere = Vigenere('californication')
        entry = 'John Frusciante'

        encryption_result = vigenere.encrypt(entry)
        expected_encryption = 'Losv Kflfkkagbs'

        decryption_result = vigenere.decrypt(expected_encryption)
        expected_decryption = 'John Frusciante'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_receives_key_cantstop_and_then_encrypts_and_decrypts_a_text_returns_the_proper_values(
        self,
    ):
        vigenere = Vigenere('cantstop')
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encryption_result = vigenere.encrypt(entry)
        expected_encryption = 'Drnlae (cukcvtdfscve Exhnpakcn Ywwsgctvos wc Qtafbd), x c bcibk htwh fa Nfwkwrc db Lme s sc rrzatc sc Azxjbqp Nagbft, gtpdb h inwcvo ztahf sq mhgvh sb crrt lxfgktbkatz (tsuvosescve n 47,3% wg msgtighjbc hwl-nfwkwrcnb), vgf 8 510 417,771 yb², g o fxlbad gm chhnzpeab (vgf 203 axnhbxk ws wcbvmsghtu, ez tyhgiq dr 2022).'

        decryption_result = vigenere.decrypt(expected_encryption)
        expected_decryption = 'Brasil (oficialmente Republica Federativa do Brasil), e o maior pais da America do Sul e da regiao da America Latina, sendo o quinto maior do mundo em area territorial (equivalente a 47,3% do territorio sul-americano), com 8 510 417,771 km², e o setimo em populacao (com 203 milhoes de habitantes, em agosto de 2022).'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_key_receives_0_raises_ValueError(self):
        with pytest.raises(ValueError):
            Vigenere(0)

    def test_when_key_receives_1_raises_ValueError(self):
        with pytest.raises(ValueError):
            Vigenere(1)

    def test_when_key_receives_empty_str_raises_ValueError(self):
        with pytest.raises(ValueError):
            Vigenere('')

    def test_when_key_receives_abcdefghijklmnopqrstuvwxyzç_raises_ValueError(self):
        with pytest.raises(ValueError):
            Vigenere('abcç')

    def test_when_key_receives_nothing_raises_TypeError(self):
        with pytest.raises(TypeError):
            Vigenere()

    def test_when_key_receives_None_raises_ValueError(self):
        with pytest.raises(ValueError):
            Vigenere(None)

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        vigenere = Vigenere('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            vigenere.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        vigenere = Vigenere('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(TypeError):
            vigenere.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        vigenere = Vigenere('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            vigenere.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        vigenere = Vigenere('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            vigenere.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        vigenere = Vigenere('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(TypeError):
            vigenere.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        vigenere = Vigenere('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            vigenere.decrypt(None)
