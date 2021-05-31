from re import split
import pytest
from moneypot import Moneypot

def test_init_cases():
    # TODO test Moneypot() for Exception
    with pytest.raises(TypeError):
        Moneypot(5)
    with pytest.raises(ValueError):
        Moneypot([1,2,3])

    assert Moneypot([1,2,3,4,5]).get_money() == [1, 2, 3, 4, 5]
    assert Moneypot.from_string("10gp 20sp 50cp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("10gp 50cp 20sp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("10gp20sp50cp").get_money() == [0, 10, 0, 20, 50]
    assert Moneypot.from_string("1 0gp 20s p 50 cp").get_money() == [0, 10, 0, 20, 50]

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
    # TODO implement 10g 10000cp (focus on when copper pool is not possible)
    pass

def test_uneven_splits():
    # deal with splits that cannot compensate evenly (small ammounts basicly)
    pass