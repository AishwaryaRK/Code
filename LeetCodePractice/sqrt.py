def sqrt(A)      
  while True:
    l = 1   
    u = A                    
    mid = int(l+(u-l)/2)     
    sq = mid*mid             
    if sq > A:
      u = mid - 1        
    elif sq == A:
      return sq
    else:
      next = mid+1           
      if next*next > A:      
        return mid  
      elif next == u:
        return next
      else:
        l = next
