from typing import List
import csv
from airports import Airport
from flight import Flight




class FlightMap:
    def __init__(self):
        self.airports = []
        self.flights = []
    
    def import_airports(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f, delimiter=' ', quotechar='"')
            next(reader)  
            for row in reader:
                name, code, lat, long = row

                lat, long = float(lat.replace(","," ")), float(long)
                code=code.replace(",","")
                airport = Airport(name, code, lat, long)
                self.airports.append(airport)

           
    
    def import_flights(self, csv_file: str) -> None:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f, delimiter=' ', quotechar='"')
            next(reader)  
            for row in reader:
                src_code, dst_code, duration = row
                src_code,dst_code=src_code.replace(",",""),dst_code.replace(",","")
                duration = float(duration)
                flight = Flight(src_code, dst_code, duration)
                self.flights.append(flight)
    
    # liste des aéroports
    
    
    def airports(self):
        return self.airports
    
    def flights(self):
        return self.flights
    
    # Recherches simple d'aéroport
    
    def airport_find(self, airport_code: str) -> Airport:
        
        for airport in self.airports:
            
            if airport.code == airport_code:
                return airport
            
        return None
    
    # Vol direct entre deux aéroports
    
    def flight_exist(self,src_airport_code: str, dst_airport_code: str)-> bool :   
    
        for flight in self.flights:
            # print(src_airport_code+" : "+flight.src_code+" / "+ dst_airport_code+" : "+flight.dst_code)
            if flight.src_code == src_airport_code and flight.dst_code == dst_airport_code :
                return True
        return False
    
    def flights_where(self,airport_code: str) -> list[Flight]:
        results = []
        for flight in self.flights:
            if flight.src_code == airport_code:
               results.append(flight)
                
        return results
    
    def airports_from(self,airport_code: str) -> list[Airport]:
        results = []
        FiltredFlights = self.flights_where(airport_code) 
        for FiltredFlight in FiltredFlights:
            airport = self.airport_find(FiltredFlight.dst_code)
            if airport !=  None : 
                results.append(airport)
                
        return results