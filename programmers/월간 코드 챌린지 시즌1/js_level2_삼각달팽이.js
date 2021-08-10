function solution(n) {
  var answer = [];
  var arr = new Array(n)
  for (var i = 0; i < n; i++) {
      arr[i] = new Array(i+1)
  }
  var r = -1, c = 0, v = 1
  var dxy = [[1, 0], [0, 1], [-1, -1]]
  var m = 0
  while(m < n) {
      var d = dxy[m % 3]
      for(var i= 0; i < n-m; i++) {
          r += d[0]
          c += d[1]
          arr[r][c] = v
          v += 1
      }
      m += 1
  }
  answer = arr.flat()
  return answer
}

n = 4
console.log(solution(n))