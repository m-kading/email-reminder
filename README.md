# email-reminder

## Configuration
The following steps are required for configuring the reminder mail application

<br />

### Credentials
**Windows**:
```
set SENDER_EMAIL=<your_email_address>
set SENDER_PASS=<your_email_pass>
```

**Linux**:
```
export SENDER_EMAIL=<your_email_address>
export SENDER_PASS=<your_email_pass>
```

<br />

### Application Config
Configuration for the application is done in the *config/application_config.json* file

To change the SMTP configuration, change the values under the **smtpConfig** key:

* **smtpHost**: This should be the host for the SMTP server (String)
* **smtpPort**: This should be the port for the SMTP server (Number)
* **useTls**: Whether the application should establish a tls connection (Boolean) 

To add recipients add an entry to the **recipients** array with the following structure:
```
"recipients": [
    {
        "name": <recipient_name>,
        "email": <recipient_email_address>
    },
    {
        "name": <recipient_name_2>,
        "email": <recipient_email_address_2>
    },
    ...
]
```
Where:
* **name** is the name the reminder will use to refer to the recipient
* **email** is the email address the reminder will be sent to

<br />

### Reminder Configuration
To configure a reminder add an entry to the array in the *config/reminders.json* file as follows:
```
[
    {
        "subject": <reminder_subject>,
        "frequency": <reminder_frequency>,
        "start_date": <first_occurrence>,
        "message": <email_message>
    },
    {
        ...
    }
    ...
]
```

Where:
* **subject**: is the string to include in the subject line
* **frequency**: is the frequency the reminder is sent with any of the following values:
    * daily
    * weekly
    * fortnightly
    * monthly
* **start_date**: is the first day the reminder should be sent
* **message**: is the string that should be included in the body of the email