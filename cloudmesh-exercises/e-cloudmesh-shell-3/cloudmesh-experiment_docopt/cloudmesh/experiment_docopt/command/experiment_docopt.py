from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.experiment_docopt.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class Experiment_docoptCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_experiment_docopt(self, args, arguments):
        """
        ::

          Usage:
                experiment_docopt --rand_1=rand_1 --rand_2=rand_2
                experiment_docopt list

          This command does some useful things.

          Arguments:
              rand_1  the first rand
              rand_2 the second rand
          Options:
              -f      specify the file

        """

        arguments.rand_1 = int(arguments['--rand_1'] or None)
        arguments.rand_2 = int(arguments['--rand_2'] or None)

        # Printing the sum of the two rands
        print(arguments.rand_1+arguments.rand_2)

        return ""