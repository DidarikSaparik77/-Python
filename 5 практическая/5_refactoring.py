def calculate_trip():
    PRICE_PER_LITER = 49.5
    
    distance = float(input("Какое расстояние (км)? "))
    fuel_per_100km = float(input("Сколько литров на 100 км ест машина? "))
    
    
    total_liters = distance * (fuel_per_100km / 100)
    total_price = total_liters * PRICE_PER_LITER
    
    
    print("\nHyжнo бензина:")
    print(f"{total_liters:.2f} литров")
    print("Стоимость:")
    print(f"{total_price:.2f} рублей")

calculate_trip()