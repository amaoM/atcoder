const input = require('fs').readFileSync('/dev/stdin', 'utf8');
const array = input.split('\n');
const line = array[0].split(' ');
const A = parseInt(line[0]);
const B = parseInt(line[1]);
const res = Math.max(A + B, A - B, A * B);
if (res === -0 || res === +0) {
  console.log(0);
} else {
  console.log(res);
}
