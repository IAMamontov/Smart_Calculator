def tallest_people(**kwargs):
    tallest_list = []
    # print(sorted(kwargs,key=kwargs.get, reverse=True))
    max_h = kwargs[sorted(kwargs, key=kwargs.get, reverse=True)[0]]
    for i in range(len(sorted(kwargs, key=kwargs.get, reverse=True))):
        if kwargs[sorted(kwargs, key=kwargs.get, reverse=True)[i]] == max_h:
            tallest_list.append(sorted(kwargs, key=kwargs.get, reverse=True)[i])

    for i in sorted(tallest_list):
        print(i, ":", kwargs[i])




# tallest_people(Jackie=176, Wilson=185, Saersha=165, Roman=185, Abram=169)
