function dubleText(str, num){
    let letters = str.split('')
    for(let item of letters){
        console.log(item * num);
    }
}

console.log(dubleText('Security', 2));

