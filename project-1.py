import re

def extract_medical_data(text):
    # Example regex to extract medical terms or data patterns
    patient_name = re.search(r"Patient Name: (\w+ \w+)", text)
    age = re.search(r"Age: (\d+)", text)
    diagnosis = re.search(r"Diagnosis: (.+)", text)

    data = {
        "Patient Name": patient_name.group(1) if patient_name else "N/A",
        "Age": age.group(1) if age else "N/A",
        "Diagnosis": diagnosis.group(1) if diagnosis else "N/A"
    }
    return data

# Sample medical document text
sample_text = """
Patient Name: John Doe
Age: 45
Diagnosis: Hypertension and Diabetes
"""

extracted_data = extract_medical_data(sample_text)
print("Extracted Data:")
for key, value in extracted_data.items():
    print(f"{key}: {value}")
