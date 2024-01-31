import json
import os

class BilingualDictionary:
    def __init__(self):
        self.dictionaries = {}
        
    def list_dictionaries(self):
        print("Rendelkezésre álló szótárak:")
        for dictionary_type in self.dictionaries:
            print(f"- {dictionary_type}")


    def create_dictionary(self):
        choice = input("Szeretne új szótárt létrehozni (1) vagy meglévőt betölteni (2)? Válasszon (1/2): ").strip()

        if choice == "1":
            dictionary_type = input("Adja meg a szótár típusát (pl. angol_magyar): ")
            self.dictionaries[dictionary_type] = {}
            print(f"{dictionary_type} szótár létrehozva.")
        elif choice == "2":
            dictionary_type = input("Adja meg a szótár típusát: ")
            file_path = f"D:\\My staff\\Python\\Januar\\Vizsga_febr_01\\{dictionary_type}.json"

            if os.path.exists(file_path) and os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    try:
                        loaded_dictionary = json.load(file)
                        self.dictionaries[dictionary_type] = loaded_dictionary
                        print(f"{dictionary_type} szótár betöltve a fájlból.")
                    except json.JSONDecodeError:
                        print("Hiba történt a fájl betöltése közben. Ellenőrizze a fájl formátumát.")
            else:
                print("A megadott fájl nem található vagy nem egy fájl.")





    def add_word(self):
        self.list_dictionaries()
        dictionary_type = input("Válassza ki a szótárt: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return

        language_prompt = self.get_language_prompts(dictionary_type)
        english_word = input(f"Adjon meg egy {language_prompt['source']} szót: ")
        translation = input(f"Adja meg a {language_prompt['target']} fordítást: ")
        definition = input("Adja meg a definíciót: ")

        if english_word in self.dictionaries[dictionary_type]:
            self.dictionaries[dictionary_type][english_word].append({
                "translation": translation,
                "definition": definition
            })
        else:
            self.dictionaries[dictionary_type][english_word] = [{
                "translation": translation,
                "definition": definition
            }]

        print(f"{english_word} hozzáadva a szótárhoz.")



    def get_language_prompts(self, dictionary_type):
        if "angol" in dictionary_type.lower() and "magyar" in dictionary_type.lower():
            return {"source": "angol", "target": "magyar"}
        elif "hun" in dictionary_type.lower() and "eng" in dictionary_type.lower():
            return {"source": "magyar", "target": "angol"}
        elif "englisch" in dictionary_type.lower() and "deutsch" in dictionary_type.lower():
            return {"source": "angol", "target": "német"}
        elif "german" in dictionary_type.lower() and "english" in dictionary_type.lower():
            return {"source": "német", "target": "angol"}
        else:
            print("nincs ilyen szótár")
        
    
        
    
    def list_words(self):
        self.list_dictionaries()  # Új sor hozzáadva
        dictionary_type = input("Válassza ki a szótárt: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return

        print(f"Szavak a(z) {dictionary_type} szótárban:")
        for word in self.dictionaries[dictionary_type]:
            print(f"- {word}")
    

    def replace_definition(self):
        dictionary_type = input("Adja meg a szótár típusát: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return
        language_prompt = self.get_language_prompts(dictionary_type)
        
        english_word = input(f"Adja meg az {language_prompt['source']} szót, amelynek definícióját szeretné cserélni: ")

        if english_word in self.dictionaries[dictionary_type]:
            new_definition = input("Adja meg az új definíciót: ")
            self.dictionaries[dictionary_type][english_word][0]["definition"] = new_definition
            print(f"A(z) {english_word} definíciója cserélve.")
        else:
            print(f"A(z) {english_word} szó nem található a szótárban.")

    def delete_word(self):
        dictionary_type = input("Adja meg a szótár típusát: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return
        language_prompt = self.get_language_prompts(dictionary_type)
        english_word = input(f"Adja meg az {language_prompt['source']} szót, amelyet törölni szeretne: ")

        if english_word in self.dictionaries[dictionary_type]:
            del self.dictionaries[dictionary_type][english_word]
            print(f"A(z) {english_word} szó és definíciói törölve.")
        else:
            print(f"A(z) {english_word} szó nem található a szótárban.")

    def search_definition(self):
        dictionary_type = input("Adja meg a szótár típusát: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return
        language_prompt = self.get_language_prompts(dictionary_type)
        english_word = input(f"Adja meg az {language_prompt['source']} szót, amelynek definícióját szeretné keresni: ")

        if english_word in self.dictionaries[dictionary_type]:
            print(f"{english_word} definíciója: {self.dictionaries[dictionary_type][english_word][0]['definition']}")
        else:
            print(f"A(z) {english_word} szó nem található a szótárban.")

    def save_to_file(self):
        dictionary_type = input("Adja meg a szótár típusát: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return

        filename = input("Adja meg a fájl nevét: ") +".json"

        try:
            with open(filename, 'w') as file:
             json.dump(self.dictionaries[dictionary_type], file)
            print("Szótár mentve a fájlba.")
        except IOError as e:
            print(f"Hiba történt a fájl mentése közben: {e}")

    def export_definitions(self):
        dictionary_type = input("Adja meg a szótár típusát: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return

        filename = input("Adja meg a fájl nevét az exportáláshoz: ")

        with open(filename, 'w') as file:
            for word, translations in self.dictionaries[dictionary_type].items():
                file.write(f"{word}: {translations[0]['definition']}\n")

        print("Definíciók exportálva a fájlba.")
    
    def search_word(self):
        self.list_dictionaries()  # Új sor hozzáadva
        dictionary_type = input("Válassza ki a szótárt: ")
        if dictionary_type not in self.dictionaries:
            print(f"Nincs ilyen szótár: {dictionary_type}")
            return

        search_term = input("Adja meg a keresési kifejezést: ")
        found_words = []

        for word, translations in self.dictionaries[dictionary_type].items():
            if any(search_term.lower() in translation["translation"].lower() or
                   search_term.lower() in translation["definition"].lower()
                   for translation in translations):
                found_words.append(word)

        if found_words:
            print(f"A keresési kifejezésre illeszkedő szavak a(z) {dictionary_type} szótárban:")
            for found_word in found_words:
                print(f"- {found_word}")
        else:
            print("Nincs találat.") 
        
  

    def display_main_menu(self):
        print("\nFőmenü:")
        print("1. Szótár létrehozása")
        print("2. Szó és definíció hozzáadása")
        print("3. Szó definíciójának cseréje")
        print("4. Szó törlése")
        print("5. Szó definíciójának keresése")
        print("6. Szótár mentése fájlba")
        print("7. Definíciók exportálása fájlba")
        print("8. Szótár listázása")
        print("9. Szó keresése")
        print("0. Kilépés")

    def run_main_menu(self):
        while True:
            self.display_main_menu()
            choice = input("Válasszon (0-9): ")

            if choice == "1":
                self.create_dictionary()
            elif choice == "2":
                self.add_word()
            elif choice == "3":
                self.replace_definition()
            elif choice == "4":
                self.delete_word()
            elif choice == "5":
                self.search_definition()
            elif choice == "6":
                self.save_to_file()
            elif choice == "7":
                self.export_definitions()
            elif choice == "8":
                self.list_dictionaries()
            elif choice == "9":
                self.search_word()
            elif choice == "0":
                print("Kilépés...")
                break
            else:
                print("Érvénytelen választás. Kérem, válasszon újra.")
                
   
                
def main():
    dictionary = BilingualDictionary()
    dictionary.run_main_menu()

if __name__ == "__main__":
    main()