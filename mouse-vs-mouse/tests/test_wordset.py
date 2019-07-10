from wordset import WordSet


def test_wordset():
    # given
    inp = [
        'your',
        'computer',
        'input',
        'input',
    ]
    sentence = 'Your bla bla bla rodent input.'
    occurences = 2

    # when
    result = WordSet(inp).count_occurrences(sentence)

    # then
    assert occurences == result
