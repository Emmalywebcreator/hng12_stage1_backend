# hng12_stage1_backend

Number Classification API

Description
The Number Classification API takes a number as input and returns interesting mathematical properties about it, along with a fun fact from the Numbers API.

Features
Determines if the number is prime or perfect
Identifies properties such as even, odd, Armstrong number, etc.
Calculates the digit sum of the number
Fetches a fun fact about the number from the Numbers API
Returns structured JSON responses
Implements error handling and input validation

Live API URL
🔗 Base URL: https://hng12-stage1-backend-6sru.onrender.com

API Endpoint
GET /api/classify_number?number=<your_number>

Example Request:
curl "https://hng12-stage1-backend-6sru.onrender.com/api/classify_number?number=371"

Example Response:
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}


Error Response (Invalid Input)
If the user provides an invalid number, the API returns:
{
    "number": "alphabet",
    "error": true
}


Tech Stack
Python (Flask) – API framework
Requests – Fetching data from external APIs
Render – Deployment platform


Setup and Installation
Clone the Repository
git clone https://github.com/yourusername/number-classification-api.git
cd number-classification-api
Install Dependencies
pip install -r requirements.txt
Run the Application Locally

python app.py
Test Locally
curl "http://127.0.0.1:5000/api/classify_number?number=371"

Deployment
The API is deployed on Render and is publicly accessible. If you wish to deploy it yourself, follow these steps:

Push the project to GitHub
Create a new web service on Render
Link your repository
Specify the build command:
pip install -r requirements.txt
Specify the start command:
python app.py
Deploy!


Author
Emmanuel Ohwoka. Connect with me on:
🔗 GitHub: Emmalywebcreator


