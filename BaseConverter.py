def baseConverter():
    #Creare dizionari corrispondenze da base 10 a base XX e viceversa
    num_to_car = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
              8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
              15: 'F', 16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K', 21: 'L',
              22: 'M', 23: 'N', 24: 'O', 25: 'P', 26: 'Q', 27: 'R', 28: 'S',
              29: 'T', 30: 'U', 31: 'V', 32: 'W', 33: 'X', 34: 'Y', 35: 'Z',
              36: 'a', 37: 'b', 38: 'c', 39: 'd', 40: 'e', 41: 'f', 42: 'g',
              43: 'h', 44: 'i', 45: 'j', 46: 'k', 47: '@', 48: 'm', 49: 'n',
              50: 'o', 51: 'p', 52: 'q', 53: 'r', 54: 's', 55: 't', 56: 'u',
              57: 'v', 58: 'w', 59: 'x', 60: 'y', 61: 'z'}

    car_to_num = {}

    for key in num_to_car:
        car_to_num[num_to_car[key]] = key

    #Altre variabili
    lista_i = [0]*25
    print('\n_Conversione numero da base A a base B_')
    base_i = int(input('\tBase A (da 2 a 62): '))
    while ((base_i > 63) and (base_i < 1)):
           print('\tErrore!')
           base_i = int(input('\tBase A (da 2 a 62): '))
    base_f = int(input('\tBase B (da 2 a 62, diversa da base A): '))  
    while ((base_f > 63) and (base_f < 1) and (base_f == base_i)):
           print('\tErrore!')
           base_f = int(input('\tBase B (da 2 a 62, diverso da base A): '))
    

    #Inserire numero (in base 10)
    print('\tInserire numero in base A (', base_i, sep='', end='')
    num_base_i = input('): ')

    if (base_i != 10) and (base_f == 10):
        from_n10_to_10(num_base_i, car_to_num, base_i, base_f)
        
        
    if (base_i == 10) and (base_f != 10):
        from_10_to_n10(num_base_i, lista_i, base_f, num_to_car)

    if (base_i != 10) and (base_f != 10):
        lista_temp = list(num_base_i)
        i = 0
        num_temp = 0
        while i < len(lista_temp):
            boh = len(lista_temp)-1-i
            num_temp += car_to_num[lista_temp[i]]*base_i**(boh)
            i += 1
        b1_to_b2(num_temp, len(lista_i), base_f, lista_i, num_to_car)
        i = 0
        num_base_f = ''
        while i < len(lista_i):
            num_base_f += lista_i[i]
            i += 1
        num_base_f = num_base_f.lstrip('0')
        print('\tNumero in base B(', base_f, '): ', num_base_f, sep='')

def b1_to_b2(num, times, base_f, lista_i, num_to_car):
    if times > 0:
        if num > 0:
            a = num % base_f
            lista_i[times-1] = num_to_car[a]
            num = num // base_f
        else:
            lista_i[times-1] = num_to_car[num]
        b1_to_b2(num, times - 1, base_f, lista_i, num_to_car)

def from_n10_to_10(num_base_i, car_to_num, base_i, base_f):
    lista_temp = list(num_base_i)
    i = 0
    num_base_f = 0
    while i < len(lista_temp):
        boh = len(lista_temp)-1-i
        num_base_f += car_to_num[lista_temp[i]]*base_i**(boh)
        i += 1
    num_base_f = str(num_base_f)
    print('\tNumero in base B (', base_f, '): ', num_base_f, sep='')
    
def from_10_to_n10(num_base_i, lista_i, base_f, num_to_car):
    b1_to_b2(int(num_base_i), len(lista_i), base_f, lista_i, num_to_car)
    i = 0
    num_base_f = ''
    while i < len(lista_i):
        num_base_f += lista_i[i]
        i += 1
    num_base_f = num_base_f.lstrip('0')
    print('\tNumero in base B(', base_f, '): ', num_base_f, sep='')
    
'''
#Convertire il numero nella base XX
b1_to_b2(int(num_base_i), len(lista_i), base_f, lista_i, num_to_car)
i = 0
while i < len(lista_i):
    num_base_f += lista_i[i]
    i += 1
num_base_f = num_base_f.lstrip('0')
print('\tNumero in base B(', base_f, '): ', num_base_f, sep='')
'''
baseConverter()

