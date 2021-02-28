function solution(A) {
    // reduce 첫번째 parameter - 누적된 값, 두번째 parameter - current 값 (처음 loop 돌때는 A의 0번째 요소이다)
    const totalCounter = A.reduce((counter, num) => {
        if (counter[num]) {
            counter[num] += 1
        } else {
            counter[num] = 1
        }
        return counter;
    }, {}) 
    // 위에서 {}는 accumulator의 기본 값이다.
    for (key in totalCounter) {
        if (totalCounter[key] % 2 === 1) {
            return Number(key);
        }
    }
    return 0
}
