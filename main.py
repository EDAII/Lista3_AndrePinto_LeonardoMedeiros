import json
import matplotlib
import random
import time

from matplotlib import pyplot

import sys

#sys.setrecursionlimit(100000)

file = open("BloodMessages.json", "r")
jsondata = file.read()

jdata = json.loads(jsondata)

data = jdata['BloodMessages']  # Lista de dicionarios de BloodMessages

def mergeSort(arr): 
	if len(arr) > 1: 
		mid = len(arr)//2 
		L = arr[:mid] 
		R = arr[mid:]
  
		mergeSort(L) 
		mergeSort(R) 
  
		i = j = k = 0
          
		while i < len(L) and j < len(R): 
			if L[i]['Owner'] < R[j]['Owner']: 
				arr[k] = L[i]
				i+=1
			else: 
				arr[k] = R[j]
				j+=1
			k+=1
          
		while i < len(L): 
			arr[k] = L[i]
			i+=1
			k+=1
          
		while j < len(R): 
			arr[k] = R[j]
			j+=1
			k+=1
			

#quickIteration = 0
def partition(arr,low,high): 
	#global quickIteration
	i = (low-1)
	pivot = arr[high]    
	for j in range(low , high): 
		if arr[j]['Owner'] <= pivot['Owner']: 
			i = i+1 
			arr[i],arr[j] = arr[j],arr[i] 
			#quickIteration+=2
	arr[i+1],arr[high] = arr[high],arr[i+1]
	#quickIteration+=2
	return (i+1) 


def quickSort(arr,low,high): 		
	if low < high: 
		pi = partition(arr,low,high) 

		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 
		
print("Foram lidos: " + str(len(data)) + " Blood Messages")
arr1 = data
begin = time.time()
quickSort(arr1, 0, len(arr1)-1)
end = time.time()
quick_time = end - begin

arr2 = data
begin = time.time()
mergeSort(arr2)
end = time.time()
merge_time = end - begin

print('O Merge sort demorou {} segundo e o Quick sorte demorou {} segundo'.format(quick_time, merge_time))

Messages_per_world_X = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],
					  6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 
					  12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: []}
					  
Messages_per_world_Y = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [],
					  6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 
					  12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: []}
					  
for each in data:
	Messages_per_world_X[each['WorldNumber']].append(each['XCoord'])
	Messages_per_world_Y[each['WorldNumber']].append(each['YCoord'])



for i in range(9):
	fig, ax = pyplot.subplots()

	pyplot.xlabel('Position X')
	pyplot.ylabel('Position Y')
	ax.scatter(Messages_per_world_X[i+10], Messages_per_world_Y[i+10], label='World: '+str(i+10))
	
	pyplot.legend()

	pyplot.show()
	
	
