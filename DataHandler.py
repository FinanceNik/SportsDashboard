import numpy as np
import pandas as pd


def dataCleaner(activityType):  # --> string: Can be [Ride, Run, Walk, Hike]
    df = pd.read_csv('activities.csv')
    df.insert(1, 'year', '')
    df.insert(1, 'month', '')
    print((df['Activity Date'][3]))
    # Convert the string object into a Datetime object
    # Then, extract year and month and fill in new columns with that.
    return df.loc[df['Activity Type'] == activityType]


dataCleaner('Ride')


def mainKpiFiller(activityType):
    df = dataCleaner(activityType=activityType)
    # totalActivities:
    # totalTime:
    # totalDistance:
    # totalElevation: