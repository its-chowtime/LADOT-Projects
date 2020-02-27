const nameArr = ["birdLa","birdSm","lime","lyft","spin","wheels"]

const apiArr = ["https://mds.bird.co/gbfs/los-angeles/free_bikes",
"https://mds.bird.co/gbfs/santamonica/free_bikes",
"https://data.lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status",
"https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json",
"https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json",
"https://la-gbfs.getwheelsapp.com/free_bike_status.json"
]

var arr = []

function reqApi(apiUrl) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            let jsonData = JSON.parse(this.responseText);
            let count = jsonData.data.bikes.length.toString();
            //console.log(count);
        }
    }
    xhttp.open("Get", apiUrl, true);
    xhttp.send();
}

function listShit() {
    for(var i=0; i < nameArr.length; i++) {
        let name = nameArr[i];    // gets the names
        console.log(name);
        let apiUrl = apiArr[i];
        console.log(apiUrl);
        let y = reqApi(apiUrl);    // should get the count
        //arr.push(x,y);
        //console.log(arr);
    };
}

listShit();