from itertools import combinations

n_attendees, n_topics = [int(x) for x in input().split(' ')]


#creating a list of indices to create combinations later on
attendees = list()
indices = list()
for i in range(n_attendees):
    indices.append(i)
    attendees.append(input())

#combinations of all indices
r = 2
combs = list(combinations(indices,r))

max_topics = 0
max_teams = 0

#compare each combination and find the best team
for i in combs:
    topics = 0
    x,y = i
    x = attendees[x]
    y = attendees[y]
    for i in range(n_topics):
        if x[i] == '1' or y[i] == '1':
            topics +=1
        elif x[i] == '0' and y[i] == '0':
            pass
    if topics == max_topics:
        max_teams +=1
    elif topics > max_topics:
        max_topics = topics
        max_teams = 1

print(max_topics)
print(max_teams)
