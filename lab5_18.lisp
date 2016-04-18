(defun intersect (lst1 lst2); в оригинале ПЕРЕСЕЧЕНИЕ
	(cond
		((null lst1) nil)
		((null lst2) nil)
		((member (car lst1) lst2) (cons (car lst1) (intersect (cdr lst1) lst2)))
		(t (intersect (cdr lst1) lst2))
	)
)