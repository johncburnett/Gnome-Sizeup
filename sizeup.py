from subprocess import check_output, call
import re

class Screen(object):
    def __init__(self):
        self.screens = self.get_screens()

    def get_screens(self):
        ''' Gets a mapping of connected screens to their position and offset. '''

        screens = {}
        xrandr = check_output(["xrandr", "-q"])
        matches = re.findall(r"\\n(\w+) connected[a-zA-Z_ ]+(\d+)x(\d+)\+(\d+)\+(\d+)", str(xrandr))
        for match in matches:
            screens[match[0]] = [int(x) for x in match[1:]]

        return screens

    def which_screen(self, x, y):
        ''' Given a position return which screen it's in '''
        for screen in self.screens:
            a,b,c,d = self.screens[screen]
            if x >= c and x < a + c:
                if y >= d and y < b+d:
                    return screen

    def left_maximize(self, screen, window_name):
        a,b,c,d = self.screens[screen]
        new_x = c
        new_y = d
        new_w = a/2 + 1
        new_h = b + 1
        return new_x, new_y, new_w, new_h

    def right_maximize(self, screen, window_name):
        a,b,c,d = self.screens[screen]
        new_x = c + (a/2)
        new_y = d
        new_w = a/2 + 1
        new_h = b + 1
        return new_x, new_y, new_w, new_h

    def up_maximize(self, screen, window_name):
        pass

    def bottom_maximize(self, screen, window_name):
        pass

    def left_up_maximize(self, screen, window_name):
        pass

    def left_down_maximize(self, screen, window_name):
        pass

    def right_up_maximize(self, screen, window_name):
        pass

    def right_down_maximize(self, screen, window_name):
        pass


class Window(object):
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.cur_screen = self.get_cur_screen(x, y)

    def get_cur_screen(self, x, y):
        pass


screen = Screen()
