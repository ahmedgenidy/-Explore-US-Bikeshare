import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! \n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city= input("Please enter city - name of the city to analyze \n'chicago' \n'new york city' \n'washington' \n= ")
    while city not in ["chicago" , "new york city" , "washington"]:
        city= input("Please enter city in the correct format \n'chicago' \n'new york city' \n'washington' \n= ").lower()
        
    print("  you have entered " + city)

    # TO DO: get user input for month (all, january, february, ... , june)
    month= input("Please enter month - name of the month to filter by \n'all' \n'january' \n'february', \n'march', \n'april', \n'may', \n'june' \n= ")
    while month not in ['all','january', 'february', 'march', 'april', 'may', 'june']:
        month= input("Please enter month in the correct format \n'all' \n'january' \n'february', \n'march', \n'april', \n'may', \n'june' \n= ").lower()
        
    print("  you have entered " + month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input(" Please enter day - name of the day of week to filter by \n'all'\n'Monday'\n'Tuesday'\n'Wednesday'\n'Thursday'\n'Friday'\n'Saturday'\n'Sunday'\n= ")           
    while day not in ["all", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        day= input("Please enter day in the correct format \n'all'\n'Monday'\n'Tuesday'\n'Wednesday'\n'Thursday'\n'Friday'\n'Saturday'\n'Sunday'\n= ").title()
   
    print("  you have entered " + day)
    print('-'*40)
    print(" You entered \n 'city'= " + city + "\n 'month'= " + month +"\n 'day'= " + day)
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
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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

    # TO DO: display the most common month
    popular_month = df['month'].mode()
    print('Most Frequent Month:',   popular_month.to_string(index=False))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()
    print('Most Frequent Day:', popular_day.to_string(index=False))

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()
    print('Most Frequent Start Hour:', popular_hour.to_string(index=False))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()
    print('Most Frequent Start Station:', start_station.to_string(index=False))

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()
    print('Most Frequent End Station:', end_station.to_string(index=False))

    # TO DO: display most frequent combination of start station and end station trip
    counts = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False)[0]
    print('Most Frequent Combination of Start Station and End Station trip:',counts)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = int(df['Trip Duration'].sum())
    total_travel_time2= datetime.timedelta(seconds=total_travel_time)
    print('Total Travel Time:', total_travel_time2)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time2= datetime.timedelta(seconds=mean_travel_time)
    print('Mean Travel Time:', mean_travel_time2)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types and Gender
    user_type = df['User Type'].count()
    print('Count of User Types:', user_type)

    # TO DO: Display counts of gender
    if "Gender" not in df.columns:
        print("There is no 'Gender' data")
    else:
        gender = df['Gender'].count()
        print('Count of Gender:', gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" not in df.columns:
        print("There is no 'Birth Year' data")
    else:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode())
        print('\nEarliest Bith Year:', earliest)
        print('Most Recent Bith Year:', most_recent)
        print('Most common Bith Year:', most_common)
    

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
        
        
        head = input('\nWould you like to show the first 5 rows in Data? Enter yes or no.\n')
        start_loc = 0
        while head.lower() == 'yes':
            print(df.iloc[start_loc : (start_loc+5)])
            start_loc += 5
            head = input('\nWould you like to show another 5 rows in Data? Enter yes or no.\n')

            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
	main()
