from cloudmesh.common.StopWatch import StopWatch
import numpy as np
import time
def stopwatch_demo():
    """
    This program measure the time elapse of sorting
    """
    StopWatch.start("Sort Test")
    np.sort(np.random.normal(size=1000))
    StopWatch.stop("Sort Test")
    print('Sorting took:',StopWatch.get("Sort Test"),'s')
    return

stopwatch_demo()