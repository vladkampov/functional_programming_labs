(defun breakByTwo (lst)
  (cond 
    ((null lst) nil) 
    ((null (cddr lst)) (list (list (car lst) (car (cdr lst)))))
    (t (append (list (list (car lst) (car (cdr lst)))) (breakByTwo (cddr lst))))
  ) 
)