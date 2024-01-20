INSERT INTO Patient (PNUM, FNAME, MNAME, LNAME, DID, GENDER, DOB, DOA, DOD, WARD, REASON) VALUES
('1', 'AMIT', NULL, 'SHARMA', 'D007', 'M', '1980-01-01', '2024-01-01', '2024-01-10', 'W03', 'ROUTINE HEALTH CHECKUP'),
('2', 'SUNITA', 'KUMARI', 'SINGH', 'D003', 'F', '1985-02-02', '2024-01-02', NULL, 'W07', 'UNDERGOING SURGERY FOR APPENDICITIS'),
('3', 'RAJESH', NULL, 'GUPTA', 'D010', 'M', '1990-03-03', '2024-01-03', '2024-01-13', 'W02', 'ROUTINE HEALTH CHECKUP'),
('4', 'ANITA', NULL, 'YADAV', 'D001', 'F', '1995-04-04', '2024-01-04', NULL, 'W10', 'UNDERGOING SURGERY FOR GALLSTONES'),
('5', 'RAVI', 'KUMAR', 'VERMA', 'D006', 'M', '2000-05-05', '2024-01-05', '2024-01-15', 'W01', 'ROUTINE HEALTH CHECKUP'),
('6', 'POOJA', NULL, 'PATEL', 'D002', 'F', '2005-06-06', '2024-01-06', '2024-01-16', 'W06', 'UNDERGOING SURGERY FOR HERNIA'),
('7', 'VIJAY', NULL, 'CHAUDHARY', 'D009', 'M', '2010-07-07', '2024-01-07', NULL, 'W04', 'ROUTINE HEALTH CHECKUP'),
('8', 'REKHA', 'DEVI', 'JHA', 'D004', 'F', '2015-08-08', '2024-01-08', '2024-01-18', 'W09', 'UNDERGOING SURGERY FOR CATARACT'),
('9', 'SANJAY', NULL, 'JAIN', 'D005', 'M', '2020-09-09', '2024-01-09', '2024-01-19', 'W05', 'ROUTINE HEALTH CHECKUP'),
('10', 'KIRAN', NULL, 'AGARWAL', 'D008', 'F', '2021-10-10', '2024-01-10', NULL, 'W08', 'UNDERGOING SURGERY FOR KNEE REPLACEMENT'),
('11', 'RAHUL', NULL, 'KHANNA', 'D001', 'M', '1981-11-11', '2024-01-11', '2024-01-21', 'W06', 'ROUTINE HEALTH CHECKUP'),
('12', 'GEETA', NULL, 'SRIVASTAVA', 'D006', 'F', '1986-12-12', '2024-01-12', NULL, 'W01', 'UNDERGOING SURGERY FOR HIP REPLACEMENT'),
('13', 'SUNIL', NULL, 'KAPOOR', 'D003', 'M', '1991-01-13', '2024-01-13', '2024-01-23', 'W07', 'ROUTINE HEALTH CHECKUP'),
('14', 'MEENA', NULL, 'RANA', 'D010', 'F', '1996-02-14', '2024-01-14', '2024-01-24', 'W02', 'UNDERGOING SURGERY FOR TONSILLECTOMY'),
('15', 'ANIL', NULL, 'MALHOTRA', 'D002', 'M', '2001-03-15', '2024-01-15', NULL, 'W10', 'ROUTINE HEALTH CHECKUP'),
('16', 'SARITA', NULL, 'DAS', 'D009', 'F', '2006-04-16', '2024-01-16', '2024-01-26', 'W03', 'UNDERGOING SURGERY FOR SINUSITIS'),
('17', 'RAKESH', NULL, 'MEHRA', 'D004', 'M', '2011-05-17', '2024-01-17', NULL, 'W04', 'ROUTINE HEALTH CHECKUP'),
('18', 'SEEMA', NULL, 'BISWAS', 'D007', 'F', '2016-06-18', '2024-01-18', '2024-01-28', 'W08', 'UNDERGOING SURGERY FOR ADENOIDECTOMY'),
('19', 'RAJIV', NULL, 'NAIR', 'D008', 'M', '2021-07-19', '2024-01-19', '2024-01-29', 'W06', 'ROUTINE HEALTH CHECKUP'),
('20', 'SAVITA', NULL, 'PANDEY', 'D005', 'F', '2022-08-20', '2024-01-20', '2024-01-30', 'W09', 'UNDERGOING SURGERY FOR MASTECTOMY'),
('21', 'AMIT', NULL, 'SHARMA', 'D010', 'M', '1990-01-01', '2024-01-01', '2024-01-10', 'W03', 'ROUTINE HEALTH CHECKUP');

