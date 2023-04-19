const p1 = ['rock', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'paper', 'paper', 'rock', 'scissors']
const p2 = ['paper', 'paper', 'rock', 'scissors', 'paper', 'scissors', 'scissors', 'rock', 'rock', 'rock']

const playGame = (p1_choice, p2_choice) => {
	// 작성해 주세요
	const r_s_p = {
		'scissors' : 1,
		'rock' : 2,
		'paper' : 3
	}
	if (r_s_p[p1_choice] === r_s_p[p2_choice]) {
		return 0	
	}
	else if (r_s_p[p1_choice] === 1 &&  r_s_p[p2_choice] === 3) {
		return 1
	}
	else if (r_s_p[p1_choice] === 3 &&  r_s_p[p2_choice] === 1) {
		return 2
	}
	else if (r_s_p[p1_choice] > r_s_p[p2_choice]) {
		return 1	
	}
	else if (r_s_p[p1_choice] < r_s_p[p2_choice]) {
		return 2
	}
}
for (let i = 0; i < 10; i++) {
	console.log(playGame(p1[i], p2[i]))
}

// 2
// 0
// 2
// 0
// 2
// 1
// 2
// 1
// 0
// 2