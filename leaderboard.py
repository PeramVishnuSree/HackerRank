def function(leaderboard,score):
    leaderboard.append(score)
    leaderboard.sort(reverse = True)
    for i in leaderboard:
        if leaderboard.count(i) > 1:
            leaderboard.remove(i)
    rank = leaderboard.index(score) + 1
    return rank

n = int(input())
lb = [int(x) for x in input().split(' ')]
l = int(input())
scores = [int(x) for x in input().split(' ')]
for k in scores:
    print(function(lb,k))
