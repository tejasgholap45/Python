balance = 1000

while balance > 0:
    print(f"\nCurrent balance: ₹{balance}")
    amount = int(input("Enter amount to withdraw: ₹"))
    if amount <= balance:
       balance -= amount
       print(f"Withdrawal successful! Remaining balance: ₹{balance}")
    else:
        print("Insufficient balance! Try a smaller amount.")

    print("Thank You Visit Again...!")
    break
