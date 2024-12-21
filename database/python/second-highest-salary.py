import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    distinct_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = distinct_salaries.sort_values(ascending=False).reset_index(drop=True)
    if len(sorted_salaries) < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    return pd.DataFrame({'SecondHighestSalary': [sorted_salaries.iloc[1]]})
    