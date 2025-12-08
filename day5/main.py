# Read the file and process the data
with open('data.txt', 'r') as file:
    fresh_ID = []
    available_ID = []
    blank_line_found = False
    
    for line in file:
        line = line.strip()
        
        if not line:
            blank_line_found = True
            continue
        
        if not blank_line_found:
            # Split by '-' and create tuple
            parts = line.split('-')
            fresh = (int(parts[0]), int(parts[1]))
            fresh_ID.append(fresh)
        else:
            # Split by ',' and add integers to list
            ID = [int(x) for x in line.split(',')]
            available_ID.append(ID)

print(fresh_ID)
print(available_ID)

###### Part 1 #######
n_available_ID=0

fresh_ID.sort(key=lambda x: x[0])
for id in available_ID: 
    for fresh in fresh_ID:
        if fresh[0]<=id[0] and fresh[1]>=id[0]:
            n_available_ID+=1
            break
        elif fresh[0]>id[0]:
            break


print(n_available_ID)

##### Part 2  #######

n_total_fresh_ID=0
new_fresh_ID=[]

prev_fresh = fresh_ID[0]

for fresh in fresh_ID[1:]:
    print(prev_fresh, fresh)
    if fresh[0]<=prev_fresh[1]+1:
        # Merge intervals
        new_ID = (prev_fresh[0], max(prev_fresh[1], fresh[1]))
        prev_fresh = new_ID
    else:
        new_fresh_ID.append(prev_fresh)
        prev_fresh = fresh 

    print("New:", new_fresh_ID)

new_fresh_ID.append(prev_fresh)
print(new_fresh_ID)

for fresh in new_fresh_ID:
    n_total_fresh_ID += fresh[1]-fresh[0]+1

print(n_total_fresh_ID)