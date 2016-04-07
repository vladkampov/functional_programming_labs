(DEFUN F (i)
	(COND 	((= i 1) 1)
			((= i 15) 1)
		((AND (>= i 2) (<= i 14)) (- (* 2 (F (- i 1))) (cos i)))
		((AND (>= i 16) (<= i 30)) (+ (* (sqrt (F (- i 1))) 5) (sin i)))
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