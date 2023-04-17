import pytest
from app.key_register import KeyRegister

@pytest.fixture
def empty_key_list():
    return KeyRegister()


@pytest.fixture
def not_empty_key_list():
    return KeyRegister(['a', 'b', 'c' ,'d'])


def test_empty_list(empty_key_list):
    assert empty_key_list.length == 4

def test_list_init(not_empty_key_list):
    assert not_empty_key_list.get_registered_keys() == ['a', 'b', 'c' ,'d']


def test_add_new_element(empty_key_list):
    empty_key_list.register_key('Key.caps_lock')
    assert empty_key_list.get_registered_keys() == ['Key.caps_lock']

def test_overload_list(not_empty_key_list):
    not_empty_key_list.register_key('Key.caps_lock')
    assert not_empty_key_list.get_registered_keys() == ['a', 'b', 'c' ,'d']
    
def test_reset_list(not_empty_key_list):
    not_empty_key_list.reset_registered_keys()
    assert not_empty_key_list.get_registered_keys() == []
    






@pytest.mark.skip(reason="no way of currently testing this")
def test_default_list_with_capslock_set(empty_key_list):
    assert empty_key_list.get_registered_keys == ['Key.caps_lock']


