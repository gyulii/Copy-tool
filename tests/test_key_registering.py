import pytest
from app.key_register import KeyRegister

@pytest.fixture
def empty_key_list():
    return KeyRegister()


@pytest.fixture
def not_empty_key_list():
    return KeyRegister(default_key_list=['a', 'b', 'c' ,'d'])


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
    
def test_if_input_keys_are_equal_to_registered_one_item(not_empty_key_list):
    not_empty_key_list.check_new_input_key('a')
    assert not_empty_key_list.check_new_input_key('a') == False
    
    
def test_if_input_keys_are_equal_to_registered_full(not_empty_key_list):
    not_empty_key_list.check_new_input_key('a')
    not_empty_key_list.check_new_input_key('b')
    not_empty_key_list.check_new_input_key('c')
    assert not_empty_key_list.check_new_input_key('d') == True
    
def test_if_input_keys_are_equal_to_registered_full_overload(not_empty_key_list):
    not_empty_key_list.check_new_input_key('a')
    not_empty_key_list.check_new_input_key('b')
    not_empty_key_list.check_new_input_key('c')
    not_empty_key_list.check_new_input_key('d')
    assert not_empty_key_list.check_new_input_key('d') == False
    
    
def test_if_input_keys_are_equal_to_registered_full_two_rotation(not_empty_key_list):
    not_empty_key_list.check_new_input_key('a')
    not_empty_key_list.check_new_input_key('b')
    not_empty_key_list.check_new_input_key('c')
    assert not_empty_key_list.check_new_input_key('d') == True
    assert not_empty_key_list.check_new_input_key('d') == False
    not_empty_key_list.check_new_input_key('a')
    not_empty_key_list.check_new_input_key('b')
    assert not_empty_key_list.check_new_input_key('c') == False
    assert not_empty_key_list.check_new_input_key('d') == True
     
    





@pytest.mark.skip(reason="no way of currently testing this")
def test_default_list_with_capslock_set(empty_key_list):
    assert empty_key_list.get_registered_keys == ['Key.caps_lock']


