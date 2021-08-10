// ##########################
// #  프로그래머스           
// #  월간 코드 챌린지 시즌1  
// #  3진법 뒤집기           
// ##########################

function solution(n) {
  return n.toString(3).split('').reduce((acc, now, i) => acc += Number(now)*3**i, 0)
}