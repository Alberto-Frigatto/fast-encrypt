import pytest

from src.easyencrypt import MorseCode


class TestMorseCode:
    def test_when_encrypts_Hello_World_returns_the_proper_morse_code(
        self,
    ):
        morse = MorseCode()
        entry = 'Hello World!'

        result = morse.encrypt(entry)
        expected = '.... . .-.. .-.. --- .-- --- .-. .-.. -..'

        assert result == expected

    def test_when_decrypts_the_morse_code_returns_HELLOWORLD(
        self,
    ):
        morse = MorseCode()
        entry = '.... . .-.. .-.. --- .-- --- .-. .-.. -..'

        result = morse.decrypt(entry)
        expected = 'HELLOWORLD'

        assert result == expected

    def test_when_encrypts_and_decrypts_John_Frusciante_returns_the_proper_values(
        self,
    ):
        morse = MorseCode()
        entry = 'John Frusciante'

        encryption_result = morse.encrypt(entry)
        expected_encryption = '.--- --- .... -. ..-. .-. ..- ... -.-. .. .- -. - .'

        decryption_result = morse.decrypt(expected_encryption)
        expected_decryption = 'JOHNFRUSCIANTE'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_encrypts_and_decrypts_a_text_returns_the_proper_values(
        self,
    ):
        morse = MorseCode()
        entry = 'Brasil (oficialmente República Federativa do Brasil), é o maior país da América do Sul e da região da América Latina, sendo o quinto maior do mundo em área territorial (equivalente a 47,3% do território sul-americano), com 8 510 417,771 km², e o sétimo em população (com 203 milhões de habitantes, em agosto de 2022).'

        encryption_result = morse.encrypt(entry)
        expected_encryption = '-... .-. .- ... .. .-.. --- ..-. .. -.-. .. .- .-.. -- . -. - . .-. . .--. ..- -... .-.. .. -.-. .- ..-. . -.. . .-. .- - .. ...- .- -.. --- -... .-. .- ... .. .-.. . --- -- .- .. --- .-. .--. .- .. ... -.. .- .- -- . .-. .. -.-. .- -.. --- ... ..- .-.. . -.. .- .-. . --. .. .- --- -.. .- .- -- . .-. .. -.-. .- .-.. .- - .. -. .- ... . -. -.. --- --- --.- ..- .. -. - --- -- .- .. --- .-. -.. --- -- ..- -. -.. --- . -- .- .-. . .- - . .-. .-. .. - --- .-. .. .- .-.. . --.- ..- .. ...- .- .-.. . -. - . .- ....- --... ...-- -.. --- - . .-. .-. .. - --- .-. .. --- ... ..- .-.. .- -- . .-. .. -.-. .- -. --- -.-. --- -- ---.. ..... .---- ----- ....- .---- --... --... --... .---- -.- -- . --- ... . - .. -- --- . -- .--. --- .--. ..- .-.. .- -.-. .- --- -.-. --- -- ..--- ----- ...-- -- .. .-.. .... --- . ... -.. . .... .- -... .. - .- -. - . ... . -- .- --. --- ... - --- -.. . ..--- ----- ..--- ..---'

        decryption_result = morse.decrypt(expected_encryption)
        expected_decryption = 'BRASILOFICIALMENTEREPUBLICAFEDERATIVADOBRASILEOMAIORPAISDAAMERICADOSULEDAREGIAODAAMERICALATINASENDOOQUINTOMAIORDOMUNDOEMAREATERRITORIALEQUIVALENTEA473DOTERRITORIOSULAMERICANOCOM8510417771KMEOSETIMOEMPOPULACAOCOM203MILHOESDEHABITANTESEMAGOSTODE2022'

        assert encryption_result == expected_encryption
        assert decryption_result == expected_decryption

    def test_when_the_encrypt_method_receives_int_raises_ValueError(self):
        morse = MorseCode()

        with pytest.raises(ValueError):
            morse.encrypt(1)

    def test_when_the_encrypt_method_receives_nothing_raises_TypeError(self):
        morse = MorseCode()

        with pytest.raises(TypeError):
            morse.encrypt()

    def test_when_the_encrypt_method_receives_None_raises_ValueError(self):
        morse = MorseCode()

        with pytest.raises(ValueError):
            morse.encrypt(None)

    def test_when_the_decrypt_method_receives_int_raises_ValueError(self):
        morse = MorseCode()

        with pytest.raises(ValueError):
            morse.decrypt(1)

    def test_when_the_decrypt_method_receives_nothing_raises_TypeError(self):
        morse = MorseCode()

        with pytest.raises(TypeError):
            morse.decrypt()

    def test_when_the_decrypt_method_receives_None_raises_ValueError(self):
        morse = MorseCode()

        with pytest.raises(ValueError):
            morse.decrypt(None)

    def test_when_the_decrypt_method_receives_a_raises_ValueError(self):
        morse = MorseCode()

        with pytest.raises(ValueError):
            morse.decrypt('a')

    def test_when_the_decrypt_method_receives_a_invalid_morse_code_char_raises_ValueError(self):
        morse = MorseCode()

        with pytest.raises(ValueError):
            morse.decrypt('.-.-.-.---.-.-.')
