class AssistantBot:
    def __init__(self):
        self.contacts = {}

    def input_error(func):
        def errors(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except KeyError:
                return "Wprowadź nazwę użytkownika."
            except ValueError:
                return "Podaj nazwę i telefon."
            except IndexError:
                return "Nie znaleziono kontaktu o podanej nazwie."

        return errors

    @input_error
    def handle_hello(self):
        return "How can I help you?"

    @input_error
    def handle_add(self, data):
        name, phone = data.split()
        self.contacts[name] = phone
        return f"Kontakt {name} dodany z numerem telefonu {phone}."

    @input_error
    def handle_change(self, data):
        name, phone = data.split()
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Zmieniono numer telefonu dla kontaktu {name} na {phone}."
        else:
            raise IndexError

    @input_error
    def handle_phone(self, name):
        if name in self.contacts:
            return f"Numer telefonu dla kontaktu {name}: {self.contacts[name]}."
        else:
            raise IndexError

    @input_error
    def handle_show_all(self):
        if not self.contacts:
            return "Brak zapisanych kontaktów."
        else:
            return "\n".join(
                [f"{name}: {phone}" for name, phone in self.contacts.items()]
            )

    def main(self):
        while True:
            user_input = input("Wprowadź polecenie: ").lower()

            if (
                user_input == "good bye"
                or user_input == "close"
                or user_input == "exit"
            ):
                print("Good bye!")
                break
            elif user_input == "hello":
                print(self.handle_hello())
            elif user_input.startswith("add"):
                print(self.handle_add(user_input[4:]))
            elif user_input.startswith("change"):
                print(self.handle_change(user_input[7:]))
            elif user_input.startswith("phone"):
                print(self.handle_phone(user_input[6:]))
            elif user_input == "show all":
                print(self.handle_show_all())
            else:
                print("Nieznane polecenie. Spróbuj ponownie.")


if __name__ == "__main__":
    bot = AssistantBot()
    bot.main()
