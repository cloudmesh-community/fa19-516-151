from cloudmesh.common import FlatDict

def flatdict_demo():
    """
    FlatDict will flatten the nested dictionary
    """

    # Creating a dict demo where the birthday is a nested dictionary
    dict_demo = {
        'Name':'Jack',
        'Gender':'Male',
        'Birthday':{'Year':1996,
                    'Month':9,
                    'Day':17}

    }
    flat_dict = FlatDict(dict_demo)
    print(flat_dict)
    return

flatdict_demo()
