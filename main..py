def assistant():
    print("🤖 Welcome to Smart Assistant!")

    name = input("What is your name? ")
    print(f"Hello {name}!")

    while True:
        command = input("How can I help you? ")

        if command.lower() == "hello":
            print("Hello! Nice to meet you.")

        elif command.lower() == "how are you":
            print("I am fine, thank you!")

        elif command.lower() == "exit":
            print("Goodbye!")
            break

        else:
            print("I don't understand yet.")

if __name__ == "__main__":
    assistant()
