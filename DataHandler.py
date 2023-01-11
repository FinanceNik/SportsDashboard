import pandas as pd
from datetime import datetime  # for getting the current year

import Styles

currentYear = int(datetime.today().strftime('%Y')) - 1


def dataCleaner(activityType, year):  # --> string: Can be [Ride, Run, Walk, Hike]
    df = pd.read_csv('activities.csv')
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
    totals = sum(values)
    percentages = []
    for i in values:
        percent = round(i / totals, 3)
        percentages.append(percent)

    percentages_for_table = [f"{round(i*100, 2)}%" for i in percentages]

    dash_table_df = pd.DataFrame(
                        {'Activity Type': keys,
                         'Percentage': percentages_for_table
                         })
    colorList = Styles.purple_list[:len(keys)]
    return keys, values, percentages, totals, dash_table_df, colorList

# mostUsedActivityType(2022)


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
    def __init__(self, activityType: str, year: int):
        df = dataCleaner(activityType, year)
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


def monthly_kpi_count(activityType, year, kpi):
    df = dataCleaner(activityType, year)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    volumes = []
    for month in range(1, 13):
        volume = int(df.loc[(df['year'] == year) & (df['month'] == month), kpi].count())
        volumes.append(volume)
    return months, volumes


def monthly_kpi_sum(activityType, year, kpi):
    df = dataCleaner(activityType, year)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    volumes = []
    if kpi == "Moving Time":
        for month in range(1, 13):
            volume = round(df.loc[(df['year'] == year) & (df['month'] == month), kpi].sum() / 3600, 2)
            volumes.append(volume)
        return months, volumes
    else:
        for month in range(1, 13):
            volume = int(df.loc[(df['year'] == year) & (df['month'] == month), kpi].sum())
            volumes.append(volume)
        return months, volumes


allActivities = Totals("all", currentYear)

# print(allActivities.get_totalActivityTime())  # THIS IS HOW U CALL THE REFERRED TO OBJECT
