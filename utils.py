import schedule
import threading

def schedule_once(minutes: int, func, *args, **kwargs) -> None:
    def wrapper():
        func(*args, **kwargs)
        return schedule.CancelJob
    
    schedule.every(minutes).minutes.do(wrapper)

def log_message(message, log_file='log.txt', print_msg = True) -> None:
    if print_msg:
        print(message)
    with open(log_file, 'a') as file:
        file.write(message + '\n')

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()