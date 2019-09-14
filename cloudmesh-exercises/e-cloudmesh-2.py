from cloudmesh.common.dotdict import dotdict

def dotdict_demo():
    """
    dotdict enables access python dictionary by dot
    """
    dict_demo = ({"key": "value"})

    # In python the value of a dictionary is retrieved by
    # using square brackets with subscriptions

    print(dict_demo['key'])

    # Using dotdict will enable the access by dots
    ddict = dotdict(dict_demo)
    print(ddict.key)
    return

dotdict_demo()