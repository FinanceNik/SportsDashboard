import pandas as pd
from datetime import datetime  # for getting the current year

currentYear = int(datetime.today().strftime('%Y'))


def dataCleaner(activityType, year):  # --> string: Can be [Ride, Run, Walk, Hike]
    df = pd.read_csv('activities.csv')
    # print(df.columns[:], "\n", "\n", "\n")
    df['Activity Date'] = pd.to_datetime(df['Activity Date'])
    df.insert(1, "year", "")
    df['year'] = df['Activity Date'].dt.year
    df.insert(1, "month", "")
    df['month'] = df['Activity Date'].dt.month

    if activityType == "all":
        return df.loc[df['year'] == year]
    else:
        df = df.loc[df['Activity Type'] == activityType]
        return df.loc[df['year'] == year]


def uniqueActivityTypes(year):
    df = dataCleaner("all", year)
    uniqueActivities = df["Activity Type"].unique()
    return uniqueActivities


def mostUsedActivityType(year):
    df = dataCleaner("all", year)
    activityTypes = uniqueActivityTypes(year)
    counts = []
    for activityType in activityTypes:
        n = df["Activity Type"].str.count(activityType).sum()
        counts.append(n)
    dictActivityInstances = (dict(zip(activityTypes, counts)))
    dictActivityInstances = dict(sorted(dictActivityInstances.items(), key=lambda item: item[1], reverse=True))
    keys = list(dictActivityInstances.keys())
    values = list(dictActivityInstances.values())

    return keys, values


class Totals:
    def __init__(self, activityType: str, year: int):
        df = dataCleaner(activityType, year)
        self.nOfActivities = df["Activity Type"].count()
        self.totalActiveDays = df['Activity Date'].count()
        self.totalElevationGain = df['Elevation Gain'].sum()
        self.totalActivityTime = df['Moving Time'].sum()
        self.totalActivityDistance = df['Distance'].sum()

    def get_nrOfActivities(self) -> int:
        return self.nOfActivities

    def get_totalActiveDays(self) -> int:
        return self.totalActiveDays

    def get_totalElevationGain(self) -> float:
        return round(self.totalElevationGain, 2)

    def get_totalActivityTime(self) -> int:
        return int(self.totalActivityTime / 3600)

    def get_totalActivityDistance(self) -> float:
        return round(self.totalActivityDistance, 2)


class Max:
    def __init__(self, activityType: str, startYear: int):
        df = dataCleaner(activityType, startYear)
        self.maxElevationGain = df['Elevation Gain'].max()
        self.maxMovingTime = df['Moving Time'].max()
        self.maxActivityDistance = df['Distance'].max()
        self.maxAverageSpeed = df['Average Speed'].max()
        self.maxSpeed = df['Max Speed'].max()
        self.maxElevation = df['Elevation High'].max()

    def get_maxElevationGain(self) -> int:
        return self.maxElevationGain

    def get_maxMovingTime(self) -> int:
        return self.maxMovingTime

    def get_maxActivityDistance(self) -> int:
        return self.maxActivityDistance

    def get_maxAverageSpeed(self) -> int:
        return self.maxAverageSpeed

    def get_maxSpeed(self) -> int:
        return self.maxSpeed

    def get_maxElevation(self) -> int:
        return self.maxElevation


allActivities = Max("Ride", 2022)
# print(allActivities.get_maxElevationGain())  # THIS IS HOW U CALL THE REFERRED TO OBJECT
