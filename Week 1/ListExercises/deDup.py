# De-dup
things = ['apple', 'cheese', 'milk', 'cheese', 'bread', ]
deduped = []

for thing in things:
    if thing not in deduped: 
        deduped.append(thing)
print deduped