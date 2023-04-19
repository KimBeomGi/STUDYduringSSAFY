//문제풀이
// 1. 전기버스 한번 충전으로 K만큼 이동 가능
// 2. 0번에서 출발해 종점 N에 도착해야하고, M개의 충전기가 설치된 정류장번호 주어짐
// 3. 최소 몇번의 충전을 해야하는가?
// 4. 주어지는 것은 K,N,M 정류장번호가 주어진다.
//이곳에 코드를 작성합니다.
const inputs = [
    [3, 10, 5, [1, 3, 5, 7, 9]],    // 3
    [3, 10, 5, [1, 3, 7, 8, 9]],    // 0
    [5, 20, 5, [4, 7, 9, 14, 17]],  // 4
  ]

function solution(K, N, M, chargers) {
    chargers.push(N)
    chargers.unshift(0)
    // console.log("ㅁㄴ"+chargers)
    // 우선 각 충전소에서 충전해서 다음 충전소까지 충분히 갈 수 있는지 확인하기
    for (let i = 1; i < M+1; i++) {
        if ((chargers[i]-chargers[i-1]) > K ) {             // 다음 충전소에서 전 충전소 거리가 K보다 크면
            min_charge = 0
            return                                          // 못가니까 0반환
        }
    }

    // 충전하면서 가면 끝까지 갈 수 있음 확인했으니 이제 필요내용 작성
    return check(K, K, N, 0, 0, chargers)                   // check함수로 보내기
}
// check 함수 생성
function check(battery, K,  N, my_p, count, chargers) {     // 내 위치를 받아오기
    if (chargers[my_p]===N && battery >= 0) {               // 내 위치가 마지막 정류장이면
        if (min_charge > count)                             // 최소 충전값 비교하고 retrun하기
        {min_charge = count}
        return
    }

    if (battery < 0){                                       // K < 0 즉, 배터리가 0보다 적으면 돌아가!
        return}

    let distance = chargers[my_p+1] - chargers[my_p]        // 다음 충전소까지 거리
    check(battery-distance, K, N, my_p+1, count, chargers)  // 충전 안하고 넘어가기
    battery = K
    check(battery-distance, K, N, my_p+1, count+1, chargers)  // 충전 무조건 하기
    return
}

  
for (const input of inputs) {
// 글로벌 변수로 만들기
min_charge=input[1] //최소 충전수를 초기화.(우선 정류장 수만큼 충전시킴)
// 함수실행
solution(input[0], input[1], input[2], input[3])
console.log(min_charge)
}