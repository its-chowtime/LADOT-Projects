const nameArr = ["birdLa","birdSm","lime","lyft","spin"]

const apiArr = ["https://mds.bird.co/gbfs/los-angeles/free_bikes",
"https://mds.bird.co/gbfs/santamonica/free_bikes",
"https://data.lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status",
"https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json",
"https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json"
]

var arr = []

function reqApi(apiUrl, name) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            let jsonData = JSON.parse(this.responseText);
            let count = jsonData.data.bikes.length.toString();
            console.log("inside xhr");
            arr.push(name,count);
        }
    }
    xhttp.open("Get", apiUrl, true);
    xhttp.send();
}

for(var i=0; i < nameArr.length; i++) {
    let name = nameArr[i];
    let apiUrl = apiArr[i];
    console.log("outside");
    reqApi(apiUrl, name);
};

console.log(arr);

