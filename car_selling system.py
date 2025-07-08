cars = [
    {"id": 1, "brand": "Toyota", "model": "Corolla", "price": 8000},
    {"id": 2, "brand": "Honda", "model": "Civic", "price": 9000},
    {"id": 3, "brand": "Ford", "model": "Focus", "price": 7500}
]

def show_cars():
    print("\nAvailable Cars:")
    for car in cars:
        print(f"{car['id']}. {car['brand']} {car['model']} - ${car['price']}")

def sell_car(car_id):
    for car in cars:
        if car["id"] == car_id:
            print(f"\nSold: {car['brand']} {car['model']} for ${car['price']}")
            cars.remove(car)
            return
    print("Car not found!")

while True:
    show_cars()
    choice = input("\nEnter car ID to buy (or 'q' to quit): ")
    if choice.lower() == 'q':
        print("Thank you for visiting!")
        break
    sell_car(int(choice))
