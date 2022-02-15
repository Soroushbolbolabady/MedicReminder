from datetime import date, datetime , timedelta
import sqlite3
import re


start_date = datetime.now()


def reminder(use : str,time : datetime , repeat : int , time_to_use : int):
    #starting from here
    yet_hour = time.strftime("%H")
    yet_minute = time.strftime("%M")

    #conver str to useful format
    use_time = re.findall("[\d*]" , use)
    clock_use = time.replace(hour = int(use_time[0]), minute = int(use_time[2]))
    hour = clock_use.strftime("%H")
    minute = clock_use.strftime("%M")



    #Database 
    sqlconnection = sqlite3.connect('sql.db')

    cursor = sqlconnection.cursor()

    cursor.execute("DROP TABLE IF EXISTS REMINDER")

    table = """ CREATE TABLE REMINDER (
                Date TEXT NOT NULL
            ); """    
    cursor.execute(table)
    for i in range(0,5):
        tmp_date = clock_use + timedelta(hours = repeat)
        string_date = tmp_date.strftime("%H:%M:%S")
        sqlconnection.execute("INSERT INTO REMINDER (Date) VALUES (?)",(string_date,))

    statement = '''SELECT * FROM REMINDER'''
    cursor.execute(statement)
    output = cursor.fetchall()
    outputsql = []
    for i in output:
        outputsql.append(output)
    
    sqlconnection.commit()


    #main logic
    if int(yet_hour) == int(hour):
        if int(yet_minute) - int(minute) == time_to_use:
            return {"send_it" : datetime.now(), 
                    "next" : outputsql}


    sqlconnection.close()





