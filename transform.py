def data_transform(df):
    # standard score normalization
    mean_writing_score = df.loc[:,'writing score'].mean()
    stdev_writing_score = df.loc[:,'writing score'].std()
    df["norm_writing_score"] = df["writing score"].apply(
        lambda x: (x
                   -mean_writing_score)
                  /stdev_writing_score)
    mean_math_score = df.loc[:,'math score'].mean()
    stdev_math_score = df.loc[:,'math score'].std()
    df["norm_math_score"] = df["math score"].apply(
        lambda x: (x
                   -mean_math_score)
                  /stdev_math_score)
    mean_reading_score = df.loc[:,'reading score'].mean()
    stdev_reading_score = df.loc[:,'reading score'].std()
    df["norm_reading_score"] = df["reading score"].apply(
        lambda x: (x
                   -mean_reading_score)
        /stdev_reading_score)
    return df
