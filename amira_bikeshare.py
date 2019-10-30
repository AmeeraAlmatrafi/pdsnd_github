import time
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

    print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    #get user input for city (chicago, new york city, washington). 
    while True:
      city = input("Please enter the city you want to filter by? new york city, chicago or washington?\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("Sorry,Try again...choose one of the three cities.")
        continue
      else:
         break

    #get user input for month (all, january, february, ... , june)
    while True:
      month= input("\n Choose a month you want or say all, ex: january, february, march, april, may, june:\n").lower()
      if month.lower() not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry,Try again...")
        continue
      else:
        break

    #get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\n Choose a day you want or say all, ex: sunday, monday, tuesday, wednesday, thursday, friday, saturday:\n").lower()
      if day.lower() not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry,Try again...")
        continue
      else:
         break

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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month if applicable 
    if month != 'all':
   	 	# use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    	# filter by month to create the new dataframe
        df = df[df['month'] == month]

    #filter by day if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """The Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    most_common_month = df['month'].mode()[0]
    print('Most Common Month:\n', most_common_month)


    # display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('\nThe Most Common day:\n', most_common_day)

    # display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('\nThe Most Common Hour:\n', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """The Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('\nThe Most Commonly used start station:\n', start_station)

    # display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax())
    print('\nThe Most Commonly used end station:\n', end_station)

    # display most frequent combination of start station and end station trip
    Combination = df.groupby(['Start Station', 'End Station']).count()
    print('\nThe most frequent combination of start station and end station trip:\n',start_station , 'and' ,end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    """The Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The Total travel time :\n", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("\nThe Mean travel time :\n", mean_travel_time)
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n")
    print('The counts of User Types:\n', user_types)
  
   
    # Display counts of gender
    try:
      gender = df['Gender'].value_counts()
      print('\nThe Gender Types:\n', gender)
    except KeyError:
      print("No data..")
    

    # Display earliest year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print("\nThe most earliest birth year:\n", earliest_year)
    except KeyError:
      print("\nthe most earliest birth year:\nNo data.")
      
    # Display most recent year of birth
    try:
        most_recent = df['Birth Year'].max()
        print("\nThe most recent birth year:\n", most_recent)
    except KeyError:
      print("\n\nThe most recent birth year:\nNo data.")

    #Display most common year of birth    
    try:
         most_year = df['Birth Year'].value_counts().idxmax())
         print("\nThe most common birth year:\n", most_year)
    except KeyError:
      print("\nThe most common birth year:\nNo data.")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """
Display contents of the CSV file to the display as requested by
    the user
    """
    start = 0
    end = 5

    display_data = input("Do you want to see the raw data?say yes or no: ")

    if display_data == 'yes':
        while end <= df.shape[0] - 1:

            print(df.iloc[start:end,:])
            start += 5
            end += 5

            end_data = input("Do you want to continue?say yes or no: ")
            if end_data == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
       
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
