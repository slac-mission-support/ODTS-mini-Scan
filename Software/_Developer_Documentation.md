# General Workflow

The scanner box uses a USB camera to read the barcode, then makes a data request from a VIEW in the ODTS database.
The data returned includes user information.  This data is displayed sequentially on the scanner box' LCD display.

The box then calls an ODTS stored procedure to update the return date for that dosimeter with the current date.

Details related to the transaction are written locally on the box in an SQL Lite database file (test_records.db or prod_records.db).

Finally, the box composes an email and sends it to the user or their supervisor providing a receipt of the return.
The email will also show additional unreturned dosimeters, if any.  These are queried using the PERSON ID against a second VIEW.

## Accessing the Software: 
The IDE for the application is the GEANY editor on the raspberry pi.  Open the lid of the box and connect a monitor to the Raspberry PI board, then navigate to the cloned repository in the home subfolder "ODTS-mini-Scan" using the Pi OS file explorer.

## Software Requirements:
Requirements for the function of the source code are provided in the `Specification for mini-Scan.docx` in this repository.

## Boot procedure:
When the Pi boots, it starts by loading the programs listed in the rc.local file.  To edit the file, type `sudo nano /etc/rc.local` from a command prompt on the Pi.  This file must be revised when changing from TEST to PROD, which are subfolders within this repository.

* The first file the Pi loads is for the reset button.  The reset button must be held for 6 seconds then the Pi will reboot safely.

* The other file is the Capture_barcode.py file.  This file contains a series of methods followed by a while loop (which calls those methods) 
and runs continuously so that barcodes can be scanned sequentially and returned into the ODTS system.

* The Capture_barcode.py file references a set of 10 - 15 other class libraries which drive the LCD, pings the network, queries ODTS, composes the email, etc.

## Scheduled Programs (crontab):
The box runs two scheduled programs using the built-in utility crontab.  To edit the scheduler type `sudo crontab -e` from a command prompt on the Pi.  There is a file in this repo titled `Git_Pull_Scheduling.txt` which describes how to use the scheduler.

* The first program is scheduled daily which is `crontab_daily_gitpull.py`.  This performs a git pull command to fetch latest software from the repo.  In order for this to work the gitconfig file in /home/ryanford needs to have an entry for a proxy server that was created as follows: `git config --global http.proxy http://mgmt-authproxy01:3128`.  The port has to be opened on the device's IP for this to work by the Networking team.  See incident INC0457115 for more information. To view the contents use the Pi's file explorer or type `git config --list --show-origin --show-scope` from the $ prompt.

* The second program is scheduled daily which is daily_email.py.  This sends the Dosimetry Group a daily record of all transactions on the box.  Both the daily_email.py and smtp_email.py programs use SMTPOUT.slac.stanford.edu smtp relay.  In order for this to work, port 25 must be opened on the device's IP by the Networking team.

* Three additional crontab files reside in the source code folder:  crontab_weekly.py, crontab_monthly.py, and crontab_yearly.py.  Crontab is scheduled to run them at the noted frequency.  At rollout the programs were empty and were intended for future expandability, which prevents the need to recall the boxes and edit crontab.

## Configuration File
There is a configuration file called `config.py` that creates the `config.ini`.  Both of these files are excluded from the repo using the `.gitignore` file.

In order for the box to operate the `config.ini` file must exist.  If the file is deleted, recreate it by running config.py.  This will populate the config.ini file and some of the values will have an initial value of NULL.  A Capture_barcode method will then write those NULL values with data from ODTS so that later the email builder can read them.

The configuration file contains password data for ODTS as well as database pathways and other variables used throughout the library files.

## Test vs. Prod:
All remotes will pull the repo changes on a daily basis.  Work in test then migrate to prod:

Move Test to Prod by copying and pasting all files except:
* `config.py` and `config.ini` if unchanged
* `history.xlsx`
* `sqlite_master.db`, `sqlite_schema.db`, `test_records.db` which has a production version `prod_records.db`

The differences between the TEST and PROD folders are as follows:
* The config.py and config.ini files will differ by:
  * The database section.
  * The hostname and device location in Scanner section.  The first box is ODTSSCAN01, the second box ODTSSCAN02, etc.
* The prod_records.db SQLite file will differ by the data it contains versus what is in test.
* The py files which send emails will differ by the "send to" address which in test is hard coded to a single person (who is testing) or listserv account.
This prevents actual users from receiving test emails.  Verify the recipients are correct in `smtp_email.py` and `crontab_daily_email.py`

## Using GitHub
* From the scanner box, change directory:  `cd /home/ryanford/ODTS-mini-Scan`'
* Pull the changes in main:  `git pull` or `git pull --rebase`
* Push changes from remote (`origin` or similar) to `main` (github repo):
  * `git add --all`
  * `git commit -m "description of changes to commit"`
  * `git push -u origin main`
  * Note:  Origin is the remote name for the first host (ODTSSCAN01).
* Git Ignore
  * Add the following files to .gitignore:
  * Both config files (`config.ini`, `config.py`).  These contain password information that must be kept off Github
  * Excel files, log files, .db files.  If these are not ignored, then git pull won't work because local changes are not committed

## Cloning a box:
Cloning a box will require change of the static IP address, as well as the hostname and location in the config file.  One would delete the ini file, then change the config.py file to the correct host name, then run the config.py file to re-generate the ini file. Finally change the rc.local file.  See `_cloning_instructions`.md.

## Conclusion:
Python files are commented to help with the purpose and readability of the code.

## Testing
Any changes to the source code must be followed by the testing plan which outlines 10 or more scenarios to test.  Use of the box must be
documented in Dosimetry Group (DG) procedures, and testing results must be published in Dosimetry Records.



