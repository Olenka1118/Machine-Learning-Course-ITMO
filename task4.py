Уменьшите размерность при помощи библиотеки sklearn. Обратите внимание на параметр svd_solver, он отвечает за способ 
построения матричного разложения. Чтобы получать одинаковые результаты, используйте следующий параметр метода PCA: 

svd_solver='full'.

Подробнее об алгоритме PCA в библиотеке sklearn. 
https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

Для выполнения работы настоятельно рекомендуем использовать сервис Google Colab. Именно в этом случае мы можем гарантировать, 
что система зачтет ответы в случае правильного выполнения задания! 

Задание 1

В предложенном файле находится набор синтетических данных. Данные описывают 60 объектов, каждый из которых обладает 10 признаками. 
Ваша задача, используя метод главных компонент, перейти к новым координатам и найти следующие параметры.

1.1 Введите координату первого объекта относительно первой главной компоненты.
Десятичный разделитель точка. Ответ округлите до тысячных.
 
1.2 Введите координату первого объекта относительно второй главной компоненты.
Десятичный разделитель точка. Ответ округлите до тысячных.

1.3 Введите долю объясненной дисперсии при использовании первых двух главных компонент.
Десятичный разделитель точка. Ответ округлите до тысячных.
 
1.4 Какое минимальное количество главных компонент необходимо использовать, чтобы доля объясненной дисперсии превышала 0.85
Введите целое неотрицательное число

1.5 Какое количество групп объектов можно выделить, если использовать только первые две главных компоненты?
Введите целое неотрицательное число

Задание 2

Для прохода на новогодний корпоратив при входе нужно отгадать «логотип мероприятия». Для получения изображения логотипа 
необходимо по первым десяти главным компонентам восстановить исходное изображение (в качестве пригласительных рассылались 
матрица счётов и матрица весов первых десяти ГК).

Введите номер верного «логотипа мероприятия»