import os
import subprocess
import json

def get_file_properties(source):
    properties = {
        'FileVersion': '',
        'StringFileInfo': {
            'CompanyName': '',
            'ProductName': '',
            'ProductVersion': '',
            'OriginalFilename': '',
            'FileDescription': '',
            'LegalCopyright': '',
            'LegalTrademarks': ''
        }
    }

    try:
        exiftool_cmd = ['exiftool', '-json', source]
        result = subprocess.run(exiftool_cmd, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout.strip()
            data = json.loads(output)[0]
            
            properties['FileVersion'] = data.get('FileVersion', '')
            properties['StringFileInfo']['CompanyName'] = data.get('CompanyName', '')
            properties['StringFileInfo']['ProductName'] = data.get('ProductName', '')
            properties['StringFileInfo']['ProductVersion'] = data.get('ProductVersion', '')
            properties['StringFileInfo']['OriginalFilename'] = data.get('OriginalFilename', '')
            properties['StringFileInfo']['FileDescription'] = data.get('FileDescription', '')
            properties['StringFileInfo']['LegalCopyright'] = data.get('LegalCopyright', '')
            properties['StringFileInfo']['LegalTrademarks'] = data.get('LegalTrademarks', '')
    except:
        pass

    return properties


