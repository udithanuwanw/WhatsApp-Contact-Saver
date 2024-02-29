<!DOCTYPE html>
<html>

<body>
  <h1>WhatsApp Contact Saver</h1>
  <p>This script saves unsaved numbers from WhatsApp messages to a CSV file.</p>
  
  <h2>Features</h2>
  <ul>
    <li>Automatically saves unsaved numbers from WhatsApp messages to a CSV file.</li>
    <li>Utilizes Selenium for web automation.</li>
    <li>Easy to use and deploy.</li>
  </ul>
  
  <h2>Installation</h2>
  <ol>
    <li>Clone this repository to your local machine.</li>
    <li>Install the required Python libraries using `pip install -r requirements.txt`.</li>
    <li>Run the script using `python save_contacts.py`.</li>
    <li>Scan the QR code displayed in the browser window with your WhatsApp mobile app.</li>
    <li>Wait for the script to finish processing. It will automatically save unsaved numbers to `google_contacts.csv`.</li>
  </ol>

  <h2>How to Upload CSV to Google Contacts</h2>
  <p>Follow these steps to upload the CSV file to your Google Contacts:</p>
  <ol>
    <li>Go to Google Contacts (https://contacts.google.com/).</li>
    <li>Click on "Import" from the left sidebar.</li>
    <li>Choose the CSV file (`google_contacts.csv`) you generated using the script.</li>
    <li>Click on "Import" to upload the contacts.</li>
    <li>Google Contacts will automatically sync the uploaded contacts with your account.</li>
  </ol>

  <h2>Contributing</h2>
  <p>Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.</p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.</p>
</body>


</html>