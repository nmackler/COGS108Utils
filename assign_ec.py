import pandas as pd


def assign_ec(gradebook, survey_sheet, survey_column, grade_user_column, grade_ec_column, ec_value):
    """
    Update the gradebook with extra credit for students who completed a google form or equivalent

    Args:
        gradebook (pandas.DataFrame): The gradebook containing student information and grades.
        survey_sheet (pandas.DataFrame): The sheet containing the survey results.
        survey_column (str): The column name in the survey sheet containing the values (user ID or email) to match in the gradebook.
        grade_user_column (str): The column name in the gradebook containing the values (user ID or email) to match in the survey)
        grade_ec_column (str): The column name in the gradebook where the extra credit value should be updated.
        ec_value (float): The extra credit value to assign.

    Returns:
        pandas.DataFrame: The updated gradebook with extra credit values assigned.

    """
    values_to_match = survey_sheet[survey_column].values
    bool_array = gradebook[grade_user_column].isin(values_to_match)
    gradebook.loc[bool_array, grade_ec_column] = ec_value
    return gradebook
