from hello import moreHello, moreGoodBye


def test_moreHello():
    assert "hi" == moreHello()


def test_moreGoodBye():
    assert "bye" == moreGoodBye()
