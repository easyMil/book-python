#!/usr/bin/env python3
"""
The /etc/passwd file is a colon-separated file that contains the following information:
- User name
- Encrypted password
- User ID number (UID)
- User's group ID number (GID)
- Full name of the user (GECOS)
- User home directory
- Login shell
"""

FILENAME = '../tmp/etc-passwd.txt'

with open(FILENAME) as file:
    print(file.read())