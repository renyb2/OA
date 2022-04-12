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

# Modify the directory of python lib packages
import sys
sys.path.append(sys.path[0].replace('test', 'src'))

# Test Code
from common.cfg import YAML
from common.mailbox import Mailbox


CONF_FILE = r"./etc/oa.yaml"

CONF = YAML()
CONF = CONF.load(CONF_FILE)
print(CONF)

mail = Mailbox(CONF['mailbox']['smtp'], CONF['mailbox']['send'])

txt = 'renyb send email'
subject = 'OA'
receive = '779783219@qq.com'

attachment = './workload/base.xlsx'

msg = mail.init_msg(txt, attachment=True)
mail.add_attachment(msg, attachment)


if mail.send_email(receive , subject, msg):
    print('send success')
else:
    print('send failed')
