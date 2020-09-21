a = ['monday','tue','wed','thurs','fri','sat','sun']
a_len = len(a)
iterate = iter(a)
for i in range(0,a_len):
    print(next(iterate))

print("==============")

for i in a:
    print(i)