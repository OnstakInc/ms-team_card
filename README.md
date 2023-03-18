# Project Name: MS-TEAMS_CARD

1. **In a simple UI page have "Request Approval" button. 
     When user click on that, it will send that request to Teams channel with the details of the request and show the couple of buttons to user as "Approve", "Reject" and comment as optional.
     That response should be send back in email.**

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgments](#acknowledgments)

## Installation

To install the Python Weather App, follow these steps:

1. Clone the repository from GitHub:
    > git clone URL
2. Install the required dependencies:
    > pip install -r requirements.txt
3. Mention Teams channel WebhookUrl for receive the request in Environment.py as `webhook_url`
4. add sender mail using microsoft graph api.
   1. login to microsoft azure -> `https://portal.azure.com/`
   2. Go to **App registrations** --> **New_registration**,Fill the details and copy the `Tenant_id` and `Client_id` and paste in Environment.py file in code.
   3. Get the client_secret using below steps:
   4. Open certificates and secrets --> add one new secret and copy the secret value and paste in `client_secret` in Environment.py file in code.
   5. Get the Required permission from Admin for sending mail ( send.mail )
   6. You will get the access token
7. add the recipient mail  mentioned in Environment.py as `to_address`
8. Run this project :
    > python main.py

## Usage

To use this python MSTEAMS CARD project:

Run this project in your local using : > python main.py

1. open the link that you are getting in terminal,after execute
2. It will redirect the web page have buttons, select the button as you want. it will send the request to teams channel based on the webhook URl.
3. open the teams and accept the request "Approve " or "Reject". once you click on this it will send a request to your mail
