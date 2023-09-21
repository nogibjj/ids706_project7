#!/usr/bin/env python3

import polars as pl
import pandas as pd
import matplotlib.pyplot as plt


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