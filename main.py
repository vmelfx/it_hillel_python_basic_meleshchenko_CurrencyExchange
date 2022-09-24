import requests


class Cashier:
    def __init__(self, uah_count: float, usd_count: float) -> None:
        self.set_uah_balance(uah_count=uah_count)
        self.set_usd_balance(usd_count=usd_count)

    def rate_and_cash_balance(self, currency=None) -> None:
        """
        This method is for getting current usd and uah balance
        Takes currency name and prints how much of it you have
        """
        currency_rate: float = self.get_currency_rate()
        if currency == 'usd':
            current_usd_balance: str = self.get_usd_balance()
            print("\n\nRATE: ", currency_rate, "AVAILABLE: ", current_usd_balance, "\n\n")
        elif currency == 'uah':
            current_uah_balance: str = self.get_uah_balance()
            print("\n\nRATE: ", currency_rate, "AVAILABLE: ", current_uah_balance, "\n\n")
        else:
            print(f"Invalid currency{currency}")

    def currency_exchange(self, amount, currency_to_exchange=None) -> None:
        """
        This method is responsible for currency exchange operations.
        When called, first it gets current currency rate from NBU-API, using get_currency_rate method
        and writes it into the currency_rate variable, then it gets current uah and usd balance and writes it into
        current_uah_balance and current_usd_balance respectively.
        After that, depending on given currency_to_exchange value method performs the exchange operation.
        If method can't get exchange rate, then, the program will be terminated
        to avoid mathematical errors.
        The result of the method is updated balances in files, printed status and printed updated balances
        :param amount: amount of currency you want to exchange
        :param currency_to_exchange: currency, you want to exchange
        """
        currency_rate: float = round(self.get_currency_rate(), 2)
        current_uah_balance: float = float(self.get_uah_balance())
        current_usd_balance: float = float(self.get_usd_balance())
        if currency_to_exchange == 'usd':
            if amount * currency_rate <= current_uah_balance:
                self.set_usd_balance(current_usd_balance + amount)
                self.set_uah_balance(current_uah_balance - amount * currency_rate)
                print("\n\nSuccess!")
                print("UAH AVAILABLE: ", self.get_uah_balance(), '\n' "USD AVAILABLE: ", self.get_usd_balance(), "\n\n")
            else:
                required_balance: float = round(amount * currency_rate, 2)
                print("\n\nUNAVAILABLE, REQUIRED BALANCE:", required_balance, "AVAILABLE: ",
                      current_uah_balance, "\n\n")
        elif currency_to_exchange == 'uah':
            if amount <= current_uah_balance:
                self.set_usd_balance(current_usd_balance - round(amount / currency_rate))
                self.set_uah_balance(current_uah_balance + amount)
                print("\n\nSuccess!")
                print("UAH AVAILABLE: ", self.get_uah_balance(), '\n' "USD AVAILABLE: ", self.get_usd_balance(), "\n\n")
            else:
                required_balance: float = round(amount / currency_rate, 2)
                print("\n\nUNAVAILABLE, REQUIRED BALANCE:", required_balance, "AVAILABLE: ",
                      current_usd_balance, "\n\n")

    @staticmethod
    def get_currency_rate() -> float:
        """
        This method gets the current exchange rate UAH-USD from NBU-API and returns it in float-format
        """
        api_url_currency_data: str = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?" \
                                     f"valcode=USD&json"
        response_currency = requests.request("GET", api_url_currency_data)

        if response_currency.status_code == requests.codes.ok:
            raw_currency_data = response_currency.json()
            if raw_currency_data:
                currency_rate: float = float(raw_currency_data[0]['rate'])
                return currency_rate
            else:
                print("En empty response from API. Program will be terminated")
                raise SystemExit(1)
        else:
            print("Error:", response_currency.status_code, response_currency.text, '\n', "Program will be terminated")
            raise SystemExit(1)

    @staticmethod
    def get_usd_balance() -> str:
        """
        This method gets current usd balance from USD_Balance.txt and return the value as string
        """
        with open("USD_Balance.txt", "r") as usd_wallet:
            current_usd_balance = usd_wallet.read()
        return current_usd_balance

    @staticmethod
    def get_uah_balance() -> str:
        """
        This method gets current uah balance from UAH_Balance.txt and return the value as string
        """
        with open("UAH_Balance.txt", "r") as uah_wallet:
            current_uah_balance = uah_wallet.read()
        return current_uah_balance

    @staticmethod
    def set_usd_balance(usd_count: float) -> None:
        """
        This method takes amount of usd cash as an argument and write it in USD_Balance.txt
        :param usd_count: amount of usd cash
        """
        with open("USD_Balance.txt", "w") as usd_wallet:
            usd_wallet.write(str(usd_count))

    @staticmethod
    def set_uah_balance(uah_count: float) -> None:
        """
        This method takes amount of usd cash as an argument and write it in UAH_Balance.txt
        :param uah_count: amount of uah cash
        """
        with open("UAH_Balance.txt", "w") as uah_wallet:
            uah_wallet.write(str(uah_count))


