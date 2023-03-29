# include <stdio.h>
# define LEN 7
 
def quick_sort(arr, left, right):                   #
    if left >= right:                               # 왼쪽이 오른쪽보다 크면
        return                                      # 돌아가

    pivot = arr[(left + right) // 2]                # 피봇을 중앙 값으로 정해주고
    i, j = left, right                              # 왼쪽과 오른쪽을 정함
    while i <= j:                                   # 왼쪽이 오른쪽보다 크다면
        while arr[i] < pivot:                       # arr[i]가 피봇보다 작을때동안 반복하고
            i += 1                                  # i를 +1 해서 오른쪽으로 보내기
        while arr[j] > pivot:                       # arr[j]가 피봇보다 클 때동안 반복하고
            j -= 1                                  # j를 -1 해서 왼쪽으로 보내기
        if i <= j:                                  # 만약 i가 j보다 작거나 같으면
            arr[i], arr[j] = arr[j], arr[i]         # 서로의 값을 바꿔주라.
            i += 1                                  # i 값에 +1해서 오른쪽으로 보내주고
            j -= 1                                  # j 값에 -1해서 왼쪽으로 보내주기

    quick_sort(arr, left, j)                        # 왼쪽 값들에 대해 퀵소트 진행
    quick_sort(arr, i, right)                       # 오른쪽 값들에 대해 퀵소트 진행


if __name__ == '__main__':                          # 현재 모듈의 이름이 main일 때는 직접 실행되었음을 의미,
                                                    # 모듈로 사용될 때는 실행되지 않음
    # 이 코드를 import하여 사용할 때에는 실행되지 않음. 따라서 모듈로서 사용하고 싶다면 위 if 문을 제하면 됨
                                                    #
    arr = [5, 1, 6, 3, 4, 2, 7]                     # 정렬할 arr 리스트
    print("정렬 전 : ", arr)

    quick_sort(arr, 0, len(arr) - 1)                # 정렬 실시!

    print("정렬 후 : ", arr)


#########################
# 이건 C언어로 작성된 코드
# # include <stdio.h>
# # define LEN 7
 
# void quickSort(int arr[], int L, int R) {
#       int left = L, right = R;
#       int pivot = arr[(L + R) / 2];    // pivot 설정 (가운데) 
#       int temp;
#       do
#       {
#         while (arr[left] < pivot)    // left가 pivot보다 큰 값을 만나거나 pivot을 만날 때까지 
#             left++;
#         while (arr[right] > pivot)    // right가 pivot보다 작은 값을 만나거나 pivot을 만날 때까지 
#             right--;
#         if (left<= right)    // left가 right보다 왼쪽에 있다면 교환 
#         {
#             temp = arr[left];
#             arr[left] = arr[right];
#             arr[right] = temp;
#             /*left 오른쪽으로 한칸, right 왼쪽으로 한칸 이동*/
#             left++;
#             right--;
#         }
#       } while (left<= right);    // left가 right 보다 오른쪽에 있을 때까지 반복 
 
#     /* recursion */
#     if (L < right)
#         quickSort(arr, L, right);    // 왼쪽 배열 재귀적으로 반복 
 
#     if (left < R)
#         quickSort(arr, left, R);    // 오른쪽 배열 재귀적으로 반복 
# }
 
# int main(){
#   int i;
#   int arr[LEN] = {5,1,6,3,4,2,7};
#   printf("정렬 전 : ");
#   for(i=0; i<LEN; i++){
#     printf("%d ", arr[i]);
#   }
#   printf("\n");
    
#   quickSort(arr, 0, LEN-1);
  
#   printf("정렬 후 : ");
#   for(i=0; i<LEN; i++){
#     printf("%d ", arr[i]);
#   }
  
#   return 0; 
# }