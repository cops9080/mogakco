ah, bm, ch, dm = map(int, input().split())

ab_time = 60*ah + bm
cd_time = 60*ch + dm

total_minute = cd_time - ab_time
print(total_minute)
    
