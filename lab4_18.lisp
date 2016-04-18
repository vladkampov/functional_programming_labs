(defun makeNewList (lst1 lst2)
  (cond
  	((null lst1) nil)
  	((null lst2) nil)
  	((and (null (cdr lst1)) (null (cdr lst2))) (list (list (car lst2) (car lst1) (car lst2))))
  	(t (append (list (list (car lst2) (car lst1) (car lst2))) (makeNewList (cdr lst1) (cdr lst2))))
  )
)