def main():
    """
    This is main function where all logic is configured.
    Before the first use, you need to specify your USD and UAH balance to be able to do operations.
    Once you entered your balance you will get to operations menu.
    All inputs are protected from incorrect input.
    If any exception will be raised during execution you will get a "System error" message.
    Detailed information about how this program works will be placed in readme.md.
    """
    try:
        print("Hi. Before use main functionality, you need to specify your USD and UAH balance")
        while True:
            try:
                usd_count: float = float(input("Please, enter your USD balance (only digits accepted): "))
                uah_count: float = float(input("Please, enter your UAH balance (only digits accepted): "))
            except ValueError:
                print("Invalid input! Try again")
            else:
                break
        cashier = Cashier(usd_count=usd_count, uah_count=uah_count)
        while True:
            print("Please choose one of the following action (just type the action name:",
                  "--RATE-- (Access to the currency rate and balance operations)",
                  "--EXCHANGE-- (Access to exchanging USD-UAH or UAH-USD)",
                  "--EXIT-- (Exit from the program)", sep='\n')
            action: str = input("Action: ").lower()
            match action:
                case "rate":
                    while True:
                        print("Please, choose one of the following actions:",
                              "--RATE USD-- (will show you current exchange rate and availability(USD))",
                              "--RATE UAH-- (will show you current exchange rate and availability(UAH))",
                              "--EXIT--  will return you to previous menu", sep='\n')
                        rate_action: str = input("Action: ").lower()
                        match rate_action:
                            case "rate usd":
                                cashier.rate_and_cash_balance(currency='usd')
                            case "rate uah":
                                cashier.rate_and_cash_balance(currency='uah')
                            case "exit":
                                print("Exiting to main menu...")
                                break
                            case _:
                                print(f"\n\nInvalid input: {rate_action}! Try again.\n\n")
                case "exchange":
                    while True:
                        print("Please, choose one of the following actions:",
                              "--EXCHANGE USD--", "--EXCHANGE UAH--", "--EXIT-- (will return you to previous menu)",
                              sep='\n')
                        exchange_action: str = input("Action: ").lower()
                        match exchange_action:
                            case "exchange usd":
                                while True:
                                    try:
                                        amount_usd: float = float(
                                            input("Please, enter the amount of usd you want to exchange"
                                                  " (only digits accepted): "))
                                    except ValueError:
                                        print("\n\nInvalid input! Try again.\n\n")
                                    else:
                                        break
                                cashier.currency_exchange(amount_usd, currency_to_exchange='usd')
                            case "exchange uah":
                                while True:
                                    try:
                                        amount_uah: float = float(
                                            input("Please, enter the amount of uah you want to exchange"
                                                  " (only digits accepted): "))
                                    except ValueError:
                                        print("\n\nInvalid input! Try again.\n\n")
                                    else:
                                        break
                                cashier.currency_exchange(amount_uah, currency_to_exchange='uah')
                            case "exit":
                                print("Exiting to main menu...")
                                break
                            case _:
                                print(f"\n\nInvalid input: {exchange_action}! Try again.\n\n")
                case "exit":
                    print("Good bye!")
                    raise SystemExit(0)
                case _:
                    print(f"\n\nInvalid input: {action}! Try again.\n\n")
    except KeyboardInterrupt:
        print("\nProgram exited via keyboard interrupt. Good bye!")
    except Exception:
        print("\nSystem error!")


if __name__ == '__main__':
    main()
