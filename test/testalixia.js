// This function sends a POST request to the backend (Flask server) at http://127.0.0.1:5000/chat
// with a user message in the request body. It expects a JSON response containing the AI's reply.
//
// The process is as follows:
// 1. `fetch` is used to make an asynchronous request to the Flask backend with the user message.
// 2. The request includes the necessary headers (Content-Type: application/json) to specify that
//    the data being sent is in JSON format.
// 3. The message is packaged in the request body using `JSON.stringify`.
// 4. Once the request is successful, the response is processed:
//    - If the response status is not OK (200-299), an error is thrown.
//    - If the response is valid, it extracts the `response` field from the JSON and logs it to the console.
// 5. If there is any error during the fetch request or response processing, the error is logged to the console.

const TestAlixia = async () => {
  fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: "." }),
  })
    .then((res) => {
      if (!res.ok) throw new Error("Failed to get response");
      return res.json();
    })
    .then((data) => console.log(data.response)) // Logs the AI's response
    .catch((err) => console.error("Error:", err)); // Logs any errors that occur during the fetch
};

TestAlixia(); // Call the function to test the API response
