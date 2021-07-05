# AnsibleOracle

The fallowing description will document requirements for reproducing task results and limitations that if not met will result in exception.


Task 1
Requires: \n
	-Installed Oracle DB with table for storing standart OHLC data. This part is taken care in Task 2 where db is installed and includes additional task for creating table stocks_candle (/support_files/create_stock_table.sql for reference)\n
	-Libraries in Python/stock.py are assubed to be already installed\n
	-API key needs to be obtained from https://www.alphavantage.co/ and stored in file Alpha.txt in the same directory as the stock.py file\n
	-running stock.py on the same machine as db\n
Limitations:
	-Developed as prototype
	-Exception handling not implemented due to time constraints
	-Hardcoded values in DB connection. Same credentials used and hardcoded throughout Task 2
	-Unformated response from DB due to time constraints
	-Ploting of chart uses initialy retrieved values instead of retrieving from DB

Task 2
Requires:
	-Oracle Linux app server with configured ssh connection. In this case used phisical machine instead of VR due to disk space limitations.
	-root folder for project was set to be root ansible folder /etc/ansible/, which is very bad. Lesson learned to incorporate that in different place going forward, but due to hardcoded file path while learning on the job (not enough time to fix), that's the current setup.
	-Downloading 19.3 EE Linux x86-64 DB from https://www.oracle.com/database/technologies/oracle-database-software-downloads.html#19c and placing it in support_files folder
	-Due to file size limitations of GitHub Python/DataGenerator.py cretes insert_sample_data.sql in the same folder as DataGenerator.py and needs to be placed in support_files folder. 
	-support_files folder includes cropped file insert_sample_data_cropped.sql. It represents first 1000 inserts used in running playbook to verify data input/output of db. For cross referencing data source, this is the script used for sample data insert.
	-updating vars/main.yml for both roles to have oracle_user variable set to the user of APP SERVER

Limitations:
	-Root folder beeing etc/ansible. Lesson learned not to do that.
	-Hardcoded file/folder locations on host used for moving files to APP server
	-No checks for pre-existing instalations or created database leading to errors if playbook is re-run. This is mainly due to time constraints, should be used to pass without errors. 
	-No checks for script execution validation. Sqlplus runs without errors if connection issues or did not manage to insert, create or retrieve data, but will compleate task instead.
	-Hardcoded values in scripts even thou ansible has them in roles/{role}/vars/main.yml There was a problem of beeing stuck with sqlplus working from terminal, but not throu command module in ansible. To minimize the impact of steep learning curve, used scripts.


Lessons learned and more on what would be done differently with current knowladge to be discussed.
