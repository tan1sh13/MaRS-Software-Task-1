import numpy as np

def muchiko_filter(data, window_size):
    result = []
    
    for i in range(len(data)-window_size+1):
        window=data[i:i+window_size] #Slice the required values
        result.append(float(np.mean(window)))   # finding average
 
    return result
 
 
def sanchiko_filter(data, window_size):
    result = []
    for i in range(len(data)-window_size+1):
        window=data[i:i+window_size] #Slice the required values
        result.append(float(np.median(window)))  # finding and appending median
 
    return result

def hybrid_filter(data, window_size):
    after_median=sanchiko_filter(data, window_size)
    after_mean=muchiko_filter(after_median, window_size)
    return after_mean

data=eval(input("Enter the data:"))
window_size=int(input("Enter window size:"))
print("Muchiko Result:",muchiko_filter(data, window_size))
print("Sanchiko Result:",sanchiko_filter(data, window_size))
print("Hybrid Result:",hybrid_filter(data, window_size))
print("Median filter(Sanchiko) is the best because it removes noise and outliers effectively without distorting the original data")