# Python Security Log Analyser

## Overview

I built a Python security log analyser to practise analysing authentication data and identifying patterns that could be useful during a security investigation.

The program uses Pandas to process a synthetic login activity dataset, analyse suspicious authentication events and identify anonymised IP addresses associated with repeated suspicious activity.

It also exports the results of the repeated-IP analysis to a CSV file so that the findings can be reviewed separately.

## Technologies Used

- Python
- Pandas
- CSV
- Visual Studio Code
- Git/GitHub

## What the Program Does

The analyser:

- Loads authentication log data from a CSV dataset
- Displays the number of login records and available security fields
- Filters events marked as suspicious in the dataset
- Calculates the percentage of login activity flagged as suspicious
- Groups suspicious events by system
- Identifies suspicious events where second-factor authentication was not used
- Analyses the most common anonymised source countries
- Counts suspicious events associated with each anonymised IP address
- Flags IP addresses associated with 5 or more suspicious events
- Exports those results to a separate CSV security report

## Detection Logic

After filtering the suspicious authentication events, the program groups them by anonymised IP address and counts how many suspicious events are associated with each address.

For this project, I used a threshold of **5 or more suspicious events** to identify IP addresses that may require further investigation.

The detection works by counting suspicious events for each anonymised IP address and selecting addresses with at least five events.

This threshold is a simple project rule and does not mean the activity is a confirmed cyberattack.

## Second-Factor Authentication Analysis

The program also checks suspicious events where second-factor authentication was not used.

This allowed me to compare suspicious authentication activity with the use of additional authentication controls.

## Report Generation

The repeated suspicious IP results are exported to:

`output/suspicious_ip_report.csv`

The report contains:

- Anonymised IP address
- Number of suspicious events associated with that address

## Project Screenshot

The screenshot below shows the analyser being used to investigate authentication activity.

![Repeated suspicious IP detection](screenshots/Screenshot%202026-10-05%20113711.png)

## What I Learned

Through this project I developed practical experience with:

- Reading CSV datasets using Pandas
- Filtering security-related data
- Analysing authentication events
- Counting and grouping events to identify patterns
- Applying a simple threshold to prioritise repeated suspicious activity
- Analysing second-factor authentication information
- Exporting investigation results to CSV
- Structuring a Python cybersecurity project using GitHub

## Future Improvements

Possible future improvements include adding configurable detection thresholds, analysing suspicious activity over time and creating visualisations to make authentication patterns easier to investigate.


