from typing import List

def insertionSort(array) -> List[int]:
  # Write your code here
  l=len(array)
  for i in range(1,l+1):
    item=array[i]
    currentitem=i-1
    while ((array[currentitem]>item) and (currentitem>-1)):
      array[currentitem+1]=array[currentitem]
      currentitem=currentitem-1
    array[currentitem+1]=item
  return array  
      

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(insertionSort(data))
