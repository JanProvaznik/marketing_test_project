import mimetypes
import sys, os
from email.message import EmailMessage
from email.utils import make_msgid
import re


# a script that makes an email with embedded png images

def create_email(html_path, subject, msg_from, recipient):
    dir_path = os.path.dirname(html_path)

    with open(html_path, 'r') as html_email_file:
        html_email = html_email_file.read()

    msg = EmailMessage()
    msg["To"] = recipient
    msg["From"] = msg_from
    msg["Subject"] = subject

    regex_pattern = r'\ssrc="\S*"'
    # put regex matches in a list
    msg.set_content('')  # plain text body
    attachments = []
    paths = re.findall(regex_pattern, html_email)
    for img_name in paths:
        attachment_cid = make_msgid(domain='xyz.com')
        img_name = img_name.replace(' src="', '')
        img_name = img_name.replace('"', '')
        #html_email=  html_email.replace(f'"{img_name}"', f'"cid:{attachment_cid}"')
        html_email=  html_email.replace(f'"{img_name}"', f'"cid:{attachment_cid[1:-1]}"')
        #        if html_email== htmlemai.replace('src="', ''):
        #            print('wtf')
        composite_path = dir_path + img_name
        with open(composite_path, 'rb') as img:
            maintype, subtype = mimetypes.guess_type(img.name)[0].split('/')
            attachment_params = (img.read(), maintype, subtype, attachment_cid)
            attachments.append(attachment_params)
    # get absolute path of img_path
    # set an alternative html body
    msg.add_alternative(html_email, subtype='html')

    for attachment in attachments:
        msg.get_payload()[1].add_related(attachment[0],maintype=attachment[1],subtype=attachment[2],cid=attachment[3])

    return msg
