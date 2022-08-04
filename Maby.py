from freegames import vector;
import pygame;
import time;
from pygame.locals import *;
import math,random,sys;
from hit import *;
import os;
from pickle import *;
path =str(os.getcwd());
try:
	f=open(path+'\\savedata.pnes');
	f.close();
except IOError:
	open('savedata.pnes','w');
try:
	load(open('savedata.pnes','rb'));
except EOFError:
	dump([0,0,0],open('savedata.pnes','wb'));
savedata = load(open('savedata.pnes','rb'));
px,py,pxx,pyy = 0,0,0,0;
dex = 5;
global devmode;
devmode = True;
def deathl(self):
	global y;
	global x;
	global bx;
	global by;
	global tallgooms;
	global starttallgooms;
	global buffgooms;
	global startbuffgooms;
	global startcoins;
	global coins;
	global firegooms;
	global startfiregooms;
	global startoctogooms;
	global octogooms;
	global bosslevel;
	global boss;
	iboss=True;
	try:
		self.type;
	except AttributeError:
		iboss=False;
	if bosslevel ==False or iboss:
		x,y=startx,starty;
	else:
		x,y = boss.x,boss.y;
	if iboss:
		self.x=self.startx if boss.type != 3 else self.x;
		self.y=self.starty if boss.type != 3 else self.y;
		self.health=3;
	tallgooms = [];
	buffgooms = [];
	firegooms = [];
	octogooms=[];
	for i in starttallgooms:
		tallgooms.append(tallgoom(i.x,i.y));
	for i in startbuffgooms:
		buffgooms.append(buffgoom(i.x,i.y));
	coins = [];
	for i in startcoins:
		coins.append(coin(i.x,i.y));
	for i in startfiregooms:
		firegooms.append(firegoom(i.x,i.y));
		firegoom.fireball=0;
	for i in startoctogooms:
		octogooms.append(octogoom(i.x,i.y));
	if iboss:
		return self;

def savequit():
	global level;
	global tscore;
	global gameslow;
	dump([level,tscore,gameslow], open('savedata.pnes','wb'));
	pygame.quit();
def save():
	global level;
	global tscore;
	global gameslow;
	dump([level,tscore,gameslow], open('savedata.pnes','wb'));
def checklevel():
	global done;
	global level;
	global tklevel;
	if tklevel < level:
		done = True;
