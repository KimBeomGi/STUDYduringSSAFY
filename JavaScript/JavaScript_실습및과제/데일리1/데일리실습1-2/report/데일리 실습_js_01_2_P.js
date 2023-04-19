word_list = ['mom',   'happy','level', 'ssafy', 'life','noon']

function palindrome(word) {
    // word가 회문인지 아닌지 판별
    // let A = "true"
    // let middle = Math.floor(word.length / 2)
    // for (let i = 0; i < middle ; i++){
    for (let i = 0; i < word.length / 2; i++){
      // if (word[i] === word[word.length-1-i]){
      //   // A = "true";
      //   continue
      // }
      // else{
      if (word[i] !== word[word.length-1-i]){
        // A = "false";
        return false;
      }
    }
    return true;
  }
  
for (const word of word_list) {
  console.log(palindrome(word))
}

// 출력 예시
// true
// true
// true
// false
// false
// false