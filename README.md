# Currency exchange application for cashier
## Description
This is simple cli currency exchange application for cashier.
It allows you store your balance, convert UAH to USD and vice versa.
This application was created as part of my thesis in IT Hillel school.
## User story
So, you are a cashier in currency exchange and to simplify your life you need an application,
that will automate your currency exchange operations. Here is a list of options you would like to have in the app:
1. Access to current exchange rate*
2. Ability to see how much and which currency you have
3. Ability to exchange your money

*This exchange program uses the exchange rate of the National Bank of Ukraine for the exchange in both directions.
It's not the best solution, cause in real life we have separate exchange rates for buying and selling, but in my case,
I couldn't find api, that gives rates required rates for free ([API-Ninjas](https://api-ninjas.com/api/convertcurrency)
also gives just NBU rates). You can modify this code for your needs. Due to design of itself it shouldn't be hard to implement
separate exchange rates.
## Requirements
Python 3.10+  
requests module
## Installation  
Install requests module:  
```bash
 pip install requests
```

Clone this repo:  
```bash
 git clone https://github.com/vmelfx/it_hillel_python_basic_meleshchenko_CurrencyExchange.git
```
## Usage
Go to the directory you cloned repo to and run main.py  
Your balance will be stored in two .txt files: UAH_Balance.txt and USD_Balance.txt.  
You will be asked to specify your USD and UAH balance:
```
Hi. Before use main functionality, you need to specify your USD and UAH balance
Please, enter your USD balance (only digits accepted): "Your input here"
Please, enter your UAH balance (only digits accepted): "Your input here"
```
Then you will get access to the main menu:
```
Please choose one of the following action (just type the action name:
--RATE-- (Access to the currency rate and balance operations)
--EXCHANGE-- (Access to exchanging USD-UAH or UAH-USD)
--EXIT-- (Exit from the program)
Action: Your action here
```
To make choice you need to type action name (rate, exchange or exit). Input is case-insensitive.  
Once you made a choice you will get in action menu, where you can choose what to do next. Once again,
to continue you need to type an action name
```
Action: rate
Please, choose one of the following actions:
--RATE USD-- (will show you current exchange rate and availability(USD))
--RATE UAH-- (will show you current exchange rate and availability(UAH))
--EXIT--  will return you to previous menu
```
For example, let's see current usd exchange rate and how much usd we have:
```
Action: rate usd


RATE:  36.5686 AVAILABLE:  1000.0 


Please, choose one of the following actions:
--RATE USD-- (will show you current exchange rate and availability(USD))
--RATE UAH-- (will show you current exchange rate and availability(UAH))
```
Let's return to previous menu and try another actions:
```
Action: exit
Exiting to main menu...
Please choose one of the following action (just type the action name:
--RATE-- (Access to the currency rate and balance operations)
--EXCHANGE-- (Access to exchanging USD-UAH or UAH-USD)
--EXIT-- (Exit from the program)
```
Let's try to exchange some money:
```
Action: exchange
Please, choose one of the following actions:
--EXCHANGE USD--
--EXCHANGE UAH--
--EXIT-- (will return you to previous menu)
```
For example, I want to exchange some usd. As we remember, we work as a cashier,
so for us the exchange of dollars means that the client gives us dollars,
and in return we give hryvnias:
```
Action: exchange usd
Please, enter the amount of usd you want to exchange (only digits accepted): 200


Success!
UAH AVAILABLE:  37686.0 
USD AVAILABLE:  1200.0 


Please, choose one of the following actions:
--EXCHANGE USD--
--EXCHANGE UAH--
--EXIT-- (will return you to previous menu)
```
Let's look at the reverse action:
```
Action: exchange uah
Please, enter the amount of uah you want to exchange (only digits accepted): 20000


Success!
UAH AVAILABLE:  57686.0 
USD AVAILABLE:  653.0 


Please, choose one of the following actions:
--EXCHANGE USD--
--EXCHANGE UAH--
--EXIT-- (will return you to previous menu)
```
As we finished our work, so let's close our program:
```
Please, choose one of the following actions:
--EXCHANGE USD--
--EXCHANGE UAH--
--EXIT-- (will return you to previous menu)
Action: exit
Exiting to main menu...
Please choose one of the following action (just type the action name:
--RATE-- (Access to the currency rate and balance operations)
--EXCHANGE-- (Access to exchanging USD-UAH or UAH-USD)
--EXIT-- (Exit from the program)
Action: exit
Good bye!
```
## License
[MIT](https://choosealicense.com/licenses/mit/)

