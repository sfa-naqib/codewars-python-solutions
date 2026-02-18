def bouncing_ball(h, bounce, window):
    # your code
    if h>0 and bounce>0 and bounce<1 and window<h:
        count = 1
        while bounce*h > window:
            count +=2
            h = bounce*h
        return count
    return -1
        
