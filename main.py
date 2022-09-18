import requests


class Cashier:
    def __init__(self, uah_count, usd_count):
        self.set_uah_balance(uah_count=uah_count)
        self.set_usd_balance(usd_count=usd_count)

    def rate_and_cash_balance(self, currency=None):
        currency_rate = self.get_currency_rate()
        if currency == 'usd':
            current_usd_balance = self.get_usd_balance()
            print("RATE: ", currency_rate, "AVAILABLE: ", current_usd_balance)
        elif currency == 'uah':
            current_uah_balance = self.get_uah_balance()
            print("RATE: ", currency_rate, "AVAILABLE: ", current_uah_balance)
        else:
            print(f"Invalid currency{currency}")

    def currency_exchange(self, amount, currency_to_exchange=None):
        currency_rate = round(self.get_currency_rate(), 2)
        current_uah_balance = float(self.get_uah_balance())
        current_usd_balance = float(self.get_usd_balance())
        if currency_to_exchange == 'usd':
            if amount * currency_rate <= current_uah_balance:
                self.set_usd_balance(current_usd_balance + amount)
                self.set_uah_balance(current_uah_balance - amount * currency_rate)
                print("Success!\n", "UAH AVAILABLE: ",
                      self.get_uah_balance(), '\n' "USD AVAILABLE: ", self.get_usd_balance())
            else:
                required_balance = amount * currency_rate
                print("UNAVAILABLE, REQUIRED BALANCE:", required_balance, "AVAILABLE: ", current_uah_balance)
        elif currency_to_exchange == 'uah':
            if amount <= current_usd_balance:
                self.set_usd_balance(current_usd_balance - amount)
                self.set_uah_balance(current_uah_balance + amount * currency_rate)

    @staticmethod
    def get_currency_rate():
        api_url_currency_data = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchangenew?" \
                                f"valcode=USD&json"
        response_currency = requests.request("GET", api_url_currency_data)
        if response_currency.status_code == requests.codes.ok:
            raw_currency_data = response_currency.json()
            currency_rate = raw_currency_data[0]['rate']
            return currency_rate
        else:
            print("Error:", response_currency.status_code, response_currency.text)

    @staticmethod
    def get_usd_balance():
        with open("USD_Balance.txt", "r") as usd_wallet:
            current_usd_balance = usd_wallet.read()
        return current_usd_balance

    @staticmethod
    def get_uah_balance():
        with open("UAH_Balance.txt", "r") as uah_wallet:
            current_uah_balance = uah_wallet.read()
        return current_uah_balance

    @staticmethod
    def set_usd_balance(usd_count):
        with open("USD_Balance.txt", "w") as usd_wallet:
            usd_wallet.write(str(usd_count))

    @staticmethod
    def set_uah_balance(uah_count):
        with open("UAH_Balance.txt", "w") as uah_wallet:
            uah_wallet.write(str(uah_count))


def main():
    print("Hi. Before use main functionality, you need to specify your USD and UAH balance")
    usd_count = int(input("Please, enter your USD balance (only digits accepted): "))
    uah_count = int(input("Please, enter your UAH balance (only digits accepted): "))
    cashier = Cashier(usd_count=usd_count, uah_count=uah_count)
    while True:
        print("Please choose one of the following action (just type the action name:",
              "RATE (Access to the currency rate and balance operations)",
              "EXCHANGE (Access to exchanging USD-UAH or UAH-USD)",
              "EXIT (Exit from the program)", sep='\n')
        action = input("Action: ").lower()
        match action:
            case "rate":
                print("Please, choose one of the following actions:",
                      "RATE USD", "RATE UAH", "EXIT - will return you to previous menu", sep='\n')
                rate_action = input("Action: ").lower()
                match rate_action:
                    case "rate usd":
                        cashier.rate_and_cash_balance(currency='usd')
                    case "rate uah":
                        cashier.rate_and_cash_balance(currency='uah')
                    case "exit":
                        print("Exiting to main menu...")
                    case _:
                        print("Invalid input! You will be returned to main menu.")
            case "exchange":
                while True:
                    print("Please, choose one of the following actions:",
                          "EXCHANGE USD", "EXCHANGE UAH", "EXIT - will return you to previous menu", sep='\n')
                    exchange_action = input("Action: ").lower()
                    match exchange_action:
                        case "exchange usd":
                            amount_usd = int(input("Please, enter the amount of usd you want to exchange"
                                                   " (only digits accepted): "))
                            cashier.currency_exchange(amount_usd, currency_to_exchange='usd')
                        case "exchange uah":
                            amount_uah = int(input("Please, enter the amount of uah you want to exchange"
                                                   " (only digits accepted): "))
                            cashier.currency_exchange(amount_uah, currency_to_exchange='uah')
                        case "exit":
                            print("Exiting to main menu...")
                        case _:
                            print("Invalid input! Try again.")
            case "exit":
                raise SystemExit(0)
            case _:
                print()


if __name__ == '__main__':
    main()
