import pandas as pd


# Perform data validation
def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print('There are no recipes of such')
        return False

    # check for duplicate values
    if pd.Series(df['title']).is_unique:
        pass
    else:
        raise Exception('Title has duplicates, failed!')

    # check for nulls
    if df.isnull().values.any() is False:
        raise Exception('Null values found')

    return True
