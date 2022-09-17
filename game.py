from cocos.scene import Scene
from cocos.layer import Layer
from cocos.sprite import Sprite
import useful


class Game:
    def __init__(self, level, size):
        self.crates = []
        self.size = size
        self.level = level
        self.points = []
        self.main_scene = Scene()
        self.first_plane = Layer()
        self.flag_win = False
        self.player = Sprite("PNG/Character4.png")
        self.second_plane = Layer()
        self.create_graphical_map()
        self.main_scene.add(self.first_plane)
        self.main_scene.add(self.second_plane)

    def create_graphical_map(self):
        for i in self.level:
            x, y = i
            self.first_plane.add(Sprite("PNG/GroundGravel_Concrete.png", position=(64 * x + 32, 64 * y + 32)))
            if self.level[i][1] == 4:
                self.player.position = (64 * x + 32, 64 * y + 32)
                self.second_plane.add(self.player)
            else:
                self.level[i][0].position = (64 * x + 32, 64 * y + 32)
                if self.level[i][1] == 2:
                    self.points.append((x, y))
                if self.level[i][1] == 1:
                    self.crates.append((x, y))
                    self.second_plane.add(self.level[i][0])
                else:
                    self.first_plane.add(self.level[i][0])

    def win(self):
        count = 0
        for i in self.crates:
            for j in self.points:
                if i == j:
                    count += 1
        if count == len(self.crates) and not self.flag_win:
            print("You win")
            print('Close the window for next level')
            self.flag_win = True

    @staticmethod
    def solve(level_level):
        answer = useful.a_star(level_level.getMatrix())
        print(answer)
        return answer
