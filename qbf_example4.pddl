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
		(so-forall_suc_t obj1 obj2)
		(so-forall_zero_t zero)
		(so-forall_max_t obj2)
		(not_t zero)
		(not_t obj1)
		(not_t obj2)
		(not_e zero)
		(not_e obj1)
		(not_e obj2)
		(not_r obj3)
		(not_r obj4)
		(not_r obj5)
		(e obj3)
		(e obj4)
		(e obj5)
		(N zero zero)
		(N obj4 zero)
		(N obj5 zero)
		(N obj3 zero)
		(P obj2 obj1)
		(P obj5 obj1)
		(P obj3 obj1)
		(N obj4 obj1)
		(N obj1 obj2)
		(N obj5 obj2)
		(N obj4 obj2)
		(N obj3 obj2)
		(N obj2 obj3)
		(P obj3 obj3)
		(N obj5 obj3)
		(N obj4 obj3)
		(P obj1 obj4)
		(N obj4 obj4)
		(N obj3 obj4)
		(P obj5 obj4)
		(P zero obj5)
		(P obj4 obj5)
		(N obj5 obj5)
		(N obj3 obj5)
		(N obj2 obj6)
		(N obj3 obj6)
		(P obj5 obj6)
		(P obj4 obj6)
		(P obj1 obj7)
		(P obj4 obj7)
		(N obj3 obj7)
		(P obj5 obj7)
		(N obj1 obj8)
		(P obj5 obj8)
		(N obj3 obj8)
		(P obj4 obj8)
		(N obj1 max)
		(N obj5 max)
		(N obj3 max)
		(N obj4 max)
	)
	(:goal (holds_goal)
	)
)