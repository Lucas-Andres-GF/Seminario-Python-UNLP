#La ideas es demostrar la llamada indirecta de una funcion a si misma 
def ping (x):
    if x > 10:
        return
    print('ping',x)
    pong(x+1)

def pong (x):
    if x > 10:
        return
    print('pong',x)
    ping(x+1)

ping(1)