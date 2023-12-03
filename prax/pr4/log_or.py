import random
import numpy as np

# Инициализируем любым числом крутизны наклона прямой w1 = A
w1 = random.uniform(-4, 4)
w1_vis = w1 # Запоминаем начальное веса w1

# Инициализируем параметр w2 = b - отвечающий за точку прохождения прямой через ос Y
w2 = random.uniform(-4, 4) 
w2_vis = w2 # Запоминаем начальное значение веса w2

# Вывод данных начальных значений весовых коэффициентов
print('Начальные весовые коэффициенты:', '\nw1 = ', w1, '\nw2 = ', w2)

# Скорость обучения
lr = 0.001
# Зададим количество эпох
epochs = 5000
# Зададим порог единичной функции активации
bias = 3

# Создадим массив данных функции логического (И)
log_or = np.array([[0, 0, 0],
                    [1, 0, 1],
                    [0, 1, 1],
                    [1, 1, 1]])

# Прогон по выборке
for e in range(epochs):
    for i in range(log_or.shape[0]): # shape - возвращает размерность массива, [0] - индекс числа строк в массиве
        # Получить x1 координату точки
        x1 = log_or[i, 0] # i - строка, 0 -столбец
        
        # Получить x2 координату точки
        x2 = log_or[i, 1] # i - строка, 1 -столбец
        
        # Взвешенная сумма
        y = (w1 * x1) + (w2 * x2)
        
        if y >= bias:
            # Когда превышено пороговое значение, выход должен быть - y = 1
            y = 1
            # Получить целевую Y, координату точки
            target_Y = log_or[i, 2] # i - строка, 2 -столбец            

            # Ошибка E = -(целевое значение - выход нейрона)
            E = - (target_Y - y)
 
            # Меняем вес при x1
            w1 -= lr * E * x1
        
            # Меняем вес при x2
            w2 -= lr * E * x2
                
        else:
            # Когда не превышено пороговое значение, выход должен быть - y = 0
            y = 0
            # Получить целевую Y, координату точки
            target_Y = log_or[i, 2] # i - строка, 2 -столбец

            # Ошибка E = -(целевое значение - выход нейрона)
            E = - (target_Y - y)
 
            # Меняем вес при x1
            w1 -= lr * E * x1
        
            # Меняем вес при x2
            w2 -= lr * E * x2
                

# Вывод данных готовой прямой
print('\nОбученные весовые коэффициенты:', '\nw1 = ', w1, '\nw2 = ', w2)

print('\nПроверка логической функции (И):')
print('( 0, 0,', int((0*w1 + 0*w2)>=3), ')')
print('( 1, 0,', int((1*w1 + 0*w2)>=3), ')')
print('( 0, 1,', int((0*w1 + 1*w2)>=3), ')')
print('( 1, 1,', int((1*w1 + 1*w2)>=3), ')')