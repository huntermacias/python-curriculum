class SelectionSort(): 

	def sort(arr): 
		#loop through array and find the smallest val
		smallest = 1e4
		for i in range(len(arr)):
			idx = i
			for j in range(i+1, len(arr)):
				if arr[idx] > arr[j]:
					idx = j
			print(arr)
			arr[i], arr[idx] = arr[idx], arr[i]
			
					
			
			
	
	print("array before selection sort")
	arr = [23,55,21,5,56,34,64,88,34]
	print(arr)
	sort(arr)
	print("array after selection sort")
	print(arr)

	