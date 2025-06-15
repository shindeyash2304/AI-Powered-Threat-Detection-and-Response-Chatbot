import json
import pandas as pd

# Load the JSON file
with open("enterprise-attack.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract only attack patterns
attack_patterns = [obj for obj in data["objects"] if obj.get("type") == "attack-pattern"]

# Prepare rows
rows = []
for obj in attack_patterns:
    external_refs = obj.get("external_references", [])
    mitre_ref = next((ref for ref in external_refs if ref.get("source_name") == "mitre-attack"), {})
    external_id = mitre_ref.get("external_id", "")
    
    rows.append({
        "id": external_id,
        "name": obj.get("name", ""),
        "description": obj.get("description", "").replace("\n", " ").strip(),
        "mitigation": ""  # Leave blank for now (can be filled later)
    })

# Create DataFrame and save as CSV
df = pd.DataFrame(rows)
df = df[df["id"] != ""]  # Remove blank ID rows
df.to_csv("mitre.csv", index=False)

print("✅ MITRE dataset converted to mitre.csv!")
