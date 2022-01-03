#way1- cache as global variable
cache={} #stores already calculated values
def memoizedadd80(n):
  if n in cache: #checks if the value is in cache, to avoid unnecesary operation
    print('found in cache')
    return cache[n]
  else:
    print('Not in cache') 
    cache[n] = n+80 #registers in cache
    return cache[n]

print(memoizedadd80(6))
print(memoizedadd80(6))

#way2- cache as local variable - prefered
def memoizeadd80():
  cache = {}

  def memoized(n):
	  if n in cache:
	    return n + 80
	  else:
	    print('Long time')
	    cache[n] = n+80
	    return cache[n]
  return memoized

memo = memoizeadd80()
print(memo(7))
print(memo(7))