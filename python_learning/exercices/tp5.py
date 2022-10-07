names = ["Smith", "Doe", "Jones", "Williams", "Brown"]
short_names = []
long_names = []

for name in names:
    if len(name) >= 6:
        long_names.append(name)
    else:
        short_names.append(name)

print(f"Short names: {short_names}")
print(f"Long names: {long_names}")