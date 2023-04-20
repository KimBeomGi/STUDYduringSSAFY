//this
let obj = {
    name : '홍길동',
    // a : function(bf){
    //     console.log(this)
    //     bf()
    // },
    // bf란 매개변수 하나 주고 초기값으로 화살표함수 주고
    a : function(bf=() =>{console.log(this)}){
        console.log(this)
        // 화살표 함수 실행
        bf()
    },
    b : function(){
        console.log(this)
    }
}
// const b = function(){
//     console.log(this)
// }
obj.a()
// b()