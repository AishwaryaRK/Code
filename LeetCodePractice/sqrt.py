def sqrt(A)      
  while True:
    l = 1   
    u = A                    2
    mid = int(l+(u-l)/2)     1
    sq = mid*mid             1
    if sq > A:
      u = mid - 1        
    elif sq == A:
      return sq
    else:
      next = mid+1           2
      if next*next > A:      
        return mid  
      elif next == u:
        return next
      else:
        l = next
