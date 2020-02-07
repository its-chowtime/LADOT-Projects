// JS
const personTemplate = document.querySelector("#person");
const peopleContainer = document.querySelector("#people");

async function getApi() {
  const req = await fetch("https://mds.bird.co/gbfs/los-angeles/free_bikes"); // https://reqres.in/api/users?page=2
  const resp = await req.json();

  for (const person of resp.data.bikes) {
    let clone = document.importNode(personTemplate.content, true);
    clone.querySelector(".id").textContent = person.bike_id;
    clone.querySelector(".lat").textContent = person.lat;
    clone.querySelector(".lon").textContent = person.lon;
    // clone.querySelector(".image").src = person.avatar;
    peopleContainer.appendChild(clone);
  }
}

getApi();