import time

def chronometre(fonction): 
    def wrapper(*args, **kwargs): 
        debut = time.perf_counter()
        fonction(*args,**kwargs)
        fin = time.perf_counter()
        duree = fin - debut
        print(f"La fonction {fonction.__name__} a pris {duree} secondes.")
        return fonction(*args,**kwargs)
    return wrapper


@chronometre
def grosse_multiplication(multiplicateur):
    multiplicande = 1000000000000000*9999
    resultat = 0
    for i in range(1,multiplicateur):
        resultat += (multiplicande*multiplicateur*i)
    return resultat


resultat = grosse_multiplication(56897 * 2)
print(resultat)