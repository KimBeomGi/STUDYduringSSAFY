// axios.(a)('https://api.example.com/data')
axios.get('https://api.example.com/data')	// 답 get
	// .(b)(function (response) {
	.then(function (response) {	// 답 then
	// console.log((c))
	console.log(response)		// 답 response
})

// 동기, 비동기 함수의 차이점
// 동기는 입력받은 순서대로 출력이 그대로 진행된다.
// 예시로 줄을 서서 주문받고 그 주문 순서대로 물품을 받는 것이 된다.

// 비동기는 입력받은 순서대로 출력이 되는 것이 아닌,
// 이후 일어나는 동기를 먼저 진행 또는 먼저 완료되는 비동기 작업을 수행하는 것이다.
//  에시로 줄을 서서 주문을 받지만 물품을 받는 것은 꼭 주문 순서대로 받는 것이 아닌 경우가 되겠다.