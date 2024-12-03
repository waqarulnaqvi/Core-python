# break statement ka matlab hai loop ko chor ke nikal jao but continue statement ka matlab hai iteration ko chor ke nikal jao.
for i in range(1,15):
    if i>10:
        print("Skip the loop")
        break

    if i==5:
        print("Skip the iteration")
        continue
    else:
        print("5 X ",i," = ",i*5 )


