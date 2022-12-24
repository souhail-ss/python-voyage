from flight_map import FlightMap 

fm = FlightMap()
fm.import_airports('airports.csv')
fm.import_flights('flights.csv')

        # D -- affiche la liste des aéroports

# print(*fm.airports ,sep = "\n")

        # D -- affiche la liste des vols

# print(*fm.flights,sep = "\n")

        # E --- Recherches simple d'aéroport 

print(str(fm.airport_find("LAX")))

        # F ---- Vol direct entre deux aéroports


# print(fm.flight_exist("LAX", "SFO"))

        # ---- G Recherche des vols et aéroports accessibles à partir d'un aéroport donné

# print(fm.flights_where("MIA"))


# print(str(fm.airports_from("CDG")))






