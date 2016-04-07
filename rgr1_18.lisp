(DEFUN F (i)
	(COND 	((= i 1) 2)
			((= i 10) 1)
		((AND (>= i 2) (<= i 9)) (+ (* (log (F (- i 1))) 2) + i))
		((AND (>= i 11) (<= i 20)) (* (sqrt (F (- i 1))) (cos i)))
			(t NIL)
	)
)

(PRINT "Enter your number")
(SETQ num (read))
(COND 
(	
	(NUMBERP num) (PRINT (F num)))
	(t (PRINT "NaN"))
)