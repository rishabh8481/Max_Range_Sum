# perform the calculation to fetch the maximum range value  
def max_sum(gain_loss,index,bucket,length,temp):
# if condition will execute once all the possible sum are calculated from the information provided by bob 
# and display the output 0 the max sum of data is negative else return the max sum.
    if((index+bucket) > length):
        max_profit = max(temp)
        if(max_profit<0):
            print('0')
        else:
            print(max_profit)
    else:
# temp contain the sum of all the possible buckets from the given info using sliding window concept
        temp.append(sum(gain_loss[index:index+bucket]))
        index=index+1
# recursion call is made so that all the values of the possible values is made 
        max_sum(gain_loss,index,bucket,length,temp)

# data read operation from the file  
f = open('C:/Users/A/Desktop/MS/csci174/assignments/CodeEval_Data_Files/mrs.txt','r' )
for line in f:
    data = line.split(';')
    info =data[1].split(' ')
    info[-1] = info[-1].strip()
    gain_loss = list(map(int, info))
    length = int(len(gain_loss))
    temp = []
# initialize the max_sum function
    max_sum(gain_loss,0,int(data[0]),length,temp)
