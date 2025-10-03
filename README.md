<<<<<<< HEAD
# Certificate Automation Tool

This Streamlit app automates the process of generating personalized certificates from a CSV file containing participant names and emails, previewing them, and sending the certificates by email using SendGrid.

## Features

- Upload CSV with `Name` and `Email` columns
- Generate certificates with participant names on a template
- Preview all generated certificates in the app
- Send certificates via email with progress feedback

---

## How to Run Locally

1. Clone the repository:


2. Create a virtual environment (optional but recommended):


3. Install dependencies:


4. Create an `email_config.py` file with your email credentials (this file is excluded from GitHub for security):


5. Run the app:


6. Upload your CSV file in the app and use the interface to generate and send certificates.

---

## Project Structure

- `app_core.py`: Core functions for CSV processing, certificate generation, and email sending.
- `app_frontend.py`: Streamlit frontend UI for uploading files, previewing certificates, and sending emails.
- `certificate_template.png`: Template image used for certificates.
- `requirements.txt`: Required Python packages to install.
- `.gitignore`: Files and folders excluded from GitHub.
- `email_config.py`: (Not included) Your private email and API key config.

---

## Security Note

Make sure **not to commit your API keys** to GitHub. Use the `.gitignore` file to exclude `email_config.py` which contains sensitive information.

---

## License

MIT License

---

# Thank you for using the Certificate Automation Tool!
=======
# Hackmanthon_Auto_certificate_generator
>>>>>>> 4f2aff4a20b36f0340d0dbf590a9a5a8349774f9
