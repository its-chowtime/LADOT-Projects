const generateJson = () => {
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    
    xhr.onreadystatechange = () => {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            //renderResponse(xhr.response);
            //    changeButton();
            console.log("sometyhing something");
            console.log(xhr.response);
            
            document.getElementById('message02').innerHTML = JSON.parse(xhr.response);
        }
    }
    xhr.open('GET', 'https://mds.bird.co/gbfs/los-angeles/free_bikes');
    xhr.send();

    

    console.log("ran");
}

generateJson();

console.log("Finished");
document.write(Date());

