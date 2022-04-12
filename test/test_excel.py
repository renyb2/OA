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
import shutil
from common.cfg import YAML
from common.excel import Excel


CONF_FILE = r"./etc/oa.yaml"

CONF = YAML()
CONF = CONF.load(CONF_FILE)

file = CONF['payroll']['src']['file']
base = CONF['payroll']['dest']['base_file']


excel_operator = Excel(file)

info = excel_operator.get_row_index_by_value(CONF['payroll']['src']['name_range'])
print(info)

for person in CONF['mailbox']['receive']:
    name = person['name']

    if name not in info.keys():
        print('[ERROR] Payroll information not found: %s.' % name)
        continue

    index = info[name]
    perfix = CONF['payroll']['dest']['prefix']
    storage_dir = CONF['payroll']['dest']['storage_dir']
    payroll_file = '%s/%s%s.xlsx' % (storage_dir, perfix, name)

    shutil.copyfile(base, payroll_file)
    payroll_operator = Excel(payroll_file)

    for i in index:
        payroll = excel_operator.get_row_values_by_index(i)
        payroll_operator.add_row_with_values(payroll, format=True)

        print('[INFO] Payroll generated successfully: %s, file: %s.' 
            % (name, payroll_file))
