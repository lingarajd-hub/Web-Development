# ================================
# DAILY ACTIVITY PLANNER
# ================================

# ---------- PART 1: homework time ----------
homework_time = int(input("How many minutes is your homework? "))

# ---------- PART 2: choose a plan ----------
if homework_time > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

# ---------- PART 3: free time ----------
free_time = input("Is there free time after homework? (yes/no) ")

if free_time == "yes":
    print("Remember to pick a hobby.")

# ---------- PART 4: summary ----------
print("===== DAILY PLAN =====")
print("Homework minutes:", homework_time)
print("Plan:", plan)
print("Free time:", free_time)