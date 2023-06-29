import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def city_month_day():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city would you like to explore? Chicago, New York City, or Washington? ").lower()
        if city not in ("chicago", "new york city", "washington"):
            print("That input is invalid. Your choices are Chicago, New York City, or Washington. Please try again.\n")
            continue
        else:
            break         
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month would you like to explore? All, January, February, March, April, May, June? ").lower()
        if month not in ("all", "january", "february", "march", "april", "may", "june"):
            print("Sorry, I don't understand that. Please try again.\n")
            continue
        else:
            break  
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day's data would you like to explore?  All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday? ").lower()
        if day not in ("all", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"):
            print("Sorry, I don't understand that. Please try again.\n")
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A').str.lower()
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
        df = df[df['day_of_week'] == day.lower()]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_start_month = df['month'].mode()[0]
    print('Most common month: ', common_start_month)

    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['dayofweek'] = df['Start Time'].dt.dayofweek
    common_day_of_week = df['dayofweek'].mode()[0]
    print('Most common day of week: ', common_day_of_week)
        
    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('Common start hour: ', common_start_hour)    
       
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_common_start_station = df['Start Station'].mode()[0]
    print('Commonly used start station: ', Most_common_start_station)    
        
          
          
          
    # TO DO: display most commonly used end station
    Most_common_end_station = df['End Station'].mode()[0]
    print('Commonly used end station: ', Most_common_end_station) 


    # TO DO: display most frequent combination of start station and end station trip
    df['combo_station'] = df['Start Station'] + ' ' + df['End Station']
    combo = df['combo_station'].mode()[0]
    print('The most frequent combination of start station and end stations are ', combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = sum(df['Trip Duration'])
    print('The total travel time is ', total)
    # TO DO: display mean travel time
    mean= np.mean(df['Trip Duration'])
    print('The average travel time is ', mean)
            
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
#(not in washington Add a condition to handle missing gender column Washington data)
    while True:
        try:
            gender_counts = df['Gender'].value_counts()
            print(gender_counts)
            break
        except:
            print('Gender information is not available')
            break
        
    # TO DO: Display earliest, most recent, and most common year of birth
    #(not available in washington csv Add a condition to handle to handle the missing info)
    #(earliest = min, most recent = max, most common = mode)
    while True:
        try:
            oldest = min(df['Birth Year'])
            print('The oldest person was born on ', oldest)
            youngest = max(df['Birth Year'])
            print('The youngest person was born on ', youngest)
            common_by = (df['Birth Year']).mode()[0]
            print('The most common birth year is ',common_by)
            break
        except:
            print('Birth year information is not available')
            break
    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city,month,day):
    
    
    df = load_data(city,month,day)
    counter = 0
               
    while True:
        question = input('Would you like to see 5 rows of raw data? Enter yes or no.\n').lower()
        if question.lower() == 'yes':
            print(df[counter:counter+5])
            counter += 5
        elif question.lower() == 'no':
            break
        
        elif question not in ('yes', 'no'):
            print("Sorry, I don't understand that. Please type yes or no.\n")
        else:
            break
    
def main():
    while True:
        city, month, day = city_month_day()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city, month, day)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes': 
            break


if __name__ == "__main__":
	main()

    

