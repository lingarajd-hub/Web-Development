# ================================
# SHOPPING DISCOUNT CALCULATOR
# ================================

# ---------- PART 1: retry loop ----------
valid = False

while not valid:

    # ---------- PART 2: input and calculation ----------
    try:
        bill = float(input("Enter the bill amount: "))
        discount = float(input("Enter the discount percentage: "))
        people = int(input("Enter the number of people: "))

        discount_amount = bill * discount / 100
        final_bill = bill - discount_amount
        each_person = final_bill / people

    # ---------- PART 3: handle errors ----------
    except ValueError:
        print("Please enter numbers only.")

    except ZeroDivisionError:
        print("The number of people cannot be 0.")

    # ---------- PART 4: else and finally ----------
    else:
        print("Final bill:", final_bill)
        print("Each person pays:", each_person)
        valid = True

    finally:
        print("Attempt finished.")