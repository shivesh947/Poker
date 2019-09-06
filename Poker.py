def check ( play0 ) :
	play1 = play0
	playrank = [ ]
	playdeck = [ ]
	for i in range ( 0 , 5 ) :

		if play1 [ i ] [ :-1 ] == 'J' :
			playrank.append ( 11 )
		elif play1 [ i ] [ :-1 ] == 'Q' :
			playrank.append ( 12 )
		elif play1 [ i ] [ :-1 ] == 'K' :
			playrank.append ( 13 )
		elif play1 [ i ] [ :-1 ] == 'A' :
			playrank.append ( 14 )
		else :
			playrank.append ( int ( play1 [ i ] [ :-1 ] ) )

	for i in range ( 0 , 5 ) :
		playdeck.append ( play1 [ i ] [ -1 ] )

	def kind ( n , ranks ) :
		for r in set ( ranks ) :
			if ranks.count ( r ) == n :
				return 'yes' , r
		return 'no'

	def two_pair ( p , ranks ) :
	    counts=0
	    n=len ( ranks )
	    if p == len ( set ( ranks ) ) :
	        for i in range ( n ) :
	            for j in range ( i + 1 , n ) :
	                if ranks [ i ] == ranks [ j ] :
	                    counts = counts + ranks [ i ]
	        return 'yes', counts
	    else:
	        return 'no'

	def flush ( deck ) :
		if len ( set ( deck ) ) == 1 :
			return 'yes'
		return 'no'

	def stright ( rank ) :
		a = min ( rank )
		l = sorted ( rank )
		l2 = [ a , a + 1 , a + 2 , a + 3 , a + 4 ]
		if (l2 == l) :
			return 'yes' , a + 4
		return 'no'

	def royal ( rank ) :
		l = sorted ( rank )
		a = int ( min ( l ) )
		b = int ( max ( l ) )
		if a == 10 and b == 14 :
			return 'yes'
		return 'no'

	num = 0
	res = ''

	ss = stright ( playrank )
	if flush ( playdeck ) == 'yes' and royal ( playrank ) == 'yes' :
		res = 'royal flush'
		num = 29 * 10
	elif ss [ 0 ] == 'yes' and flush ( playdeck ) == 'yes' :
		res = 'strightflush'
		num = 28 * 10 + ss [ 1 ]
	elif kind ( 4 , playrank ) [ 0 ] == 'yes' :
		res = '4 kind'
		num = 27 * 10 + kind ( 4 , playrank ) [ 1 ]
	elif kind ( 3 , playrank ) [ 0 ] == 'yes' and kind ( 2 , playrank ) [ 0 ] == 'yes' :
		res = '3kind'
		num = 26 * 10 + kind ( 3 , playrank ) [ 1 ] + kind ( 2 , playrank ) [ 1 ]
	elif flush ( playdeck ) == 'yes' :
		res = 'flush'
		num = 25 * 10
	elif ss [ 0 ] == 'yes' :
		res = 'stright'
		num = 24 * 10 + ss [ 1 ]
	elif kind ( 3 , playrank ) [ 0 ] == 'yes' :
		res = '3 kind'
		num = 23 * 10 + kind ( 3 , playrank ) [ 1 ]
	elif two_pair ( 3 , playrank )[ 0 ] == 'yes' :
		res = '2 pair'
		num = 22 * 10 + two_pair ( 3 , playrank ) [ 1 ]
	elif two_pair ( 4 , playrank )[ 0 ] == 'yes' :
		res = '1 pair'
		num = 21 * 10 + two_pair ( 4  , playrank ) [ 1 ]
	else :
		n = str ( max ( playrank ) )
		num = int ( n )
		res="highcard"
	return res , num
