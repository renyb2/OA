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

from common.cfg import YAML
from common.utils import Email


CONF_FILE = r"./etc/email.yaml"

CONF = YAML()
CONF = CONF.load(CONF_FILE)
print(CONF)

EMAIL = Email(CONF['smtp'], CONF['send'])


txt = 'renyb send email'
subject = 'OA'
receive = CONF['receive']['email'][1]

if EMAIL.send_email(receive , subject, txt):
    print('send success')
else:
    print('send failed')
