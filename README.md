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




