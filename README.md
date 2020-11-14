# Bikeshare Project

### Date created
13th November 2020

### Description
This program processes different .csv files containing the bikeshare data of different cities and creates a summary statistics:

1. First the user has to **select the .csv file of an city**
2. Then the user needs to **select filters**:
   -Month, day or no filters
   -Which month or day
3. The summary **statistics is calculated**:
   -Most frequent travel times
   -Most frequent stations
   -Travel durations (total, average)
   -Some user statistics (user type, genders, birth years)
4. Finally the user can **choose to see some data**...

### Software to be required
1. You should have _Python 3_, _NumPy_, and _pandas_ installed using **Anaconda**
2. A **text editor**, like _Sublime_ or _Atom_.
3. A **terminal application** (Terminal on Mac and Linux or Cygwin on Windows)

### Installations Instructions
1.**Anaconda**: click [here](https://docs.anaconda.com/anaconda/navigator/tutorials/pandas/)
2.**Atom**: click [here](https://atom.io/)
3.**Terminal Application**:
  -For Windows, get a terminal application
  -For Mac, use provided terminal.

### Files used
To run this program, you need the following files:
- [_chicago.csv_](https://www.divvybikes.com/system-data)
- [_new_york_city.csv_](https://www.citibikenyc.com/system-data)
- [_washington.csv_](https://www.capitalbikeshare.com/system-data)

### Copyright
Bikeshare Project is released under [GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)


### Credits
Credits go to the mentor Clinton A. from Udacity who helped me out correcting my error messages (Check it out [here](https://knowledge.udacity.com/questions/367104)).

###Known Bugs
Some data wrangling has been done by Udacity.
If you use the links to the raw data files, you need to perform some data wrangling to get the following table format :

Start Time | End Time | Trip Duration | Start Station | End Station | User Type | Gender | Birthdate
-----------|----------|---------------|---------------|-------------|-----------|--------|----------
   ...     |   ...    |     ...       |      ...      |     ...     |    ...    |   ...  |   ...

Else this program will run into an error.

###Version
Version I released on 14th November 2020
