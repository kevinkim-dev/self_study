function solution(v) {
  var ax = 0, ay = 0
  const x=v[0][0], y = v[0][1]
  for (var i=1; i < 3; i++) {
      if (x == v[i][0]) {
          ax = 3 - i
      }
      if (y == v[i][1]) {
          ay = 3 - i
      }
  }
  return [v[ax][0], v[ay][1]];
}

console.log(solution([[1, 4], [3, 4], [3, 10]]))