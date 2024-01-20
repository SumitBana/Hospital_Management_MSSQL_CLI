create table Patient ( PNUM int Primary key ,FNAME varchar(20) Not NULL,MNAME varchar (20),LNAME varchar(20) Not NULL,DID varchar(4) NOT NULL,GENDER char(1) NOT NULL,DOB date NOT NULL,DOA date NOT NULL,DOD date,WARD varchar(3) NOT NULL,REASON varchar(50) not null);
create table usr_pwd (USERNAME varchar(15) not null , PASSWORD varchar(15) not null);
create table doc (DID varchar(4) Primary Key, DFNAME varchar(15) Not Null,DMNAME varchar(15),DLNAME varchar(15) Not Null, FIELD VARCHAR(30) Not Null, DOJ date Not Null);
create table nurse(NID varchar(4) Primary Key, NFNAME varchar(15) Not Null,NMNAME varchar(15),NLNAME varchar(15) Not Null, WARD VARCHAR(3) Not Null, DOJ date Not Null)
create table dtime (DID varchar(4) Primary key,MON varchar(12),TUE varchar(12),WED varchar(12),THU varchar(12),FRI varchar(12),SAT varchar(12),SUN varchar(12))
