def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func
        end = time.time()
        print("[*] time spent {} секунд.".format(end-start))
    return wrapper()

@benchmark
def fetch_webpage():
    import requests
    webpage = requests.get(url)
    return