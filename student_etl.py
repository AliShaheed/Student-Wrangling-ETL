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


def extract(file):
    data_frame = pd.read_csv(file)
    return data_frame

def transform(data_frame):
    dropped_df = drop_columns(data_frame)
    missing_df = remove_missing(dropped_df)
    trans_df = remove_absentee(missing_df)
    return trans_df

csv_file = "al_results_2020.csv"
df = extract(csv_file)
trans_df = transform(df)


print(trans_df)