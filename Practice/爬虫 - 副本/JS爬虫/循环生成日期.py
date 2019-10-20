
url1 = 'month='
for i in range(2014,2019):
      for j in range(1,13):
              f='0'+str(j) if j<=9 else str(j)
              url=url1+str(i)+f
              print(url)
              
              
