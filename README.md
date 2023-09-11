Study Space Finder
A web application to find and display study spaces at Dartmouth. The project uses Flask for the backend, web scraping to fetch study space data, Firebase's Firestore for data storage, and a daily cron job to update the study spaces.

Setup
1. Clone the Repository
bash
Copy code
git clone https://github.com/YOUR_USERNAME/study-space-finder.git
cd study-space-finder
Replace YOUR_USERNAME with your GitHub username.

2. Set Up a Virtual Environment (Optional but Recommended)
bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install Dependencies
bash
Copy code
pip install flask flask_cors firebase_admin requests beautifulsoup4
4. Firebase Setup
Go to the Firebase Console.
Create a new project.
Navigate to the Firestore Database section and create a new database.
Navigate to Project Settings > Service Accounts.
Click "Generate New Private Key" and save the JSON file to the project directory.
Rename the saved JSON file to my-file.json or update the filename in app.py.
5. Running the Application
bash
Copy code
python app.py
Visit http://localhost:5001 in your browser to view the application.

6. Setting Up the Cron Job
To update the study spaces daily:

Make the script executable:
bash
Copy code
chmod +x update_study_spaces.py
Open your crontab:
bash
Copy code
crontab -e
Add a line to run the script every day at a specific time (e.g., 2 AM):
bash
Copy code
0 2 * * * /usr/bin/python3 /path/to/update_study_spaces.py
Replace /usr/bin/python3 with the path to your Python interpreter (you can find this with the which python3 command) and /path/to/update_study_spaces.py with the absolute path to the update_study_spaces.py script.

Usage
Once everything is set up, the application will display study spaces fetched from Firestore. The data in Firestore will be updated daily via the cron job.

Remember to replace placeholders like YOUR_USERNAME with your actual GitHub username or other relevant information. Also, ensure that any sensitive information (like Firebase credentials) is not pushed to the public repository.
