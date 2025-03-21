def file_statistics(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_words = sum(len(line.split()) for line in lines)
            num_chars = sum(len(line) for line in lines)
        
        print(num_lines)
        print(num_words)
        print(num_chars)
    
    except FileNotFoundError:
        print("Chyba: Súbor nebol nájdený.")
    except Exception as e:
        print(f"Chyba: {e}")

if __name__ == "__main__":
    filename = input("Zadajte názov súboru: ")
    file_statistics(filename)
