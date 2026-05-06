def calculate_risk(lethality, homelessness, economy):
    # This formula weights death toll highest (40%), followed by homes and money (30% each)
    score = (lethality * 0.4) + (homelessness * 0.3) + (economy * 0.3)
    return round(score, 1)

# Rank hazards on a scale of 1-10 for each category
hazards = [
    {"name": "Tsunami", "lethality": 9, "homeless": 8, "econ": 9},
    {"name": "Earthquake", "lethality": 7, "homeless": 9, "econ": 8},
    {"name": "Landslides", "lethality": 6, "homeless": 4, "econ": 3},
    {"name": "Flooding", "lethality": 3, "homeless": 5, "econ": 4}
]

print("--- Lebu Hazard Priority Rankings ---")
# Calculate and sort hazards by highest risk score
results = []
for h in hazards:
    score = calculate_risk(h["lethality"], h["homeless"], h["econ"])
    results.append((h["name"], score))

results.sort(key=lambda x: x[1], reverse=True)

for rank, (name, score) in enumerate(results, 1):
    print(f"{rank}. {name}: {score}/10")
