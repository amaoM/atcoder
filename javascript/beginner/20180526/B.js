"use strict"

const input = require('fs').readFileSync('/dev/stdin', 'utf8').split('\n');
const N = input[0];
const S = input[1];
let max = 0;
let used = [];
for (let i = 1; i < N; i++) {
  const k = S.slice(i - 1, i);
  if (used.indexOf(k) >= 0) {
    used.splice(used.indexOf(k), 1);
  }
  for (let ii = i; ii < N; ii++) {
    if (k == S.slice(ii, ii + 1) && 0 > used.indexOf(k)) {
      used.push(k);
    }
  }
  if (used.length > max) max = used.length;
}
console.log(max);
