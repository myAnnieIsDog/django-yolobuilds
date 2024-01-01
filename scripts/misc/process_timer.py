from datetime import datetime as dt


def main():
    log_start = Log_start()
    Log_end(log_start)

def Log_start():
    log_start = dt.now()
    print(f"\nStarting... {log_start.strftime('%A, %B %d %Y %I:%M:%S %p')}\n")
    return log_start 


def Log_end(log_start):
    # time.sleep(0.001)
    delta = dt.now() - log_start 
    print(f"\nThat took {(delta).total_seconds()} seconds.")
    return delta


if __name__ == '__main__':
    main()
