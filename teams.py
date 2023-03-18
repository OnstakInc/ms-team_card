import json
import requests

# this function is used to send the request to teams using webhook url
def send_request_to_teams(webhook_url):
    try:
        message = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "summary": "Approval Request",
            "themeColor": "0072C6",
            "sections": [
                {
                    "activityTitle": "Please approve this request",
                    "activitySubtitle": "Request ID: 1234",
                    "activityImage": "https://www.example.com/images/request.png",
                    "facts": [
                        {
                            "name": "Requested by",
                            "value": "sreenivasulu"
                        },
                        {
                            "name": "Request details",
                            "value": "Requesting for Git access"
                        }
                    ],
                    "potentialAction": [
                        {
                            "@type": "OpenUri",
                            "name": "Approve",
                            "targets": [
                                {
                                    "os": "default",
                                    "uri": "http://127.0.0.1:5000/approve"
                                }
                            ],
                        },

                        {
                            "@type": "OpenUri",
                            "name": "Reject",
                            "targets": [
                                {
                                    "os": "default",
                                    "uri": "http://127.0.0.1:5000/reject"
                                }

                            ]
                        }
                    ]
                }
            ]
        }

        headers = {"Content-Type": "application/json"}

        print("message : ",message)
        response = requests.post(webhook_url, data=json.dumps(message), headers=headers)

        #potential_actions = response.json().get("potentialAction")
        response.raise_for_status()  # raises an error if the response is not 200 OK
        print("sent a message card to teams  text: ", response.text)
        return "Successfully sent an Approval Request to Teams"
    except requests.exceptions.HTTPError as err:
        print("Error: unable to send request to teams")
        return f"Not able to send approval request to teams , Due to Below Error occurred:<br>  {err}"
    except requests.exceptions.RequestException as err:
        print("Error: unable to send request to teams")
        return f"Request Exception occurred: {err}"
    except Exception as err:
        print("Error: unable to send request to teams")
        return f"Error occurred: {err}"

    potential_actions = response.json().get("potentialAction")
    if potential_actions is not None and isinstance(potential_actions, list) and len(potential_actions) > 0:
        approval_response = potential_actions[0].get("body", {}).get("body")
        print("AP_RESPO :   ", approval_response)
        if approval_response == "Your request has been approved.":
            print("Request is approved")
    else:
        print("No potential actions found in response")
