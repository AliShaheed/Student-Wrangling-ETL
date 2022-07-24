import pandas as pd


def drop_columns(data_frame):
    data_frame = data_frame.drop(columns=['Zscore',
                                          'gender',
                                          'syllabus'],
        axis=1)
    return data_frame

def remove_missing(data_frame):
    missing_df = data_frame.dropna()
    return missing_df

def remove_absentee(data_frame):
    absent_df = data_frame.drop(data_frame[(data_frame.sub1_r == 'Absent') &
                           (data_frame.sub2_r == 'Absent') &
                           (data_frame.sub3_r == 'Absent') &
                           (data_frame.general_english_r == 'Absent')
                           ].index)
    return absent_df

def remove_invalid_days(data_frame):
    data_frame = data_frame.drop(data_frame[(data_frame.birth_day == 'Invalid error') | (data_frame.birth_day == 'Invalid')].index)
    data_frame['birth_day'] = data_frame['birth_day'].convert_dtypes()
    data_frame['birth_day'] = pd.to_numeric(data_frame['birth_day'])
    data_frame = data_frame.drop(data_frame[(data_frame.birth_day > 31) | (data_frame.birth_day < 1)].index)
    return data_frame

def merge_birthdate(data_frame):
    data_frame = remove_invalid_days(data_frame) # check if number of days is out of range, if true remove them.
    data_frame['birth_date'] = data_frame['birth_day'].astype(str) + " " + (data_frame['birth_month'].astype(str) + " " + data_frame['birth_year'])
    data_frame = data_frame.drop(columns=['birth_day',
                                          'birth_month',
                                          'birth_year'],
        axis=1)

    return data_frame

def extract(file):
    data_frame = pd.read_csv(file)
    return data_frame

def transform(data_frame):
    dropped_df = drop_columns(data_frame)
    missing_df = remove_missing(dropped_df)
    not_absent_df = remove_absentee(missing_df)
    trans_df = merge_birthdate(not_absent_df)
    return trans_df

def load(data_frame):
    return data_frame.to_csv('cleaned_results.csv')

csv_file = "al_results_2020.csv"
df = extract(csv_file)
trans_df = transform(df)
load(trans_df)