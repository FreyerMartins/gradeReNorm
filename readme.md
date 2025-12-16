# ETLpy

This is an ETL python script that ingest some data,
applies some transformation, and loads them back into a file.

## running script
to run the script, simply run `uv run run.py` to leverage uv's package management.
If package dependencies do not sync automatically, run `uv sync` and rerun the script.

## data source
Data was taken from kaggle using the students academic performance dataset.
This data set can be found [here](https://www.kaggle.com/datasets/sadiajavedd/students-academic-performance-dataset)

## data transformation
Student scores were normalized using the standard score methodology.
This implies that your data is normally distributed.

This sort of information is useful when comparing scores that operate using different scales.


