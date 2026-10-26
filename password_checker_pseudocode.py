#OH, period 1, password strength checker pseudocode
#SET score to 0
#GET password from user 
#SET password to password
#IF password has 8 characters or more
    #UPDATE score +1
#IF password has at least 1 uppercase character
    #UPDATE score +1
#END IF
#IF password has at least 1 lowercase character
    #UPDATE score +1
#END IF
#IF password has at least one number
    #UPDATE score +1
#END IF
#IF password has at least one special character
    #UPDATE score +1
#END IF
#IF score is 1 OR 2
    #DISPLAY "Weak"
#END IF
#IF score is 3
    #DISPLAY "Moderate"
#IF score is 4
    #DISPLAY "Strong"
#If score is 5
    #DISPLAY "Very strong"

#For character in password
    #IF character is uppercase 
        #UPDATE score +1
    #IF character is lowercase 
        #UPDATE score + 1
    #IF character is a number
        #UPDATE
        #END IF
#END FOR
