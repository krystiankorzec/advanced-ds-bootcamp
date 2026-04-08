import polars as pl
import numpy as np

# 1. Tworzymy sztuczne dane (Twoje małe Allegro)
data = {
    "product_id": range(1, 11),
    "category": ["A", "A", "B", "B", "C", "C", "A", "B", "C", "A"],
    "price": [10.5, 20.0, 50.0, 45.0, 100.0, 120.0, 15.0, 30.0, 80.0, 25.0],
    "sales_count": [5, 10, 2, 1, 0, 5, 20, 3, 1, 8]
}

df = pl.DataFrame(data)

final_df = (
    df
    .filter(pl.col("price") > 15)
    .select([
        "product_id",
        "category",
        (pl.col("sales_count")*pl.col("price")).alias("total_revenue")
    ])
)
final_df

# ZADANIE EXTRA: Policz średnią cenę na kategorię (dplyr: group_by(category) %>% summarize(mean_price = mean(price)))
summary_df = (
    df
    .group_by("category")
    .agg([
        pl.col("price").mean().alias("mean_price"),
        pl.col("sales_count").sum().alias("total_sales"),
        pl.len().alias("n_products")
    ])
    .sort("total_sales", descending=True)
)

print(summary_df)