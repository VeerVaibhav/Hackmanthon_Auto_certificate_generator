import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import io
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition
import streamlit as st

EMAIL_ADDRESS = st.secrets["EMAIL_ADDRESS"]
SENDGRID_API_KEY = st.secrets["SENDGRID_API_KEY"]


def read_csv(uploaded_file):
    return pd.read_csv(uploaded_file)

def generate_certificate(name):
    image = Image.open("certificate_template.png")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 40)
    text_position = (700, 625)
    draw.text(text_position, name, font=font, fill="black")
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    buf.seek(0)
    return buf

def show_certificates(df, st):
    st.write("Certificate Preview:")
    for index, row in df.iterrows():
        name = row['Name']
        cert_image = generate_certificate(name)
        st.image(cert_image, caption=f"Certificate for {name}")

def send_email(to_address, name, image_bytes):
    message = Mail(
        from_email=EMAIL_ADDRESS,
        to_emails=to_address,
        subject='Your Event Certificate',
        plain_text_content=f'Hi {name},\n\nPlease find your event certificate attached.\n\nRegards,\nEventEye Team',
    )
    image_base64 = base64.b64encode(image_bytes.getvalue()).decode()
    attachment = Attachment(
        FileContent(image_base64),
        FileName('certificate.png'),
        FileType('image/png'),
        Disposition('attachment')
    )
    message.attachment = attachment

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        st.success(f"Email sent to {to_address} (Status: {response.status_code})")
    except Exception as e:
        st.error(f"Failed to send email to {to_address}: {e}")

def send_all_emails(df, st):
    error_list = []

    # Create a progress bar on the Streamlit page
    progress_bar = st.progress(0)
    total = len(df)

    for i, row in enumerate(df.itertuples()):
        name = row.Name
        email = row.Email
        cert_image = generate_certificate(name)
        try:
            send_email(email, name, cert_image)
        except Exception as e:
            error_list.append(f"Failed to send to {email}: {e}")

        # Update progress bar
        progress_bar.progress((i + 1) / total)

    if error_list:
        st.error("Errors occurred during sending:")
        for err in error_list:
            st.write(err)
    else:
        st.success("All certificates sent successfully!")
