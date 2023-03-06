dict1= {}
def most_frequent():
    str1=input(("Please enter the string:"))
    for i in str1:
        if i in dict1:
            dict1[i]= dict1[i]+1
        else:
            dict1[i] = 1
    sorted_dict = dict(sorted(dict1.items(),key=lambda item: item[1],reverse=True))
    print(sorted_dict)
most_frequent()
