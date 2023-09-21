from lib import read_dataset, calculate_summary_statistics, create_data_visualization


def main():
    # Adjust with your file path
    dataset = read_dataset("./Book.xlsx")
    # print(dataset.describe())
    print(dataset)

    _, _ = calculate_summary_statistics(dataset)
    create_data_visualization(dataset)
    # generate_report(dataset)


if __name__ == "__main__":
    main()
