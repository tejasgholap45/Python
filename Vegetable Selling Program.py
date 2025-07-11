vegetables = {
    "Tomato": 20,
    "Potato": 15,
    "Onion": 25,
    "Carrot": 30
}
total = 0
print("Available Vegetables (per kg):")
for veg, price in vegetables.items():
    print(f"{veg}: ₹{price}")
while True:
    choice = input("\nEnter vegetable name to buy (or 'done' to finish): ").title()
    if choice == "Done":
        break
    if choice in vegetables:
        kg = float(input(f"How many kg of {choice}? "))
        total += vegetables[choice] * kg
    else:
        print("Sorry, not available.")
print(f"\nTotal Bill: ₹{total}")
