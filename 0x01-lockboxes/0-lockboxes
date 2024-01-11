#!/usr/bin/python3
"""
Module that provides a function for determining if all
boxes in a given list can be opened.
"""


def next_open_box(open_boxes):
    """Looks for next opened box
    """
    for index, box in open_boxes.items():
        if box.get('status') == 'opened':
            box['status'] = 'opened/checked'
            return box.get('keys')
    return None


def canUnlockAll(boxes):
    """Check if all boxes can be opened
    """
    if len(boxes) <= 1 or boxes == [[]]:
        return True

    bx_aux = {}
    while True:
        if len(bx_aux) == 0:
            bx_aux[0] = {
                'status': 'opened',
                'keys': boxes[0],
            }
        bx_keys = next_open_box(bx_aux)
        if bx_keys:
            for k in bx_keys:
                try:
                    if bx_aux.get(k) and bx_aux.get(k).get('status') \
                       == 'opened/checked':
                        continue
                    bx_aux[k] = {
                        'status': 'opened',
                        'keys': boxes[k]
                    }
                except (KeyError, IndexError):
                    continue
        elif 'opened' in [box.get('status') for box in bx_aux.values()]:
            continue
        elif len(bx_aux) == len(boxes):
            break
        else:
            return False

    return len(bx_aux) == len(boxes)


def main():
    """Entry point"""
    canUnlockAll([[]])


if __name__ == '__main__':
    main()
