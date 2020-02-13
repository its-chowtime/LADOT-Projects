
// Set up our HTTP request
var xhr = new XMLHttpRequest();

// Setup our listener to process compeleted requests
xhr.onreadystatechange = function () {

	// Only run if the request is complete
	if (xhr.readyState !== 4) return;

	// Process our return data
	if (xhr.status >= 200 && xhr.status < 300) {
		// What do when the request is successful
		console.log('success', JSON.parse(xhr.responseText));
	} else {
		// What to do when the request has failed
		console.log('error', xhr);
	}

};

// Create and send a GET request
// The first argument is the post type (GET, POST, PUT, DELETE, etc.)
// The second argument is the endpoint URL
xhr.open('GET', 'https://mds.bird.co/gbfs/los-angeles/free_bikes');
xhr.send();






// wrote this code but idk if it works
const newJson = () => {
    const xhr = new XMLHttpRequest();
    xhr.responseType = 'json';
    
    // listener to process completed requests
    xhr.onreadystatechange = () => {
      // run if the request is complete
      if(xhr.readyState !== 4) return;
  
      // process returned data
      if (xhr.status >= 200 && xhr.status<300) {
        // what to do when the request is sucessful
        console.log('success', JSON.parse(xhr.responseText));
      } else {
        // what to do when the request has failed
        console.log('error', xhr);
      }
    
    }
  }