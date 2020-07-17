# Made by Abdul Rafi Radityo Hutomo - X MIPA D - 1
# Program Gambar + Ngitung segi-N

	# Ini buat import module pak :
import turtle 
import math
		
	# Ini inputnya pak :
n=int(input("Jumlah Sisi = "))
side_length=int(input("Panjang Sisi = "))
		
	# Ini Ngitungnya Pak
angular=180-((180*(n-2))/n)
apothem=side_length/2*math.tan(math.pi/n)
radius=apothem/math.cos(math.radians(angular/2))
		
	# Ini Hasilnya pak
print("Apotema = ", apothem, "Satuan")
print("Jari-Jari = ", radius, "Satuan")
print("Luas = ", n*side_length*apothem, "Satuan")
		
	# Ini buat nulis satuan doang pak
def unit(x) :
	return (str(x) + " satuan")
	
	# Ini persiapan screenya		
t=500*math.tan(math.pi/n)
turtle.shape('turtle')
turtle.bgcolor('black')
turtle.pencolor('blue')
turtle.fillcolor('yellow')
turtle.right(90)
turtle.forward(250)
turtle.right(90)
turtle.forward((500*math.tan(math.pi/n))/2)
turtle.right(180)
turtle.begin_fill()
		
	# Ini bikin segi-n nya
for x in range(n):
	turtle.forward(t)
	turtle.left(angular)
turtle.end_fill()
		
	# Ini ngelabel yg butuh untuk di label
turtle.forward(250*math.tan(math.pi/n))
turtle.left(90)
turtle.forward(125)
turtle.write(unit(apothem), align="left")
turtle.forward(125)
turtle.right(180+180/n)
turtle.forward(200/math.cos(math.pi/n))
turtle.write(unit(radius), align="left")
turtle.forward(50/math.cos(math.pi/n))
turtle.left(90+180/n)
turtle.forward(t/2)
turtle.pencolor('black')
turtle.right(90)
turtle.forward(20)
turtle.pencolor('white')
turtle.write(unit(side_length) , align="center")
turtle.pencolor('black')
	
	# Ini selesainya
turtle.goto(-4000,-4000)
turtle.exitonclick()
