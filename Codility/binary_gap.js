function solution(N) {
    const binaryNum = N.toString(2);
    const binaryGaps = binaryNum.slice(binaryNum.indexOf('1') + 1, binaryNum.lastIndexOf('1'));
    const zeroCounted = binaryGaps.split('1').map(zeros => zeros.length);
    return Math.max(...zeroCounted)
}
    