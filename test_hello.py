from hello import hello


def test_greeting():
    msg = hello()
    assert "hello" in msg["hi"]
