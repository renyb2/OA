#    Copyright 2022 Renyb && Liyr
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import smtplib
from email.mime.text import MIMEText


class Email(object):

    def __init__(self, smtp, send) -> None:
        self.smtp_server = smtp['server']
        self.smtp_port = smtp['port']
        self.send_address = send['email']
        self.send_passwd = send['passwd']

    def send_email(self, receive, subject, txt) -> bool:
        try:
            #import pdb;pdb.set_trace()
            msg = MIMEText(txt, 'plain', 'utf-8')
            msg['From'] = self.send_address
            msg['To'] = receive
            msg['Subject'] = subject

            server = smtplib.SMTP_SSL(
                self.smtp_server, self.smtp_port)

            server.login(self.send_address, self.send_passwd)
            server.sendmail(self.send_address, [receive,], msg.as_string())
            server.quit()
        except Exception as e:
            print(e)
            return False
        return True

