from greeting import my_name

def test_my_name():
    assert "My name is: bob"==my_name("bob")

def test_my_name1():
    assert "My name is: bob"== my_name("bob")