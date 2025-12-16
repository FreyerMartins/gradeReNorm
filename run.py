from src.extract import data_extract
from src.transform import data_transform
from src.load import data_load

# data extraction
df = data_extract()

# data transformation
norm_df = data_transform(df)

# data loading
data_load(norm_df)