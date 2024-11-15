import numpy as np
from matplotlib import pyplot as plt

def f(x): # объявляем функцию f
    return ((4*x + 5) / (3*x - 2))* np.arccos((1 + (-1) ** x) / 2 )

x = np.array(list(range(1, 50000))) # создаем массив натуральных чисел от 1 до 100 включительно
y = f(x)
# выделяем подпоследовательность x2k-1
def f2(x):
    return f(x*2 - 1)
# делаем функцию поиска xn0 при котором выполняется неравенство при некотором эпсилон
def epsilon(x):
    b = 0
    while abs(f2(b) - lim)>= x:
        b+= 1
    return b

lim = (2*np.pi)/3
a = 1
b = 0
plt.figure(figsize=(12, 6)) # изменяем размер графика
plt.scatter(x, y) # передаем для построения все точки
plt.plot([0 for i in range(len(x))],color='yellow')# отмечаем линию, равную инфинуму и нижнему пределу последовательности
plt.plot([(9*np.pi)/2 for _ in range(1,50000)], color = 'blue')#отмечаем линию, равную супремуму последовательности
plt.plot([(2*np.pi)/3 for _ in range(1,50000)])# отмечаем линию, равную верхнему пределу последовательности
# выделяем хn, начиная с которого элементы подпоследовательности входят в е-окрестность предела при е = 0.1
plt.scatter(x[epsilon(0.1)*2],y[epsilon(0.1)*2], color='red')
#выделяем саму е-окрестность предела
plt.plot([lim - 0.1 for i in range(len(x))], color='red')
plt.plot([lim + 0.1 for i in range(len(x))], color='red')
# аналогично для значений е: 0,05; 0,001 и 0,0001
plt.scatter(x[epsilon(0.05)*2],y[epsilon(0.05)*2], color='orange')
plt.plot([lim-0.05 for i in range(len(x))],color='orange')
plt.plot([lim+0.05 for i in range(len(x))],color='orange')
plt.scatter(x[epsilon(0.001)*2],y[epsilon(0.001)*2], color='yellow')
plt.plot([lim-0.001 for i in range(len(x))],color='yellow')
plt.plot([lim+0.001 for i in range(len(x))],color='yellow')
plt.scatter(x[epsilon(0.0001)*2],y[epsilon(0.0001)*2], color='pink')
plt.plot([lim-0.0001 for i in range(len(x))],color='pink')
plt.plot([lim+0.0001 for i in range(len(x))],color='pink')
# выводим получившиеся xn для заданных e
print(f'для е=0.1 k0={epsilon(0.1)}')
print(f'для е=0.05 k0={epsilon(0.05)}')
print(f'для е=0.001 k0={epsilon(0.001)}')
print(f'для е=0.0001 k0={epsilon(0.0001)}')
sup_ = 4.5*np.pi
def sup(x): # задаем функцию поиска хm для заданного е
    b = 0
    while f2(b)< sup_ - x:
        b += 1
    return b
print(f'для е=0.1 m={sup(0.1)}')
print(f'для е=0.05 m={sup(0.05)}')
print(f'для е=0.001 m={sup(0.001)}')
print(f'для е=0.0001 m={sup(0.0001)}')
plt.show() # строим сам график
# все точные границы последовательности достигаются,