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
            //console.log(nameArr);
            //console.log(count);
            //console.log(jsonData);
            console.log("inside out");
            for(var i=0; i<nameArr.length;i++) { // This is looping and repringting too much, I just want the name to append
                let provider = nameArr[i];
                arr.push(provider,count);
                console.log("inside" + i);
                break;
            }
            //console.log(arr);
        }
    }
    xhttp.open("Get", apiUrl, true);
    xhttp.send();
}

for(var i=0; i<nameArr.length;i++) {
    let apiUrl = apiArr[i]
    reqApi(apiUrl);
    console.log("outside" + i);
}
//let apiUrl = apiArr[0];
//reqApi(apiUrl);
console.log(arr);