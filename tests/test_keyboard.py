import pytest

from src.keyboard import Keyboard


def test_initial_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb.language == "EN"


def test_change_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert kb.language == "RU"


def test_change_language_twice():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    kb.change_lang()
    assert kb.language == "EN"


def test_set_language_error():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    with pytest.raises(AttributeError):
        kb.language = 'CH'


if __name__ == "__main__":
    pytest.main()
