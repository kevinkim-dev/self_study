// 1. call stack
// function c(){
//   console.log('hello')
// }
// function b(){
//   c()
// }
// function a(){
//   b()
// }
// a()

// 4. Type Coercion
// 4-1. boolean 변환

// console.log(1 + true)
// console.log(1 + false)

// // 4-2. string '+' 연산자

// console.log(1 + 'hi')
// console.log(1.1 + 'hi')

// // 4-3. 다양한 primitive 타입의 + 연산

// console.log(1 + null)
// console.log(1 + undefined)
// console.log(1 + NaN)
// console.log(1 + '')

// // 4-4. 다양한 primitive 타입의 boolean

// console.log(Boolean(null))
// console.log(Boolean(undefined))
// console.log(Boolean(NaN))
// console.log(Boolean(''))
// console.log(Boolean('0'))

// 5. typeof

// console.log(typeof(0))
// console.log(typeof(NaN))
// console.log(typeof('0'))
// console.log(typeof(true))
// console.log(typeof(false))
// console.log(typeof(undefined))
// console.log(typeof(null))


// 6. scope

// const a = 3

// for (var i = 0; i < 3; i++) {
//   console.log(a)
//   let b = 3
// }

// console.log(b)

for (var i = 0; i < 3; i++) {
  var c = 3
}

console.log(c)

function hello() {
  var d = 4
  console.log(d)
}

hello()
console.log(d)