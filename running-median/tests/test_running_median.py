from running_median import running_median, custom_format


def test_running_median():
    # given
    inp = [
        94455,
        20555,
        20535,
        53125,
        73634,
        148,
        63772,
        17738,
        62995,
        13401,
        95912,
        13449,
        92211,
    ]
    expected = [
        94455.,
        57505.,
        20555.,
        36840.,
        53125.,
        36840.,
        53125.,
        36840.,
        53125.,
        36840.,
        53125.,
        36840.,
        53125.,
    ]

    # when
    output = list(running_median(inp))

    # then
    assert expected == output


def test_running_median_return_floats():
    # given
    inp = [
        94455,
        20555,
        20535,
        53125,
        73634,
        148,
        63772,
        17738,
        62995,
        13401,
        95912,
        13449,
        92211,
    ]
    # when
    output = list(running_median(inp))

    # then
    assert all(isinstance(element, float) for element in output)


def test_custom_format_integer():
    # given
    expected = '12.0'
    inp = 12

    # when
    output = custom_format(inp)

    # then
    assert expected == output


def test_custom_format_float1():
    # given
    expected = '12.0'
    inp = 12.

    # when
    output = custom_format(inp)

    # then
    assert expected == output


def test_custom_format_float2():
    # given
    expected = '12.2'
    inp = 12.2

    # when
    output = custom_format(inp)

    # then
    assert expected == output
