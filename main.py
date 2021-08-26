def sum_of_squares(a):
    total = 0
    for i in a:
        total += i*i
    return total


def test_one():
    assert sum_of_squares([1,2,3]) == 14

def test_two():
    assert sum_of_squares([1,2,3,4]) == 30

test_one()
test_two()