def est_subsets(arr):
    import itertools
    import numpy as np
    arr = np.array(list(set(map(str, arr))), dtype=object)
    result = np.array([x for x in itertools.chain.from_iterable(itertools.combinations(arr, r) for r in range(len(arr)+1))], dtype=object)
    return len(result) -1

