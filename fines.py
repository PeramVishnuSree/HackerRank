sd,sm,sy = [int(x) for x in input().split(' ')]
dd,dm,dy = [int(x) for x in input().split(' ')]

if sy>dy:
    result = (sy-dy)*10000

elif sy==dy and sm>dm:
    result = (sm-dm)*500

elif sy==dy and sm==dm and sd>dd:
    result = (sd-dd)*15

else:
    result = 0

print(result)
