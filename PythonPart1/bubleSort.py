####

import random
 
def bubble_sort(arr):
    n = len(arr)
   
    print(f"정렬 전: {arr}\n")
   
    for i in range(n):
        swapped = False
        print(f"--- 패스 {i + 1} ---")
       
        for j in range(n - 1 - i):
            print(f"비교: {arr[j]} vs {arr[j + 1]}", end=" ")
           
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"→ 교환 {arr}")
            else:
                print(f"→ 유지")
       
        print(f"패스 {i + 1} 결과: {arr}\n")
 
        if not swapped:
            print("정렬 완료! (더 이상 교환 없음)")
            break
   
    print(f"정렬 후: {arr}")
    return arr
 
def main():
    array_size = int(input("배열 크기를 입력하세요 (예: 5): "))
    min_value = int(input("최소값을 입력하세요 (예: 1): "))
    max_value = int(input("최대값을 입력하세요 (예: 100): "))
 
    arr = [random.randint(min_value, max_value) for _ in range(array_size)]
   
    print("\n" + "=" * 50)
    print("버블소트 시작!")
    print("=" * 50 + "\n")
   
    bubble_sort(arr)
 
if __name__ == "__main__":
    main()