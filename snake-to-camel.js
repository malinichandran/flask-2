function snakeToCamel(str) {
    let arr = str.split('');
    for(let i in arr){
        if(arr[i]==="_"){
            arr.splice(arr.indexOf(arr[i]),1)
            arr[i]=arr[i].toUpperCase()
            }
        }
    return arr.join('');
    }


