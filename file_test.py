print("Hello world")

endpoint = 10

def loop(endpoint):
    while True:
        if endpoint != 0:
            endpoint -= 1
            print(endpoint)
        else:
            print(endpoint, ' is the limit')
            break

loop(10)