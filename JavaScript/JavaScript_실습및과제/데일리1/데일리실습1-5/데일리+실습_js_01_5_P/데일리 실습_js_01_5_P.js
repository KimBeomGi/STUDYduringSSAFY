const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]


for (let i = 0; i < participantNums.length; i++) {
  // 검사 대상이라면 오른쪽에 있는 요소 중에 나랑 같은 숫자가 있는지 확인
  const check = []
  let result = []
  for (let j = 0; j < participantNums[i].length; j++) {
    if(!check[j]){ // j번째 참가자가 짝꿍을 못찾았으면 뒤쪽 참가자 확인
      let is_find = false
      for(let k=j+1; k < participantNums[i].length;k++){
        // 만약에 짝꿍을 찾으면, j번과 k번 요소가 짝꿍
        if(participantNums[i][j] === participantNums[i][k]){
          check[j] = true
          check[k] = true
          is_find = true
          break
        }
      }
      if (!is_find){
        result = participantNums[i][j]
        break
      }
    }
  }
  console.log(result)
  // console.log(i, result)
}

// 3
// 100
// 62