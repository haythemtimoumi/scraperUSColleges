Overview
This project consists of a web scraper that extracts student directory information from the University of Texas at Dallas (UTD) website. The scraper collects student names, emails, majors, graduation years, schools, and phone numbers, then saves the data to a CSV file.

Features
Comprehensive Scraping: Collects student data for all letters A-Z

Data Validation: Includes checks for duplicate emails

Undetectable Scraping: Uses undetected_chromedriver to avoid bot detection

CSV Export: Saves data with timestamps for versioning

Files
scrapstudent.py: Main scraper script

Collects student data from UTD directory

Handles pagination and search filters

Saves data to timestamped CSV files

test_dup.py: Data validation script

Checks for duplicate email addresses in the CSV

Provides detailed report of duplicates

![Image](https://github.com/user-attachments/assets/5d93eb27-b1ed-47e6-8c97-e24ed3a3f4dd)
![Image](https://github.com/user-attachments/assets/ecf0c8f2-1d70-4406-9c68-ef026ad1378e)
![Image](https://github.com/user-attachments/assets/be390e58-ab35-44c5-91fe-da61c9a4aaa2)


Out of 2,601 emails, 92 are duplicates 



![Image](https://github.com/user-attachments/assets/5e7df1bd-8a53-4b2a-911b-cabb617f4f00)



and this the final result 

No duplicate emails found

![Image](https://github.com/user-attachments/assets/f47c01b7-d6a2-4fae-b050-4ffd1f15bb3e)

![Image](https://github.com/user-attachments/assets/8b807391-ce6c-4cab-b7e9-fa9d780a997c)



