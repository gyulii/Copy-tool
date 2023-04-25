import pytest
from app.key_register import KeyRegister

@pytest.fixture
def empty_key_list():
    return KeyRegister()


@pytest.fixture
def not_empty_key_list():
    pass


def test_empty_list(empty_key_list):
    assert empty_key_list.length == 4


def test_4_long_list(empty_key_list):
    keycomb_1 = ['a', 'a', 'a', 'a']
    empty_key_list.add_new_input_key_to_queue('a')
    assert empty_key_list.check_queue_to_keycombination(keycomb_1) == False
    assert empty_key_list.get_queue() == ['a']
    empty_key_list.add_new_input_key_to_queue('a')
    empty_key_list.add_new_input_key_to_queue('a')
    empty_key_list.add_new_input_key_to_queue('a')
    assert empty_key_list.get_queue() == ['a', 'a', 'a', 'a']
    assert empty_key_list.check_queue_to_keycombination(keycomb_1) == True
    
def test_3_long_list(empty_key_list):
    keycomb_1 = ['a', 'a', 'a']
    empty_key_list.add_new_input_key_to_queue('b')
    empty_key_list.add_new_input_key_to_queue('a')
    empty_key_list.add_new_input_key_to_queue('a')
    empty_key_list.add_new_input_key_to_queue('a')
    assert empty_key_list.get_queue() == ['b', 'a', 'a' ,'a']
    assert empty_key_list.check_queue_to_keycombination(keycomb_1) == True
    empty_key_list.add_new_input_key_to_queue('b')
    assert empty_key_list.check_queue_to_keycombination(keycomb_1) == False

@pytest.mark.skip(reason="no way of currently testing this")
def test_default_list_with_capslock_set(empty_key_list):
    assert empty_key_list.get_registered_keys == ['Key.caps_lock']


