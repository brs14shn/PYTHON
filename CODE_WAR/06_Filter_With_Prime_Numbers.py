
#all==>- all(iterable => Boolean sonuç döndürür. 
# Bütün values true ise veya boş ise true döndürür. Haricinde false döndürür.
#filter(Function,iterable)

"""Filter ve all fonksiyonları ile asal sayı bulma"""



primes=list(filter(lambda x:all(x%y!=0 for y in range(2,x)),range(2,10)))

#Output==>[2,3,5,7]


