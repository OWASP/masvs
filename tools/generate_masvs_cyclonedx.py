#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' CycloneDX converter class

    Converts the MASVS YAML into CycloneDX Standards format
    Copyright (c) 2023 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import datetime
import json
import uuid
import yaml
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

class CycloneDX:
    bom = {'bomFormat': "CycloneDX", 'specVersion': "1.6", 'serialNumber': "urn:uuid:" + str(uuid.uuid4()),
           'version': 1, 'metadata': {}}
    bom['metadata']['timestamp'] = datetime.datetime.now().astimezone().replace(microsecond=0).isoformat()
    bom['metadata']['licenses'] = []
    bom['metadata']['licenses'].append({})
    bom['metadata']['licenses'][0]['license'] = {}
    bom['metadata']['licenses'][0]['license']['id'] = "CC-BY-SA-4.0"
    bom['metadata']['licenses'][0]['license']['url'] = "https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt"
    bom['metadata']['supplier'] = {}
    bom['metadata']['supplier']['name'] = "OWASP Foundation"
    bom['metadata']['supplier']['url'] = [ "https://owasp.org" ]
    bom['definitions'] = {}
    bom['definitions']['standards'] = []
    bom['definitions']['standards'].append({})

    def __init__(self, masvs):
        bom_ref = "MASVS-" + masvs["metadata"]["version"]
        self.bom['definitions']['standards'][0]['bom-ref'] = bom_ref
        self.bom['definitions']['standards'][0]['name'] = masvs["metadata"]["title"]
        self.bom['definitions']['standards'][0]['version'] = masvs["metadata"]["version"]
        self.bom['definitions']['standards'][0]['description'] = masvs["metadata"]["remarks"]
        self.bom['definitions']['standards'][0]['owner'] = "OWASP Mobile Application Security Verification Standard Project"

        requirements = []
        for masvs_group in masvs['groups']:
            group_req = self.convert_masvs_group(masvs_group)
            requirements.append(group_req)
            if 'controls' in masvs_group:
                for masvs_control in masvs_group['controls']:
                    control_req = self.convert_masvs_control(masvs_control, group_req['bom-ref'])
                    requirements.append(control_req)

        self.bom['definitions']['standards'][0]['requirements'] = requirements
        self.bom['definitions']['standards'][0]['externalReferences'] = []
        self.bom['definitions']['standards'][0]['externalReferences'].append({})
        self.bom['definitions']['standards'][0]['externalReferences'][0]['type'] = 'website'
        self.bom['definitions']['standards'][0]['externalReferences'][0]['url'] = 'https://owasp.org/masvs'
        self.bom['definitions']['standards'][0]['externalReferences'].append({})
        self.bom['definitions']['standards'][0]['externalReferences'][1]['type'] = 'vcs'
        self.bom['definitions']['standards'][0]['externalReferences'][1]['url'] = 'https://github.com/OWASP/masvs'
        self.bom['definitions']['standards'][0]['externalReferences'].append({})
        self.bom['definitions']['standards'][0]['externalReferences'][2]['type'] = 'issue-tracker'
        self.bom['definitions']['standards'][0]['externalReferences'][2]['url'] = 'https://github.com/OWASP/masvs/issues'
        self.bom['definitions']['standards'][0]['externalReferences'].append({})
        self.bom['definitions']['standards'][0]['externalReferences'][3]['type'] = 'social'
        self.bom['definitions']['standards'][0]['externalReferences'][3]['url'] = 'https://twitter.com/OWASP_MAS'

    def convert_masvs_group(self, masvs_group):
        requirement = {}
        requirement['bom-ref'] = masvs_group['id']
        requirement['identifier'] = masvs_group['id']
        requirement['title'] = masvs_group['title']
        requirement['text'] = masvs_group['description'].replace('\n', '')
        return requirement

    def convert_masvs_control(self, masvs_control, parent):
        requirement = {}
        requirement['bom-ref'] = masvs_control['id']
        requirement['identifier'] = masvs_control['id']
        requirement['title'] = masvs_control['statement']
        requirement['text'] = masvs_control['description']
        if parent:
            requirement['parent'] = parent
        return requirement

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.bom, indent = 2, sort_keys = False, ensure_ascii=False).strip()


try:
    with open("OWASP_MASVS.yaml", 'r') as stream:
        data = yaml.safe_load(stream)
        cdx = CycloneDX(data)
        bom = cdx.to_json()
        f = open("OWASP_MASVS.cdx.json", "w")
        f.write(bom)
        f.close()
except FileNotFoundError:
    print("OWASP_MASVS.yaml not found. Be sure to run generate_masvs_yaml.py prior to running this script.")
