#!/usr/bin/python

# Author: Artur Tamm arturt@ut.ee

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the 
# Free Software Foundation, either version 3 of the License, or (at your option) 
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY 
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along with 
# this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

counter = 0
mass = []

if (len(sys.argv) < 2):
	print "Too few arguments"
	sys.exit(1)

try:
	a=int(sys.argv[1])
except ValueError:
	print "Multiplier is not a number"
	sys.exit(1)

if(a<2):
	print "Multiplier is smaller than 2"
	sys.exit(1)

for line in sys.stdin:
	mass.append(line)
	counter = counter + 1

print mass[0],
print mass[1],

tmp=mass[2].split()

a1=float(tmp[0])
a2=float(tmp[1])
a3=float(tmp[2])

tmp=mass[3].split()

b1=float(tmp[0])
b2=float(tmp[1])
b3=float(tmp[2])

tmp=mass[4].split()

c1=float(tmp[0])
c2=float(tmp[1])
c3=float(tmp[2])

#multiply vector a by factor a
print mass[2],
print mass[3],
print str(c1*a) + "   " + str(c2*a) + "   " + str(c3*a)

print mass[5],
oldd=[int(x) for x in mass[6].split()]
newd=[a*int(x) for x in mass[6].split()]

print "   ",
for x in newd:
   print str(x) + "   ",

print ""
print mass[7],

atoms1=[]
atoms2=[]
atoms3=[]

for i in xrange(0,sum(oldd),1):
	tmp = mass[8+i].split()
	atoms1.append(float(tmp[0]))
	atoms2.append(float(tmp[1]))
	atoms3.append(float(tmp[2]))

for i in xrange(0,sum(oldd),1):
	for j in xrange(0,a,1):
		print str((atoms1[i]+j*c1)) + "   " + str(atoms2[i]+j*c2) + "   " + str((atoms3[i]+j*c3)/a)

print 

