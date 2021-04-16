/** process Form data: get data from form and make AJAX call to our API. */

$("#lucky-form").on("submit", async (evt)=>{
    evt.preventDefault();
    let name = $('#name').val();
    let birth_year = $('#year').val();
    let email = $('#email').val();
    let color = $('color').val()
    
    const response = await axios.post('/api/get-lucky-num',{
        name,
        birth_year,
        email,
        color
    });
    
     console.log(response.data);
    //handleApiResponse(response);
    luckynumApiCall();
    yearApiCall(birth_year);
});

async function luckynumApiCall(){
    const res = await axios.get('http://numbersapi.com/random?min=1&max=100&json')
    const luckynum = {text:res.data.text,
                        num:res.data.number}
    
    const result = `<p> Your lucky number is ${luckynum.num}. ${luckynum.text} </p>
                    `
    $("#lucky-results").append(result)
}

async function yearApiCall(birth_year){
    const res = await axios.get(`http://numbersapi.com/${birth_year}/year?json`)
    const yearData = {text:res.data.text,
                      num : res.data.number}

    const result1 = `<p> Your birth year ${yearData.num} fact is ${yearData.text} </p>`
    
    $("#lucky-results").append(result1)
}

/** handleResponse: deal with response from our lucky-num API. */




function handleApiResponse(response) {
    
    console.log(response);
}






// TO DISCUSS WITH MENTOR
// try{
    //     const res= await Promise.all([
    //         axios.get('http://numbersapi.com/random?min=1&max=100'),
    //         axios.get(`http://numbersapi.com/number/${birth_year}`)
    //     ]);
    //     const data = res.map((res)=>res.data);
    //     console.log(data.flat());
    
    // }
    // catch(err) {
    //     console.log(err)
    //   }