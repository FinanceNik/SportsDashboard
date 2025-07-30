import pandas as pd  # for data handling
from datetime import datetime, date  # for getting the current year
import Styles  # for styling and coloring
import requests  # for getting weather data

currentYear = int(datetime.today().strftime('%Y'))  # the current year
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def dataCleaner(activityType, year):  # --> string: Can be [Ride, Run, Walk, Hike]
    df = pd.read_csv('assets/activities.csv')
    df['Activity Date'] = pd.to_datetime(df['Activity Date'])
    df["Distance"] = pd.to_numeric(df['Distance'], errors='coerce')
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
    # TODO match the colors to one type of activity regardless of the year --> ColorX == "Hike"
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
        percent = round(int(i) / int(totals), 3)
        percentages.append(percent)

    percentages_for_table = [f"{round(i*100, 2)}%" for i in percentages]

    dash_table_df = pd.DataFrame(
                        {'Activity Type': keys,
                         'Percentage': percentages_for_table
                         })
    colorList = Styles.purple_list[:len(keys)]
    return keys, values, percentages, totals, dash_table_df, colorList


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
        # TODO remove the elevation of activity_type == "alpine ski"
        return int(self.totalElevationGain)

    def get_totalActivityTime(self) -> int:
        return int(self.totalActivityTime / 3600)

    def get_totalActivityDistance(self) -> float:
        return int(self.totalActivityDistance)


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
    volumes = []
    for month in range(1, 13):
        volume = int(df.loc[(df['year'] == year) & (df['month'] == month), kpi].count())
        volumes.append(volume)
    return months, volumes


def monthly_kpi_sum(activityType, year, kpi):
    df = dataCleaner(activityType, year)
    volumes = []
    if kpi == "Moving Time":
        for month in range(1, 13):
            volume = int(df.loc[(df['year'] == year) & (df['month'] == month), kpi].sum() / 3600)
            volumes.append(volume)
        return months, volumes
    else:
        for month in range(1, 13):
            volume = int(df.loc[(df['year'] == year) & (df['month'] == month), kpi].sum())
            volumes.append(volume)
        return months, volumes


def thousands(x):
    return "{:,}".format(int(x))

# print(allActivities.get_totalActivityTime())  # THIS IS HOW U CALL THE REFERRED TO OBJECT

# Get months and counts for previous and current year
def higher_or_lower(activityType, kpi, aggType):
    if aggType == "count":
        prev_x, prev_y = monthly_kpi_count(activityType=activityType, year=currentYear - 1, kpi=kpi)
        curr_x, curr_y = monthly_kpi_count(activityType=activityType, year=currentYear, kpi=kpi)
    else:
        prev_x, prev_y = monthly_kpi_sum(activityType=activityType, year=currentYear - 1, kpi=kpi)
        curr_x, curr_y = monthly_kpi_sum(activityType=activityType, year=currentYear, kpi=kpi)

    curr_colors = [
        Styles.high_color if curr_val >= prev_val else Styles.low_color
        for curr_val, prev_val in zip(curr_y, prev_y)
    ]
    return curr_colors


def dataCleanerWeather():  # --> string: Can be [Ride, Run, Walk, Hike]
    df = pd.read_csv('assets/activities.csv')
    df['Activity Date'] = pd.to_datetime(df['Activity Date'])
    df.insert(1, "year", "")
    df['year'] = df['Activity Date'].dt.year
    df.insert(1, "rain", pd.NA)
    df = df[["Activity Date", "rain"]]

    # Luzern coordinates
    latitude = 47.0502
    longitude = 8.3093

    start_date = df['Activity Date'].min().strftime('%Y-%m-%d')
    end_date = df['Activity Date'].max().strftime('%Y-%m-%d')
    url = (
        f"https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={latitude}&longitude={longitude}"
        f"&start_date={start_date}&end_date={end_date}"
        f"&daily=precipitation_sum"
        f"&timezone=Europe%2FBerlin"
    )
    response = requests.get(url)

    data = response.json()
    precipitation_by_date = dict(
        zip(data['daily']['time'], data['daily']['precipitation_sum'])
    )

    df['rain'] = df['Activity Date'].dt.strftime('%Y-%m-%d').map(
        lambda d: 1 if precipitation_by_date.get(d, 0) > 0 else 0
    )
    return df




def activity_rain_sun_ratio():
    df = dataCleanerWeather()
    # Count days with activity on rainy and sunny days (group by date to get distinct days)
    day_rain_status = df.groupby(df['Activity Date'].dt.date)['rain'].max()  # max to mark day rainy if any activity had rain=1

    rainy_days = (day_rain_status == 1).sum()
    sunny_days = (day_rain_status == 0).sum()

    if sunny_days == 0:
        return None

    ratio = rainy_days / sunny_days
    return ratio