# Day 29
import simple_chalk
import terminal_banner
colors = simple_chalk.chalk
banner = terminal_banner.Banner

class Color():
    def __init__(self):
        pass
    def blue(self, words):
        return colors.blue(words)
    def blue_white(self, words):
        return colors.blue.bgWhite.bold(words)
    def blue_yellow(self, words):
        return colors.blue.bgYellow.bold(words)
    def green_white(self, words):
        return colors.white.bgGreen.bold(words)
    def red_white(self,words):
        return colors.red.bgWhite.bold(words)
    def white_magenta(self, words):
        return colors.white.bgMagenta.bold(words)
color = Color()

print(color.green_white(banner(f'''    Welcome To ATM   
Please select the transaction number ...
------------------
|  1)  Balance   |
|  2)  Withdraw  |
|  3)  Quit      |
------------------
''')))

transaction = None
balance = 2334128.23
withdraw = None
try:
    transaction = int(input('What is your transaction: '))
    if transaction == 1:
        print(color.green_white(banner(f'''Your Balase is {balance}$''')))
    elif transaction == 2:
        try:
            withdraw = float(input(f'''Please Enter The Amount Of Money ... $'''))
            if withdraw < balance and withdraw > 0:
                print(color.green_white(banner(f'''Please Take The Money
And Your New Balance is {balance - withdraw}$''')))
            if withdraw == 0 or withdraw > balance:
                print(color.green_white(banner(f'''Sorry, We Can not procces, your balance is {balance}$''')))
        except:
            print(color.green_white(banner("Error, Try agin later")))
    elif transaction == 3:
        print(color.green_white(banner(f'''Thank you for using ATM service''')))
    else:
        print(color.green_white(banner(f'''Error, Try agin later
Please select the transaction number ...
------------------
|  1)  Balance   |
|  2)  Withdraw  |
|  3)  Quit      |
------------------
''')))
except:
    print(color.green_white(banner('''Please try again later''')))    