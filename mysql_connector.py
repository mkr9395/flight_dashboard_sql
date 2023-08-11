# pip install mysql.connector

import mysql

import pandas as pd

from mysql import connector as c
from mysql.connector import Error



try:
    conn = c.connect(host="localhost",user="root",password="mohit@123",database='flights')
    if conn.is_connected():
        cursor = conn.cursor()
        print("succesfully connected")
        
        ##  create a database
        # cursor.execute("CREATE DATABASE flights;")
        # conn.commit()
        
        ## select database
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        
        # creating table airport to add the data in the table.
        table_name = "flights_data"
        
        cursor.execute(f'DROP TABLE IF EXISTS {table_name};')
        print('Creating table....')
        

        # creating structure of table
        create_table_query = f"""
        CREATE TABLE {table_name}(
            airline VARCHAR(255),
            date_of_journey DATE,
            source VARCHAR(255),
            destination VARCHAR(255),
            route VARCHAR(255),
            dep_time TIME,
            duration INT,
            total_stops VARCHAR(255),
            price INT
            );"""
        
        cursor.execute(create_table_query)
        print("Table is created....")
        
        # loading the CSV file into a pandas DataFrame
        df = pd.read_csv(r"D:\SQL\data\flights_cleaned - flights_cleaned.csv")
        
        # removing duplicates
        df.dropna(inplace=True)


        # converting date_of_journey and dep_time columns to datetime format
        df['date_of_journey'] = pd.to_datetime(df['date_of_journey'], format='%d-%m-%Y')
        df['dep_time'] = pd.to_datetime(df['dep_time'])

        
        # iterating through the dataFrame and inserting rows into the mysql table
        for index, row in df.iterrows():
            insert_query = f"""INSERT INTO {table_name} (airline, date_of_journey, source, destination, route, dep_time, duration, total_stops, price)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
            cursor.execute(insert_query, tuple(row))
    
            print("Record inserted")
    
            conn.commit()


except Error as e:
    print("Error while connecting to MySQL", e)

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("connection closed")