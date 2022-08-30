def cakes(recipe, available):
    ratio = []
    no_excess = []
    recipe = list(recipe.items())
    available = list(available.items())
    for i in range(0, len(available)):
        for j in range(0,len(recipe)):
            if available[i][0] == recipe[j][0]:
                no_excess.append(available[i])
            else:
                continue
    available = no_excess
    recipe = list(map(tuple, recipe))
    recipe = dict(sorted(recipe))
    available = dict(sorted(available))
    for key, value in recipe.items():
        if key not in available.keys():
            return 0
        else:
            for i,k in enumerate(available.keys()):
                if key == k:
                   a = list(available.values())[i]/list(recipe.values())[i]
                   ratio.append(a)
    ratio = list(map(int, ratio))
    ratio = sorted(ratio)
    return ratio[0]
