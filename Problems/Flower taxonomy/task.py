iris = {}


def add_iris(id_n, species, petal_lenght, petal_width, **kwargs):
    global iris
    iris[int(id_n)] = {'species': species, 'petal_length': petal_lenght, 'petal_width': petal_width, **kwargs}



# add_iris(0, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac', petal_hue2='pale lilac2')
# add_iris(1, 'Iris versicolor', 4.0, 1.3, petal_hue='pale lilac')
# add_iris(2, 'Iris versicolor', 4.0, 1.3)
# add_iris(3, 'Iris_setosa', 3.7005577757757555, 0.2549310850180984, 5.951860817825088, 2.9197982289519357)

# print(iris)