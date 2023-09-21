from lib import (
    read_dataset,
    calculate_summary_statistics,
    get_mean,
    get_median,
    get_std,
    create_data_visualization,
)


def test_script_main_logic():
    # test read_dataset()
    dataset = read_dataset("./Book.xlsx")
    print(dataset)
    assert dataset, "Dataset is not correctly loaded!"

    # test calculate_summary_statistics() & specific functions
    stock_stats, sold_stats = calculate_summary_statistics(dataset)
    assert stock_stats["Mean"] == get_mean(dataset, "Stock")
    assert stock_stats["Median"] == get_median(dataset, "Stock")
    assert stock_stats["Standard Deviation"] == get_std(dataset, "Stock")

    assert sold_stats["Mean"] == get_mean(dataset, "Sold")
    assert sold_stats["Median"] == get_median(dataset, "Sold")
    assert sold_stats["Standard Deviation"] == get_std(dataset, "Sold")

    # check data_visualization function
    try:
        create_data_visualization(dataset)
    except Exception as e:
        assert False, f"Function raised an exception: {e}"


if __name__ == "__main__":
    test_script_main_logic()
    print("Python script is tested to be right.")
