import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Saurabh Kohade'
email['to'] = 'rapchikssk@gmail.com'
email['subject'] = 'Stay Home stay safe '

email.set_content('''
COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.
Most common symptoms:
fever
dry cough
tiredness
Less common symptoms:
aches and pains
sore throat
diarrhoea
conjunctivitis
headache
loss of taste or smell
a rash on skin, or discolouration of fingers or toes
Serious symptoms:
difficulty breathing or shortness of breath
chest pain or pressure
loss of speech or movement
Seek immediate medical attention if you have serious symptoms. Always call before visiting your doctor or health facility.
People with mild symptoms who are otherwise healthy should manage their symptoms at home.
On average it takes 5–6 days from when someone is infected with the virus for symptoms to show, however it can take up to 14 days.''')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rapchikssk@gmail.com', 'Kohade12345@')
    smtp.send_message(email)
    print('All is WEll')







# gmail_user = "rapchikssk@gmail.com"
# gmail_pwd = "Kohade12345@"
# TO = 'skohade1@gmail.com'
# SUBJECT = "Testing sending using gmail"
# TEXT = "Testing sending mail using gmail servers"
# server = smtplib.SMTP(host='smtp.gmail.com', port=587)
# server.ehlo()
# server.starttls()
# server.login(gmail_user, gmail_pwd)
# BODY = '\r\n'.join(['To: %s' % TO,
#         'From: %s' % gmail_user,
#         'Subject: %s' % SUBJECT,
#         '', TEXT])

# server.sendmail(gmail_user, [TO], BODY)
# print ('email sent')