from filosofos import *
def main():
    num_filosofos = 5
    max_comidas = 4
    tenedores = [threading.Lock() for n in range(num_filosofos)]
    filosofos = [Filosofo(f'Filosofo {n}', tenedores[n%num_filosofos], tenedores[(n+1)%num_filosofos], max_comidas) 
                 for n in range(num_filosofos)]
        
    for filosofo in filosofos:
        filosofo.start()
        
    for filosofo in filosofos:
        filosofo.join()