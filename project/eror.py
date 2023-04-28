def selection_sort_descend_trace(values):
    for i in range(len(values) - 1):
        largest_index = i
        for j in range(i + 1, len(values)):
            if values[j] > values[largest_index]:
                largest_index = j
        values[i], values[largest_index] = values[largest_index], values[i]
        '''after every loop complete then whitespace craeted to used end=" " but 
        this line indicate new character so here used end="\n".
        passing the end of parameter. '''
        print(' '.join([str(x) for x in values]),end="\n")  
    return values


if __name__ == '__main__':
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)