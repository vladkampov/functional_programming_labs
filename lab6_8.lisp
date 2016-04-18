(defun allSubsets (lst)
	(cond 
		((null (cdr lst)) (list nil (list (car lst))))
		(t (let ((a (car lst)) (b (allSubsets (cdr lst))))
			(append nil b (mapcar #'(lambda (x) (cons a x)) b)))
		)
	)
)