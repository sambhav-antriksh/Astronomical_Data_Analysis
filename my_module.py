''' The module computes the mean,median,standard deviation and sorting in ascending order '''
def my_mean(list_number):
    ''' my_mean(list) -> gives average '''
    sum=0
    for j in range (0,len(list_number)):
        sum=sum+list_number[j]
    return (sum/(len(list_number)))



def my_median(list_number):
    ''' my_median(list) -> gives median'''
    sorted_list=my_sorting(list_number)
    length=len(sorted_list)
    if length%2==0:
        return (sorted_list[int(length/2)-1]+sorted_list[int(length/2)])/2
    else:
        return (sorted_list[int(length/2)])


def my_sorting(list_number):
    ''' my_sorting(list) -> gives the sorted list in ascending order '''
    for k in range(0,len(list_number)):
        for j in range(k+1,len(list_number)):
            if list_number[k]>list_number[j]:
                list_number[k],list_number[j]=list_number[j],list_number[k] #swapping in python beautiful and elegant
            else:
                continue
    return list_number


def my_standard_deviation(list_number):
    ''' my_standard_deviation(list) -> gives standard deviation '''
    n=len(list_number)
    ave=my_mean(list_number)
    sum_square=0
    for j in range(1,n):
        sum_square=sum_square+(list_number[j]-ave)**2
    assert sum_square >= 0
    return (sum_square)**0.5
    
