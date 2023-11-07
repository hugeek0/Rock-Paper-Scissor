from datetime import datetime, timedelta


def log_time(func):
    def wrapped_func(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"your game duration: {duration.seconds} seconds")
        return result

    return wrapped_func
