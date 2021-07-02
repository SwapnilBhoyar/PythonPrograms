from RegexPattern import RegexPattern
from CliniqueLogger import CliniqueLogegr
import json
import re

class CliniqueManager:
    
    def addDoctor(self):
        regexPattern = RegexPattern()
        try:
            while True:
                doctorId = input("Enter doctor id:")
                if(re.match(re.compile(regexPattern.ID_PATTERN), doctorId)):
                    break
                else:
                    print("Id entered is not valid")

            while True:
                name = input("Enter doctor name:")
                if(re.match(re.compile(regexPattern.NAME_PATTERN), name)):
                    break
                else:
                    print("Name entered is not valid")

            while True:
                availability = input("Enter availability:")
                if(re.match(re.compile(regexPattern.AVAILABILIRY_PATTERN), availability)):
                    break
                else:
                    print("availability entered is not valid(capital ltters only)")

            
            while True:
                specilization = input("Enter specialization:")
                if(re.match(re.compile(regexPattern.NAME_PATTERN), specilization)):
                    break
                else:
                    print("specialization entered is not valid")
        except Exception as e:
            print(e)

        record = {
            "doctorId": doctorId,
            "name": name,
            "availability": availability,
            "specialization": specilization
        }
        
        self.writeJsonDoctor(record)

    def writeJsonDoctor(self, newData):
        with open('doctor.json','r') as file:
            fileRead = file.read()
            fileData = json.loads(fileRead)

        with open('doctor.json', 'w') as file:
            fileData["doctorDetails"].append(newData)
            file.write(json.dumps(fileData, indent = 2))

    def addPatient(self):
        patientId = input("Enter patient id:")
        patientName = input("Enter patient name:")
        mobileNumber = input("Enter mobile number:")
        age = input("Enter age:")

        patientRecord = {
            "patientId": patientId,
            "patientName": patientName,
            "mobileNumber": mobileNumber,
            "age": age
        }

        self.writeJsonDoctor(patientRecord)

    def writeJsonDoctor(self, newPatientData):
        with open('patient.json','r') as file:
            fileRead = file.read()
            fileData = json.loads(fileRead)

        with open('patient.json', 'w') as file:
            fileData["patientDetails"].append(newPatientData)
            file.write(json.dumps(fileData, indent = 2))
            
            

    