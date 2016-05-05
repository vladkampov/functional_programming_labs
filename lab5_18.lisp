(defun newMember (item lst)
	(if lst
		(if (eql item (car lst))
			lst 
			(newMember item (cdr lst))
		)
	)
)

(defun intersect (lst1 lst2); в оригинале ПЕРЕСЕЧЕНИЕ
	(cond
		((null lst1) nil)
		((null lst2) nil)
		((newMember (car lst1) lst2) (cons (car lst1) (intersect (cdr lst1) lst2)))
		(t (intersect (cdr lst1) lst2))
	)
)