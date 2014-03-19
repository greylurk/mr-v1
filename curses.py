import curses
import locale

class ControlPanel:

    def __init__(self):
        self.sensors = []
        self.actuators = []
        self.screen = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1)
        locale.setLocale(locale.LC_ALL,'')
        

    def close(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()


        
