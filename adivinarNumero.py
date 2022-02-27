import random;

def run():
    numeroRandom = random.randint(0,50);
    numero = int(input("Adivina que número es: "));    
    print(numeroRandom);

    while numeroRandom != numero:      
        while numeroRandom > numero:
            print("Es mayor que tu número");
            numero = int(input("Elije otro número: "));
            print(numeroRandom);

        while numeroRandom < numero:
            print("Es menor que tu número: ");
            numero = int(input("Elige otro número: "));        
    print("Si, ese es!");


if __name__ == '__main__':
    run()