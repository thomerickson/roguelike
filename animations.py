# animations.py

import tdl
import math

class Expand_Circle():
    def __init__(self, con, root, colors, coords, radius, duration, char, color='white'):
        self.con = con
        self.root = root
        self.colors = colors
        self.color = colors.get(color)
        self.x, self.y = coords
        self.radius = radius
        self.duration = duration
        self.step = 0
        self.char = char
    # create offscreen console that represents the menu's window

    def animate(self, game_map, mouse_coordinates):
        if self.step >= self.duration:
            return {'done': True}
        else:
            cur_radius = math.ceil((self.step / self.duration) * self.radius)
            diameter = self.radius*2

            window = tdl.Console(diameter, diameter)

            for x in range (0, diameter):
                for y in range(0, diameter):
                    if math.sqrt((x-self.radius)**2 + (y-self.radius)**2) <= cur_radius:
                        if game_map.fov[0-self.radius+x+self.x, 0-self.radius+self.y+y] and game_map.transparent[0-self.radius+x+self.x, 0-self.radius+self.y+y]:
                            window.draw_char(x, y, self.char, fg=self.color)
            self.root.blit(window, self.x-self.radius, self.y-self.radius, diameter, diameter, 0, 0, fg_alpha=0.8, bg_alpha=0.0)
            self.step += 1
        return {}

class Targeting_Circle():
    def __init__(self, con, root, colors, coords, diameter, color='white'):
        self.con = con
        self.root = root
        self.colors = colors
        self.color = colors.get(color)
        self.x, self.y = coords
        self.diameter = diameter
        self.radius = int(self.diameter/2)
        self.step = 0
        self.end = False

    def animate(self, game_map, coords):
        if self.end == True:
            return {'done': True}
        self.x, self.y = coords

        print('animating targeting circle at coords' + str(self.x) + str(self.y))
        
        window = tdl.Console(self.diameter, self.diameter)

        for x in range (0, self.diameter):
            for y in range(0, self.diameter):
                if math.sqrt((x-self.radius)**2 + (y-self.radius)**2) <= self.radius:
                    if game_map.fov[0-self.radius+x+self.x, 0-self.radius+self.y+y] and game_map.transparent[0-self.radius+x+self.x, 0-self.radius+self.y+y]:
                        window.draw_char(x, y, 'o', fg=self.color)
        self.root.blit(window, self.x-self.radius, self.y-self.radius, self.diameter, self.diameter, 0, 0, fg_alpha=0.8, bg_alpha=0)
        self.step += 1
        return {}

    def endself(self):
        print('removing targeting')
        self.end = True