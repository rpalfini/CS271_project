def getInput(file_input):
    num_loc = int(file_input.readline())
    graphmap = []
    for n in range(num_loc):
        arr_row=[]
        for i in file_input.readline().split():
            arr_row.append(float(i))
        graphmap.append(arr_row)
    return graphmap