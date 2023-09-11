# Study Space Finder

A web application to help Dartmouth students find the perfect study space tailored to their needs.

## Overview

This project provides up-to-date information on available study spaces, their features, and reservation options using advanced web scraping techniques.

## Setup

### Prerequisites

- Python 3.x
- Virtual environment (recommended)

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sajjad-source/StudySpace.git
   cd StudySpace

Set Up a Virtual Environment (Recommended):

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the Required Packages:

bash
Copy code
pip install -r requirements.txt
Set Up Firebase:

Go to the Firebase Console and set up a new project.
Navigate to Project Settings > Service accounts.
Click on "Generate new private key" and save the JSON file.
Replace path_to_your_firebase_admin_sdk_key.json in app.py with the path to your downloaded JSON file.
Run the Application:

bash
Copy code
python3 app.py
Features
Real-time data scraping from Dartmouth's library website.
User-friendly interface with sorting options.
Direct reservation links for study spaces.
Data storage using Firebase Firestore.
Cron Job Setup
To periodically scrape the website and update the study spaces, set up a cron job:

bash
Copy code
0 0 * * * /path_to_your_python3 /path_to_your_script/webscraper.py
This will run the scraper every day at midnight.
