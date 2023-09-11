# Study Space Finder

**Study Space Finder** is a web application designed to assist Dartmouth students in finding the ideal study space tailored to their preferences and needs. By leveraging advanced web scraping techniques, the application provides real-time information on available study spaces, detailing their features and offering direct reservation options. Whether you're in search of a quiet corner for focused study or a collaborative workspace for group projects, Study Space Finder has got you covered.

## Overview

The primary goal of this project is to simplify the process of finding and reserving study spaces at Dartmouth. With an intuitive user interface, users can easily sort through available spaces based on various criteria, ensuring they find a spot that aligns with their study habits and requirements.

## Setup

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/sajjad-source/StudySpace.git
   cd StudySpace

2. **Set Up a Virtual Environment (Recommended):**
   ```python
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt

## Firebase Setup
   1. **Go to the Firebase Console.**
   2. **Create a new project.**
   3. **Navigate to the Firestore Database section** and create a new database.
   4. **Navigate to Project Settings > Service Accounts.**
   5. Click **"Generate New Private Key"** and save the JSON file to the project directory.
   6. Rename the saved JSON file to `my-file.json` or update the filename in `app.py`.

4. **Running the Application** 
   ```python
   python app.py

## Cron Job
   **Make the script executable:**
   ```bash
      chmod +x update_study_spaces.py
   ```

   **Open your crontab:**
   ```bash
      crontab -e
   ```
   **Add a line to run the script every day at a specific time (e.g., 2 AM):**
   ```bash
      0 2 * * * /usr/bin/python3 /path/to/update_study_spaces.py
   ```
   **Replace /usr/bin/python3 with the path to your Python interpreter. (You can find this with the which python3 command.)**
   
   **Replace /path/to/update_study_spaces.py with the absolute path to the update_study_spaces.py script.**




