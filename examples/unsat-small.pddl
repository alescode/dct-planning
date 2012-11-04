(define (problem p)
	(:domain unsat)
	(:objects zero
	 		obj1
			obj2
			max 
	)
	(:init
		(begin)
		(cls zero)
		(cls obj1)
		(cls obj2)
		(cls max)
		
		(var zero)
		(var obj1)		
		(var_suc zero obj1)
		(var_suc obj1 obj2)
		(var_suc obj2 max)
		
		(not_t zero)
		(not_t obj1)
		(not_t obj2)
		(not_t max)
		
        (P zero zero)
		(P obj1 zero)
		(P zero obj1)
		(N obj1 obj1)
		(N zero obj2)
		(P obj1 obj2)
		(N zero max)
        (N obj1 max)

    ;   (M obj2 zero)
	;   (M obj2 obj1)
	;   (M obj2 obj2)
	;   (M obj2 max)
    ;   (M max zero)
	;   (M max obj1)
	;   (M max obj2)
	;   (M max max)
	)
	(:goal (holds_goal)
	)
)
