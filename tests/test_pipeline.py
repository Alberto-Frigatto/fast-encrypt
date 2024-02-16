import pytest

from src.fast_encrypt import Atbash, CaesarsCipher, HomophonicSubstitution, MorseCode, Pipeline


class TestPipeline:
    def test_when_receives_AtBash_CaesarsCipher_MorseCode_and_then_encrypts_Hello_World_returns_the_proper_cipher_text(
        self,
    ):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])
        entry = 'Hello World!'

        result = pipeline.encrypt(entry)
        expected = '...- -.-- .-. .-. --- --. --- .-.. .-. --..'

        assert result == expected

    def test_when_receives_AtBash_CaesarsCipher_MorseCode_and_then_decrypts_the_cipher_text_returns_HELLOWORLD(
        self,
    ):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])
        entry = '...- -.-- .-. .-. --- --. --- .-.. .-. --..'

        result = pipeline.decrypt(entry)
        expected = 'HELLOWORLD'

        assert result == expected

    def test_when_receives_AtBash_CaesarsCipher_MorseCode_and_then_encrypts_and_decrypts_John_Frusciante_returns_the_proper_values(
        self,
    ):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])
        entry = 'John Frusciante'

        encryption_result = pipeline.encrypt(entry)
        expected_encryption = '- --- ...- .--. -..- .-.. .. -.- .- ..- -.-. .--. .--- -.--'

        decryption_result = pipeline.decrypt(expected_encryption)
        expected_decryption = 'JOHNFRUSCIANTE'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_receives_key_mnbvcxzpoiuytrewqlkjhgfdsa_and_then_encrypts_and_decrypts_a_text_returns_the_proper_values(
        self,
    ):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encryption_result = pipeline.encrypt(entry)
        expected_encryption = '-... .-.. -.-. -.- ..- .-. --- -..- ..- .- ..- -.-. .-. --.- -.-- .--. .--- -.-- .-.. -.-- -. .. -... .-. ..- .- -.-. -..- -.-- --.. -.-- .-.. -.-. .--- ..- .... -.-. --.. --- -... .-.. -.-. -.- ..- .-. -.-- --- --.- -.-. ..- --- .-.. -. -.-. ..- -.- --.. -.-. -.-. --.- -.-- .-.. ..- .- -.-. --.. --- -.- .. .-. -.-- --.. -.-. .-.. -.-- .-- ..- -.-. --- --.. -.-. -.-. --.- -.-- .-.. ..- .- -.-. .-. -.-. .--- ..- .--. -.-. -.- -.-- .--. --.. --- --- -- .. ..- .--. .--- --- --.- -.-. ..- --- .-.. --.. --- --.- .. .--. --.. --- -.-- --.- -.-. .-.. -.-- -.-. .--- -.-- .-.. .-.. ..- .--- --- .-.. ..- -.-. .-. -.-- -- .. ..- .... -.-. .-. -.-- .--. .--- -.-- -.-. ....- --... ...-- --.. --- .--- -.-- .-.. .-.. ..- .--- --- .-.. ..- --- -.- .. .-. -.-. --.- -.-- .-.. ..- .- -.-. .--. --- .- --- --.- ---.. ..... .---- ----- ....- .---- --... --... --... .---- ... --.- -.-- --- -.- -.-- .--- ..- --.- --- -.-- --.- -. --- -. .. .-. -.-. .- -.-. --- .- --- --.- ..--- ----- ...-- --.- ..- .-. ...- --- -.-- -.- --.. -.-- ...- -.-. -... ..- .--- -.-. .--. .--- -.-- -.- -.-- --.- -.-. .-- --- -.- .--- --- --.. -.-- ..--- ----- ..--- ..---'

        decryption_result = pipeline.decrypt(expected_encryption)
        expected_decryption = 'BRASILOFICIALMENTEREPUBLICAFEDERATIVADOBRASILEOMAIORPAISDAAMERICADOSULEDAREGIAODAAMERICALATINASENDOOQUINTOMAIORDOMUNDOEMAREATERRITORIALEQUIVALENTEA473DOTERRITORIOSULAMERICANOCOM8510417771KMEOSETIMOEMPOPULACAOCOM203MILHOESDEHABITANTESEMAGOSTODE2022'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_steps_receives_0_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline(0)

    def test_when_steps_receives_1_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline(1)

    def test_when_steps_receives_abc_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline('abc')

    def test_when_steps_receives_None_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline(None)

    def test_when_steps_receives_list_int_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([1, 2, 3])

    def test_when_steps_receives_invalid_list_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([Atbash(), 2])

    def test_when_steps_receives_2_HomophonicSubstitution_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([HomophonicSubstitution('KEY'), HomophonicSubstitution('KEY')])

    def test_when_steps_receives_2_MorseCode_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([MorseCode(), MorseCode()])

    def test_when_steps_receives_2_MorseCode_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([MorseCode(), MorseCode()])

    def test_when_steps_MorseCode_and_Atabsh_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([MorseCode(), Atbash()])

    def test_when_steps_MorseCode_and_HomophonicSubstitution_raises_ValueError(self):
        with pytest.raises(ValueError):
            Pipeline([HomophonicSubstitution('KEY'), MorseCode()])

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])

        with pytest.raises(ValueError):
            pipeline.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])

        with pytest.raises(TypeError):
            pipeline.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])

        with pytest.raises(ValueError):
            pipeline.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])

        with pytest.raises(ValueError):
            pipeline.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])

        with pytest.raises(TypeError):
            pipeline.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        pipeline = Pipeline([Atbash(), CaesarsCipher(3), MorseCode()])

        with pytest.raises(ValueError):
            pipeline.decrypt(None)
