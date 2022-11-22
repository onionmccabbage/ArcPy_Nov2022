cities = ["Alameda", "Brazos", "Chimayo", "Dulce"]
len(cities)

del cities[2]
print(cities)

cities.sort(reverse = True) 
print(cities)
print("Zuni" in cities) # False

cities.append("Zuni") # ok now it exists
print(cities)

cities.insert(0,"Espanola") # insert at position zero
print(cities)   