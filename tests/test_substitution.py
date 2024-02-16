import pytest

from src.fast_encrypt import Substitution


class TestSubstitution:
    def test_when_receives_key_POIUYTREWQLKJHGFDSAMNBVCXZ_and_then_encrypts_Hello_World_returns_Eykkg_Vgsku(
        self,
    ):
        substitution = Substitution('POIUYTREWQLKJHGFDSAMNBVCXZ')
        entry = 'Hello World!'

        result = substitution.encrypt(entry)
        expected = 'Eykkg Vgsku!'

        assert result == expected

    def test_when_receives_key_POIUYTREWQLKJHGFDSAMNBVCXZ_and_then_decrypts_Eykkg_Vgsku_returns_Hello_World(
        self,
    ):
        substitution = Substitution('POIUYTREWQLKJHGFDSAMNBVCXZ')
        entry = 'Eykkg Vgsku!'

        result = substitution.decrypt(entry)
        expected = 'Hello World!'

        assert result == expected

    def test_when_receives_key_lkjhgfdsamnbvcxzpoiuytrewq_and_then_encrypts_and_decrypts_John_Frusciante_returns_the_proper_values(
        self,
    ):
        substitution = Substitution('lkjhgfdsamnbvcxzpoiuytrewq')
        entry = 'John Frusciante'

        encryption_result = substitution.encrypt(entry)
        expected_encryption = 'Mxsc Foyijalcug'

        decryption_result = substitution.decrypt(expected_encryption)
        expected_decryption = 'John Frusciante'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_receives_key_mnbvcxzpoiuytrewqlkjhgfdsa_and_then_encrypts_and_decrypts_a_text_returns_the_proper_values(
        self,
    ):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encryption_result = substitution.encrypt(entry)
        expected_encryption = 'Nlmkoy (exobomytcrjc Lcwhnyobm Xcvclmjogm ve Nlmkoy), c e tmoel wmok vm Mtclobm ve Khy c vm lczome vm Mtclobm Ymjorm, kcrve e qhorje tmoel ve thrve ct mlcm jcllojelomy (cqhogmycrjc m 47,3% ve jcllojeloe khy-mtclobmre), bet 8 510 417,771 ut², c e kcjote ct wewhymbme (bet 203 toypeck vc pmnojmrjck, ct mzekje vc 2022).'

        decryption_result = substitution.decrypt(expected_encryption)
        expected_decryption = 'Brasil (oficialmente Republica Federativa do Brasil), e o maior pais da America do Sul e da regiao da America Latina, sendo o quinto maior do mundo em area territorial (equivalente a 47,3% do territorio sul-americano), com 8 510 417,771 km², e o setimo em populacao (com 203 milhoes de habitantes, em agosto de 2022).'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_key_receives_0_raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution(0)

    def test_when_key_receives_1_raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution(1)

    def test_when_key_receives_abc_raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution('abc')

    def test_when_key_receives_abcdefghijklmnopqrstuvwxy__raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution('abcdefghijklmnopqrstuvwxy_')

    def test_when_key_receives_abcdefghijklmnopqrstuvwxyzç_raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution('abcdefghijklmnopqrstuvwxyzç')

    def test_when_key_receives_abcdefghijklmnopqrstuvwxya_raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution('abcdefghijklmnopqrstuvwxya')

    def test_when_key_receives_nothing_raises_TypeError(self):
        with pytest.raises(TypeError):
            Substitution()

    def test_when_key_receives_None_raises_ValueError(self):
        with pytest.raises(ValueError):
            Substitution(None)

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            substitution.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(TypeError):
            substitution.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            substitution.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            substitution.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(TypeError):
            substitution.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        substitution = Substitution('mnbvcxzpoiuytrewqlkjhgfdsa')

        with pytest.raises(ValueError):
            substitution.decrypt(None)
