(define (problem p)
	(:domain qbf)
	(:objects 			obj1 
			obj2 
			obj3 
			obj4 
			obj5 
			obj6 
			obj7 
			obj8 

	)
	(:init
		(begin)
		(suc zero obj1)
		(suc obj1 obj2)
		(suc obj2 obj3)
		(suc obj3 obj4)
		(suc obj4 obj5)
		(suc obj5 obj6)
		(suc obj6 obj7)
		(suc obj7 obj8)
		(suc obj8 max)
		(so-forall_suc_t zero obj1)
		(so-forall_zero_t zero)
		(so-forall_max_t obj1)
		(not_t zero)
		(not_t obj1)
		(not_e zero)
		(not_e obj1)
		(not_r obj2)
		(not_r obj3)
		(e obj2)
		(e obj3)
		(P obj1 zero)
		(P zero zero)
		(P obj2 zero)
		(P zero obj1)
		(P obj1 obj1)
		(P obj2 obj1)
		(P obj1 obj2)
		(N zero obj2)
		(N obj3 obj2)
		(N obj1 obj3)
		(N zero obj3)
		(P obj2 obj3)
		(N zero obj4)
		(N obj1 obj4)
		(P obj2 obj4)
		(P zero obj5)
		(P obj1 obj5)
		(N obj2 obj5)
		(P obj1 obj6)
		(P zero obj6)
		(N obj3 obj6)
		(P zero obj7)
		(P obj1 obj7)
		(N obj3 obj7)
		(N zero obj8)
		(P obj1 obj8)
		(N obj2 obj8)
		(P zero max)
		(N obj1 max)
		(P obj2 max)
	)
	(:goal (holds_goal)
	)
)