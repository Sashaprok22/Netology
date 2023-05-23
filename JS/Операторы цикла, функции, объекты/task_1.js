function isPrime(num){
    for(let i = 2, s = Math.sqrt(num); i <= s; i++) {
        if(num % i === 0) return false;
    }
    return num > 1;
}

function primesArray(count){
    let primeNums = []
    let currentNum = 2
    while (primeNums.length < count) {
        if (isPrime(currentNum)) {
            primeNums.push( currentNum )
        }
        currentNum++;
    }
    return primeNums;
}

console.log(primesArray(process.argv[2]));