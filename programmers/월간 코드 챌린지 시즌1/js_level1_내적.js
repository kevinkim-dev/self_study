// ##########################
// #  프로그래머스           #
// #  월간 코드 챌린지 시즌1  #
// #  내적                  #
// ##########################

function solution(a, b) {
  var answer = 0;
  var l = a.length
  for (var i = 0; i < l; i++) {
      answer += a[i]*b[i]
  }
  return answer;
}

function solution2(a, b) {
  var answer = a.reduce((acc, now, i) => acc += now*b[i], 0)
  return answer
}