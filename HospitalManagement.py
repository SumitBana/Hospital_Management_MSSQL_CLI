import pyodbc
import os
from datetime import datetime
import time
class usr_pwd:
    __id = None
    __pd = None

    def new_user(self):
        try:
            self.__id = input("Enter UserName (No Spaces Allowed)(It Can be Upto 15 Character Long & Alphanumeric) : ")
            if (self.__id).isalnum():
                if (len(self.__id)) <= 15:
                    q = "select COUNT(*) FROM usr_pwd WHERE USERNAME = ?;"
                    cursor.execute(q, self.__id)
                    if cursor.fetchone()[0] == 0:
                        self.__pd = input("Enter Password (No Spaces Allowed)(It Can be Upto 15 Character Long) : ")
                        if not (self.__pd).isspace():
                            if (len(self.__pd)) <= 15:
                                q = "INSERT INTO usr_pwd values (?,?);"
                                cursor.execute(q, self.__id, self.__pd)
                                cursor.commit()
                                os.system('cls')
                                msg="User Registered Successfully"
                                t = 1
                                print(msg)
                                time.sleep(t)
                            else:
                                print("Password too Long\n")
                                input("Enter To Try Again")
                        else:
                            print("Password Contains Spaces\n")
                            input("Enter To Try Again")
                    else:
                        print("UserName Already Exists (Use a Different Username)\n")
                        input("Enter To Try Again")
                else:
                    print("Username too Long\n")
                    input("Enter To Try Again")
            else:
                print("UserName is not Alphanumeric\n")
                input("Enter To Try Again")
        except Exception as e:
            print("Error While Registering Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")


    def old_user(self):
        try:
            self.__id = input("Enter your UserName : ")
            if (self.__id).isalnum():
                if (len(self.__id)) <= 15:
                    q = "select COUNT(*) FROM usr_pwd WHERE USERNAME = ?;"
                    cursor.execute(q, self.__id)
                    if cursor.fetchone()[0] == 1:
                        self.__pd = input("Enter your Password : ")
                        if not (self.__pd).isspace():
                            if (len(self.__pd)) <= 15:
                                q = "select PASSWORD FROM usr_pwd WHERE USERNAME = ?;"
                                cursor.execute(q, self.__id)
                                if cursor.fetchone()[0] == self.__pd:
                                    os.system('cls')
                                    msg = "Login Successful\n"+"\nWelcome: "+ self.__id+',\n'+'\nEstablishing Connection With MSSQL,Please Wait!'
                                    t = 2
                                    print(msg)
                                    try:
                                        fpath='hmsaccess.log'
                                        fob=open(fpath,'a+')
                                        fob.seek(0,2)
                                        ct = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                        s='USER: '+self.__id+' | '+'LOGIN: '+ct+'\n'
                                        fob.write(s)
                                        fob.flush()
                                    except:
                                        print("Logs Entry Error")
                                        return 1
                                    time.sleep(t)
                                    return 1
                                else:
                                    print("Wrong Password\n")
                                    input("Enter Any Key to Continue")
                                    return 0
                            else:
                                print("Wrong Password\n")
                                input("Enter To Try Again")
                        else:
                            print("Wrong Password\n")
                            input("Enter To Try Again")
                    else:
                        print("No Username Found\n")
                        input("Enter To Try Again")
            else:
                print("Wrong Username\n")
            input("Enter To Try Again")
        except Exception as e:
            print("Error While Login Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return
    def set_pass(self):
        try:
            self.__id = input("Enter your UserName : ")
            q = "select COUNT(*) FROM usr_pwd WHERE USERNAME = ?;"
            cursor.execute(q, self.__id)
            if cursor.fetchone()[0] == 1:
                self.__pd = input("Enter New Password (No Spaces Allowed)(It Can be Upto 15 Character Long) : ")
                if not(self.__pd).isspace():
                    if (len(self.__pd)) <= 15:
                        q = "update usr_pwd set PASSWORD = ? where USERNAME = ?;"
                        cursor.execute(q, self.__pd, self.__id)
                        print("PASSWORD UPDATED")
                        cursor.commit()

                    else:
                        print("Password too Long\n")
                else:
                    print("Password Contains Spaces\n")
            else:
                print("No Username Found\n")
            input("Enter Any Key to Continue")
        except Exception as e:
            print("Error While Changing Password Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return

class patient:

    __pid=__fname=__mname=__lname=__did=__gender=__dob=__doa=__dod=__ward=__reason=None

    def add_patient(self):
        flag=flg=0
        try:
            q = "SELECT TOP 1 * FROM Patient ORDER BY PNUM DESC;"
            cursor.execute(q)
            val=cursor.fetchone()
            if (val == None): self.__pid = 1
            else: self.__pid = (val[0])+1
            while (flag==0):#FNAME
                self.__fname = input("Enter the First Name (Atmost 15 Characters long): ")
                if self.string_checker(self.__fname):
                    self.__fname=self.__fname.upper()
                    while (flag==0):#MNAME
                        self.__mname = input("Enter the Middle Name (If Any,Else Press Enter to Continue) (Atmost 15 Characters long): ")
                        if len(self.__mname) == 0 : self.__mname = 'NULL'
                        if self.string_checker(self.__mname):
                            self.__mname=self.__mname.upper()
                            if self.__mname in ['NULL','NIL','None']:self.__mname=None
                            while (flag==0):#LNAME
                                self.__lname = input("Enter the Last Name (Atmost 15 Characters long): ")
                                if self.string_checker(self.__lname):
                                    self.__lname=self.__lname.upper()
                                    os.system('cls')
                                    while (flag==0): #DID
                                        self.__did = input("Enter the Doctor Id (Format Like : D000): ")
                                        self.__did=self.__did.upper()
                                        if(self.__did[0]=="D"):
                                            if(len(self.__did)==4):
                                                q = "SELECT * FROM doc where DID = ?"
                                                cursor.execute(q,self.__did)
                                                val = cursor.fetchone()
                                                if(val != None):
                                                    if(val[2]!=None):print('Dr. '+val[1]+' '+val[2]+' '+val[3]+'\n')
                                                    else : print('Dr. '+val[1]+' '+val[3]+'\n')
                                                    input("Enter to Continue")
                                                    os.system('cls')
                                                    while (flag==0): #GENDER
                                                        self.__gender = input("Enter Gender (M for Male / F for Female / O for Others ): ")
                                                        self.__gender=self.__gender.upper()
                                                        if self.__gender in ["M","F","O"] :
                                                            #DATES
                                                            os.system('cls')
                                                            print("Date Of Birth")
                                                            self.__dob = self.date_maker()
                                                            os.system('cls')
                                                            print("Date of Admission")
                                                            self.__doa = self.date_maker()
                                                            self.__dod = None
                                                            while (flag==0): #WARD
                                                                os.system('cls')
                                                                cursor.execute('SELECT TOP 1 WARD FROM Patient ORDER BY WARD DESC;')
                                                                maxward = cursor.fetchone()[0]
                                                                self.__ward = input("Enter the Ward Number (W01 - "+maxward+"): ")
                                                                self.__ward = self.__ward.upper()
                                                                if(self.__ward[0]=="W"):
                                                                    if(len(self.__ward)==3):
                                                                        cursor.execute('select distinct(WARD) from Patient order by WARD')
                                                                        wards=[]
                                                                        tward = cursor.fetchall()
                                                                        for i in tward:wards.append(i[0])
                                                                        if self.__ward=='W00': print("W00 is Not possible, Try Again")
                                                                        if(self.__ward not in wards):
                                                                            opt=input("The Entered Ward Number is not yet have any records in Database,\nPress Y/y to Continue or Press any other button to go Back: ")
                                                                            opt=opt.upper()
                                                                            if opt in ['YES','Y']:flg=1
                                                                        if(self.__ward in wards):flg=1
                                                                        if(flg==1):
                                                                            while (flag==0): #REASON
                                                                                os.system('cls')
                                                                                self.__reason = input("Enter the Reason for Admission (CANNOT BE EMPTY) : ")
                                                                                if(len(self.__reason)>0):
                                                                                    self.__reason=self.__reason.upper()
                                                                                    q = 'INSERT INTO Patient (PNUM, FNAME, MNAME, LNAME, DID, GENDER, DOB, DOA, DOD, WARD, REASON) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
                                                                                    cursor.execute(q,self.__pid,self.__fname,self.__mname,self.__lname,self.__did,self.__gender,self.__dob,self.__doa,self.__dod,self.__ward,self.__reason)
                                                                                    cursor.commit()
                                                                                    flag=1
                                                                    else : print("Ward Number Format Error\n")
                                                                else : print("Ward Number Format Error\n")
                                                        else : print("Gender Should be Provided in the Specified Format Only (Try Again)\n")
                                                else:print("Doctor Id Not Found, Please Check and Try Again\n")
                                            else : print("Doctor Id Format Error\n")
                                        else : print("Doctor Id Format Error\n")
                                else : print("Last Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                        else : print("Middle Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                else : print("First Name Provided Contains Characters Other than Alphabets (Try Again!)\n")

            print("New Patient Entry Successful\n")
            input("Enter Any Key to Continue")
            os.system('cls')
            self.display_single(self.__pid)
            input("Enter Any Key to Continue")

        except Exception as e:
            print("Error Occured While Adding Patient Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
            return
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return

    def search_patient_pid(self):
        try:
            while True:
                try:
                    self.__pid=int(input("Enter the PID:"))
                    q=' select count(*) from Patient where PNUM=?;'
                    cursor.execute(q,self.__pid)
                    row=cursor.fetchone()
                    if row[0]==1:
                        self.display_single(self.__pid)
                        input("Enter Any Key to Continue")
                        return
                    else :
                        print("Wrong PID Entered, Try Again\n")
                        return
                except Exception as e:
                    print("Please provide a proper PID\n")
                    input("Enter To Try Again")
                    os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return



    def search_patient_name(self):
        try:
            while (True):#FNAME
                self.__fname = input("Enter the First Name (Atmost 15 Characters long): ")
                if self.string_checker(self.__fname):
                    self.__fname=self.__fname.upper()
                    while (True):#MNAME
                        self.__mname = input("Enter the Middle Name (If Any,Else Press Enter to Continue) (Atmost 15 Characters long): ")
                        if len(self.__mname) == 0 : self.__mname = 'NULL'
                        if self.string_checker(self.__mname):
                            self.__mname=self.__mname.upper()
                            if self.__mname in ['NULL','NIL','None']:self.__mname=None
                            while (True):#LNAME
                                self.__lname = input("Enter the Last Name (Atmost 15 Characters long): ")
                                if self.string_checker(self.__lname):
                                    self.__lname=self.__lname.upper()
                                    os.system('cls')
                                    if self.__mname==None:
                                        q=' select count(*) from Patient where FNAME=? AND LNAME=?;'
                                        cursor.execute(q,self.__fname,self.__lname)
                                    else:
                                        q=' select count(*) from Patient where FNAME=? AND MNAME=? AND LNAME=?;'
                                        cursor.execute(q,self.__fname,self.__mname,self.__lname)

                                    val=cursor.fetchone()

                                    if val[0]==1:
                                        os.system('cls')
                                        if self.__mname==None:
                                            q=' select PNUM from Patient where FNAME=? AND LNAME=?;'
                                            cursor.execute(q,self.__fname,self.__lname)
                                        else:
                                            q=' select PNUM from Patient where FNAME=? AND MNAME=? AND LNAME=?;'
                                            cursor.execute(q,self.__fname,self.__mname,self.__lname)
                                        row=cursor.fetchone()
                                        self.display_single(row[0])
                                        input("Enter Any Key to Continue")
                                        return

                                    elif val[0]>1:
                                        os.system('cls')
                                        list_pid=[]
                                        if self.__mname==None:
                                            q=' select * from Patient where FNAME=? AND LNAME=?;'
                                            cursor.execute(q,self.__fname,self.__lname)
                                        else:
                                            q=' select * from Patient where FNAME=? AND MNAME=? AND LNAME=?;'
                                            cursor.execute(q,self.__fname,self.__mname,self.__lname)

                                        allrow = cursor.fetchall()
                                        while True:
                                            list_pid = self.display_multiple(allrow)

                                            try:
                                                opt=int(input("Enter the PID of the Patient Between the above provided: "))
                                                if opt in list_pid:
                                                    os.system('cls')
                                                    self.display_single(opt)
                                                    input("Enter Any Key to Continue")
                                                    return
                                                else:
                                                    print("Entered PID is not matching with the above displayed records\n")
                                                    input("Enter To Try Again")
                                                    os.system('cls')
                                            except Exception as e:
                                                print("Provided PID is not the Correct\n")
                                                input("Enter To Try Again")
                                                os.system('cls')
                                    else:
                                        print("No Patient Found\n")
                                        input("Press any Button to Go Back")
                                        return
                                else : print("Last Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                        else : print("Middle Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                else : print("First Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
        except Exception as e:
            print("Error Occured While Searching Patient Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
            return
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return

    def modify_patient(self,ch):
        try:
            self.__pid=int(input("Enter the PID:"))
            q=' select count(*) from Patient where PNUM=?;'
            cursor.execute(q,self.__pid)
            row=cursor.fetchone()
            if row[0]==1:
                self.display_single(self.__pid)
                if ch==1:
                    try:
                        while (True):#FNAME
                            self.__fname = input("Enter the First Name (Atmost 15 Characters long): ")
                            if self.string_checker(self.__fname):
                                self.__fname=self.__fname.upper()
                                while (True):#MNAME
                                    self.__mname = input("Enter the Middle Name (If Any,Else Press Enter to Continue) (Atmost 15 Characters long): ")
                                    if len(self.__mname) == 0 : self.__mname = 'NULL'
                                    if self.string_checker(self.__mname):
                                        self.__mname=self.__mname.upper()
                                        if self.__mname in ['NULL','NIL','None']:self.__mname=None
                                        while (True):#LNAME
                                            self.__lname = input("Enter the Last Name (Atmost 15 Characters long): ")
                                            if self.string_checker(self.__lname):
                                                self.__lname=self.__lname.upper()
                                                q='update Patient set FNAME=?, MNAME=?, LNAME=? where PNUM=?'
                                                cursor.execute(q,self.__fname,self.__mname,self.__lname,self.__pid)
                                                cursor.commit()
                                                os.system('cls')
                                                print("NAME UPDATED SUCCESSFULLY\n")
                                                opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                                                opt=opt.upper()
                                                if opt in ['YES','Y']:
                                                    os.system('cls')
                                                    self.display_single(self.__pid)
                                                    input("Enter To Continue")
                                                    return
                                                else:
                                                    os.system('cls')
                                                    return
                                            else : print("Last Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                                    else : print("Middle Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                            else : print("First Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return

                elif ch==2:
                    try:
                        while True:
                            self.__did = input("Enter the New Doctor Id: ")
                            self.__did=self.__did.upper()
                            if(self.__did[0]=="D"):
                                if(len(self.__did)==4):
                                    q = "SELECT * FROM doc where DID = ?"
                                    cursor.execute(q,self.__did)
                                    val = cursor.fetchone()
                                    if(val != None):
                                        if(val[2]!=None):print('Dr. '+val[1]+' '+val[2]+' '+val[3]+'\n')
                                        else : print('Dr. '+val[1]+' '+val[3]+'\n')
                                        input("Enter to Continue")
                                        os.system('cls')
                                        q='update Patient set DID=? where PNUM=?'
                                        cursor.execute(q,self.__did,self.__pid)
                                        cursor.commit()
                                        os.system('cls')
                                        print("APPOINTED DOCTOR UPDATED SUCCESSFULLY\n")
                                        opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                                        opt=opt.upper()
                                        if opt in ['YES','Y']:
                                            os.system('cls')
                                            self.display_single(self.__pid)
                                            input("Enter To Continue")
                                            return
                                        else:
                                            os.system('cls')
                                            return
                                    else:print("Doctor Id Not Found, Please Check and Try Again\n")
                                else : print("Doctor Id Format Error\n")
                            else : print("Doctor Id Format Error\n")

                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return

                elif ch==3:
                    try:
                        while True:
                            self.__gender = input("Enter Gender (M for Male / F for Female / O for Others ) for Modification: ")
                            self.__gender=self.__gender.upper()
                            if self.__gender in ["M","F","O"] :
                                q='update Patient set GENDER=? where PNUM=?'
                                cursor.execute(q,self.__gender,self.__pid)
                                cursor.commit()
                                os.system('cls')
                                print("APPOINTED GENDER UPDATED SUCCESSFULLY\n")
                                opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                                opt=opt.upper()
                                if opt in ['YES','Y']:
                                    os.system('cls')
                                    self.display_single(self.__pid)
                                    input("Enter To Continue")
                                    return
                                else:
                                    os.system('cls')
                                    return
                            else : print("Gender Should be Provided in the Specified Format Only (Try Again)\n")
                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return

                elif ch==4:
                    try:
                        print("New Date Of Birth")
                        self.__dob = self.date_maker()
                        q='update Patient set DOB=? where PNUM=?'
                        cursor.execute(q,self.__dob,self.__pid)
                        cursor.commit()
                        os.system('cls')
                        print("APPOINTED DATE-OF-BIRTH UPDATED SUCCESSFULLY\n")
                        opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                        opt=opt.upper()
                        if opt in ['YES','Y']:
                            os.system('cls')
                            self.display_single(self.__pid)
                            input("Enter To Continue")
                            return
                        else:
                            os.system('cls')
                            return
                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return


                elif ch==5:
                    try:
                        print("New Date of Admission")
                        self.__doa = self.date_maker()
                        q='update Patient set DOA=? where PNUM=?'
                        cursor.execute(q,self.__doa,self.__pid)
                        cursor.commit()
                        os.system('cls')
                        print("APPOINTED DATE-OF-ADMISSION UPDATED SUCCESSFULLY\n")
                        opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                        opt=opt.upper()
                        if opt in ['YES','Y']:
                            os.system('cls')
                            self.display_single(self.__pid)
                            input("Enter To Continue")
                            return
                        else:
                            os.system('cls')
                            return

                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return

                elif ch==6:
                    try:
                        print("New Date of Discharge")
                        self.__dod = self.date_maker()
                        q='update Patient set DOD=? where PNUM=?'
                        cursor.execute(q,self.__dod,self.__pid)
                        cursor.commit()
                        os.system('cls')
                        print("APPOINTED DATE-OF-DISCHARGE UPDATED SUCCESSFULLY\n")
                        opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                        opt=opt.upper()
                        if opt in ['YES','Y']:
                            os.system('cls')
                            self.display_single(self.__pid)
                            input("Enter To Continue")
                            return
                        else:
                            os.system('cls')
                            return

                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return


                elif ch==7:
                    try:
                        while True:
                            cursor.execute('SELECT TOP 1 WARD FROM Patient ORDER BY WARD DESC;')
                            maxward = cursor.fetchone()[0]
                            self.__ward = input("Enter the New Ward Number (W01 - "+maxward+"): ")
                            self.__ward = self.__ward.upper()
                            if(self.__ward[0]=="W"):
                                if(len(self.__ward)==3):
                                    q = "SELECT * FROM Patient where WARD = ?"
                                    cursor.execute(q,self.__ward)
                                    val = cursor.fetchone()
                                    if(val != None):
                                        q='update Patient set WARD=? where PNUM=?'
                                        cursor.execute(q,self.__ward,self.__pid)
                                        cursor.commit()
                                        os.system('cls')
                                        print("APPOINTED WARD NUMBER UPDATED SUCCESSFULLY\n")
                                        opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                                        opt=opt.upper()
                                        if opt in ['YES','Y']:
                                            os.system('cls')
                                            self.display_single(self.__pid)
                                            input("Enter To Continue")
                                            return
                                        else:
                                            os.system('cls')
                                            return
                                    else:print("Ward Number Not Found, Please Check and Try Again\n")
                                else : print("Ward Number Format Error\n")
                            else : print("Ward Number Format Error\n")
                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return



                elif ch==8:
                    try:
                        while True:
                            self.__reason = input("Enter the New Reason for Admission (CANNOT BE EMPTY) : ")
                            if(len(self.__reason)>0):
                                self.__reason=self.__reason.upper()
                                q='update Patient set REASON=? where PNUM=?'
                                cursor.execute(q,self.__reason,self.__pid)
                                cursor.commit()
                                os.system('cls')
                                print("APPOINTED DATE-OF-DISCHARGE UPDATED SUCCESSFULLY\n")
                                opt=input("Press Y/y for to Display the Updated Patient Details or Press any other button to go Back: ")
                                opt=opt.upper()
                                if opt in ['YES','Y']:
                                    os.system('cls')
                                    self.display_single(self.__pid)
                                    input("Enter To Continue")
                                    return
                                else:
                                    os.system('cls')
                                    return
                    except pyodbc.Error as e:
                        print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                        input("Enter To Try Again")
                        return
            else : print("Wrong PID Entered, Try Again\n")
        except Exception as e:
                print("Please provide a proper PID\n")
                input("Enter To Try Again")
                os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return

    def date_maker(self):
        try:
            while(True):
                day = int(input("Enter the Day (1-31): "))
                if day>=1 and day<=31:
                    month = int(input("Enter the Month (1-12): "))
                    if month>=1 and month<=12:
                        if (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31) or (month in [2, 4, 6, 9, 11] and day <= 30):
                            if month==2 and day>29: print("The Day corresponding to the Month February is not possible, Try Again\n")
                            else:
                                year = int(input("Enter the Year (YYYY): "))
                                cy = datetime.now().year
                                if year>=1900 and year<=cy:
                                    is_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
                                    if (month==2 and day==29) and not is_leap_year: print("The Day Entered doesnot exists in that year as it is not a leap year, Try Again\n")
                                    else:
                                        day=str(day)
                                        month=str(month)
                                        year = str(year)
                                        if len(day)==1:
                                            day='0'+day
                                        if len(month)==1:
                                            month='0'+month

                                        d=year+'-'+month+'-'+day
                                        return d

                                else : print("Invalid Year, Try Again\n")
                        else:print("The Day corresponding to the Month provided is not possible, Try Again\n")
                    else :print("Invalid Month Provided, Try Again\n")
                else : print("Invalid Day Provided, Try Again\n")
        except Exception as e:
            print("Unexpected Value Encountered Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
            self.date_maker()



    def string_checker(self,s):
        if len(s)>0:
            if (s).isalpha():
                if (len(s)) <= 15:
                    return True
        return False


    def display_single(self,pid):
        os.system('cls')
        q = 'SELECT * FROM Patient WHERE PNUM = ?'
        cursor.execute(q,pid)
        row = cursor.fetchone()
        print("PATIENT DETAILS:\n")
        print("PID: ",row[0])
        if(row[2]!=None):
            print("Name: "+row[1]+" "+row[2]+" "+row[3])
        else:
            print("Name: "+row[1]+" "+row[3])

        if(row[5]=='M'):
            print("Gender: Male")
        elif(row[5]=='F'):
            print("Gender: Female")
        elif(row[5]=='O'):
            print("Gender: Others")

        print("Date of Bith (YYYY-MM-DD): ",row[6])
        q='SELECT DATEDIFF(year, DOB, GETDATE()) FROM Patient WHERE PNUM = ?;'
        cursor.execute(q,pid)
        age = cursor.fetchone()[0]
        print("Age: ",age)

        print()

        did = row[4]
        q = "SELECT * FROM doc where DID = ?"
        cursor.execute(q,did)
        val=cursor.fetchone();
        if(val[2]!=None):dname = 'Dr. '+val[1]+' '+val[2]+' '+val[3]
        else : dname = 'Dr. '+val[1]+' '+val[3]
        print("DID : "+row[4]+'     '+'Doctor Name: '+dname)


        print("Date of Admission : ",row[7])
        print("Date of Discharge : ",row[8])
        print("Ward Number : ",row[9])
        print("Reason For Admission : ",row[10])
        print()



    def display_multiple(self,allrow):
        format_string = "{:<6} | {:<15} | {:<15} | {:<15} | {:<2} | {:<45} | {:<20} | {:<9}"
        header=["PID","First Name","Middle Name","Last Name","Gender","Doctor","Date of Admission","Ward No."]
        print(format_string.format(header[0], header[1], header[2], header[3], header[4], header[5], header[6],header[7]))
        print('-' * 145)
        list_pid=[]
        for row in allrow:
            did = row[4]
            q = "SELECT * FROM doc where DID = ?"
            cursor.execute(q,did)
            val=cursor.fetchone();
            if(val[2]!=None):dname = 'Dr. '+val[1]+' '+val[2]+' '+val[3]
            else : dname = 'Dr. '+val[1]+' '+val[3]
            list_pid.append(row[0])
            row_string = (
                    str(row[0])[:6].ljust(6) + " | " +
                    str(row[1])[:15].ljust(15) + " | " +
                    str(row[2])[:15].ljust(15) + " | " +
                    str(row[3])[:15].ljust(15) + " | " +
                    str(row[5])[:2].ljust(6) + " | " +
                    dname[:45].ljust(45) + " | " +
                    str(row[7])[:20].ljust(20) + " | " +
                    str(row[9])[:9].ljust(9)
                )

            print(row_string)
            print()
        return list_pid


class doc:
    __did=__dfname=__dmname=__dlname=None

    def search_doc_did(self):
        try:
            while True:
                try:
                    self.__did=input("Enter the Doctor ID (Format : D000): ")
                    self.__did=self.__did.upper()
                    q=' select count(*) from doc where DID=?;'
                    cursor.execute(q,self.__did)
                    row=cursor.fetchone()
                    if row[0]==1:
                        self.display_single_doc(self.__did)
                        input("Enter Any Key to Continue")
                        return
                    else :
                        print("Wrong Doctor ID Entered, Try Again\n")
                        input("Enter Any Key to Continue")
                        return
                except Exception as e:
                    print("Please provide a proper Doctor ID\n")
                    input("Enter To Try Again")
                    os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter Any Key to Continue")
            return




    def search_doc_name(self):
        try:
            while (True):#DFNAME
                self.__dfname = input("Enter the First Name (Atmost 15 Characters long): ")
                if self.string_checker(self.__dfname):
                    self.__dfname=self.__dfname.upper()
                    while (True):#DMNAME
                        self.__dmname = input("Enter the Middle Name (If Any,Else Press Enter to Continue) (Atmost 15 Characters long): ")
                        if len(self.__dmname) == 0 : self.__dmname = 'NULL'
                        if self.string_checker(self.__dmname):
                            self.__dmname=self.__dmname.upper()
                            if self.__dmname in ['NULL','NIL','None']:self.__dmname=None
                            while (True):#DLNAME
                                self.__dlname = input("Enter the Last Name (Atmost 15 Characters long): ")
                                if self.string_checker(self.__dlname):
                                    self.__dlname=self.__dlname.upper()
                                    os.system('cls')
                                    if self.__dmname==None:
                                        q=' select count(*) from doc where DFNAME=? AND DLNAME=?;'
                                        cursor.execute(q,self.__dfname,self.__dlname)
                                    else:
                                        q=' select count(*) from doc where DFNAME=? AND DMNAME=? AND DLNAME=?;'
                                        cursor.execute(q,self.__dfname,self.__dmname,self.__dlname)

                                    val=cursor.fetchone()
                                    print(val[0])
                                    if val[0]==1:
                                        os.system('cls')
                                        if self.__dmname==None:
                                            q=' select DID from doc where DFNAME=? AND DLNAME=?;'
                                            cursor.execute(q,self.__dfname,self.__dlname)
                                        else:
                                            q=' select DID from doc where DFNAME=? AND DMNAME=? AND DLNAME=?;'
                                            cursor.execute(q,self.__dfname,self.__dmname,self.__dlname)
                                        row=cursor.fetchone()
                                        self.display_single_doc(row[0])
                                        input("Enter Any Key to Continue")

                                    elif val[0]>1:
                                        os.system('cls')
                                        if self.__dmname==None:
                                            q=' select * from doc where DFNAME=? AND DLNAME=?;'
                                            cursor.execute(q,self.__dfname,self.__dlname)
                                        else:
                                            q=' select * from doc where DFNAME=? AND DMNAME=? AND DLNAME=?;'
                                            cursor.execute(q,self.__dfname,self.__dmname,self.__dlname)

                                        allrow = cursor.fetchall()
                                        while True:
                                            list_did = self.display_multiple_doc(allrow)

                                            try:
                                                opt=input("Enter the Doctor ID Between the above provided: ")
                                                opt=opt.upper()
                                                if opt in list_did:
                                                    os.system('cls')
                                                    self.display_single_doc(opt)
                                                    input("Enter Any Key to Continue")
                                                    return
                                                else:
                                                    print("Entered Doctor ID is not matching with the above displayed records\n")
                                                    input("Enter To Try Again")
                                                    os.system('cls')
                                            except Exception as e:
                                                print("Provided Doctor ID is not the Correct\n")
                                                input("Enter To Try Again")
                                                os.system('cls')
                                    else:
                                        print("No Doctor Found\n")
                                        input("Press any Button to Go Back")
                                        return
                                else : print("Last Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                        else : print("Middle Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                else : print("First Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
        except Exception as e:
            print("Error Occured While Searching Doctor Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
            return
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return


    def avail_doc(self):
            try:
                print("Available Doctor\n")
                q='select * from dtime;'
                cursor.execute(q)
                allrow = cursor.fetchall()
                format_string = "{:<4} | {:<45} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}"
                header=["DID","Doctor Name","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
                print(format_string.format(header[0], header[1], header[2], header[3], header[4], header[5],header[6],header[7],header[8]))
                print('-' * 155)
                for row in allrow:

                    q = "SELECT * FROM doc where DID = ?"
                    cursor.execute(q,row[0])
                    val=cursor.fetchone();
                    if(val[2]!=None):dname = 'Dr. '+val[1]+' '+val[2]+' '+val[3]
                    else : dname = 'Dr. '+val[1]+' '+val[3]

                    row_string = (
                            str(row[0])[:4].ljust(4) + " | " +
                            dname[:45].ljust(45) + " | " +
                            str(row[1])[:12].ljust(12) + " | " +
                            str(row[2])[:12].ljust(12) + " | " +
                            str(row[3])[:12].ljust(12) + " | " +
                            str(row[4])[:12].ljust(12) + " | " +
                            str(row[5])[:12].ljust(12) + " | " +
                            str(row[6])[:12].ljust(12) + " | " +
                            str(row[7])[:12].ljust(12)
                        )
                    print(row_string)
                input("\nEnter Any Key to Continue")

            except pyodbc.Error as e:
                print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
                input("Enter To Try Again")
                return



    def string_checker(self,s):
        if len(s)>0:
            if (s).isalpha():
                if (len(s)) <= 15:
                    return True
        return False



    def display_multiple_doc(self,allrow):
        format_string = "{:<4} | {:<15} | {:<15} | {:<15} | {:<20} | {:<9}"
        header=["DID","First Name","Middle Name","Last Name","Field of Specialization","Date of Joining"]
        print(format_string.format(header[0], header[1], header[2], header[3], header[4], header[5]))
        print('-' * 100)
        list_did=[]
        for row in allrow:
            list_did.append(row[0])
            row_string = (
                    str(row[0])[:4].ljust(4) + " | " +
                    str(row[1])[:15].ljust(15) + " | " +
                    str(row[2])[:15].ljust(15) + " | " +
                    str(row[3])[:15].ljust(15) + " | " +
                    str(row[4])[:20].ljust(20) + " | " +
                    str(row[5])[:9].ljust(9)
                )
            print(row_string)
        print()
        return list_did




    def display_single_doc(self,did):
        os.system('cls')
        q = 'SELECT * FROM doc where DID=?;'
        cursor.execute(q,did)
        row = cursor.fetchone()
        print("DOCTOR DETAILS:\n")
        print("DID: ",row[0])
        if(row[2]!=None):
            print("Name: Dr. "+row[1]+" "+row[2]+" "+row[3])
        else:
            print("Name: Dr. "+row[1]+" "+row[3])
        print("Field of Specialization : ",row[4])
        print("Date of Joining : ",row[5])
        print()
        print("DOCTOR AVAILABLILTY\n")

        qty=' select * from dtime where DID=?;'
        cursor.execute(qty,did)
        allrow = cursor.fetchall()
        format_string = "{:<12} | {:<12} | {:<12} | {:<12} | {:<12} | {:<12}| {:<12}"
        header=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        print(format_string.format(header[0], header[1], header[2], header[3], header[4], header[5],header[6]))
        print('-' * 100)
        for row in allrow:
            row_string = (
                    str(row[1])[:12].ljust(12) + " | " +
                    str(row[2])[:12].ljust(12) + " | " +
                    str(row[3])[:12].ljust(12) + " | " +
                    str(row[4])[:12].ljust(12) + " | " +
                    str(row[5])[:12].ljust(12) + " | " +
                    str(row[6])[:12].ljust(12) + " | " +
                    str(row[7])[:12].ljust(12)
                )
            print(row_string)
        print()
        return

class nurse:

    __nid=__nfname=__nmname=__nlname__ward=None

    def search_nurse_nid(self):
        try:
            while True:
                try:
                    self.__nid=input("Enter the Nurse ID (Format : N000): ")
                    self.__nid=self.__nid.upper()
                    q=' select count(*) from nurse where NID=?;'
                    cursor.execute(q,self.__nid)
                    row=cursor.fetchone()
                    if row[0]==1:
                        self.display_single_nurse(self.__nid)
                        input("Enter Any Key to Continue")
                        return
                    else :
                        print("Wrong Nurse ID Entered, Try Again\n")
                        input("Enter Any Key to Continue")
                        return
                except Exception as e:
                    print("Please provide a proper Nurse ID\n")
                    input("Enter To Try Again")
                    os.system('cls')
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter Any Key to Continue")
            return

    def search_nurse_name(self):
        try:
            while (True):#NFNAME
                self.__nfname = input("Enter the First Name (Atmost 15 Characters long): ")
                if self.string_checker(self.__nfname):
                    self.__nfname=self.__nfname.upper()
                    while (True):#NMNAME
                        self.__nmname = input("Enter the Middle Name (If Any,Else Press Enter to Continue) (Atmost 15 Characters long): ")
                        if len(self.__nmname) == 0 : self.__nmname = 'NULL'
                        if self.string_checker(self.__nmname):
                            self.__nmname=self.__nmname.upper()
                            if self.__nmname in ['NULL','NIL','None']:self.__nmname=None
                            while (True):#NLNAME
                                self.__nlname = input("Enter the Last Name (Atmost 15 Characters long): ")
                                if self.string_checker(self.__nlname):
                                    self.__nlname=self.__nlname.upper()
                                    os.system('cls')
                                    if self.__nmname==None:
                                        q=' select count(*) from nurse where NFNAME=? AND NLNAME=?;'
                                        cursor.execute(q,self.__nfname,self.__nlname)
                                    else:
                                        q=' select count(*) from nurse where NFNAME=? AND NMNAME=? AND NLNAME=?;'
                                        cursor.execute(q,self.__nfname,self.__nmname,self.__nlname)

                                    val=cursor.fetchone()
                                    print(val[0])
                                    if val[0]==1:
                                        os.system('cls')
                                        if self.__nmname==None:
                                            q=' select NID from nurse where NFNAME=? AND NLNAME=?;'
                                            cursor.execute(q,self.__nfname,self.__nlname)
                                        else:
                                            q=' select NID from nurse where NFNAME=? AND NMNAME=? AND NLNAME=?;'
                                            cursor.execute(q,self.__nfname,self.__nmname,self.__nlname)
                                        row=cursor.fetchone()
                                        self.display_single_nurse(row[0])
                                        input("Enter Any Key to Continue")

                                    elif val[0]>1:
                                        os.system('cls')
                                        if self.__nmname==None:
                                            q=' select * from nurse where NFNAME=? AND NLNAME=?;'
                                            cursor.execute(q,self.__nfname,self.__nlname)
                                        else:
                                            q=' select * from nurse where NFNAME=? AND NMNAME=? AND NLNAME=?;'
                                            cursor.execute(q,self.__nfname,self.__nmname,self.__nlname)

                                        allrow = cursor.fetchall()
                                        while True:
                                            list_nid = self.display_multiple_nurse(allrow)

                                            try:
                                                opt=input("Enter the Nurse ID Between the above provided: ")
                                                opt=opt.upper()
                                                if opt in list_nid:
                                                    os.system('cls')
                                                    self.display_single_nurse(opt)
                                                    input("Enter Any Key to Continue")
                                                    return
                                                else:
                                                    print("Entered Nurse ID is not matching with the above displayed records\n")
                                                    input("Enter To Try Again")
                                                    os.system('cls')
                                            except Exception as e:
                                                print("Provided Nurse ID is not the Correct\n")
                                                input("Enter To Try Again")
                                                os.system('cls')
                                    else:
                                        print("No Nurse Found\n")
                                        input("Press any Button to Go Back")
                                        return
                                else : print("Last Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                        else : print("Middle Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
                else : print("First Name Provided Contains Characters Other than Alphabets (Try Again!)\n")
        except Exception as e:
            print("Error Occured While Searching Nurse Try Again ! Error Code : ",e.args[0])
            input("Enter To Try Again")
            os.system('cls')
            return
        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter To Try Again")
            return


    def nurse_ward(self):
        try:
            cursor.execute('SELECT TOP 1 WARD FROM nurse ORDER BY WARD DESC;')
            maxward = cursor.fetchone()[0]
            self.__ward = input("Enter the Ward Number (W01 - "+maxward+"): ")
            self.__ward = self.__ward.upper()
            if(self.__ward[0]=="W"):
                if(len(self.__ward)==3):
                    q = "SELECT * FROM nurse where WARD = ?"
                    cursor.execute(q,self.__ward)
                    val = cursor.fetchone()
                    if(val != None):
                        print("\nNurses Under Ward: "+self.__ward+'\n')
                        q = 'SELECT * FROM nurse where WARD=?;'
                        cursor.execute(q,self.__ward)
                        allrow = cursor.fetchall()
                        for row in allrow:
                            if(row[2]!=None):
                                nname= row[1]+" "+row[2]+" "+row[3]
                            else:
                                nname = row[1]+" "+row[3]
                            print("NID: ",row[0],"  |  ","Name: ",nname)
                            print()

                        input("Enter Any Key to Continue")

                    else:
                        print("Ward Number Not Found, Please Check and Try Again\n")
                        input("Enter Any Key to Try Again")
                else :
                    print("Ward Number Format Error\n")
                    input("Enter Any Key to Try Again")
            else :
                print("Ward Number Format Error\n")
                input("Enter Any Key to Try Again")

        except pyodbc.Error as e:
            print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
            input("Enter Any Key to Continue")
            return


    def display_multiple_nurse(self,allrow):
        list_nid=[]
        format_string = "{:<4} | {:<15} | {:<15} | {:<15} | {:<13} | {:<9}"
        header=["NID","First Name","Middle Name","Last Name","Assigned Ward","Date of Joining"]
        print(format_string.format(header[0], header[1], header[2], header[3], header[4], header[5]))
        print('-' * 100)
        for row in allrow:
            list_nid.append(row[0])
            row_string = (
                        str(row[0])[:4].ljust(4) + " | " +
                        str(row[1])[:15].ljust(15) + " | " +
                        str(row[2])[:15].ljust(15) + " | " +
                        str(row[3])[:15].ljust(15) + " | " +
                        str(row[4])[:3].ljust(13) + " | " +
                        str(row[5])[:9].ljust(9)
                    )
            print(row_string)
        print()
        return list_nid

    def display_single_nurse(self,nid):
        os.system('cls')
        q = 'SELECT * FROM nurse where NID=?;'
        cursor.execute(q,nid)
        row = cursor.fetchone()
        print("NURSE DETAILS:\n")
        print("NID: ",row[0])
        if(row[2]!=None):
            print("Name: "+row[1]+" "+row[2]+" "+row[3])
        else:
            print("Name: "+row[1]+" "+row[3])
        print("Assigned Ward : ",row[4])
        print("Date of Joining : ",row[5])
        print()
        return

    def string_checker(self,s):
        if len(s)>0:
            if (s).isalpha():
                if (len(s)) <= 15:
                    return True
        return False



try:
    try:
        os.system('cls')
        fpath='server_database.log'
        fob=open(fpath,'r')
        s=(fob.read()).split(',')
        server=s[0]
        db=s[1]
        path = "DRIVER={SQL Server};SERVER=" + server + ";DATABASE="+db  # server = Bana\SQLEXPRESS  db=master
        conn = pyodbc.connect(path)
        print("SERVER CONNECTED SUCCESSFULLY")
        t = 2
        time.sleep(t)
    except:
        os.system('cls')
        print("One-Time Process")
        try:
            server = input("Enter the MSSQL Server Name : ")
            db = input("Enter the Database Name (Where the tables are loaded): ")
            s=server+','+db
            path = "DRIVER={SQL Server};SERVER=" + server + ";DATABASE="+db  # server = Bana\SQLEXPRESS  db=master
            conn = pyodbc.connect(path)
            print("SERVER CONNECTED SUCCESSFULLY")
            t = 2
            time.sleep(t)
        except pyodbc.Error as e:
            os.system('cls')
            print("Error Connecting Server: \nError Code: ",e.args[0])
            print('\nError: SQL Server does not exist or access denied')
            t = 2
            time.sleep(t)
            exit(0)
        fpath='server_database.log'
        fob=open(fpath,'w+')
        fob.write(s)
        fob.flush()
    cursor = conn.cursor()
    usr = usr_pwd()
    while True:
        try:
            os.system('cls')
            print("Hospital Management System")
            print("1. SIGN UP (Register)")
            print("2. SIGN IN (LOG IN)")
            print("3. FORGOT PASSWORD? ")
            print("4. EXIT ")
            c = int(input("Enter the Option No."))
            if c == 1:
                os.system('cls')
                usr.new_user()
                os.system('cls')
            elif c == 2:
                os.system('cls')
                flag=usr.old_user()
                if(flag==1):
                    p=patient()
                    d=doc()
                    n=nurse()
                    while True:
                        try:
                            os.system('cls')
                            print(" 1) Patient")
                            print(" 2) Doctors")
                            print(" 3) Nurses")
                            print(" 4) Exit")
                            ch=int(input("ENTER YOUR CHOICE : "))
                            if ch==1:

                                while True:

                                    try:
                                        os.system('cls')
                                        print(" 1) New Patient Entry")
                                        print(" 2) Search Patient")
                                        print(" 3) Modification of Existing Patient")
                                        print(" 4) Exit")
                                        ch=int(input("ENTER YOUR CHOICE : "))
                                        if ch==1:
                                            os.system('cls')
                                            p.add_patient()
                                            os.system('cls')
                                        elif ch==2:
                                            while True:
                                                try:
                                                    os.system('cls')
                                                    print(" 1) Search with Patient Id")
                                                    print(" 2) Search with Patient Name")
                                                    print(" 3) Back")
                                                    ch=int(input("ENTER YOUR CHOICE : "))
                                                    if ch==1:
                                                        os.system('cls')
                                                        p.search_patient_pid()
                                                        os.system('cls')
                                                    elif ch==2:
                                                        os.system('cls')
                                                        p.search_patient_name()
                                                        os.system('cls')
                                                    elif ch==3:break
                                                    else:
                                                        print("Wrong Option\n")
                                                        input("Enter Any Key to Continue")
                                                        os.system('cls')
                                                except Exception :
                                                    print("Invalid Input\n")
                                                    input("Enter Any Key to Continue")
                                                    os.system('cls')
                                        elif ch==3:
                                            while True:
                                                try:
                                                    os.system('cls')
                                                    print(" 1) Change Patient Name")
                                                    print(" 2) Change Patient Appointed Doctor")
                                                    print(" 3) Change Patient Gender")
                                                    print(" 4) Change Patient Date of Birth")
                                                    print(" 5) Change Patient Date of Admission")
                                                    print(" 6) Change Patient Date of Discharge")
                                                    print(" 7) Change Patient Ward Number")
                                                    print(" 8) Change Patient Reason of Admission")
                                                    print(" 9) Back")
                                                    ch=int(input("ENTER YOUR CHOICE : "))
                                                    if ch==1:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==2:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==3:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==4:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==5:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==6:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==7:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==8:
                                                        os.system('cls')
                                                        p.modify_patient(ch)
                                                        os.system('cls')
                                                    elif ch==9:break
                                                    else:
                                                        print("Wrong Option\n")
                                                        input("Enter Any Key to Continue")
                                                        os.system('cls')
                                                except Exception :
                                                    print("Invalid Input\n")
                                                    input("Enter Any Key to Continue")
                                                    os.system('cls')


                                        elif ch==4:break
                                        else:
                                            print("Wrong Option\n")
                                            input("Enter Any Key to Continue")
                                            os.system('cls')
                                    except Exception :
                                        print("Invalid Input\n")
                                        input("Enter Any Key to Continue")
                                        os.system('cls')




                            elif ch==2:
                                while True:
                                    try:
                                        os.system('cls')
                                        print(" 1) Search with Doctor Id")
                                        print(" 2) Search with Doctor by Name")
                                        print(" 3) All Available Doctors")
                                        print(" 4) Back")
                                        ch=int(input("ENTER YOUR CHOICE : "))
                                        if ch==1:
                                            os.system('cls')
                                            d.search_doc_pid()
                                            os.system('cls')
                                        elif ch==2:
                                            os.system('cls')
                                            d.search_doc_name()
                                            os.system('cls')
                                        elif ch==3:
                                            os.system('cls')
                                            d.avail_doc()
                                            os.system('cls')
                                        elif ch==4:break
                                        else:
                                            print("Wrong Option\n")
                                            input("Enter Any Key to Continue")
                                            os.system('cls')
                                    except Exception :
                                        print("Invalid Input\n")
                                        input("Enter Any Key to Continue")
                                        os.system('cls')


                            elif ch==3:
                                while True:
                                    try:
                                        os.system('cls')
                                        print(" 1) Search with Nurse Id")
                                        print(" 2) Search with Nurse by Name")
                                        print(" 3) Nurses According to Ward Number")
                                        print(" 4) Back")
                                        ch=int(input("ENTER YOUR CHOICE : "))
                                        if ch==1:
                                            os.system('cls')
                                            n.search_nurse_nid()
                                            os.system('cls')
                                        elif ch==2:
                                            os.system('cls')
                                            n.search_nurse_name()
                                            os.system('cls')
                                        elif ch==3:
                                            os.system('cls')
                                            n.nurse_ward()
                                            os.system('cls')
                                        elif ch==4:break
                                        else:
                                            print("Wrong Option\n")
                                            input("Enter Any Key to Continue")
                                            os.system('cls')
                                    except Exception :
                                        print("Invalid Input\n")
                                        input("Enter Any Key to Continue")
                                        os.system('cls')

                            elif ch==4:
                                os.system('cls')
                                msg = "Logout Successful"
                                t = 1
                                print(msg)
                                time.sleep(t)
                                break
                            else:
                                print("Wrong Option\n")
                                input("Enter Any Key to Continue")
                                os.system('cls')
                        except Exception :
                            print("Invalid Input\n")
                            input("Enter Any Key to Continue")
                            os.system('cls')
                os.system('cls')

            elif c == 3:
                os.system('cls')
                usr.set_pass()
                os.system('cls')
            elif c == 4:
                os.system('cls')
                print("Exited Program Successfully")
                break
            else:
                print("Wrong Option\n")
                input("Enter Any Key to Continue")
                os.system('cls')
        except Exception :
            print("Invalid Input\n")
            input("Enter Any Key to Continue")
            os.system('cls')





except pyodbc.Error as e:
    print("SERVER CONNECTION ERROR : Error Code :", e.args[0])
except pyodbc.Error as ex:
    if ex.args[0] == '08001':
        print("DATABASE CONNECTION ERROR (CHECK DATABASE SERVER NAME!!)")
except Exception as e:
    print(e)
finally:
    try:
        cursor.close()
    except NameError:
        pass
    try:
        conn.close()
    except NameError:
        pass
    os.system(exit(0))
