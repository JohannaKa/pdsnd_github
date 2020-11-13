import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york', 'washington']
    while True:
        city = input('\nWould you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in cities:
            break
        else:
            print('Input is incorrect. Please reenter city name')
            continue
    print('\nIt seems that you chose','{}'.format(city).capitalize(),'!')
        # ask filter filter criteria (day, month, none)

    while True:
        try:
            datefilter = input('\nWould you like to filter the data by month, day, or not at all? Type none if you wish no filtering.\n').lower()

            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month='all'
            day='all'
            while datefilter == 'month':
            # get user input for month (all, january, february, ... , june)
                try:
                    month = input('\nWhich month - January, February, March, April, May, or June?\n').lower()
                    if month in months:
                        print("Okay, you want to filter after", "{}".format(month).capitalize(),'.')
                        break

                    else:
                        print("Month name is not correctly spelled. Please reenter the month name")
                        continue
                except:
                        print("Input is incorrect")
                        continue

            days = [0,1,2,3,4,5,6]
            while datefilter == 'day':
                # get user input for day of week (all, monday, tuesday, ... sunday)
                try:
                    day = int(input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?Please type your day as an integer (e.g. Monday = 0)').lower())
                    if day in days:
                        print("Okay, you want to filter after", "{}".format(day).capitalize(),'.')
                        break

                    else:
                        print("Day name is not correctly spelled")
                        continue
                except:
                        print("Input is incorrect")
                        continue

            while datefilter == "none":
                print("Okay, you want no filtering")
                break

            break

        except NameError:
            print('Something went wrong')
            continue

        print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    common_month_name = calendar.month_name[common_month]

    bol_common_month = df[df['month'] == common_month]
    count_common_month = bol_common_month.count()[0]

    print('Most common month:', common_month_name, 'Count:', count_common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]

    common_day_name = calendar.day_name[common_day]

    bol_common_day = df[df['day_of_week'] == common_day]
    count_common_day = bol_common_day.count()[0]

    print('Most common day:', common_day_name, 'Count:', count_common_day)

    # RECHECK THIS: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()[0]

    bol_common_start_hour = df[df['Start Hour'] == common_start_hour]
    count_common_start_hour = bol_common_start_hour.count()[0]
    print('Most common start hour:', common_start_hour, 'o\'clock\n', 'Count:', count_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    bol_common_start_sta = df[df['Start Station'] == common_start_station]
    count_start_station = bol_common_start_sta.count()[0]
    print('Most common start station:', common_start_station, 'Count:', count_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    bol_common_end_station = df[df['End Station'] == common_end_station]
    count_end_station = bol_common_end_station.count()[0]
    print('Most common end station:', common_end_station, 'Count:', count_end_station)

    # display most frequent combination of start station and end station trip
    df['Start-End Station'] = df['Start Station'] + ' , ' + df['End Station']

    common_start_end_station = df['Start-End Station'].mode()[0]

    bol_start_end_station = df[df['Start-End Station'] == common_start_end_station]
    count_start_end_station = bol_start_end_station.count()[0]

    print('Most common start and end station combination:', common_start_end_station, 'Count:', count_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Trip Duration'] = df['Trip Duration'].astype('int64')
    sum_travel_time = df['Trip Duration'].sum()
    print('The total travel time is:', sum_travel_time, 'seconds')

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is:', mean_travel_time, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df['User Type'].fillna('No User Type', inplace=True)
    user_types = df['User Type'].value_counts()
    print('User Type:\n', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        df['Gender'].fillna('No Gender', inplace=True)
        gender_types = df['Gender'].value_counts()
        print('Gender type:\n', gender_types)
    else:
        print("Gender column does not exists")

    # Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        df['Birth Year'].fillna(df['Birth Year'].median(), inplace=True)
        earlist_birthdate = df['Birth Year'].min()
        recent_birthdate = df['Birth Year'].max()
        common_birthdate = df['Birth Year'].mode()[0]

        print('Earliest birthdate:', earlist_birthdate)
        print('Most recent birthdate:', recent_birthdate)
        print('Common birthdate:', common_birthdate)
    else:
        print("Birth Year columns does not exist.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
