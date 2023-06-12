friend_ages = {"Rolf": 24, "Adam": 45, "Anne": 35}

print(friend_ages)

friend_ages['Abdi'] = 26


for friend, ages in friend_ages.items():
    print(friend, ages)

for friend in friend_ages:
    print(f"{friend}: {friend_ages[friend]}")

if "Adam" in friend_ages:
    print(f"my friend Adam with this age {friend_ages['Adam']}")
else:
    print("Adam is not a friend")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"name: {name}, Age: {age}, Profession: {profession}")
print("=========================")
for person in people:
    print(f"name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")