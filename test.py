def test_data_col(df):
    if 'writing score' in df.columns:
        print("Column 'writing score' is present in the DataFrame")
    else:
        print("Column 'writing score' is not present in the DataFrame")