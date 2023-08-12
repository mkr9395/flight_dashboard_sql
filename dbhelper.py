import mysql
from mysql import connector as c
from mysql.connector import Error

class DB:
    def __init__(self):
        # connect to database
        
        try:
            self.conn = c.connect(host="localhost",user="root",password="mohit@123",database='flights')
            if self.conn.is_connected():
                self.cursor = self.conn.cursor()
                print("succesfully connected")
            
            
                ## select database
                self.cursor.execute("select database();")
                self.record = self.cursor.fetchone()
                print("You're connected to database: ", self.record)
                
        except Error as e:
            print("Error while connecting to MySQL", e)
            
            
                
    def fetch_city_names(self):
        
        self.cursor.execute("""
                            SELECT DISTINCT(destination) FROM flights.flights_data
                            UNION
                            SELECT DISTINCT(source) FROM flights.flights_data
                            """)
        data = self.cursor.fetchall()
        
        print(data)     
        
        cities = [] # as the city names are in tuple, need to extract it
        
        for item in data:
            cities.append(item[0])
            
        return cities 
    
    def fetch_all_flights(self,source_city,destination_city):
        
        self.cursor.execute(f"""
                            SELECT airline,source,destination,route,duration,dep_time,price
                            FROM flights.flights_data as f
                            WHERE f.source = '{source_city}' AND f.destination = '{destination_city}'
                            """) 
        
        data = self.cursor.fetchall()
        return data
    
    
    def fetch_airline_frequency(self):
        
        airline_name=[]
        frequency = []
        
        self.cursor.execute(f"""
                            SELECT airline,COUNT(airline)
                            FROM flights.flights_data as f
                            GROUP BY airline,source,destination""")
        data = self.cursor.fetchall()
        
        for item in data:
            airline_name.append(item[0])
            frequency.append(item[1])
            
        return airline_name,frequency
    
    
    def busy_airport(self):
        
        self.cursor.execute(f"""
                            SELECT t.source, count(*) from (SELECT source from flights.flights_data
                                                            UNION ALL
                                                            SELECT destination FROM flights.flights_data)t
                            GROUP BY t.source
                            ORDER BY count(*) DESC;
                            """)
        data = self.cursor.fetchall()
        
        city_name=[]
        freq = []
        
        for item in data:
            city_name.append(item[0])
            freq.append(item[1])
            
        return city_name,freq