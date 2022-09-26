from cProfile import label
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, FunctionTransformer
import matplotlib.pyplot as plt

def get_monthsdays():
    """Define (order of) days and months.
    Output:
        months: list of ordered month names
        days: list of ordered day names
    """
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    days = ['mon','tue','wed','thu','fri','sat','sun']
    return months, days

def make_numeric(data_df):
    """Make categorical attributes numeric.
    Input:
        dataframe
    Output:
        entirely numeric version of dataframe
    """
    # one-hot encode coordinates, month, day
    X_df = pd.get_dummies(data_df.X, prefix='X')
    Y_df = pd.get_dummies(data_df.Y, prefix='Y')
    month_df = pd.get_dummies(data_df.month)
    day_df = pd.get_dummies(data_df.day)
    # remove alphabetical ordering
    months, days = get_monthsdays()
    month_df = month_df.reindex(columns=months)
    day_df = day_df.reindex(columns=days)
    # binary weekday-weekend encoding
    day_df['weekend'] = data_df['day'].apply(lambda x: 1 if x == 'sun' or x == 'sat' else 0)
    day_df['weekend_adj'] = data_df['day'].apply(lambda x: 0 if x == 'tue' or x == 'wed' or x == 'thu' else 1)
    # binary calender quarters
    month_df['q1'] = data_df['month'].apply(lambda x: 1 if x == 'jan' or x == 'feb' or x == 'mar' else 0)
    month_df['q2'] = data_df['month'].apply(lambda x: 1 if x == 'apr' or x == 'may' or x == 'jun' else 0)
    month_df['q3'] = data_df['month'].apply(lambda x: 1 if x == 'jul' or x == 'aug' or x == 'sep' else 0)
    month_df['q4'] = data_df['month'].apply(lambda x: 1 if x == 'oct' or x == 'nov' or x == 'dec' else 0)

    # combine to new dataframe (for correlation heat map)
    numeric_df = pd.concat([X_df, Y_df, month_df, day_df, data_df[['FFMC','DMC','DC','ISI','temp','RH','wind','rain','area']]], axis=1)
    return numeric_df

def get_target(data_df):
    """Get target values: split y (area) from X.
    Input:
        dataframe
    Output:
        X: features
        y: targets
    """
    X = data_df.drop('area', axis=1)
    y = data_df['area']
    return X, y

def drop_outliers(data_df):
    """Drop datapoints that are below the FFMC threshold, and the ISI outlier.
    Input:
        dataframe
    Output:
        dropped: altered dataframe without set datapoints
    """
    indices = set()
    for i in data_df[data_df.FFMC < 80].index:
        indices.add(i)
    for i in data_df[data_df.ISI == data_df.ISI.max()].index:
        indices.add(i)
    dropped = data_df.drop(labels=indices)
    dropped.reset_index(drop=True, inplace=True)
    return dropped

def select_features(data_df):
    """Select the different relevant feature columns for the different models.
    Input:
        dataframe
    Output:
        original: original features (only with entirely numeric columns)
        qw: no months or days, only binary calender quarters and weekend (Mon-Fr: 0, Sat-Sun:1)
        qwa: no months or days, only binary calender quarters and weekend adjacency (Tue-Thu: 0, Fri-Mon:1)
    """
    X = data_df.loc[:,data_df.columns.str.startswith('X')]
    Y = data_df.loc[:,data_df.columns.str.startswith('Y')]
    months, days = get_monthsdays()
    ms = data_df[months]
    ds = data_df[days]
    qs = data_df.loc[:,data_df.columns.str.startswith('q')]
    ws = data_df['weekend']
    was = data_df['weekend_adj']
    codes = data_df[['FFMC','DMC','DC','ISI','temp','RH','wind','rain','area']]

    original = pd.concat([X,Y,ms,ds,codes], axis=1)
    qw = pd.concat([X,Y,qs,ws,codes], axis=1)
    qwa = pd.concat([X,Y,qs,was,codes], axis=1)
    return original, qw, qwa

    
def show_plot(predictions, target):
    #add the predicitons and true values to a dataframe to easily sort them in unison
    df_scatter = target.to_frame().assign(pred_area=predictions).sort_values(by=["area"])
    plt.scatter(np.arange(len(target)) , df_scatter["area"], label='true y')
    plt.scatter(np.arange(len(target)) , df_scatter["pred_area"], c='green', label='predicted y')
    plt.title('Mapped values of predited and actual area')
    plt.xlabel('Datapoint')
    plt.ylabel('log-transformed area')
    plt.legend()
    plt.show()