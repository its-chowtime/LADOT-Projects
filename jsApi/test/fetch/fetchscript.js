const provList = ["birdLa", "birdSm", "lime", "lyft", "spin", "wheels"]

const apiArr = {
    "birdLa":"https://mds.bird.co/gbfs/los-angeles/free_bikes",
    "birdSm":"https://mds.bird.co/gbfs/santamonica/free_bikes",
    "lime":"https://data.lime.bike/api/partners/v1/gbfs/los_angeles/free_bike_status",
    "lyft":"https://s3.amazonaws.com/lyft-lastmile-production-iad/lbs/lax/free_bike_status.json",
    "spin":"https://web.spin.pm/api/gbfs/v1/los_angeles/free_bike_status.json",
    "wheels":"https://la-gbfs.getwheelsapp.com/free_bike_status.json"
}

var arr = []

async function getApi(url = "") {
    fetch(url)
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((myJson) => {
        const count = myJson.data.bikes.length.toString();
        console.log(count);
      })
      .catch((error) => {
        console.error('There is a problem with the fetch operation', error);
      });
  }

  getApi('https://mds.bird.co/gbfs/los-angeles/free_bikes');