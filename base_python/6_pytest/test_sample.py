# content of test_sample.py
import pytest


def inc(x):
    return x + 1


class TestDemo:
    def test_answer(self):
        assert inc(3) == 5

    def test_answer2(self):
        assert inc(4) == 5


def test_a():
    pytest.assume(8 == 9)
    pytest.assume(9 == 9)


if __name__ == '__main__':
    # pytest.main("-v -x TestDemo")
    # pytest.main(["-v", "-x", "TestDemo"])
    pytest.main()
