function triple(x){
    return x*x*x
}

const nums = [1, 2, 3, 4]
let new_nums = nums.map(triple)
console.log(new_nums)