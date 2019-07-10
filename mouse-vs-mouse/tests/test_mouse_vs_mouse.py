from unittest.mock import MagicMock

from mouse_vs_mouse import mouse_vs_mouse
from wordset import WordSet


def test_mouse_vs_mouse():
    # given
    computer_mouse_mock = WordSet([])
    animal_mock = WordSet([])
    computer_mouse_mock.count_occurrences = MagicMock(return_value=10)
    animal_mock.count_occurrences = MagicMock(return_value=5)
    inp = object()
    expected = ['computer-mouse']

    # when
    output = list(mouse_vs_mouse(computer_mouse_mock, animal_mock, [inp]))

    # then
    assert expected == output
    computer_mouse_mock.count_occurrences.assert_called_once_with(inp)
    animal_mock.count_occurrences.assert_called_once_with(inp)