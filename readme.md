# FelipedelosH

In this time i see with my eyes what happend with:

numbers = [0..N]
data = X
step = 0
for i in numbers:
    if data==1:
       print(f"END\n Steps:{step}")
       break
    if data%2==0:
       data = data / 2
    else:
       data = (data*3)+1

    step = step + 1
       