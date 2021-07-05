#!/bin/bash

/u01/app/oracle/product/19.2.0/db100/bin/sqlplus -S SYSTEM/#BadPractice6@localhost/cdb2 < /u01/ordata/temp_scripts/retrieve_first_100.sql 

exit 0