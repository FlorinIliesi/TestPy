print("Hello world")

endpoint = 10

def loop(endpoint):
    while True:
        if endpoint != 0:
            endpoint -= 1
        else:
            print(endpoint, ' is the limit')
