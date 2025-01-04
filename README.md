SF3E Alert Project

Overview

SF3E Alert is an emergency application designed to provide quick and reliable assistance during emergencies. The app connects users to emergency services and personal contacts by sharing their real-time location. It was developed using Python with the Kivy and KivyMD libraries, and integrates Twilio to send SMS messages containing location details.

Key Features

Emergency Alert System: Sends SMS alerts to pre-configured personal contacts with the user's current location.

Real-Time Location Sharing: Shares a Google Maps link of the user's location.

User-Friendly Interface: Simple and intuitive design for quick access during emergencies.

Cross-Platform Support: Compatible with multiple operating systems.

Tech Stack

Programming Language: Python

Frameworks: Kivy, KivyMD

Third-Party Integration: Twilio for SMS services

Development Environment: PyCharm

How It Works

Users configure their emergency contact numbers within the app.

During an emergency, users can trigger the alert button.

The app sends an SMS to the designated contacts with a Google Maps link to the user's real-time location.

Installation

Clone the repository:

git clone [https://github.com/your-username/sf3e-alert.git](https://github.com/anudeep0011/SF3E)

Navigate to the project directory:

cd sf3e-alert

Install the required dependencies:

pip install -r requirements.txt

Run the application:

python main.py

Configuration

Set up a Twilio account and get your Account SID, Auth Token, and a Twilio phone number.

Add your Twilio credentials to the config.py file:

TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'

Usage

Open the app and add your emergency contacts.

Click on the "Send Alert" button during an emergency.

Your contacts will receive an SMS with your location details.

Screenshots

(Include relevant screenshots here to showcase the app interface.)

Future Enhancements

Adding voice activation for triggering alerts.

Integrating with wearable devices for automated alerts.

Supporting additional messaging platforms (e.g., WhatsApp).

Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch:

git checkout -b feature-name

Make your changes and commit them:

git commit -m 'Add feature-name'

Push to your branch:

git push origin feature-name

Open a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

Kivy for the app framework.

Twilio for SMS integration.

The Python community for their support and resources.
