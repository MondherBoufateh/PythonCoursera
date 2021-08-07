def problem4_2(ran_list):
    import random
    import statistics
    """ Compute the mean and standard deviation of a list of floats """
    numList = []
    random.seed(150)
    for i in range(0,ran_list):
        numList.append(round(100*random.random(),1))
    print(statistics.mean(numList))
    print(statistics.stdev(numList))