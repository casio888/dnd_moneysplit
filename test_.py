from re import split
import pytest
from moneypot import Moneypot


def test_init_cases():
    # TODO test Moneypot() for Exception
    with pytest.raises(TypeError):
        Moneypot(5)
    with pytest.raises(ValueError):
        Moneypot([1,2,3])

    assert Moneypot().get_money() == [0, 0, 0, 0, 0]
    assert Moneypot([1,2,3,4,5]).get_money() == [1, 2, 3, 4, 5]
    assert Moneypot.from_string("10gp 20sp 50cp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("10gp 50cp 20sp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("10gp20sp50cp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("1 0gp 20s p 50 cp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("10pp 10gp 5ep 20sp 50cp").get_money() == "10pp 10gp 5ep 20sp 50cp"
    assert Moneypot.from_string("10gp 20sp 50cp").get_money() == "10gp 20sp 50cp"


def test_normal_splits():
    m = Moneypot([0,100,0,100,100])
    goal = ["25gp 25sp 25cp",
            "25gp 25sp 25cp",
            "25gp 25sp 25cp",
            "25gp 25sp 25cp"]
    assert goal == m.split(num_people=4)
    goal = ["27gp 7sp",
            "27gp 7sp",
            "27gp 7sp",
            "19gp 79sp 100cp"]
    assert goal == m.split(num_people=4, pool_copper=True)


def test_unbalanced_split():
    m = Moneypot([0,8,0,0,10000]) # 2g 2000c
    goal = ["2gp",
            "2gp",
            "2gp",
            "2gp",
            "10000cp"]
    assert goal == m.split(num_people=5, pool_copper=True)

def test_uneven_splits():
    m = Moneypot([0,4,0,0,0]) # 2g 2000c
    goal = ["2gp",
            "1gp",
            "1gp"]
    assert goal == m.split(num_people=3)
