from freegames import vector;
def hitbox(x,y):
	bobnob = False;
	for i in snmps:
		if int(x) in range(i[0]-1,(i[1]+1)):
			if int(y) in range(i[2]-1,i[3]+1):
				bobnob = True;
	return bobnob;
def wet(x,y):
	bobnob = False;
	for i in wnmps:
		if int(x) in range(i[0]-1,(i[1]+1)):
			if int(y) in range(i[2]-1,i[3]+1):
				bobnob = True;
	return bobnob;
snmps = [];
wnmps = [];
dnmps = [];
def die(x,y):
	bobnob = False;
	for i in dnmps:
		if int(x) in range(i[0]-1,(i[1]+1)):
			if int(y) in range(i[2]-1,i[3]+1):
				bobnob = True;
	return bobnob;
def saps(x1,x2,y1,y2):
	snmps.append([x1,x2,y1,y2]);
	return([x1,x2-x1,y1,y2-y1]);
def kaps(x1,x2,y1,y2):
	dnmps.append([x1,x2,y1,y2]);
	return([x1,x2-x1,y1,y2-y1]);
def nobe():
	global wnmps;
	return(wnmps);
def waps(x1,x2,y1,y2):
	wnmps.append([x1,x2,y1,y2]);
	return([x1,x2-x1,y1,y2-y1]);
def exa(x1,x2,y1,y2):
	return x1,x2+x1,y1,y2+y1;
def daps(x1,x2,y1,y2):
	return [x1,x2-x1,y1,y2-y1],[x1,x2],[y1,y2];
def xes(xl):
	xed = [];
	for x in xl:
		xed.append(x.x);
	return(xed);
def yes(yl):
	yed = [];
	for y in yl:
		yed.append(y.y);
	return(yed);
def clsn():
	global snmps;
	global wnmps;
	global dnmps;
	snmps = [];
	wnmps=[];
	dnmps = [];
def rmove(x1,x2,y1,y2):
	for i in snmps:
		if i[0] in range(x1,x2) and i[1] in range(x1,x2) and i[2] in range(y1,y2) and i[3] in range(y1,y2):
			snmps.pop(snmps.index(i));
def safe(x1,x2,y1,y2):
	global dnmps;
	for i in dnmps:
		if i[0] in range(x1,x2) and i[1] in range(x1,x2) and i[2] in range(y1,y2) and i[3] in range(y1,y2):
			dnmps.pop(dnmps.index(i));
def dry(x1,x2,y1,y2):
	for i in wnmps:
		if i[0] in range(x1,x2) and i[1] in range(x1,x2) and i[2] in range(y1,y2) and i[3] in range(y1,y2):
			wnmps.pop(wnmps.index(i));