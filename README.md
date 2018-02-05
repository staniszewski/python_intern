# hack_power.py (Python 3.6)

The script calculates power of hack. User types hack and program returns its power.  
Allowed characters in hack are: 'a', 'b', 'c'. Other characters are ineffective.  
If hack contains other characters than allowed has power equal to zero.  
Each character has own power which is added to final hack power.  
Each repeated character in a hack brings more power than its previous iteration.  
`'a' has 1 power, 'b' - 2 and 'c' - 3.`  
Hack containing phrases 'ba' or 'baa' has extra power. For 'ba' - 10 power and for 'baa' - 20.  
For example:  
```
hack 'ccbc' has 20 power
c + c + b + c		
3 + 3*2 + 2 + 3*3 = 20 power

hack 'baaca' has 31 power
b + a + a + c + a	
2 + 1 + 1*2 + 3 + 1*3 	= 11 power

extra power for 'baa'
+ 20 = 31 power
```

## Usage

Run:  
`python hack_power.py`  
Program will ask you to 'Enter hack' and return power of typed hack.  
Example:  
```
python hack_power.py
Enter hack: abc
Your hack "abc" has 6 power.
```
## Optional
To make this script working dynamically, to provided own letters and phrases we could for example:
```
1.	Read dictionary letters and phrases from file
2.	Read dictionary letters and phrases from server
3.	Pass keys and values of letters and phrases dictionaries as system arguments
4.	Make function which passes own keys and values to dictionary and then calculate hack power
5.	Make it as a class and passes dictionaries as class variables while creating object of class
```


# page_report.py (Python 3.6)

Script to strip names of requested URLs from log file and counts number of requests for every URL in log file.  
Every log in log file should start by IPv4 address. It returns error when log is invalid by checking if the beginning of log contains IPv4.  
Parsing URL is provided by urllib library. Urlparse method divides passed url to parts, then script rejects query parameters.  
Each stripped URL is passed to data structure which keep URLs names and number of requests to.  
Script returns URLs names and number of requests for it in csv format:  
`"<stripped url>",<requests count>`  

## Usage

Example:  
```py
python page_report.py today.log > report.csv

#page_report.py - script name
#today.log - your log file name
#report.csv - your csv format file where you want to save stripped log file
```
Script takes log file name as system argument and then passes it to function.  
Make sure to edit 10th line in script and pass your directory where log file is!  
For example:  
```py
today_log = open(r'C://Users/your_username/your_directory/some_subdirectory/' + log_file, 'r')
```
Otherwise script will not work correctly!


