var nameArr = ["birdLa","birdSm","lime","lyft","spin"]

var apiArr = ["https://mds.bird.co/gbfs/los-angeles/free_bikes",
"https://mds.bird.co/gbfs/santamonica/free_bikes",
"https://data.lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status",
"https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json",
"https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json"
]

var countArr = []
var proxyUrl = "https://cors-anywhere.herokuapp.com/";

async function fetchApi(url = "", name) {
    fetch(url)
    .then((response) => {
        return response.json();
    })
    .then((myJson) => {
        let count = myJson.data.bikes.length.toString();
        return count;
    })
    .then((count) =>{ // append data into an array
        let x = count;
        let y = name;
        countArr.push(x,y);
        console.log(countArr);
    })
    .catch((error) => {
    console.error('There is a problem with the fetch operation', error);
    });
}

function arrFunc() {
    for(var i=0; i < nameArr.length; i++) {
        let name = nameArr[i];
        let apiUrl = apiArr[i];
        fetchApi(apiUrl, name); // passes the arguments into the function
    };
}    

// arrFunc();

setInterval(arrFunc, 5000);