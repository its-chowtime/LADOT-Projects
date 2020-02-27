function runFunc(arg) {
    const listOfProv = ["birdLa","birdSm","lime","lyft","spin","wheels"]
    let companyName = listOfProv[arg];
    console.log(companyName);
    nextFunc(companyName);
}

function nextFunc(companyName) {
    const provApi = {"birdLa":"https://mds.bird.co/gbfs/los-angeles/free_bikes",
                   "birdSm":"https://mds.bird.co/gbfs/santamonica/free_bikes",
                   "lime":"https://data.lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status",
                   "lyft":"https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json",
                   "spin":"https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json",
                   "wheels":"https://la-gbfs.getwheelsapp.com/free_bike_status.json"}
    let apiLink = provApi[companyName];
    requestApi(apiLink);
}
function thisCallback() {
    var myArr, counts;
    myArr = JSON.parse(this.responseText);
    console.log(status);
    console.log(myArr);
    counts = myArr.data.bikes.length;
    console.log(counts);
    document.getElementById("demo").innerHTML = counts;
}
function requestApi(apiLink) {
            // Pulling data from API
            var xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if(this.readyState == 4 && this.status == 200) {
                    thisCallback();
                }
            };
            xhttp.open("GET", apiLink,true);
            xhttp.send();
}