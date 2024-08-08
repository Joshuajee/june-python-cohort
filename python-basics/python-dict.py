car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2009,
    "doors": 4,
}

print(car["doors"])
print(car["model"])

car["year"] = 2015
car["speed"] = 200

print(car)

car.update({"year": 2018, "engine": 200})

print(car)

car.pop("speed")

print(car)

car.update({"engine": { "cycl": "v6", "power": 200 }})

print(car)

print(car["engine"])

print(car.get("doors"))

print(car.get("engine").get("power"))

print(car.items())

for x in car.items():
    print(x[0], x[1])
    
print(car.keys())

print(car.values())

car.popitem()

print(car)

car.popitem()

print(car)