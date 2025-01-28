def main():
    # Krok 1: Načítanie názvu súboru
    filename = input("Zadajte názov súboru: ")

    try:
        # Krok 2: Otvorenie súboru a načítanie dát
        with open(filename, "r") as file:
            data = [int(line.strip()) for line in file.readlines()]

        # Krok 3: Výpočty
        if len(data) == 0:
            print("Súbor je prázdny.")
        else:
            max_value = max(data)
            min_value = min(data)
            average = sum(data) / len(data)

            # Krok 4: Výpis výsledkov
            print(f"Maximálna hodnota: {max_value}")
            print(f"Minimálna hodnota: {min_value}")
            print(f"Priemer hodnôt: {average:.2f}")
    
    except FileNotFoundError:
        print(f"Súbor '{filename}' neexistuje.")
    except ValueError:
        print("Súbor obsahuje neplatné dáta (necelé čísla).")
    except Exception as e:
        print(f"Došlo k chybe: {e}")

if __name__ == "__main__":
    main()
