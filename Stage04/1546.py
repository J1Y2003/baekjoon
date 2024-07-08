N = int(input())
scores = [int(x) for x in input().split()]
max_score = max(scores)

scores = [(score / max_score) * 100 for score in scores]

print(sum(scores)/len(scores))