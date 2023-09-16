from describe_statistics import *


def test():
    dataset = read_dataset("./Book.xlsx")
    stock_stats, sold_stats = calculate_summary_statistics(dataset)
    assert stock_stats["Mean"] == 15.2
    assert stock_stats["Median"] == 14.0
    assert stock_stats["Standard Deviation"] == 9.148770409186143


if __name__ == "__main__":
    test()
    print("CICD Passed.")
