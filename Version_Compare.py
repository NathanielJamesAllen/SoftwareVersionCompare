import re

def validate_version(version):
    if not re.match(r'^\d{1,2}(\.\d{1,2}){0,4}$', version):
        raise ValueError("Invalid version format.")
    

def version_compare( version1, version2 ):
        validate_version(version1)
        validate_version(version2)
        
        if (version1 < version2):
            return -1
        elif (version1 == version2):
            return 0
        elif (version1 > version2):
            return 1
        
version1="2.2"
version2="2.1.0"

result=version_compare(version1,version2)
print(result)
    