class finalboss(object):
	def __init__(self, x,y):
		self.startx=x;
		self.starty=y;
		self.x,self.y=0,0;
		self.x+=self.startx;
		self.y+=self.starty;
		self.mov = 0.07;
		self.nop = 0.1;
		self.by = 80;
		self.bx = 40;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 500;
		self.type = 5;
		self.health = 5;
		self.dist=0;
		self.fireballs = [];
	def draw(self,screen):
		global fbsp;
		screen.blit(fbsp,(int(self.x),int(self.y)));
		#pygame.draw.rect(screen,(255,0,255),pygame.Rect(self.x,self.y,self.bx,self.by));
		for fireball in self.fireballs:
			fireball.draw(screen);
	def move(self):
		global x;
		global y;
		global bx;
		global by;
		#if y+by < self.y+self.by:
			#self.y-=self.nop/2;
		#elif y > self.y:
			#self.y+=self.nop/2;
		#if not int(x) in range(int(self.x),int(self.x+self.bx)) and int(y) in range(int(self.y),int(self.y+self.by)) or int(y+by) in range(int(self.y),int(self.y+self.by)):
		if x+bx//2 > self.x+self.bx//2:
			self.x+=self.mov;
		elif x+bx//2 < self.x+self.bx//2:
			self.x-=self.mov;
	def gravity(self):
		pass;
	def fire(self):
		global x;
		global y;
		global bx;
		global by;
		global dex;
		if not self.dist >0:
			self.fireballs.append(projectile(round(self.x+self.bx//2),round(self.y+self.by//4),6,(255,100,0)));
			self.pmx,self.pmy = round(self.x+self.bx//2),round(self.y+self.by//4);
		#print(self.dist);
		for fireball in self.fireballs:
			if fireball.done == False:
				self.radians = math.atan2(y+bx//2-self.pmy,x+bx//2-self.pmx);
				self.dist = 200#int(disten);
				fireball.dx = math.cos(self.radians);
				fireball.dy = math.sin(self.radians);
				fireball.done = True;		
			if not (0 < fireball.x < 500 and 0 < fireball.y < 500 and not hitbox(fireball.x,fireball.y)):
				self.fireballs.pop(self.fireballs.index(fireball));
			elif self.dist:
				fireball.x+=fireball.dx/dex;
				fireball.y+=fireball.dy/dex;
			else:
				fireball.x += fireball.dx/dex;
				fireball.y +=fireball.dy/dex;
		if self.dist:
			self.dist -=1/dex;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		global startoctogooms;
		global octogooms;
		global bosslevel;
		global boss;
		if((int(y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))) or ((int(y+by) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx)))):
			self = deathl(self);
			self.health=5;
		for fireball in self.fireballs:
			fireball.killmaby();
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global boss;
		global jumpn;
		global jumpmon;
		global nop;
		global nomp;
		global done;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			y+=200;
			jumpn = True;
			nomp=True;
			self.health-=1;
			if self.health==0:
				score+=self.score;
				self.type=0;
				bosslevel=False;
				done=True;
				boss=0;
class octoboss(object):
	def __init__(self, x,y):
		self.startx=x;
		self.starty=y;
		self.x,self.y=0,0;
		self.x+=self.startx;
		self.y+=self.starty;
		self.mov = 0.05;
		self.nop = 0.1;
		self.by = 20;
		self.bx = 20;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 100;
		self.type = 4;
		self.health = 3;
	def draw(self,screen):
		global bosp;
		screen.blit(bosp,(int(self.x),int(self.y)));
		#pygame.draw.rect(screen,(255,0,255),pygame.Rect(self.x,self.y,self.bx,self.by));
	def move(self):
		global x;
		global y;
		global bx;
		global by;
		if y+by < self.y+self.by:
			self.y-=self.nop/2;
		elif y > self.y:
			self.y+=self.nop/2;
		if not int(x) in range(int(self.x),int(self.x+self.bx)) and int(y) in range(int(self.y),int(self.y+self.by)) or int(y+by) in range(int(self.y),int(self.y+self.by)):
			if x+bx//2 > self.x+self.bx//2:
				self.x+=self.mov;
			elif x+bx//2 < self.x+self.bx//2:
				self.x-=self.mov;
	def gravity(self):
		pass;
		if (wet(self.x,self.y) or wet(self.x+bx,self.y)):
			self.jumpn=False;
			self.nomp=False;
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False and not (wet(self.x,self.y) or wet(self.x+bx,self.y)):
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		global startoctogooms;
		global octogooms;
		global bosslevel;
		global boss;
		if((int(y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))) or ((int(y+by) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx)))):
			self = deathl(self);
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global boss;
		global jumpn;
		global jumpmon;
		global nop;
		global nomp;
		global done;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			if y>200:
				y-=300;
			else:
				y+=300;
			jumpn = True;
			nomp=True;
			self.health-=1;
			if self.health==0:
				score+=self.score;
				self.type=0;
				bosslevel=False;
				done=True;
				boss=0;
class tallboss(object):
	def __init__(self, x,y):
		self.startx=x;
		self.starty=y;
		self.type=1;
		self.x=self.startx;
		self.y=self.starty;
		self.mov = 0.1;
		self.nop = 0.1;
		self.by = 40;
		self.bx = 20;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 50;
		self.health=3;
	def draw(self,screen):
		global btsp;
		screen.blit(btsp,(int(self.x),int(self.y)));
		#pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y,self.bx,self.by));
	def move(self):
		global x;
		global y;
		global bx;
		global by;
		if not int(x) in range(int(self.x),int(self.x+self.bx)) and y>self.y:
			self.direction = -1 if (x+bx//2)-(self.x+self.bx//2) < 0 else 1;
			self.mov=0.1;
		else:
			self.direction = 1 if (x+bx//2)-(self.x+self.bx//2) < 0 else -1;
			self.mov = 0.15;
		if not hitbox(self.x+self.bx,self.y+self.by-1) and not hitbox(self.x,self.y) and self.x < 500-self.bx and self.direction == 1:
			self.x+=self.mov*self.direction;
		elif not hitbox(self.x-1,self.y) and not hitbox(self.x,self.y+self.by-1) and self.x > 0 and self.direction == -1:
			self.x+=self.mov*self.direction;
	def gravity(self):
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False:
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		if ((int(y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))) or ((int(y) in range(int(self.y),int(self.y+self.by))and int(x+bx) in range(int(self.x),int(self.x+self.bx))) or (int(y+by) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			self = deathl(self);
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global boss;
		global done;
		global jumpn;
		global nop;
		global jumpmon;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			jumpmon = nop*3;
			jumpn = True;
			nomp=True;
			self.health-=1;
			x-=self.direction*300;
			if self.health==0:
				score+=self.score;
				self.type=0;
				bosslevel=False;
				done=True;
				boss=0;
class projectile(object):
	def __init__(self,x,y,radius,color):
		self.x = x;
		self.y = y;
		self.radius = radius;
		self.color = color;
		self.dx = 0;
		self.dy = 0;
		self.done = False;
	def draw(self,screen):
		global fsp;
		screen.blit(fsp,(int(self.x-6),int(self.y-6)));
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global startfiregooms;
		global firegooms;
		global startx;
		global starty;
		global bosslevel;
		global boss;
		if (int(self.x+self.radius) in range(int(x),int(x+bx)) or int(self.x-self.radius) in range(int(x),int(x+bx)) or int(self.x) in range(int(x),int(x+bx))) and (int(self.y+self.radius) in range(int(y),int(y+by)) or int(self.y-self.radius) in  range(int(y),int(y+by)) or int(self.y) in range(int(y),int(y+by))):
			deathl(self);
class buffboss(object):
	def __init__(self, x,y):
		self.startx=x;
		self.starty=y;
		self.x=0+startx;
		self.y=0+starty;
		self.mov = 0.2;
		self.nop = 0.1;
		self.by = 20;
		self.bx = 40;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 100;
		self.vulnerable = False;
		self.health = 3;
		self.type=2;
	def draw(self,screen):
		global bb1sp;
		global bb2sp;
		if self.vulnerable:
			screen.blit(bb2sp,(int(self.x),int(self.y)));
		else:
			screen.blit(bb1sp,(int(self.x),int(self.y)));
	def move(self):
		if not self.vulnerable:
			global x;
			global y;
			global bx;
			global by;
			if int(x) in range(int(self.x-60),int(self.x+self.bx+40)) and y+by<self.y:
				self.direction = 1 if (x+bx//2)-(self.x+self.bx//2) < 0 else -1;
			else:
				self.direction = -1 if (x+bx//2)-(self.x+self.bx//2) < 0 else 1;
			if not hitbox(self.x+self.bx,self.y+self.by-1) and not hitbox(self.x,self.y) and self.x < 500-self.bx and self.direction == 1:
				self.x+=self.mov*self.direction;
			elif not hitbox(self.x-1,self.y) and not hitbox(self.x,self.y+self.by-1) and self.x > 0 and self.direction == -1:
				self.x+=self.mov*self.direction;
	def gravity(self):
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False:
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def bouncemaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global jumpmon;
		global jumpn;
		global score;
		if(((int(y+by) in range(int(self.y),int(self.y+1))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+1))and int(bx+x) in range(int(self.x),int(self.x+self.bx))))) and not self.vulnerable:
			#x,y= 1+self.x+self.bx//2,self.y-by-1;
			self.y-=500;
			self.vulnerable=True;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		global bosslevel;
		global boss;
		if((int(y+by) in range(int(self.y+3),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y+3),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			self = deathl(self);
			self.vulnerable=False;
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global boss;
		global done;
		global jumpn;
		global nop;
		global jumpmon;
		if((int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6))))) and self.vulnerable:
			jumpmon = nop;
			jumpn = True;
			nomp=True;
			self.health-=1;
			self.x=random.randint(0,480);
			if self.health==0:
				score+=self.score;
				boss=0;
				done=True;
			self.vulnerable=False;
class fireboss(object):
	def __init__(self, x,y):
		self.x=x;
		self.y=y;
		self.nop = 0.1;
		self.by = 30;
		self.bx = 20;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.score = 200;
		self.dist=0;
		self.fireballs = [];
		self.health = 3;
		self.type = 3;
	def draw(self,screen):
		global bfsp;
		screen.blit(bfsp,(int(self.x),int(self.y)));
		for fireball in self.fireballs:
			fireball.draw(screen);
	def gravity(self):
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False:
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global startfiregooms;
		global firegooms;
		global bosslevel;
		global boss;
		if((int(y+by) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			self = deathl(self);
		for fireball in self.fireballs:
			fireball.killmaby();

	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global boss;
		global jumpn;
		global jumpmon;
		global nomp;
		global done;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			jumpmon = nop*3;
			jumpn = True;
			nomp=True;
			self.health-=1;
			if self.health==0:
				score+=self.score;
				boss=0;
				done=True;
	def fire(self):
		global x;
		global y;
		global bx;
		global by;
		global dex;
		if not self.dist >0:
			self.fireballs.append(projectile(round(self.x+self.bx//2),round(self.y+self.by//4),6,(255,100,0)));
			self.pmx,self.pmy = round(self.x+self.bx//2),round(self.y+self.by//4);
		#print(self.dist);
		for fireball in self.fireballs:
			if fireball.done == False:
				self.radians = math.atan2(y+bx//2-self.pmy,x+bx//2-self.pmx);
				self.dist = 250#int(disten);
				fireball.dx = math.cos(self.radians);
				fireball.dy = math.sin(self.radians);
				fireball.done = True;		
			if not (0 < fireball.x < 500 and 0 < fireball.y < 500 and not hitbox(fireball.x,fireball.y)):
				self.fireballs.pop(self.fireballs.index(fireball));
			elif self.dist:
				fireball.x+=fireball.dx/dex;
				fireball.y+=fireball.dy/dex;
			else:
				fireball.x += fireball.dx/dex;
				fireball.y +=fireball.dy/dex;
		if self.dist:
			self.dist -=1/dex;
class firegoom(object):
	def __init__(self, x,y):
		self.x=x;
		self.y=y;
		self.nop = 0.1;
		self.by = 14;
		self.bx = 10;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.score = 20;
		self.dist=0;
		self.fireball=0;
	def draw(self,screen):
		global vsp;
		screen.blit(vsp,(int(self.x),int(self.y)));
		if self.fireball!=0:
			self.fireball.draw(screen);
	def gravity(self):
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False:
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global startfiregooms;
		global firegooms;
		global bosslevel;
		global boss;
		if((int(y+by) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			deathl(self);
		if self.fireball!=0:
			self.fireball.killmaby();
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global firegooms;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			score+=self.score;
			firegooms.pop(firegooms.index(self));
	def fire(self):
		global x;
		global y;
		global bx;
		global by;
		if not self.dist >0 and self.fireball==0:
			self.fireball = projectile(round(self.x+self.bx//2),round(self.y+self.by//4),6,(255,100,0));
			self.pmx,self.pmy = round(self.x+self.bx//2),round(self.y+self.by//4);
			if self.fireball.done == False:
				self.radians = math.atan2(y+bx//2-self.pmy,x+bx//2-self.pmx);
				self.dist = 100#int(disten);
				self.fireball.dx = math.cos(self.radians);
				self.fireball.dy = math.sin(self.radians);
				self.fireball.done = True;
		if self.fireball!=0:		
			if not (0 < self.fireball.x < 500 and 0 < self.fireball.y < 500 and not hitbox(self.fireball.x,self.fireball.y)):
					self.fireball = 0;
			elif self.dist:
				self.fireball.x+=self.fireball.dx/dex;
				self.fireball.y+=self.fireball.dy/dex;
			else:
				self.fireball.x += self.fireball.dx/dex;
				self.fireball.y +=self.fireball.dy/dex;
		self.dist -=1/dex;
class tallgoom(object):
	def __init__(self, x,y):
		self.x=x;
		self.y=y;
		self.mov = 0.05;
		self.nop = 0.1;
		self.by = 20;
		self.bx = 10;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 10;
	def draw(self,screen):
		global tsp;
		screen.blit(tsp,(int(self.x),int(self.y)));
	def move(self):
		if not hitbox(self.x+self.bx,self.y+self.by-1) and not hitbox(self.x,self.y) and self.x < 500-self.bx and self.direction == 1:
			self.x+=self.mov*self.direction;
		elif not hitbox(self.x-1,self.y) and not hitbox(self.x,self.y+self.by-1) and self.x > 0 and self.direction == -1:
			self.x+=self.mov*self.direction;
		else:
			self.direction = -self.direction;
	def gravity(self):
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False:
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		global bosslevel;
		global boss;
		if((int(y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			deathl(self);
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global tallgooms;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			score+=self.score;
			tallgooms.pop(tallgooms.index(self));
class octogoom(object):
	def __init__(self, x,y):
		self.x=x;
		self.y=y;
		self.mov = 0.05;
		self.nop = 0.1;
		self.by = 10;
		self.bx = 10;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 10;
	def draw(self,screen):
		global osp;
		screen.blit(osp,(int(self.x),int(self.y)));
		#pygame.draw.rect(screen,(255,0,255),pygame.Rect(self.x,self.y,self.bx,self.by));
	def move(self):
		if (wet(self.x,self.y) or wet(self.x+bx,self.y)):
			self.mov = 0.05;
		elif not (wet(self.x,self.y) or wet(self.x+bx,self.y)):
			self.mov = 0.01;
		if not hitbox(self.x+self.bx,self.y+self.by-1) and not hitbox(self.x,self.y) and self.x < 500-self.bx and self.direction == 1:
			self.x+=self.mov*self.direction;
		elif not hitbox(self.x-1,self.y) and not hitbox(self.x,self.y+self.by-1) and self.x > 0 and self.direction == -1:
			self.x+=self.mov*self.direction;
		else:
			self.direction = -self.direction;
	def gravity(self):
		if (wet(self.x,self.y) or wet(self.x+bx,self.y)):
			self.jumpn=False;
			self.nomp=False;
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False and not (wet(self.x,self.y) or wet(self.x+bx,self.y)):
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		global startoctogooms;
		global octogooms;
		global bosslevel;
		global boss;
		if((int(y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))) or ((int(y+by) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y//2) in range(int(self.y),int(self.y+self.by)) and ((int(x+bx) in range(int(self.x),int(self.x+self.bx))) or (int(x) in range(int(self.x),int(self.x+self.bx)))))):
			deathl(self);
	def killself(self):
		global y;
		global x;
		global by;
		global bx;
		global score;
		global octogooms;
		if(int(y+by) in range(int(-6+self.y),int(self.y-3))) and ((int(bx+x) in range(int(self.x-3),int(self.x+self.bx+6))) or (int(x) in range(int(self.x-3),int(self.x+self.bx+6)))):
			score+=self.score;
			octogooms.pop(octogooms.index(self));
class buffgoom(object):
	def __init__(self, x,y):
		self.x=x;
		self.y=y;
		self.mov = 0.15;
		self.nop = 0.1;
		self.by = 10;
		self.bx = 20;
		self.jumpn = False;
		self.nomp = False;
		self.jumpmon = self.nop;
		self.direction = -1 if random.randint(0,1) == 1 else 1;
		self.score = 5;
	def draw(self,screen):
		global bsp;
		screen.blit(bsp,(int(self.x),int(self.y)));
	def move(self):
		if not hitbox(self.x+self.bx,self.y+self.by-1) and not hitbox(self.x,self.y) and self.x < 500-self.bx and self.direction == 1:
			self.x+=self.mov*self.direction;
		elif not hitbox(self.x-1,self.y) and not hitbox(self.x,self.y+self.by-1) and self.x > 0 and self.direction == -1:
			self.x+=self.mov*self.direction;
		else:
			self.direction = -self.direction;
	def gravity(self):
		if self.y < 500-self.by and not hitbox(self.x+self.bx,self.y+self.by) and self.jumpn == False:
			if self.nomp:
				self.jumpmon = -self.nop;
			else:
				self.jumpmon = 0;
			self.jumpn = True;
		elif (hitbox(self.x+1,self.y+self.by) or hitbox(self.x+self.bx-1,self.y+self.by) or self.y >= 500-self.by) and self.jumpn == True:
			self.y-=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = self.nop;
		elif (hitbox(self.x+1,self.y) or hitbox(self.x+self.bx-1,self.y)) and self.jumpn == True:
			self.y+=1;
			self.jumpn = False;
			self.nomp = False;
			self.jumpmon = -self.nop;
		if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
			if self.jumpn:
				if self.jumpmon >= -self.nop*500:
					if not hitbox(self.x+1,self.y+1) and not hitbox(self.x+self.bx-1,self.y+self.by-1):
						self.y -= self.jumpmon * 3;
					self.jumpmon -= self.nop/800;
				else:
					self.nomp = False;
					self.jumpn = False;
	def bouncemaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global jumpmon;
		global jumpn;
		global score;
		if((int(y+by) in range(int(self.y),int(self.y+1))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y),int(self.y+1))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			#x,y= 1+self.x+self.bx//2,self.y-by-1;
			jumpmon = nop;
			jumpn = True;
			nomp=True;
			score+=self.score;
	def killmaby(self):
		global y;
		global x;
		global bx;
		global by;
		global tallgooms;
		global starttallgooms;
		global buffgooms;
		global startbuffgooms;
		global startcoins;
		global coins;
		global firegooms;
		global startfiregooms;
		global bosslevel;
		global boss;
		if((int(y+by) in range(int(self.y+3),int(self.y+self.by))and int(x) in range(int(self.x),int(self.x+self.bx))) or (int(by+y) in range(int(self.y+3),int(self.y+self.by))and int(bx+x) in range(int(self.x),int(self.x+self.bx)))):
			deathl(self);
class coin(object):
	def __init__(self, x,y):
		self.x=x;
		self.y=y;
		self.score=10;
		self.radius=6;
	def colec(self):
		global x;
		global y;
		global bx;
		global by;
		global score;
		global coins;
		if (self.x+self.radius in range(int(x),int(x+bx)) or self.x-self.radius in range(int(x),int(x+bx)) or self.x in range(int(x),int(x+bx))) and (self.y+self.radius in range(int(y),int(y+by)) or self.y-self.radius in  range(int(y),int(y+by)) or self.y in range(int(y),int(y+by))):
			score+=self.score;
			coins.pop(coins.index(self));
	def draw(self,screen):
		#pygame.draw.circle(screen,(255,255,0),(self.x,self.y), self.radius);
		screen.blit(csp,(self.x-6,self.y-6));
def dude():
	global devmode;
	global x;
	global y;
	global bx;
	global by;
	global sx;
	global sy;
	global nop;
	global jumpn;
	global jumpmon;
	global done;
	global color;
	global mov;
	global draws;
	global win;
	global nomp;
	global editor;
	global screen;
	global font;
	global xx;
	global yy;
	global xy;
	global yx;
	global disten;
	global pmx;
	global pmy;
	global dx;
	global dy;
	global px;
	global py;
	global pxx;
	global pyy;
	global startx;
	global starty;
	global score;
	global coins;
	global noo;
	global gameslow;
	global paused;
	global dex;
	global firegooms;
	global bosslevel;
	global boss;
	global tallgooms;
	global starttallgooms;
	global buffgooms;
	global startbuffgooms;
	global startfiregooms;
	global water;
	global startoctogooms;
	global octogooms;
	global death;
	global title;
	global a;
	global textures;
	global tex;
	global lsp;
	checklevel();
	if bosslevel==True:
		if boss!=0:
			if boss.type == 1:
				boss.gravity();
				boss.move();
				boss.killmaby();
				boss.killself();
			elif boss.type == 2:
				boss.gravity();
				boss.move();
				boss.bouncemaby();
				boss.killmaby();
				boss.killself();
			elif boss.type == 3:
				boss.gravity();
				boss.killmaby();
				boss.fire();
				boss.killself();
			elif boss.type == 4:
				boss.gravity();
				boss.killmaby();
				boss.move();
				boss.killself();
			elif boss.type == 5:
				boss.gravity();
				boss.killmaby();
				boss.fire();
				boss.move();
				boss.killself();
	if not paused:
		if gameslow>0:
			for i in range(1,(gameslow-1)*100):
				coin(x,y);
		else:
			time.sleep(0.000001);
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit();
		for goom in tallgooms:
			goom.gravity();
			if bosslevel==False:
				goom.killself();
			goom.move();
			goom.killmaby();
		for goom in buffgooms:
			goom.gravity();
			goom.move();
			goom.bouncemaby();
			goom.killmaby();
		for coinc in coins:
			coinc.colec();
		for goom in firegooms:
			goom.gravity();
			if bosslevel==False:
				goom.killself();
			goom.killmaby();
			goom.fire();
		for goom in octogooms:
			goom.gravity();
			if bosslevel==False:
				goom.killself();
			goom.killmaby();
			goom.move();
		if x==startx and y==starty:
			score = 0;
			y-=0.01;
		key=pygame.key.get_pressed();
		#screen.blit(sky,(0,0));
		if int(x+bx//2) in range(win[1][0],win[1][1]):
			if int(y+by//2) in range(win[2][0],win[2][1]):
				done = True;
		if y < sy-by and not hitbox(x+bx,y+by) and jumpn == False:
			if nomp:
				jumpmon = -nop;
			else:
				jumpmon = 0;
			jumpn = True;
		elif (hitbox(x+1,y+by) or hitbox(x+bx-1,y+by) or y >= sy-by) and jumpn == True:
			y-=1;
			jumpn = False;
			nomp = False;
			jumpmon = nop;
		elif (hitbox(x+1,y) or hitbox(x+bx-1,y)) and jumpn == True:
			y+=1;
			jumpn = False;
			nomp = False;
			jumpmon = -nop;
		if not hitbox(x+bx,y+by-1) and not hitbox(x+bx,y):
			if key[pygame.K_RIGHT] and x < sx-bx:
				x+=mov;
		if not hitbox(x+1,y+1) and not hitbox(x+bx-1,y+by-1):
			if not jumpn:
				if key[pygame.K_UP] and y > 0:
					jumpn = True;
					nomp = True;
			else:
				if key[pygame.K_UP] and (wet(x+bx//2,y+by+10) or wet(x+bx//2,y+by)):
					jumpmon = nop;
				if jumpmon >= -nop*sy and jumpmon <= nop*sy:
					if not hitbox(x+1,y+1) and not hitbox(x+bx-1,y+by-1):
						y = y- jumpmon if wet(x+bx//2,y+by//2) or wet(x+bx//2,y+by+10) else y- (jumpmon * 3);
					if wet(x+bx//2,y+by//2):
						jumpmon += nop/800;
					else:
						if key[pygame.K_DOWN]:
							jumpmon -= nop/100;
						else:
							jumpmon -= nop/800;
					if wet(x+bx//2,y+by+10) and jumpmon > 0 and not wet(x+bx//2,y+by):
						jumpmon =-nop/800;
				else:
					nomp = False;
					jumpn = False;
		if not hitbox(x,y+by) and not hitbox(x+bx-1,y+by):
			if key[pygame.K_DOWN] and y < 500 and wet(x+bx//2,y+by//2):
				jumpmon = -jumpmon/2 if jumpmon > 0 else jumpmon;
				if jumpmon > -nop/800:
					jumpmon-=nop; 
			elif y < 500 and wet(x+bx//2,y+by//2):
				jumpmon = -jumpmon if jumpmon < 0 else jumpmon;
		if not hitbox(x-1,y) and not hitbox(x,y+by):
			if key[pygame.K_LEFT] and x > 0:
				x-=mov;
		if key[pygame.K_SPACE]:
			print(pygame.mouse.get_pos());
		if key[pygame.K_t]:
			x,y = pygame.mouse.get_pos();
		if key[pygame.K_e]:
			if editor == True:
				editor = False;
			else:
				editor = True;
			pygame.time.delay(100);
		if key[pygame.K_ESCAPE]:
			paused=True;
			pygame.time.delay(300);
		if die(x+bx//2,y+bx//2):
			if bosslevel==False:
				x,y=startx,starty;
			else:
				x,y=boss.x,boss.y;
			tallgooms = [];
			buffgooms = [];
			firegooms = [];
			octogooms=[];
			for i in starttallgooms:
				tallgooms.append(tallgoom(i.x,i.y));
			for i in startbuffgooms:
				buffgooms.append(buffgoom(i.x,i.y));
			coins = [];
			for i in startcoins:
				coins.append(coin(i.x,i.y));
			for i in startfiregooms:
				firegooms.append(firegoom(i.x,i.y));
				firegoom.fireball=0;
			for i in startoctogooms:
				octogooms.append(octogoom(i.x,i.y));
		if editor:
			screen.fill((0,0,0));
			for i in water:
				pygame.draw.rect(screen,(0,0,255),pygame.Rect(i[0],i[2],i[1],i[3]));
			for goom in startbuffgooms:
				goom.draw(screen);
			for goom in startfiregooms:
				goom.draw(screen);
			for goom in starttallgooms:
				goom.draw(screen);
			for goom in startoctogooms:
				goom.draw(screen);
			for i in draws:
				pygame.draw.rect(screen,(0,200,0),pygame.Rect(i[0],i[2],i[1],i[3]));
			if noo ==False:
				buffgooms=[];
				tallgooms=[];
				firegooms=[];
				octogooms=[];
				noo=True;
			if key[pygame.K_p]:
				if xx+yy == 0:
					xx,yy = pygame.mouse.get_pos();
					xx,yy = int((xx/10)+0.5)*10,int((yy/10)+0.5)*10;
				elif xy+yx == 0:
					xy,yx = pygame.mouse.get_pos();
					xy,yx = int((xy/10)+0.5)*10,int((yx/10)+0.5)*10;
				else:
					xlr = [xx,xy];
					xlr.sort();
					ylr = [yy,yx];
					ylr.sort();
					xx,yy,xy,yx = xlr[0],ylr[0],xlr[1],ylr[1];
					draws.append(saps(xx,xy,yy,yx));
					xx,yy,xy,yx = 0,0,0,0;
				pygame.time.delay(200);
			if key[pygame.K_m]:
				if xx+yy == 0:
					xx,yy = pygame.mouse.get_pos();
					xx,yy = int((xx/10)+0.5)*10,int((yy/10)+0.5)*10;
				elif xy+yx == 0:
					xy,yx = pygame.mouse.get_pos();
					xy,yx = int((xy/10)+0.5)*10,int((yx/10)+0.5)*10;
				else:
					xlr = [xx,xy];
					xlr.sort();
					ylr = [yy,yx];
					ylr.sort();
					xx,yy,xy,yx = xlr[0],ylr[0],xlr[1],ylr[1];
					win = daps(xx,xy,yy,yx);
					a=win[0];
					xx,yy,xy,yx = 0,0,0,0;
				pygame.time.delay(200);
			if key[pygame.K_l]:
				if xx+yy == 0:
					xx,yy = pygame.mouse.get_pos();
					xx,yy = int((xx/10)+0.5)*10,int((yy/10)+0.5)*10;
				elif xy+yx == 0:
					xy,yx = pygame.mouse.get_pos();
					xy,yx = int((xy/10)+0.5)*10,int((yx/10)+0.5)*10;
				else:
					xlr = [xx,xy];
					xlr.sort();
					ylr = [yy,yx];
					ylr.sort();
					xx,yy,xy,yx = xlr[0],ylr[0],xlr[1],ylr[1];
					death.append(kaps(xx,xy,yy,yx));
					xx,yy,xy,yx = 0,0,0,0;
				pygame.time.delay(200);
			if key[pygame.K_w]:
				if xx+yy == 0:
					xx,yy = pygame.mouse.get_pos();
					xx,yy = int((xx/10)+0.5)*10,int((yy/10)+0.5)*10;
				elif xy+yx == 0:
					xy,yx = pygame.mouse.get_pos();
					xy,yx = int((xy/10)+0.5)*10,int((yx/10)+0.5)*10;
				else:
					xlr = [xx,xy];
					xlr.sort();
					ylr = [yy,yx];
					ylr.sort();
					xx,yy,xy,yx = xlr[0],ylr[0],xlr[1],ylr[1];
					water.append(waps(xx,xy,yy,yx));
					xx,yy,xy,yx = 0,0,0,0;
				pygame.time.delay(200);
			if key[pygame.K_r]:
				if px+py == 0 and not pxx+pyy==0:
					px,py = pygame.mouse.get_pos();
					px,py = int((px/10)+0.5)*10,int((py/10)+0.5)*10;
				elif pxx+pyy == 0:
					pxx,pyy = pygame.mouse.get_pos();
					pxx,pyy = int((pxx/10)+0.5)*10,int((pyy/10)+0.5)*10;
				else:
					px+= 20;
					pxx-=20;
					py+=20;
					pyy-=20;
					xlp = [px,pxx];
					xlp.sort();
					ylp = [py,pyy];
					ylp.sort();
					px,py,pxx,pyy = xlp[0],ylp[0],xlp[1],ylp[1];
					rmove(px,pxx,py,pyy);
					for i in draws:
						ac=0;
						bc=0;
						cc=0;
						dc=0;
						ac+=i[0];
						bc+=i[1];
						cc+=i[2];
						dc+=i[3];
						ac,bc,cc,dc = exa(ac,bc,cc,dc);
						if ac in range(px,pxx) and bc in range(px,pxx) and cc in range(py,pyy) and dc in range(py,pyy):
							draws.pop(draws.index(i));
					px,py,pxx,pyy = 0,0,0,0;
				pygame.time.delay(200);
			if key[pygame.K_s]:
				if px+py == 0 and not pxx+pyy==0:
					px,py = pygame.mouse.get_pos();
					px,py = int((px/10)+0.5)*10,int((py/10)+0.5)*10;
				elif pxx+pyy == 0:
					pxx,pyy = pygame.mouse.get_pos();
					pxx,pyy = int((pxx/10)+0.5)*10,int((pyy/10)+0.5)*10;
				else:
					px+= 20;
					pxx-=20;
					py+=20;
					pyy-=20;
					xlp = [px,pxx];
					xlp.sort();
					ylp = [py,pyy];
					ylp.sort();
					px,py,pxx,pyy = xlp[0],ylp[0],xlp[1],ylp[1];
					safe(px,pxx,py,pyy);
					for i in death:
						ac=0;
						bc=0;
						cc=0;
						dc=0;
						ac+=i[0];
						bc+=i[1];
						cc+=i[2];
						dc+=i[3];
						ac,bc,cc,dc = exa(ac,bc,cc,dc);
						if ac in range(px,pxx) and bc in range(px,pxx) and cc in range(py,pyy) and dc in range(py,pyy):
							death.pop(death.index(i));
				pygame.time.delay(200);
			if key[pygame.K_d]:
				if px+py == 0 and not pxx+pyy==0:
					px,py = pygame.mouse.get_pos();
					px,py = int((px/10)+0.5)*10,int((py/10)+0.5)*10;
				elif pxx+pyy == 0:
					pxx,pyy = pygame.mouse.get_pos();
					pxx,pyy = int((pxx/10)+0.5)*10,int((pyy/10)+0.5)*10;
				else:
					px+= 40;
					pxx-=40;
					py+=40;
					pyy-=40;
					xlp = [px,pxx];
					xlp.sort();
					ylp = [py,pyy];
					ylp.sort();
					px,py,pxx,pyy = xlp[0],ylp[0],xlp[1],ylp[1];
					dry(px,pxx,py,pyy);
					for i in water:
						ac=0;
						bc=0;
						cc=0;
						dc=0;
						ac+=i[0];
						bc+=i[1];
						cc+=i[2];
						dc+=i[3];
						ac,bc,cc,dc = exa(ac,bc,cc,dc);
						if ac in range(px,pxx) and bc in range(px,pxx) and cc in range(py,pyy) and dc in range(py,pyy):
							water.pop(water.index(i));
					px,py,pxx,pyy = 0,0,0,0;
				pygame.time.delay(200);
			if key[pygame.K_g]:
				ya,ay = pygame.mouse.get_pos()
				ya,ay = round(ya/10)*10,round(ay/10)*10;
				starttallgooms.append(tallgoom(ya,ay));
				pygame.time.delay(200);
			if key[pygame.K_o]:
				ya,ay = pygame.mouse.get_pos()
				ya,ay = round(ya/10)*10,round(ay/10)*10;
				startoctogooms.append(octogoom(ya,ay));
				pygame.time.delay(200);
			if key[pygame.K_b]:
				aa,yy = pygame.mouse.get_pos();
				aa,yy = round(aa/10)*10,round(yy/10)*10;
				startbuffgooms.append(buffgoom(aa,yy));
				pygame.time.delay(200);
			if key[pygame.K_f]:
				aa,yy = pygame.mouse.get_pos();
				aa,yy = round(aa/10)*10,round(yy/6)*6;
				startfiregooms.append(firegoom(aa,yy));
				pygame.time.delay(200);
			if key[pygame.K_k]:
				durps = [];
				output = 'daps('+str(exa(a[0],a[1],a[2],a[3]))+')';
				print(output);
				for i in draws:
					durps.append(i);
				for i in durps:
					k = durps.index(i);
					ex1,ex2,ey1,ey2 = i[0],i[1],i[2],i[3];
					ex2,ey2 = ex2+ex1,ey2+ey1;
					durps[k] = ', saps({0},{1},{2},{3})'.format(ex1,ex2,ey1,ey2);
				output = '';
				if len(durps):
					durps[0] = durps[0][durps[0].find('saps('):];
				for i in durps:
					output = output + i;
				print(output);
				durps = [];
				for i in death:
					durps.append(i);
				for i in durps:
					k = durps.index(i);
					ex1,ex2,ey1,ey2 = i[0],i[1],i[2],i[3];
					ex2,ey2 = ex2+ex1,ey2+ey1;
					durps[k] = ', kaps({0},{1},{2},{3})'.format(ex1,ex2,ey1,ey2);
				output = '';
				if len(durps):
					durps[0] = durps[0][durps[0].find('kaps('):];
				for i in durps:
					output = output + i;
				print(output);
				durps = [];
				for i in water:
					durps.append(i);
				for i in durps:
					k = durps.index(i);
					ex1,ex2,ey1,ey2 = exa(i[0],i[1],i[2],i[3]);
					durps[k] = ', waps({0},{1},{2},{3})'.format(ex1,ex2,ey1,ey2);
				output = '';
				if len(durps):
					durps[0] = durps[0][durps[0].find('waps('):];
				for i in durps:
					output = output + i;
				print(output);
				output = '';
				for i in coins:
					output=output+', coin({0},{1})'.format(i.x,i.y) if coins.index(i) != 0 else output+'coin({0},{1})'.format(i.x,i.y);
				print(output);
				output = '';
				for i in starttallgooms:
					output=output+', tallgoom({0},{1})'.format(i.x,i.y) if starttallgooms.index(i) != 0 else output+'tallgoom({0},{1})'.format(i.x,i.y);
				print(output);
				output = '';
				for i in startbuffgooms:
					output=output+', buffgoom({0},{1})'.format(i.x,i.y) if startbuffgooms.index(i) != 0 else output+'buffgoom({0},{1})'.format(i.x,i.y);
				print(output);
				output = '';
				for i in startfiregooms:
					output=output+', firegoom({0},{1})'.format(i.x,i.y) if startfiregooms.index(i) != 0 else output+'firegoom({0},{1})'.format(i.x,i.y);
				print(output);
				output='';
				for i in startoctogooms:
					output=output+', octogoom({0},{1})'.format(i.x,i.y) if startoctogooms.index(i) != 0 else output+'octogoom({0},{1})'.format(i.x,i.y);
				print(output);
			if key[pygame.K_c]:
				xc,xy=pygame.mouse.get_pos();
				xc,xy=round(xc/10)*10,round(xy/10)*10;
				coins.append(coin(xc,xy));
				pygame.time.delay(200);
			if key[pygame.K_x]:
				mxm,mym = pygame.mouse.get_pos();
				for goom in starttallgooms:
					if mxm in range(int(goom.x),int(goom.x+goom.bx)) and mym in range(int(goom.y),int(goom.y+goom.by)):
						starttallgooms.pop(starttallgooms.index(goom));
				for goom in startbuffgooms:
					if mxm in range(int(goom.x),int(goom.x+goom.bx)) and mym in range(int(goom.y),int(goom.y+goom.by)):
						startbuffgooms.pop(startbuffgooms.index(goom));
				for goom in startfiregooms:
					if mxm in range(int(goom.x),int(goom.x+goom.bx)) and mym in range(int(goom.y),int(goom.y+goom.by)):
						startfiregooms.pop(startfiregooms.index(goom));
				for goom in startoctogooms:
					if mxm in range(int(goom.x),int(goom.x+goom.bx)) and mym in range(int(goom.y),int(goom.y+goom.by)):
						startoctogooms.pop(startoctogooms.index(goom));
		elif noo==True:
			tex = True;
			xx,yy,xy,yx,px,py,pxx,pyy=0,0,0,0,0,0,0,0;
			for i in starttallgooms:
				tallgooms.append(tallgoom(i.x,i.y));
			for i in startbuffgooms:
				buffgooms.append(buffgoom(i.x,i.y));
			for i in startfiregooms:
				firegooms.append(firegoom(i.x,i.y));
				firegoom.fireball=0;
			for i in startoctogooms:
				octogooms.append(octogoom(i.x,i.y));
			noo=False;
		if tex:
			textures = pygame.Surface((500,500));
			textures.fill((153,217,234));
			for i in water:
				textures.blit(wsp,(i[0],i[2]),(i[0],0,i[1],i[3]));			
			for i in draws:
				textures.blit(back,(i[0],i[2]),(i[0],0,i[1],i[3]));
			for i in death:
				textures.blit(lsp,(i[0],i[2]),(i[0],0,i[1],i[3]));
			deathl(0);
			tex=False;
		elif not editor:
			screen.blit(textures,(0,0));
		'''
		if not editor:
			for i in water:
				#pygame.draw.rect(screen,(0,0,255),pygame.Rect(i[0],i[2],i[1],i[3]));
				screen.blit(wsp,(i[0],i[2]),(0,0,i[1],i[3]));			
		for i in draws:
			#pygame.draw.rect(screen,(0,200,0),pygame.Rect(i[0],i[2],i[1],i[3]));
			screen.blit(back,(i[0],i[2]),(0,0,i[1],i[3]));
		
		for i in death:
			pygame.draw.rect(screen,(255,0,0),pygame.Rect(i[0],i[2],i[1],i[3]));
		'''
		if devmode:
			hapnu = font.render("editor: {}".format(editor),1,((0,255,0)));
			screen.blit(hapnu,(12,467));
		if boss !=0:
			scoreb = gameFont.render("Score: {0}  Total Score: {1}  Boss Health: {2} ".format(score,tscore,boss.health),1,gameFontColor);
		else:
			scoreb = gameFont.render("Score: {0}  Total Score: {1}".format(score,tscore),1,gameFontColor);
		screen.blit(scoreb,(9,7));
		#pygame.draw.circle(screen,(255,100,0),(250,250), 6);
		for goom in tallgooms:
			goom.draw(screen);
		for goom in buffgooms:
			goom.draw(screen);
		for coinc in coins:
			coinc.draw(screen);
		for goom in firegooms:
			goom.draw(screen);
		for goom in octogooms:
			goom.draw(screen);
		if bosslevel==True:
			if boss!=0:
				boss.draw(screen);
		pygame.draw.rect(screen,(255,255,0),pygame.Rect(a[0],a[2],a[1],a[3]));
		#pygame.draw.rect(screen,color,pygame.Rect(x,y,bx,by));
		screen.blit(man,(int(x),int(y)));
		pygame.display.update();
	else:
		global newthing;
		screen.fill((0,0,0));
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit();
		key = pygame.key.get_pressed();
		if key[K_ESCAPE]:
			paused=False;
			pygame.time.delay(300);
		m = pygame.mouse.get_pressed();
		if m[0] and gameslow!=88.285:
			mxf,myf = pygame.mouse.get_pos();
			if mxf in range(135,364) and myf in range(78,102):
				paused=False;
			elif mxf in range(130,368) and myf in range(441,463):
				savequit();
			elif mxf in range(137,366) and myf in range(155,343):
				oldthing =0+gameslow;
				newthing=str(gameslow+1);
				gameslow=88.285;
				m=(0,0,0);
			elif mxf in range(135,364) and myf in range(387,408):
					save();
		if gameslow ==88.285:
			if key[pygame.K_1]:
				newthing=newthing+'1';
				pygame.time.delay(200);
			if key[pygame.K_2]:
				newthing=newthing+'2';
				pygame.time.delay(200);
			if key[pygame.K_3]:
				newthing=newthing+'3';
				pygame.time.delay(200);
			if key[pygame.K_4]:
				newthing=newthing+'4';
				pygame.time.delay(200);
			if key[pygame.K_5]:
				newthing=newthing+'5';
				pygame.time.delay(200);
			if key[pygame.K_6]:
				newthing=newthing+'6';
				pygame.time.delay(200);
			if key[pygame.K_7]:
				newthing=newthing+'7';
				pygame.time.delay(200);
			if key[pygame.K_8]:
				newthing=newthing+'8';
				pygame.time.delay(200);
			if key[pygame.K_9]:
				newthing=newthing+'9';
				pygame.time.delay(200);
			if key[pygame.K_0]:
				newthing=newthing+'0';
				pygame.time.delay(200);
			if key[pygame.K_RETURN]:
				newthing = '1' if newthing=='' else newthing;
				gameslow=int(newthing)-1;
				pygame.time.delay(200);
			if key[pygame.K_BACKSPACE]:
				newthing=newthing[:len(newthing)-1];
				pygame.time.delay(200);
			slowm=font.render('{}|'.format(newthing),1,gameFontColor);
		screen.blit(paus,(0,0));
		if gameslow !=88.285:
			slowm=font.render('{}x'.format(gameslow+1),1,gameFontColor);
		screen.blit(slowm,(230,250));
		pygame.display.update();
def paiud():
	global screen;
	global paused;
	global paus;
	global gameslow;
	global title;
	global nuu;
	nuu = True;
	while nuu:
		if not paused:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit();
			m = pygame.mouse.get_pressed();
			if m[0]:
				mxf,myf = pygame.mouse.get_pos();
				if mxf in range(36,225) and myf in range(386,466):
					nuu=False;
				elif mxf in range(276,465) and myf in range(386,466):
					paused=True;
			screen.fill((0,0,0));
			screen.blit(title,(0,0));
			pygame.display.update();
		else:
			global newthing;
			screen.fill((0,0,0));
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit();
			key = pygame.key.get_pressed();
			m = pygame.mouse.get_pressed();
			if m[0] and gameslow!=88.285:
				mxf,myf = pygame.mouse.get_pos();
				if mxf in range(135,364) and myf in range(78,102):
					paused=False;
				elif mxf in range(130,368) and myf in range(441,463):
					savequit();
				elif mxf in range(137,366) and myf in range(155,343):
					oldthing =0+gameslow;
					newthing=str(gameslow+1);
					gameslow=88.285;
				elif mxf in range(135,364) and myf in range(387,408):
					save();
			if gameslow ==88.285:
				if key[pygame.K_1]:
					newthing=newthing+'1';
					pygame.time.delay(200);
				if key[pygame.K_2]:
					newthing=newthing+'2';
					pygame.time.delay(200);
				if key[pygame.K_3]:
					newthing=newthing+'3';
					pygame.time.delay(200);
				if key[pygame.K_4]:
					newthing=newthing+'4';
					pygame.time.delay(200);
				if key[pygame.K_5]:
					newthing=newthing+'5';
					pygame.time.delay(200);
				if key[pygame.K_6]:
					newthing=newthing+'6';
					pygame.time.delay(200);
				if key[pygame.K_7]:
					newthing=newthing+'7';
					pygame.time.delay(200);
				if key[pygame.K_8]:
					newthing=newthing+'8';
					pygame.time.delay(200);
				if key[pygame.K_9]:
					newthing=newthing+'9';
					pygame.time.delay(200);
				if key[pygame.K_0]:
					newthing=newthing+'0';
					pygame.time.delay(200);
				if key[pygame.K_RETURN]:
					newthing = '1' if newthing=='' else newthing;
					gameslow=int(newthing)-1;
					pygame.time.delay(200);
				if key[pygame.K_BACKSPACE]:
					newthing=newthing[:len(newthing)-1];
					pygame.time.delay(200);
				slowm=font.render('{}|'.format(newthing),1,gameFontColor);
			screen.blit(paus,(0,0));
			if gameslow !=88.285:
				slowm=font.render('{}x'.format(gameslow+1),1,gameFontColor);
			screen.blit(slowm,(230,250));
			pygame.display.update();
pygame.init();
pygame.mixer.init();
level=savedata[0];
tklevel=0;
paused=False;
gameslow=savedata[2];
noo=False;
tscore = savedata[1];
bosslevel=False;
boss=0;#boss(x,y,TYPE) 1=tall,2=buff,3=fire;
music = pygame.mixer.music.load('o.mp3');
lsp = pygame.image.load('l.png');
wsp =pygame.image.load('w.png');
pygame.mixer.music.play(-1);
pygame.mixer.music.set_volume(1);
back=pygame.image.load('dg.png');
title=pygame.image.load('title.png');
fbsp=pygame.image.load('m.png');
osp=pygame.image.load('o.png');
bosp=pygame.image.load('bo.png');
btsp=pygame.image.load('bt.png');
bfsp=pygame.image.load('bf.png');
bb1sp=pygame.image.load('bb1.png');
bb2sp=pygame.image.load('bb2.png');
paus = pygame.image.load('paus.png');
man = pygame.image.load('man.png');
tsp=pygame.image.load('t.png');
bsp=pygame.image.load('b.png');
fsp=pygame.image.load('f.png');
csp = pygame.image.load('c.png');
vsp = pygame.image.load('v.png');
font = pygame.font.SysFont("monospace",30);
gameFont = pygame.font.SysFont("impact",20);
gameFontColor = ((100,0,255));
pygame.display.set_icon(csp);
editor = False;
sx = 500;
sy = 500;
tallgooms = [];
HW,HH = sx/2,sy/2;
pmx, pmy = HW,HH;
dx, dy = 0,0;
disten = 0;
xx,yy,xy,yx = 0,0,0,0;
screen = pygame.display.set_mode((sx,sy));
pygame.display.set_caption("Mr. Maby and the Quest for a MacSandwich");
color = (255,0,0);
jumpn = False;
nop = 0.1;
bx = 10;
by = 20;
mov = 0.105;
paiud();
draws = [saps(270,500,400,500),saps(10,160,100,160),saps(180,200,300,320),saps(0,160,200,250),saps(300,410,110,140)];
water = []#waps(0,500,0,500)];
death = [];
win = daps(460,500,5,100);
a = win[0];
score = 0;
startcoins = [coin(150,190), coin(110,190), coin(70,190), coin(30,190), coin(330,90), coin(360,100), coin(400,100), coin(420,90), coin(310,70), coin(20,90), coin(60,90), coin(140,90), coin(100,90), coin(190,290), coin(230,300), coin(260,340), coin(270,380)]
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [tallgoom(145,480)];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(tallgoom(i.x,i.y));
startbuffgooms = [];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms = [];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
jumpmon = nop;
nomp= False;
done=False;
startx= 100;
starty= 480;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0; 
tklevel+=1;


clsn();
draws = [saps(0,40,0,120),saps(0,260,470,500), saps(350,420,470,480), saps(320,350,470,480), saps(430,500,390,400), saps(0,10,0,90), saps(10,40,0,90), saps(40,160,0,30), saps(0,360,320,340), saps(240,260,450,500), saps(340,360,310,340), saps(320,500,170,180), saps(150,180,220,340), saps(0,40,150,340), saps(120,150,180,340), saps(40,120,200,340), saps(240,500,200,210), saps(240,260,180,210)];#saps(0,260,470,500), saps(350,420,470,480), saps(320,350,470,480), saps(430,500,390,400), saps(0,10,0,90), saps(10,40,0,90), saps(40,160,0,30), saps(0,360,320,340), saps(240,500,200,210), saps(240,260,450,500), saps(340,360,310,340), saps(240,500,180,210), saps(320,500,170,180), saps(150,180,220,340), saps(0,40,150,340), saps(40,150,180,340)];
water = [];
death = [kaps(260,500,480,500), kaps(40,120,180,200), kaps(260,500,180,200)];
win = daps(450, 500, 90, 170);
a = win[0];
score = 0;
startcoins = [coin(50,90), coin(50,100), coin(50,120), coin(50,110), coin(50,130), coin(50,140), coin(50,150), coin(280,380), coin(330,460), coin(390,460), coin(360,460), coin(450,380), coin(350,300), coin(240,310), coin(190,270), coin(200,220), coin(140,170),  coin(250,170), coin(330,160), coin(380,160), coin(430,160)];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [tallgoom(210,440), tallgoom(290,290)];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
jumpmon = nop;
nomp= False;
done=False;
startx= 0;
starty= 430;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;

clsn();
draws = [];
water = [];
death = [];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
jumpmon = nop;
nomp= False;
done=False;
startx= 100;
starty= 480;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;
'''#level template
clsn();
draws = [];
water = [];
death = [];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
jumpmon = nop;
nomp= False;
done=False;
startx= 100;
starty= 480;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;
'''
#boss 1
clsn();
draws = [];
water = [];
death = [];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [tallgoom(0,480), tallgoom(100,480), tallgoom(200,480), tallgoom(300,480), tallgoom(400,480), tallgoom(500,480)];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
bosslevel=True;
boss=tallboss(250,250);
jumpmon = nop;
nomp= False;
done=False;
startx= 70;
starty= 400;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;
#boss 2
clsn();
draws = [];
water = [];
death = [];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[buffgoom(0,480), buffgoom(200,480), buffgoom(400,480), buffgoom(290,480), buffgoom(90,480)];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
bosslevel=True;
boss=buffboss(250,250);
jumpmon = nop;
nomp= False;
done=False;
startx= 70;
starty= 400;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;
#boss 3
clsn();
draws = [];
water = [waps(0,500,0,500)];
death = [];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [octogoom(480,50), octogoom(480,100), octogoom(480,150), octogoom(480,200), octogoom(480,250), octogoom(480,300), octogoom(480,350), octogoom(480,400)];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
bosslevel=True;
boss=octoboss(250,250);
jumpmon = nop;
nomp= False;
done=False;
startx= 70;
starty= 400;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;
#boss 4
clsn();
draws = [];
water = [];
death = [];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
startfiregooms=[firegoom(0,486), firegoom(490,486)];
firegooms = [];
for i in startfiregooms:
	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
bosslevel=True;
boss=fireboss(250,250);
jumpmon = nop;
nomp= False;
done=False;
startx= 70;
starty= 400;
x=startx;
y=starty;
tex=True;
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;

#final boss
clsn();
draws = [];
water = [waps(0,500,360,370)];
death = [kaps(0,500,0,210)];
win = daps(0,0,0,0);
a = win[0];
score = 0;
startcoins = [];
coins = [];
for i in startcoins:
	coins.append(i);
starttallgooms = [];
tallgooms = [];
for i in starttallgooms:
	tallgooms.append(i);
startbuffgooms=[];
buffgooms = [];
for i in startbuffgooms:
	buffgooms.append(buffgoom(i.x,i.y));
#startfiregooms=[firegoom(0,486), firegoom(490,486)];
firegooms = [];
#for i in startfiregooms:
#	firegooms.append(firegoom(i.x,i.y));
startoctogooms= [octogoom(490,360), octogoom(0,360)];
octogooms = [];
for i in startoctogooms:
	octogooms.append(octogoom(i.x,i.y));
bosslevel=True;
boss=finalboss(250,250);
jumpmon = nop;
nomp= False;
done=False;
startx= 70;
starty= 480;
x=startx;
y=starty;
tex=True;
print(nobe());
while not done:
	dude();
tscore+=score;
level+=1 if level == tklevel else 0;
tklevel+=1;
pygame.quit();