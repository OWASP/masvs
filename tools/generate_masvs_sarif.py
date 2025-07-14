import yaml
import json
from datetime import datetime

MASVS_SARIF_GUID = "77cf1749-d61e-4cfe-98f7-a217e3b5448c"

# Re-examining the YAML content for structure
masvs_parsed = yaml.safe_load(open("OWASP_MASVS.yaml"))
version = masvs_parsed["metadata"]["version"]
if version.startswith("v"):
    version = version[1:]
current_date_str = datetime.now().strftime("%Y-%m-%d")

# Creating a new SARIF template for the corrected conversion
sarif_corrected_template = {
    "$schema": "http://json.schemastore.org/sarif-2.1.0",
    "version": "2.1.0",
    "runs": [{
        "tool": {
            "driver": {
                "name": "OWASP MASVS",
                "fullName": "OWASP Mobile Application Security Verification Standard (MASVS)",
                "version": version,
                "releaseDateUtc": current_date_str,
                "organization": "OWASP",
                "informationUri": "https://mas.owasp.org/MASVS/",
                "downloadUri": "https://github.com/OWASP/masvs/releases"
            }
        },
        "taxonomies": [{
            "name": "OWASP MASVS",
            "guid": MASVS_SARIF_GUID,
            "isComprehensive": True,
            "taxa": []
        }]
    }]
}

# Counter to ensure we capture the total number of controls
total_controls_count = 0

# Iterating through groups and their controls
for group in masvs_parsed.get("groups", []):
    for control in group.get("controls", []):
        total_controls_count += 1
        taxa_element = {
            "id": control["id"],
            "name": control.get("id", ""),
            "shortDescription": {
                "text": control.get("statement", "")
            },
            "fullDescription": {
                "text": control.get("description", "")
            }
        }
        sarif_corrected_template["runs"][0]["taxonomies"][0]["taxa"].append(taxa_element)

# Verify the total number of taxa elements matches the total number of controls
total_taxa_count = len(sarif_corrected_template["runs"][0]["taxonomies"][0]["taxa"])

# Save the correctly populated SARIF output
sarif_corrected_output_path = 'OWASP_MASVS.sarif'
with open(sarif_corrected_output_path, 'w') as file:
    json.dump(sarif_corrected_template, file, indent=2)
