from describe_statistics import *


def test1():
    dataset = read_dataset("./Book.xlsx")
    stock_stats, _ = calculate_summary_statistics(dataset)
    assert stock_stats["Mean"] == get_mean(dataset, "Stock")
    assert stock_stats["Median"] == get_median(dataset, "Stock")
    assert stock_stats["Standard Deviation"] == get_std(dataset, "Stock")

def test2():
    dataset = read_dataset("./Book.xlsx")
    _, sold_stats = calculate_summary_statistics(dataset)
    assert sold_stats["Mean"] == get_mean(dataset, "Sold")
    assert sold_stats["Median"] == get_median(dataset, "Sold")
    assert sold_stats["Standard Deviation"] == get_std(dataset, "Sold")


if __name__ == "__main__":
    test1()
    test2()
    print("CICD Passed.")
