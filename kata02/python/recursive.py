def _chop(needle, haystack, left_index, right_index):
    if left_index > right_index:
        return -1

    midpoint = (left_index + right_index) / 2

    if haystack[midpoint] < needle:
        return _chop(needle, haystack, midpoint+1, right_index)
    elif haystack[midpoint] > needle:
        return _chop(needle, haystack, left_index, midpoint-1)
    elif haystack[midpoint] == needle:
        return midpoint
    else:
        raise RuntimeError("I screwed up somewhere")


def chop(needle, haystack):
    return _chop(needle, haystack, 0, len(haystack)-1)
