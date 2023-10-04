import main


def test_add():
    assert main.add(1, 3) == 4

if __name__ == "__main__":
    test_add()
    print("All test passed")
