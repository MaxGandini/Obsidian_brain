Theorem: given $S$ a subspace of a vectorial space.
With an inner product $V$ , v $\in$ S, y $\in$ $V$ , it's equivalent:

- 1) $||y-v|| = min {|y-S|}$ ; s $\in$ S
- 2) $<y-v,s> = 0$ ; $\forall s \in S$ 

1) => 2) : 

$||y-v||^2 <= ||y-(v+s)||^2 =  ||(y-v)-s)||^2$
$=<(y-v)-s , (y-v)-s>$
$=||y-v||^2 -2<y-v,s>+ ||s||^2$

=> $2<y-v,s> =< ||s||^2$

2) => 1) :

if $y-v \perp s$ then $\forall s \in S$ :

y-v perpendicular to v-s

$||y-v||^2 <= ||(y-v)+(v+s)||^2$ 
$= <(y-v) + (v+s) ; (y-v) + (v+s)>$
$<y-v,s> = 0$ $\forall s \in S$ 

![[least_sq.png]]

We have a function :
$$ \phi (x) = \sum_j \alpha_j \phi_j (x) $$
and we find it so that :

$$\sum_i w_i (y_i - \phi (x))^2 $$
 