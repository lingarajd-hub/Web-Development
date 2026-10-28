# PART 1: Show the people that took the test 
items = ["rex"]
score_count = [92 ,93 ,86 ,95 ,83]

# PART 2: Pair people with score counts into a dictionary
inventory = {item: count for item, count in zip(items, score_count)}
print("all marks:", all)

# PART 3: Show only the top 3 people with the highest score
score_count__items = [item for item in items if inventory[item] < 86]
print("Top 3 Scores:", score_count)

# PART 4: Ask the computer who has the highest score
chosen_item = input("What is the highest score? ")

# PART 5: Ask the computer who has the lowest score
chosen_item = input("What is the lowest score? ")

# PART 6: Show the computer the highest and lowest scores
prices = [92, 93, 86, 95, 83]
