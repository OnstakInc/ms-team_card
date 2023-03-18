import ms_mail_sender1
from teams import send_request_to_teams
import Environment
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        if request.method == 'POST':
            if request.form.get('approve') == 'true':
                teams_response = send_request_to_teams(Environment.webhook_url)

                # Process request approval
                return f'<html><body><h3>{teams_response}</h3></body></html>'
            else:
                # Process request rejection
                return '<html><body><h3> you have cancelled to send the request to teams </h3></body></html>'
        else:
            # Render form HTML
            return '''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>Request Approve Button</title>
                </head>
                <body>
                    <form method="post">
                    <h4>
                        <button  type="submit" name="approve" value="true"> <h3> Send Request to teams  </h3> </button>
                        &nbsp;
                        <button type="submit" name="cancel" value="true">  <h3> cancel   </h3></button>
                        </h4>

                    </form>
                </body>
                </html>
            '''
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

# when click on approve in teams this function run automatically
@app.route('/approve')
def approve_request1():
    try:
        # Parse the request body
        print("approve request function ")
        subject = "Request Approved"
        body = {
            'contentType': 'HTML',
            'content': "Your request has been Approved."
        }

        mail_trigger_response = ms_mail_sender1.send_mail(subject, body)
        print(mail_trigger_response)

        # TODO: Handle the approval logic (e.g. update the request status in a database)
        #return jsonify({'message': 'Your Request is Approved successfully <br> Please check your email for confirmation'})
        message = 'Your Request is Approved successfully <br> <br> Note : Please check your email for confirmation'

        return '<html><body><h3>{}</h3></body></html>'.format(message)
        # Return a response
    except Exception as e:
        return f'<html><body><h3> Error : Unable to approve the Request <br> {str(e)} </h3></body></html>'

# when click on reject in teams this function runs automatically
@app.route('/reject')
def reject_request():
    try:
        # Parse the request body
        print("reject Request function")
        subject = "Request Rejected"
        body = {
            'contentType': 'HTML',
            'content': "Your request has been Rejected."
        }

        mail_trigger_response = ms_mail_sender1.send_mail(subject, body)
        print(mail_trigger_response)
        # data = request.get_json()
        # request_id = data['request_id']
        # comment = data.get('comment')

        # TODO: Handle the rejection logic (e.g. notify the requestor via email)

        # Return a response
        return '<html><body><h3>your request is rejected <br>Note: please check a mail for confirmation</h3></body></html>'
        #return jsonify({'message': 'Your Request is Rejected. Please check a mail for confirmation'})
    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    app.run()
