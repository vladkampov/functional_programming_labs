(defun phi (x)
	(if (null x) '(nil) 
		(let* (
				(q 0)
				(lst '())

			)
			(loop for i from 1 to x
				do (setq lst (append lst (list i)))
			)
			(mapcar (lambda (i) 
				(if (= (gcd x i) 1) (setq q (+ q 1)))
				) lst
			)
			q
		)
	)
)