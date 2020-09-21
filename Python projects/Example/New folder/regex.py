import re
pattern = '^a...s$'
test_string = 'abyas'
result = re.match(pattern, test_string)

if result:
      print("Search successfuln.")
else:
      print("Search unsuccessful.")
