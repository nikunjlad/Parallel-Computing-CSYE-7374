from Script_1 import sum_cube
from Script_2 import mult_by_twoPower
from Script_3 import cube_root
from multiprocessing import Pool

if __name__== '__main__':
	numbers = [1,2,3,4,5]
	p = Pool()
	result1 = p.map(sum_cube, numbers)
	print(result1)
	
	number=[1,2,3,4]
	result2= p.map(mult_by_twoPower, number)
	print(result2)
	
	number=[9,6,16]
	result3= p.map(cube_root, number)
	print(result3)

	p.close()
	p.join()