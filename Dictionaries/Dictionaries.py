car = {"Brand" : "BMW", "Model" : "M5", "Year" : "2018"}
print(f"Model: {car["Model"]}")
print(f"Mileage: {car.get("Mileage", "Mileage not found")}")
for c in car.values():
    print(c)
for k, c in car.items():
    print(f"{k}: {c}")

