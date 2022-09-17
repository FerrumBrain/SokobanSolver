from PriorityQueue import PriorityQueue


def wall(level, coord):
    return level[(coord[0], coord[1])][1] == 0


def distance(method):
    def calc(state, cache):
        if 'min_distance' not in cache:
            cache['min_distance'] = {}
        player = state.getPlayerPosition()
        boxes = state.getBoxes()
        targets = state.getTargets()
        total = 0
        key = (",".join([str(x[0]) + "-" + str(x[1]) for x in boxes]),
               ",".join([str(x[0]) + "-" + str(x[1]) for x in targets]))
        if key in cache['min_distance']:
            total = cache['min_distance'][key]
        else:
            for b in boxes:
                total += min([method(b, t) for t in targets] or [0])
            cache['min_distance'][key] = total
        total += min([method(player, b) for b in boxes] or [0])
        return total

    return calc


def h(start, finish):
    return abs(finish[0] - start[0]) + abs(finish[1] - start[1])


def a_star(startState):
    cache1 = {}
    cache = {}
    h_f = distance(h)
    queue = PriorityQueue()
    action_map = {}
    startState.h = h_f(startState, cache1)
    queue.insert(startState, startState.h)
    action_map[startState.toString()] = ""
    while len(queue) != 0:
        state, cost = queue.extract_min()
        actions = action_map[state.toString()]
        cache[state.toString()] = len(actions)
        if state.isSuccess():
            return actions
        for (action, cost_delta) in state.getPossibleActions():
            successor = state.successor(action)
            if successor.toString() in cache:
                continue
            old = action_map[successor.toString()] if successor.toString() in action_map else None
            if not old or len(old) > len(actions) + 1:
                action_map[successor.toString()] = actions + action
            successor.h = h_f(successor, cache1)
            queue.insert(successor, cost + 1 + successor.h - state.h)
    return ""
