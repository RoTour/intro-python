import random
juneTemperatures = []
temperatures = {}

for i in range(30):
    juneTemperatures.append(random.randint(20, 40))

print(f"Temperature for June: {juneTemperatures}")

for temp in juneTemperatures:
    key = f"{temp}°C"
    if temperatures.get(key) is None:
        temperatures[key] = 0
    temperatures[key] += 1

for key in sorted(temperatures.keys()):
    print(f"{key}: {temperatures.get(key)}")
