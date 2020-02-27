fetch('https://mds.bird.co/gbfs/los-angeles/free_bikes')
.then((response) => {
    return response.json();
})
.then((myJson) => {
    console.log(myJson);
    let count = myJson.data.bikes.length.toString();
    console.log(count.toString());
    return count;
})
.then((count) =>{
    let arr = [];
    let x = count;
    let y = "bird";
    arr.push(x,y);
    console.log(arr);
})
.catch((error) => {
console.error('There is a problem with the fetch operation', error);
});

      

/*
function appendData(data) {
    var mainContainer = document.getElementById("myData");
    for (var i=0; i<data.length; i++){
        // append to page
        var div = document.createElement("div");
        div.innerHTML = 'Bike ID: ' + data[i].bikes.bike_id
        mainContainer.appendChild(div);
        console.log(data)
        }
    }


for(var i=0; i < provList.length; i++) {
            const x = provList[i];
            console.log(x);
            const y = getApi();    // puts url into getApi function to pull JSON
            console.log(y);
        };
*/