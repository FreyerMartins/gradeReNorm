from src.extract import data_extract
from src.transform import data_transform
from src.load import data_load
from test import test_data_col

# data extraction
df = data_extract()
test_data_col(df)

# data transformation
norm_df = data_transform(df)

# data loading
data_load(norm_df)