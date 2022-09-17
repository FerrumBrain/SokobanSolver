from cocos.actions import *
from cocos.director import director
from pyglet.window import key as keys
from cocos.sprite import Sprite
import useful
import move
import game


def f(cell):
    if cell == '#':
        return [Sprite("PNG/Wall_Black.png"), 0]
    if cell == '@':
        return [0, 4]
    if cell == '$' or cell == '*':
        return [Sprite("PNG/CrateDark_Purple.png"), 1]
    if cell == '.':
        return [Sprite("PNG/EndPoint_Purple.png"), 2]
    if cell == ' ' or cell == 'x':
        return [Sprite("PNG/GroundGravel_Concrete.png"), 3]


def to_dict(level):
    ans = {(j, i): f(cell) for i, line in enumerate(level) for j, cell in enumerate(line)}
    return ans


def play(level_level, num):
    level_list = level_level.getMatrix()[::-1]
    name = "Level " + str(num)
    director.init(width=64 * len(level_list[0]), height=64 * len(level_list), autoscale=False, caption=name)
    level = to_dict(level_list)
    keyboard = keys.KeyStateHandler()
    director.window.push_handlers(keyboard)
    flag_keyboard = True
    cur_dir = {'R': 0, "U": 0, "L": 0, "D": 0}
    index = 0
    answer = ''

    class KeyboardController(Action):
        def step(self, dt):
            nonlocal flag_keyboard
            nonlocal cur_dir
            nonlocal index
            nonlocal answer
            if not cur_game.player.are_actions_running():
                direction = None
                direction_s = None

                if flag_keyboard:
                    dt = 0.2
                    if keyboard[keys.SPACE]:
                        flag_keyboard = False
                        index = 0
                        answer = cur_game.solve(level_level)
                    elif keyboard[keys.LEFT]:
                        direction = (-64, 0)
                        direction_s = 'L'
                    elif keyboard[keys.RIGHT]:
                        direction = (64, 0)
                        direction_s = 'R'
                    elif keyboard[keys.UP]:
                        direction = (0, 64)
                        direction_s = 'U'
                    elif keyboard[keys.DOWN]:
                        direction = (0, -64)
                        direction_s = 'D'
                else:
                    dt = 0.3
                    cur_dir[answer[index]] = 1
                    if cur_dir['L']:
                        direction = (-64, 0)
                        direction_s = 'L'
                    elif cur_dir['R']:
                        direction = (64, 0)
                        direction_s = 'R'
                    elif cur_dir['U']:
                        direction = (0, 64)
                        direction_s = 'U'
                    elif cur_dir['D']:
                        direction = (0, -64)
                        direction_s = 'D'
                    cur_dir[answer[index]] = 0
                    index += 1
                    if index == len(answer):
                        flag_keyboard = True
                        index = 0
                if not direction:
                    cur_game.win()
                    return

                coord = ((cur_game.player.x + direction[0] - 32) // 64, (cur_game.player.y + direction[1] - 32) // 64)
                coord_to = ((cur_game.player.x + direction[0] * 2 - 32) // 64,
                            (cur_game.player.y + direction[1] * 2 - 32) // 64)

                if not useful.wall(cur_game.level, coord):
                    step = move.move(cur_game.level, coord, coord_to, cur_game.crates)
                    if step[0] != -1:
                        level[coord][0].do(MoveBy(direction, dt))
                        level[coord], level[coord_to] = level[coord_to], level[coord]
                        cur_game.crates[cur_game.crates.index(coord)] = coord_to
                        level_level.getMatrix().successorInternal(level_level.getMatrix(), direction_s)
                    if step[1]:
                        cur_game.player.do(MoveBy(direction, dt))
                        level_level.getMatrix().successorInternal(level_level.getMatrix(), direction_s)

                cur_game.win()

    cur_game = game.Game(level, (len(level_list[0]), len(level_list)))

    cur_game.second_plane.do(KeyboardController())

    director.run(cur_game.main_scene)

    for i in range(8):
        print(' ')
    flag_keyboard = True
    cur_dir = {'R': 0, "U": 0, "L": 0, "D": 0}
    index = 0
    answer = ''
