import polars as pl

def test_dict_mapping():
    df = pl.DataFrame({
        "vendor_id":[101,102,101,103]
    })
    mapping = {
        101: "junior",
        102: "mid",
        103: "senior"
    }
    result = (
        df
        .with_columns(
            pl.col("vendor_id")
            .replace_strict(mapping)
            .alias("skill_level")
        )
    )
    print(result)
    assert result["skill_level"][1] == "mid"
    
if __name__ == "__main__":
    test_dict_mapping()
    