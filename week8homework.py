# You should not import any other module
import datetime as dt

def time_it(func, parms):
    """ Returns a string representing the time it took to execute a function.

    Parameters
    ----------
    func : any function

    parms : dict
        A dictionary with the parameters that will be passed to the function.
        For instance, if `parms` is {'parm1': 1}, then the function call will be
        `func(parm1=1)`

    Returns
    -------
    str
        A string with the time it took to execute `func` with the parameters `parms`.
        This string should have the following format:

        "It took <n days> days, <n hours> hours, <n mins> mins, and <n secs> secs to execute the function"

        where:
            <n days>, <n hours>, <n mins>, and <n secs> represent the number of days, hours, minutes,
            and seconds it took to run the function.

    Example
    -------

    Suppose there is a function called `my_func` that takes a single parameter called `parm1`.

        >> res = time_it(my_func, {'parm1': 3})
        >> print(res)
        It took 0 days, 0 hours, 1 mins, and 2 secs to execute the function

    In the example above, we are assuming it took 1 minute and 2 seconds to execute the function
    `my_func(parm1=3)`.

    Note
    ----
    - You should not use the `time` module inside this function
      (meaning, do not use `import time` inside this function)

    - You can use the function _mk_msg to produce a string with the
      format specified in the docstring (given the number of days, hours,
      mins, and secs)

    """
    # You can use this function if you want
    def _mk_msg(days, hours, mins, secs):
        """ This function produces a string with the format specified in the docstring
        of the main function.
        """
        msg = f"It took {days:.0f} days, {hours:.0f} hours, {mins:.0f} mins, and {secs} secs to execute the function"
        return msg

    start_time = dt.datetime.now()
    func(list(parms.values())[0])
    end_time = dt.datetime.now()
    period = end_time - start_time
    days = period.days
    totalsecond = period.seconds
    hours = int(totalsecond // (60 * 60))
    totalsecond %= (60 * 60)
    mins = int(totalsecond // 60)
    secs = int(totalsecond % 60)
    # totalsecond = period.total_seconds()
    # days = int(totalsecond//(24*60*60))
    # totalsecond %= (24 * 60 * 60)
    # hours = int(totalsecond // (60 * 60))
    # totalsecond %= (60 * 60)
    # mins = int(totalsecond // 60)
    # secs = int(totalsecond % 60)
    result = _mk_msg(days, hours, mins, secs)
    return result

def _test_time_it():
    """ This function uses the time.sleep to test the function time_it.

    the output of this function should be:

        Note: It will take about 1 min to execute this test function...
        It took 0 days, 0 hours, 1 mins, and 4.0 secs to execute the function

    NOTE
    ----
    - The number of secs in the output may be slignly different if the ED server is busy.
      If this happens, just run this test function again.

    """
    import time
    print("Note: It will take about 1 mins to execute this test function...")
    def _my_func(secs):
        time.sleep(secs)
    res = time_it(_my_func, {'secs': 64})
    print(res)



if __name__ == "__main__":
    _test_time_it()
