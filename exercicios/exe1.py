# -*- coding: utf-8 -*-


# Preciso saber a velocidade do veiculo

veloc= float(input("Velocidade: "))

# Agora crio as condições para cada velocidade

if veloc == 0:
    print("Você está parado")
else:
    if veloc >=1 and veloc <=20:
        print("Você está na primeira marcha")
    else:
        if veloc >=21 and veloc <=35:
            print("Você está na segunda marcha")
        else:
            if veloc >=36 and veloc <=50:
                print("Você está na terceira marcha")
            else:
                if veloc >=51 and veloc <=80:
                    print("Você está na quarta marcha")
                else:
                    print("Você está na quinta marcha")