import useful


def is_2_boxes(crates, coord_to):
    for j in crates:
        if j == coord_to:
            return True
    return False


def move(level, coord, coord_to, crates):
    do_if_box, if_2_boxes, if_box, ans = False, True, False, [-1, False]
    
    for i in crates:
        if i == coord:
            if_box, if_2_boxes = True, is_2_boxes(crates, coord_to)
            
        if not if_2_boxes and not useful.wall(level, coord_to):
            ans[0], do_if_box = i, True
            break

    if (if_box and do_if_box) or not if_box:
        ans[1] = True
    return ans
