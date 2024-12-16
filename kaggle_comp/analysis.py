execute_file = True

if 'execute_file' in locals() and execute_file:
    # Execute another Python file
    exec(open("Jane_street_time_series.py").read())

