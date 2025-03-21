def process_sensor_data(filename):
    try:
        with open(filename, "r") as file:
            values = [int(line.strip()) for line in file]
        
        if not values:
            print("Súbor neobsahuje žiadne dáta.")
            return
        
        max_value = max(values)
        min_value = min(values)
        avg_value = sum(values) / len(values)
        
        print(max_value)
        print(min_value)
        print(f"{avg_value:.2f}")
    
    except FileNotFoundError:
        print("Chyba: Súbor nebol nájdený.")
    except ValueError:
        print("Chyba: Súbor obsahuje neplatné dáta.")

if __name__ == "__main__":
    filename = input("Zadajte názov súboru: ")
    process_sensor_data(filename)
