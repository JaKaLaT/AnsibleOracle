set colsep ,
set headsep off
set pagesize 0
set trimspool on

SET MARKUP CSV ON QUOTE ON

spool /home/john/Documents/gathered_data.csv

SELECT * FROM sample_data WHERE id<=100;

spool off