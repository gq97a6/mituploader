# MITUPLOADER
Batch upload files to multiple MIT App Inventor accounts.

### How it works:
- uploads ***ALL*** files in current directory with **.aia** extension
- uploads to users listed in users.txt located in current directory

### Example users.txt:
```text
user0:AAA-BBB-CCC-DDD
user1:AAA-BBB-CCC-DDD
user2:AAA-BBB-CCC-DDD
```

### Example working three:
```text
├── group1
|   ├── mituploader.exe
|   ├── users.txt
|   ├── file01.aia
|   ├── file11.aia
│   └── file21.aia
|
├── group2
|   ├── mituploader.exe
|   ├── users.txt
|   ├── file02.aia
|   ├── file12.aia
│   └── file22.aia
|
├── group3
|   ├── mituploader.exe
|   ├── users.txt
|   ├── file03.aia
|   ├── file13.aia
│   └── file23.aia
```
