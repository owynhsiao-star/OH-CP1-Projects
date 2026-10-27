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

#IF score is 1 OR 2
    #DISPLAY "Weak"
#IF score is 3
    #DISPLAY "Moderate"
#IF score is 4
    #DISPLAY "Strong"
#If score is 5
    #DISPLAY "Very strong"
#END IF