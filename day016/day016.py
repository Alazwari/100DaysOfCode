#Day 16

#pip install simple_chalk
#pip install terminal_banner

import simple_chalk
import terminal_banner
colors = simple_chalk.chalk
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
print(terminal_banner.Banner(f"""
{color.green_white('Hello World!')}
{color.green_white('From Saudi Arabia')}
{color.red_white('Here I print python in color')}
{color.blue_yellow('I use simple_chalk library')}
{color.white_magenta('And I use terminal_banner library')}
{color.blue_white('Try them!')}
"""))
