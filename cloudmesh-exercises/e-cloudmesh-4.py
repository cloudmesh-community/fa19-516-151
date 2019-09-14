from cloudmesh.common.Shell import Shell

def shell_demo():
    """
    This method demonstrates the use of the shell module.
    This example return the current status of git, version control system.
    """
    result = Shell.execute('git',['status'])
    print(result)
    return

shell_demo()
