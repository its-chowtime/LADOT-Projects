// JS
const personTemplate = document.querySelector("#person");
const peopleContainer = document.querySelector("#people");

async function getApi() {
  const req = await fetch("https://reqres.in/api/users?page=2"); // https://mds.bird.co/gbfs/los-angeles/free_bikes | https://reqres.in/api/users?page=2
  const resp = await req.json();

  for (const person of resp.data) {
    let clone = document.importNode(personTemplate.content, true);
    clone.querySelector(".name").textContent = person.first_name;
    clone.querySelector(".surname").textContent = person.last_name;
    // clone.querySelector(".image").src = person.avatar;
    peopleContainer.appendChild(clone);
  }
}

getApi();