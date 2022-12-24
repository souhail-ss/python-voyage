from flight_map import FlightMap 

fm = FlightMap()
fm.import_airports('airports.csv')
fm.import_flights('flights.csv')

# affiche la liste des aéroports
# print(*fm.airports ,sep = "\n")

# # affiche la liste des vols

# print(*fm.flights,sep = "\n")

# Recherches simple d'aéroport 


print(str(fm.airport_find("JFK")))
# print(fm.flight_exist("AKL", "CPT2"))
# print(str(fm.flights_where("SIN")))
# print(fm.airports_from("SIN"))





