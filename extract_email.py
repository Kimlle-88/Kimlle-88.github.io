#Practice Exercise (Inspired by Coursera "Python for Everybody" course)
# This is NOT an official Coursera assignment submission.
# The program reads a text file and extracts all emails found on lines
# that start with the letter 'A'. It’s meant for learning and practicing
# file handling and string processing in Python.

# Replace the path below with your own file location
# Example: fname = r"C:\path\to\email.txt"
fname = input('Enter the file name')
# try to open file safely
try:
  fh = open(fname)
except:
  print('File not found')
  quit()
# Create an empty list to store emails
lst = []
# Read each line in the file
for line in fh:
  lines = line.strip()
  if lines.startswith('A'):
 # Split the line into two parts at the first ':'
  words = lines.split(':',1)
# Split the second part (after ':') by commas
  emails = words[1].split(',')
  for email in emails:
    email = email.strip()
    lst.append(email)
# Print all collected emails
for email in lst:
  print(email)
# Show total number of emails found
print('There were', len(lst), 'emails')
