#import random
#my_list = ['text', 'str', 'two']
#print(random.choice(my_list))

import pytest
#Пример по заполнению пред и пост условию(легкий)
import pytest
@pytest.fixture()
def before_after():
    print('Before test')
    yield None
    print('\nafter test')
def test_demo1(before_after):
    assert 1 == 1
def test_demo2(before_after):
    assert 2 == 2