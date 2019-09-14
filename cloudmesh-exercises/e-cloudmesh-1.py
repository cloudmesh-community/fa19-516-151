from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables

variables = Variables()
# variables['debug'] = True
# variables['trace'] = True
# variables['verbose'] = 10

def banner_demo():
    """
    The banner "prints a banner of the form with a frame of # around the txt"
    """
    print('color - print in the given color')
    banner('Hello World', color='RED')
    banner("Hello World", color='GREEN')
    banner("Hello World", color='BLUE')

    print('label – adds a label')
    banner("Hello World", label='This is a Label')

    print('debug - prints only if debug is true')
    banner("Print only if debug is True", debug=True)
    banner("Print only if debug is True", debug=False) # This line will print nothing

    print('c(character) – the character used instead of c')
    banner("Content is surrounded by +", c='+')
    return

def heading_demo():
    """
    HEADING Prints a message to stdout with #### surrounding it.
    This is useful for pytests to better distinguish them.
    """
    HEADING() # It will print the method name of where it was surrounded
    def inner_heading_demo():
        HEADING() # This line will print the inner method name
    inner_heading_demo()

    # HEADING also takes text inputs and the frame style can be changed
    HEADING("PLUS",c='+')
    return

def verbose_demo():
    """
    Prints a data structure in verbose mode
    """
    demo_dict = {"sample": "Hello"}
    VERBOSE(demo_dict)
    return

verbose_demo()