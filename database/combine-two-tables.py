import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    output = pd.merge(person, address, on ='personId' , how='left')
    output = output[['firstName', 'lastName', 'city', 'state']]
    return output