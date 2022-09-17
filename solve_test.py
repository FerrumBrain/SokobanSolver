import unittest

import move
import Level
import useful
import keyboard


class MyTestCase(unittest.TestCase):
    level_string = '''#######
    # . . #
    #     #
    #  $$ #
    #  @  #
    #######'''
    level = Level.Level(level_string).getMatrix()

    def test_solve(self):
        assert(useful.a_star(self.level) == 'RUUDLDLUU')

    def test_move(self):
        level_dict = keyboard.to_dict(self.level[::-1])

        crates = []
        for i in range(0, len(self.level.split('\n'))):
            for k in range(0, len(self.level.split('\n')[i]) - 1):
                if self.level[i][k] == "$":
                    crates.append((k, i))

        assert(move.move(level_dict, (2, 2), (2, 3), crates) == [-1, True])
        assert(move.move(level_dict, (3, 2), (4, 2), crates) == [-1, False])
        assert(move.move(level_dict, (3, 2), (3, 3), crates) == [(3, 2), True])
        assert(move.move(level_dict, (3, 1), (3, 0), crates) == [-1, False])


if __name__ == '__main__':
    unittest.main()
