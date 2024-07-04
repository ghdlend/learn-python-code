#버블 정령 함수를 정의 이 함수는 재귀적으로 동작
def bubbleSort(arr,last):
  #'last'가 0보다 큰 경우에만 동작합니다.'last'는 정렬해야 하는 배열의 마지막 인덱스를 의미합니다.
  if last > 0:
    #지정된 범위 내의 모든 배열 요소를 순회합니다.
    for i in range(1,last):
      #앞의 요소가 뒤의 요소보다 크다면 , 두 요소의 위치를 바꿉니다.
      if arr[i-1] > arr[i]:
        arr[i-1],arr[i] = arr[i],arr[i-1]

      #배열의 다음 부분에 대해 버블 정렬을 수행합니다.
      #이는 'last' 인덱스를 1씩 감소시키면서 재귀적으로 함수를 호출함으로써 수행됩니다.
      bubbleSort(arr,last-1)

    #정렬할 숫자들을 포함하는 리스트를 정의합니다
    numbers =[64,34,25,12,22,11,90]
    #정의된 리스트에 버블 정렬 함수를 적용합니다.정렬이 필요한 마지막 인덱스로 리스트의 길이를 넘겨줍니다.
    bubbleSort(numbers,len(numbers))

    #정렬된 리스트를 출력합니다.
    print(numbers)