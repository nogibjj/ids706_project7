from lib import get_mean, get_median, get_std
import polars as pl


def test_lib():
    data = {
        "name": ["KK", "Garlic", "Jasmine", "Shirley", "Min", "Hua"],
        "age": [22, 24, 23, 23, 50, 54],
    }
    df = pl.DataFrame(data)
    print(df)

    expected_mean = df["age"].mean()
    expected_median = df["age"].median()
    expected_std = df["age"].std()

    my_mean = get_mean(df, "age")
    my_median = get_median(df, "age")
    my_std = get_std(df, "age")

    assert expected_mean == my_mean
    assert expected_median == my_median
    assert expected_std == my_std


if __name__ == "__main__":
    test_lib()
    print("Library functions are tested to be right.")
