from hello import moreHello, moreGoodBye,goodMorning



def test_moreHello():
    assert "hi" == moreHello()


def test_moreGoodBye():
    assert "bye" == moreGoodBye()
def test_goodMorning():
    assert "gm"==goodMorning()