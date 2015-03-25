from mock import patch
from randstr import randstr


def test_default_randstr():
    with patch('randstr.random') as random:
        random.choice.side_effect = 'helloworld'
        assert randstr() == 'hellowo'


def test_length():
    with patch('randstr.random') as random:
        result = 'helloworld'
        random.choice.side_effect = result
        assert randstr(len(result)) == result


def test_custom_chars():
    assert randstr(chars='x') == 'x' * 7
