const array = [1, 5, 2, 6, 3, 7, 4]
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

function solution(array, commands) {
    const answer = [];
    for (let command of commands) {
        const [i, j, k] = command
        const myarray = array.slice(i-1, j)
        // 정렬하기
        myarray.sort( function(a, b) {
            return a-b
        } )
        answer.push(myarray[k-1])
    }
    return answer;
}

// answer: [5, 6, 3]