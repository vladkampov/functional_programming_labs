(defun attOfList (item lst)
	(if lst
		(if (eql item (car lst))
			lst 
			(attOfList item (cdr lst))
		)
	)
)

(defun findDifference (lst1 lst2)
	(cond 
		((null lst1) nil)
		((null lst2) nil)
		((not (attOfList (car lst1) lst2)) (cons (car lst1) (findDifference (cdr lst1) lst2)))
		(t (findDifference (cdr lst1) lst2))
	)
)