INSERT INTO doc (DID, DFNAME, DMNAME, DLNAME, FIELD, DOJ) VALUES
('D001', 'ANAND', 'KUMAR', 'GUPTA', 'GASTROENTEROLOGIST', '2000-01-01'),
('D002', 'BHARTI', NULL, 'PATEL', 'ORTHOPEDIC', '2005-02-02'),
('D003', 'CHETAN', 'SINGH', 'SINGH', 'GYNECOLOGIST', '2010-03-03'),
('D004', 'DEEPA', NULL, 'JHA', 'OPHTHALMOLOGIST', '2015-04-04'),
('D005', 'ESHA', 'RAJ', 'JAIN', 'PEDIATRICIAN', '2020-05-05'),
('D006', 'FARHAN', NULL, 'VERMA', 'ORTHOPEDIC', '2021-06-06'),
('D007', 'GAURAV', 'KUMAR', 'SHARMA', 'CARDIOLOGIST', '2015-07-07'),
('D008', 'HEMA', NULL, 'AGARWAL', 'SURGEON', '2010-08-08'),
('D009', 'ISHA', NULL, 'CHAUDHARY', 'ENT SPECIALIST', '2005-09-09'),
('D010', 'JAYA', 'DEVI', 'GUPTA', 'DERMATOLOGIST', '2000-10-10'),
('D011', 'ANAND', 'KUMAR', 'GUPTA', 'ENT SPECIALIST', '2003-01-01');


INSERT INTO nurse (NID, NFNAME, NMNAME, NLNAME, WARD, DOJ) VALUES
('N001', 'PRIYA', 'KUMARI', 'SHARMA', 'W03', '2005-01-15'),
('N002', 'RAHUL', 'SINGH', 'MEHTA', 'W08', '2010-02-22'),
('N003', 'ANITA', NULL, 'YADAV', 'W05', '2015-03-30'),
('N004', 'VIKRAM', 'RAJ', 'VERMA', 'W02', '2020-04-10'),
('N005', 'NISHA', NULL, 'GUPTA', 'W10', '2021-05-12'),
('N006', 'ARJUN', 'KUMAR', 'SINGH', 'W06', '2010-06-18'),
('N007', 'ANJALI', NULL, 'CHAUDHARY', 'W01', '2015-07-25'),
('N008', 'RAVI', 'KUMAR', 'JHA', 'W09', '2020-08-30'),
('N009', 'SARITA', NULL, 'YADAV', 'W04', '2005-09-05'),
('N010', 'SUMIT', 'SINGH', 'RAJPUT', 'W07', '2010-10-12'),
('N011', 'NEHA', 'RAJ', 'SHARMA', 'W02', '2015-11-15'),
('N012', 'ROHIT', NULL, 'MEHTA', 'W10', '2020-12-22'),
('N013', 'POOJA', 'KUMARI', 'YADAV', 'W08', '2008-01-30'),
('N014', 'VIJAY', NULL, 'VERMA', 'W03', '2012-02-10'),
('N015', 'ANJU', 'DEVI', 'GUPTA', 'W05', '2017-03-12'),
('N016', 'RAMESH', NULL, 'SINGH', 'W01', '2019-04-18'),
('N017', 'KIRAN', 'KUMARI', 'CHAUDHARY', 'W06', '2014-05-25'),
('N018', 'SUNIL', NULL, 'JHA', 'W04', '2011-06-30'),
('N019', 'PRIYANKA', 'KUMARI', 'YADAV', 'W09', '2016-07-05'),
('N020', 'RISHABH', 'KUMAR', 'RAJPUT', 'W07', '2013-08-12'),
('N021', 'MANISH', NULL, 'SHARMA', 'W01', '2018-09-15'),
('N022', 'SIMRAN', 'KUMARI', 'MEHTA', 'W04', '2007-10-22'),
('N023', 'AJAY', NULL, 'YADAV', 'W10', '2012-11-30'),
('N024', 'KAVITA', 'DEVI', 'VERMA', 'W06', '2014-12-10'),
('N025', 'SANDEEP', NULL, 'GUPTA', 'W03', '2019-01-12'),
('N026', 'PRIYA', 'KUMARI', 'SHARMA', 'W05', '2009-03-15');


INSERT INTO dtime (DID, MON, TUE, WED, THU, FRI, SAT, SUN) VALUES
('D001', '09:00-17:00', NULL, '09:00-17:00', NULL, '09:00-17:00', '10:00-14:00', NULL),
('D002', '08:30-16:30', '08:30-16:30', NULL, '08:30-16:30', '08:30-16:30', NULL, '10:30-15:30'),
('D003', NULL, '10:00-18:00', '10:00-18:00', '10:00-18:00', NULL, '11:00-15:00', NULL),
('D004', '08:00-16:00', NULL, '08:00-16:00', NULL, '08:00-16:00', NULL, '09:00-14:00'),
('D005', '09:30-17:30', '09:30-17:30', '09:30-17:30', '09:30-17:30', '09:30-17:30', '10:30-14:30', NULL),
('D006', NULL, '10:30-18:30', NULL, '10:30-18:30', '10:30-18:30', NULL, '11:30-16:30'),
('D007', '08:00-16:00', NULL, '08:00-16:00', NULL, '08:00-16:00', '09:00-13:00', NULL),
('D008', '09:30-17:30', '09:30-17:30', NULL, '09:30-17:30', '09:30-17:30', NULL, '10:30-15:30'),
('D009', NULL, '11:00-19:00', '11:00-19:00', '11:00-19:00', '11:00-19:00', '12:00-16:00', NULL),
('D010', '08:30-16:30', NULL, '08:30-16:30', '08:30-16:30', '08:30-16:30', NULL, '09:30-14:30'),
('D011', NULL, '12:00-16:00', '13:00-15:00', '14:00-19:00', '11:00-17:00', '12:00-16:30', NULL);