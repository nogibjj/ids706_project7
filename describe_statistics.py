#!/usr/bin/env_ids706hw2 python

import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


def read_dataset(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type")


def calculate_summary_statistics(df):
    stock_stats = {
        "Mean": df["Stock"].mean(),
        "Median": df["Stock"].median(),
        "Standard Deviation": df["Stock"].std(),
    }

    sold_stats = {
        "Mean": df["Sold"].mean(),
        "Median": df["Sold"].median(),
        "Standard Deviation": df["Sold"].std(),
    }

    print(stock_stats)
    print(sold_stats)
    print("Current Stock Summary Statistics:")
    for key, value in stock_stats.items():
        print(f"{key}: {value}")

    print("\nBooks Sold Summary Statistics:")
    for key, value in sold_stats.items():
        print(f"{key}: {value}")

    return stock_stats, sold_stats


def create_data_visualization(df):
    _, axes = plt.subplots(2, 1, figsize=(10, 10))

    # Plotting Stock bar chart
    axes[0].bar(df["Book Name"], df["Stock"], color="blue")
    axes[0].set_title("Fig 1. Current Stock of the Book in the Store", fontsize=16)
    axes[0].set_xlabel("Book Name", fontsize=16)
    axes[0].set_ylabel("Current Stock", fontsize=16)
    axes[0].tick_params(axis="x", rotation=45)

    # Plotting Pages bar chart
    axes[1].bar(df["Book Name"], df["Sold"], color="green")
    axes[1].set_title("Fig 2. Books Already Sold", fontsize=16)
    axes[1].set_xlabel("Book Name", fontsize=16)
    axes[1].set_ylabel("Books Sold", fontsize=16)
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("plot.png")
    plt.show()


def generate_report(stock_stats, sold_stats):
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font
    pdf.set_font("Times", "B", 16)

    # Adding a cell for Title
    pdf_title = (
        "Descriptive Statistics Report "
        "for the Best Sellers of KK's Book Shelf (2023)"
    )

    pdf.cell(200, 10, txt=pdf_title, ln=True, align="C")

    # Line break
    pdf.ln(10)

    # image
    pdf.set_font("Times", "B", 14)

    pdf.cell(
        200,
        10,
        txt="Part 1: Data Visualization of the Best Sellers",
        ln=True,
        align="L",
    )

    pdf.image("plot.png", x=10, y=None, w=100)

    # Add Statistics
    pdf.ln(5)

    pdf.set_font("Times", "B", 14)

    pdf.cell(
        200,
        10,
        txt="Part 2: Statistics Analysis of the Best Sellers",
        ln=True,
        align="L",
    )

    pdf.set_font("Times", "", 10)

    txt_mean = (
        f"1. Mean of Current Stock: {stock_stats['Mean']}, "
        f"Mean of the Books Sold: {sold_stats['Mean']}"
    )
    pdf.cell(200, 10, txt=txt_mean, ln=True, align="L")

    txt_median = (
        f"2. Median of Current Stock: {stock_stats['Median']}, "
        f"Median of the Books Sold: {sold_stats['Median']}"
    )
    pdf.cell(200, 10, txt=txt_median, ln=True, align="L")

    txt_std = (
        "3. Std of Current Stock: "
        f"{stock_stats['Standard Deviation']}, "
        f"Std of the Books Sold: {sold_stats['Standard Deviation']}"
    )
    pdf.cell(200, 10, txt=txt_std, ln=True, align="L")

    # save the pdf with name .pdf
    pdf.output("statistics_report.pdf")


def main():
    # Adjust with your file path
    dataset = read_dataset("./Book.xlsx")
    print(dataset)

    stock_stats, sold_stats = calculate_summary_statistics(dataset)
    create_data_visualization(dataset)
    generate_report(stock_stats, sold_stats)


if __name__ == "__main__":
    main()
