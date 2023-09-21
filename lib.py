#!/usr/bin/env python3

import polars as pl
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF


def read_dataset(file_path):
    if file_path.endswith(".csv"):
        return pl.read_csv(file_path)
    elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        pandas_df = pd.read_excel(file_path)
        polars_df = pl.DataFrame(pandas_df)
        return polars_df
    else:
        raise ValueError("Unsupported file type")


def get_mean(df: pl.DataFrame, col: str):
    return df[col].mean()


def get_median(df: pl.DataFrame, col: str):
    return df[col].median()


def get_std(df: pl.DataFrame, col: str):
    return df[col].std()


def calculate_summary_statistics(df):
    stock_stats = {
        "Mean": get_mean(df, "Stock"),
        "Median": get_median(df, "Stock"),
        "Standard Deviation": get_std(df, "Stock"),
    }

    sold_stats = {
        "Mean": get_mean(df, "Sold"),
        "Median": get_median(df, "Sold"),
        "Standard Deviation": get_std(df, "Sold"),
    }

    # print(stock_stats)
    # print(sold_stats)
    print("Current Stock Summary Statistics:")
    for key, value in stock_stats.items():
        print(f"{key}: {value}")

    print("\nBooks Sold Summary Statistics:")
    for key, value in sold_stats.items():
        print(f"{key}: {value}")

    return stock_stats, sold_stats


def create_data_visualization(df):
    # Stock bar chart
    Book_Name = df.select(pl.col("Book Name")).to_numpy().flatten().astype(str)
    Stock = df.select(pl.col("Stock")).to_numpy().flatten()
    Sold = df.select(pl.col("Sold")).to_numpy().flatten()

    # Create a figure with 2 subplots: 2 rows, 1 column
    _, axs = plt.subplots(2, 1, figsize=(8, 10))

    # Plotting Stock bar chart
    axs[0].bar(Book_Name, Stock, color="blue")
    axs[0].set_title("Fig 1. Current Stock of the Book in the Store", fontsize=16)
    axs[0].set_xlabel("Book Name", fontsize=16)
    axs[0].set_ylabel("Current Stock", fontsize=16)
    axs[0].tick_params(axis="x", rotation=45)

    # Plotting Pages bar chart
    axs[1].bar(Book_Name, Sold, color="green")
    axs[1].set_title("Fig 2. Books Already Sold", fontsize=16)
    axs[1].set_xlabel("Book Name", fontsize=16)
    axs[1].set_ylabel("Books Sold", fontsize=16)
    axs[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.savefig("plot.png")
    plt.show()


def generate_report(df):
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

    for col_name in ["Stock", "Sold"]:
        mean_val = df[col_name].mean()
        median_val = df[col_name].median()
        std_val = df[col_name].std()

        pdf.cell(200, 10, txt=f"Statistics for {col_name}:", ln=True, align="L")
        pdf.cell(200, 10, txt=f"1. Mean: {mean_val}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"2. Median: {median_val}", ln=True, align="L")
        pdf.cell(200, 10, txt=f"3. Standard Deviation: {std_val}", ln=True, align="L")
        pdf.ln(10)

    # save the pdf with name .pdf
    pdf.output("statistics_report.pdf")


# def main():
#     # Adjust with your file path
#     dataset = read_dataset("./Book.xlsx")
#     # print(dataset.describe())
#     print(dataset)

#     _, _ = calculate_summary_statistics(dataset)
#     create_data_visualization(dataset)
#     generate_report(dataset)


# if __name__ == "__main__":
#     main()
