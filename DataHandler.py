import pandas as pd
from datetime import datetime  # for getting the current year

currentYear = int(datetime.today().strftime('%Y'))


def dataCleaner(activityType, startYear):  # --> string: Can be [Ride, Run, Walk, Hike]
    df = pd.read_csv('activities.csv')
    df['Activity Date'] = pd.to_datetime(df['Activity Date'])

    df.insert(1, "year", "")
    df['year'] = df['Activity Date'].dt.year

    df.insert(1, "month", "")
    df['month'] = df['Activity Date'].dt.month

    if activityType == "all":
        return df.loc[df['year'] == startYear]
    else:
        df = df.loc[df['Activity Type'] == activityType]
        return df.loc[df['year'] == startYear]


def uniqueActivityType():
    df = dataCleaner("all", currentYear)
    activityTypes = df["Activity Type"].unique()
    return activityTypes

