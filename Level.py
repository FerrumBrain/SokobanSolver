import copy


class Matrix(list):
    target_found = False
    _string = None

    def getPlayerPosition(self):
        for i in range(0, len(self)):
            for k in range(0, len(self[i]) - 1):
                if self[i][k] == "@":
                    return [k, i]

    def getBoxes(self):
        boxes = []
        for i in range(0, len(self)):
            for k in range(0, len(self[i]) - 1):
                if self[i][k] == "$":
                    boxes.append([k, i])
        return boxes

    def getTargets(self):
        boxes = []
        for i in range(0, len(self)):
            for k in range(0, len(self[i]) - 1):
                if self[i][k] == ".":
                    boxes.append([k, i])
        return boxes

    def isSuccess(self):
        return len(self.getBoxes()) == 0

    def getPossibleActions(self):
        x = self.getPlayerPosition()[0]
        y = self.getPlayerPosition()[1]

        def update_valid(item, move, get_two_step):
            if item not in "*#$":
                return move, 'Move'
            if item in "$*" and get_two_step() not in "*#$":
                return (move, "Push") if item is '$' else (move, "PushOut")
            return None
        moves = []
        action_cost = update_valid(self[y][x - 1], 'L', lambda: self[y][x - 2])
        if action_cost is not None:
            moves.append(action_cost)

        action_cost = update_valid(self[y][x + 1], 'R', lambda: self[y][x + 2])
        if action_cost is not None:
            moves.append(action_cost)

        action_cost = update_valid(self[y - 1][x], 'U', lambda: self[y - 2][x])
        if action_cost is not None:
            moves.append(action_cost)

        action_cost = update_valid(self[y + 1][x], 'D', lambda: self[y + 2][x])
        if action_cost is not None:
            moves.append(action_cost)
        return moves

    def successor(self, direction):
        matrix = copy.deepcopy(self)
        self.successorInternal(matrix, direction)
        matrix._string = None
        return matrix

    def toString(self):
        if self._string is not None:
            return self._string
        self._string = "\n".join(["".join(x) for x in self])
        return self._string

    def __hash__(self):
        return hash(self.toString())

    def successorInternal(self, matrix, direction):
        x = matrix.getPlayerPosition()[0]
        y = matrix.getPlayerPosition()[1]

        if direction == "L":
            if matrix[y][x - 1] == " ":
                matrix[y][x - 1] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                    matrix.target_found = False
                else:
                    matrix[y][x] = " "

            elif matrix[y][x - 1] == "$":
                if matrix[y][x - 2] == " ":
                    matrix[y][x - 2] = "$"
                    matrix[y][x - 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "
                elif matrix[y][x - 2] == ".":
                    matrix[y][x - 2] = "*"
                    matrix[y][x - 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

            elif matrix[y][x - 1] == "*":
                if matrix[y][x - 2] == " ":
                    matrix[y][x - 2] = "$"
                    matrix[y][x - 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

                elif matrix[y][x - 2] == ".":
                    matrix[y][x - 2] = "*"
                    matrix[y][x - 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

            elif matrix[y][x - 1] == ".":
                matrix[y][x - 1] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                else:
                    matrix[y][x] = " "
                matrix.target_found = True

        elif direction == "R":
            if matrix[y][x + 1] == " ":
                matrix[y][x + 1] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                    matrix.target_found = False
                else:
                    matrix[y][x] = " "

            elif matrix[y][x + 1] == "$":
                if matrix[y][x + 2] == " ":
                    matrix[y][x + 2] = "$"
                    matrix[y][x + 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

                elif matrix[y][x + 2] == ".":
                    matrix[y][x + 2] = "*"
                    matrix[y][x + 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

            elif matrix[y][x + 1] == "*":
                if matrix[y][x + 2] == " ":
                    matrix[y][x + 2] = "$"
                    matrix[y][x + 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

                elif matrix[y][x + 2] == ".":
                    matrix[y][x + 2] = "*"
                    matrix[y][x + 1] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

            elif matrix[y][x + 1] == ".":
                matrix[y][x + 1] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                else:
                    matrix[y][x] = " "
                matrix.target_found = True

            else:
                pass

        elif direction == "D":
            if matrix[y + 1][x] == " ":
                matrix[y + 1][x] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                    matrix.target_found = False
                else:
                    matrix[y][x] = " "

            elif matrix[y + 1][x] == "$":
                if matrix[y + 2][x] == " ":
                    matrix[y + 2][x] = "$"
                    matrix[y + 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

                elif matrix[y + 2][x] == ".":
                    matrix[y + 2][x] = "*"
                    matrix[y + 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

            elif matrix[y + 1][x] == "*":
                if matrix[y + 2][x] == " ":
                    matrix[y + 2][x] = "$"
                    matrix[y + 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

                elif matrix[y + 2][x] == ".":
                    matrix[y + 2][x] = "*"
                    matrix[y + 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

            elif matrix[y + 1][x] == ".":
                matrix[y + 1][x] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                else:
                    matrix[y][x] = " "
                matrix.target_found = True

        elif direction == "U":
            if matrix[y - 1][x] == " ":
                matrix[y - 1][x] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                    matrix.target_found = False
                else:
                    matrix[y][x] = " "

            elif matrix[y - 1][x] == "$":
                if matrix[y - 2][x] == " ":
                    matrix[y - 2][x] = "$"
                    matrix[y - 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

                elif matrix[y - 2][x] == ".":
                    matrix[y - 2][x] = "*"
                    matrix[y - 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                        matrix.target_found = False
                    else:
                        matrix[y][x] = " "

            elif matrix[y - 1][x] == "*":
                if matrix[y - 2][x] == " ":
                    matrix[y - 2][x] = "$"
                    matrix[y - 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

                elif matrix[y - 2][x] == ".":
                    matrix[y - 2][x] = "*"
                    matrix[y - 1][x] = "@"
                    if matrix.target_found:
                        matrix[y][x] = "."
                    else:
                        matrix[y][x] = " "
                    matrix.target_found = True

            elif matrix[y - 1][x] == ".":
                matrix[y - 1][x] = "@"
                if matrix.target_found:
                    matrix[y][x] = "."
                else:
                    matrix[y][x] = " "
                matrix.target_found = True


class Level:
    matrix = Matrix()
    matrix_history = []

    def __init__(self, i):
        del self.matrix[:]
        del self.matrix_history[:]
        if type(i) == int:
            filename = 'levels/level' + str(i)

            with open(filename, 'r') as f:
                    for row in f.read().splitlines():
                        self.matrix.append(list(row))
        else:
            for row in i.split('\n'):
                self.matrix.append(list(row))

        max_row_length = 0
        for i in range(0, len(self.matrix)):
            row_length = len(self.matrix[i])
            if row_length > max_row_length:
                max_row_length = row_length

    def getMatrix(self):
        return self.matrix
