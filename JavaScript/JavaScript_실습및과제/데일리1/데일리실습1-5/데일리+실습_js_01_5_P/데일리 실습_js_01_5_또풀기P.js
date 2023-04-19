const participantNums =  [[1, 3, 2, 2, 1], 
[3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21],
[9, 1, 8, 7, 71, 33, 62, 35, 11, 4, 7, 71, 33, 8, 9, 1, 4, 11, 35]
]

for( let i=0; i<participantNums.length; i++ ){
  const check =[]
  let result = []
  for(let j=0; j<participantNums[i].length; j++){
    if(!check[j]){
      let answer = false
      for(let k=j+1; k<participantNums[i].length; k++){
        if(participantNums[i][j] === participantNums[i][k]){
          check[j] == true
          check[k] == true
          answer = true
          break
        }
      }
      if (!answer){
        result = participantNums[i][j]
        break
      }
    }
  }
  console.log(result)
}
