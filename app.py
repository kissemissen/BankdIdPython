from core import model


def main():
    client = model.BankIdModel()
    while True:
        print("Select an option:")
        print("1 – Initiate BankId authentication")
        print("2 – Initiate BankId sign")
        print("3 – Collect BankId authentication/sign state")
        print("4 – Cancel BankId session")
        print("5 – Exit app")
        choice = input("Input choice: ")

        try:
            choice = int(choice)
        except ValueError:
            choice = 0

        if choice is 1:
            ssn = input("Input ssn: ")
            client.ssn = ssn
            response = client.auth()
            print(response)

        elif choice is 2:
            ssn = input("Input ssn: ")
            amount = float(input("Amount (e.g. 1500.00): "))
            client.ssn = ssn
            client.amount = amount
            response = client.sign()
            print(response)

            # print(data)

        elif choice is 3:
            response = client.collect()
            print(response)

        elif choice is 4:
            response = client.cancel()
            print(response)

        elif choice is 5:
            exit()

        else:
            print("Choice not available")
            print()


if __name__ == '__main__':
    main()
