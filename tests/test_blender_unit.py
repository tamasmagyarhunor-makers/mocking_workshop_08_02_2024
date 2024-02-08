from unittest.mock import Mock
from lib.blender import *
"""
Given a Blender adds a Fruit in the storage
The storage will contain the Fruit.
"""
def test_blender_adds_fruit():
    blender = Blender()
    fruit = Mock()
    blender.add_fruit(fruit)
    actual = blender.storage
    expected = [fruit]

    assert actual == expected

"""
Given a Blender makes juice
It returns a Mock juice.
"""
def test_blender_makes_juice():
    blender = Blender()
    mock = Mock()
    blender.add_fruit(mock)
    mock.get_name.return_value = 'orange'
    actual = blender.make_juice()
    expected = "orange juice"

    assert actual == expected

"""
Given a Blender makes a Fruit juice
It can calculate the juices calory.
"""
def test_blender_makes_juice_with_a_fruit_and_calculates_calory():
    blender = Blender()
    mock = Mock()
    blender.add_fruit(mock)
    mock.get_calory_int.return_value = 8
    actual = blender.calculate_calory()
    expected = 8

    assert actual == expected