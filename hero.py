key_switch_camera = 'c' #the camera is bound to the her or not
key_switch_mode= 'z' #can get past obstacles or not

key_forward = 'w' #fowards
key_backward = 's' #backwards
key_strafeleft = 'a' #strafe left
key_straferight = 'd' #strafe rigt
key_turn_left = 'q' #pan camera left
key_turn_right = 'e' #pan camera right

key_up = 'h' # step up
key_down = 'g' # step down


class Hero():
    def __init__(self, pos, land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setColor(1, 0.5, 0)
        self.hero.setScale(0.3)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
        

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 5, 1.7)
        self.cameraOn = True

    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False



    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()


    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)


    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)


    def look_at(self, angle):
        '''returns the coordinates which the hero at the point (x, y) moves to
        if they step towards angle'''


        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())


        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from
    
    def move_to(self, angle):
        if self.mode:
            pos = self.look_at(angle)
            self.hero.setPos(pos)
        else:
            self.try_move(angle)

    def check_dir(self, angle):
        '''returns the rounded changes in the X and Y coordinate'''
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return (0, -1)


    def forward(self):
        angle =(self.hero.getH()) % 360
        self.move_to(angle)

    def backward(self):
        angle =(self.hero.getH()+180) % 360
        self.move_to(angle)

    def strafeleft(self):
        angle =(self.hero.getH()+90) % 360
        self.move_to(angle)
    
    def straferight(self):
        angle =(self.hero.getH()+270) % 360
        self.move_to(angle)

    def changeMode(self):
        if self.mode:
            self.mode = False
        else:
            self.mode = True
            
    def try_move(self, angle):
        '''move if they can'''
        pos = self.look_at(angle)
        if self.land.isEmpty(pos):
            # there is a free space in ront of us. perheps you need to move down:
            pos = self.land.findHighestEmpty(pos)
            self.hero.setPos(pos)
        else:
            # theres no free space in front of us, if you can climb, onto that block
            pos = pos[0], pos[1], pos[2] + 1
            if self.land.isEmpty(pos):
                self.hero.setPos(pos)
                #unable to climb, we stand still

    def accept_events(self):
        base.accept(key_turn_left, self.turn_left)
        base.accept(key_turn_left + '-repeat', self.turn_left)
        base.accept(key_turn_right, self.turn_right)
        base.accept(key_turn_right + '-repeat', self.turn_right)


        base.accept(key_forward, self.forward)
        base.accept(key_forward + '-repeat', self.forward)
        base.accept(key_backward, self.backward)
        base.accept(key_backward + '-repeat', self.backward)
        base.accept(key_strafeleft, self.strafeleft)
        base.accept(key_strafeleft + '-repeat', self.strafeleft)
        base.accept(key_straferight, self.straferight)
        base.accept(key_straferight + '-repeat', self.straferight)

        
        base.accept(key_switch_camera, self.changeView)
        base.accept(key_switch_mode, self.changeMode)


