// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A, K) {
    // write your code in JavaScript (Node.js 8.9.4)
    array = A
    for (let i = 0; i < K; i ++) {
        let first = array.slice(0, array.length-1)
        let second = array.slice(array.length-1,)

        array = second.concat(first);
    }
    return array
}
