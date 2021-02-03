import socket
import curses
from ast import literal_eval

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(('', 8001))

screen = curses.initscr()
curses.noecho()

try:
    while True:
        message, server = sock.recvfrom(1024)
        message = literal_eval(message.decode())

        screen.clear()
        for key, value in message.items():
            if type(value) in [int, float]:
                screen.addstr(f'{key}: {value:.2f}\n')
            else:
                screen.addstr(f'{key}: {value}\n')
        screen.refresh()
finally:
    curses.endwin()
