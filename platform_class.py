class platform(object):
    def __init__(self, coords):
        self.xpos = coords[0]
        self.ypos = coords[1]
        self.colour = color(random(256), random(256), random(256))
        
    def display(self):
        strokeWeight(7)
        stroke(self.colour)
        fill(self.colour)
        line(self.xpos, self.ypos, self.xpos+105, self.ypos)
        quad(self.xpos + 10, self.ypos, self.xpos + 85 + 10, self.ypos, self.xpos + 70 + 10, self.ypos+20, self.xpos + 15 + 10, self.ypos+20)
        # arc(self.xpos + self.xpos / 2, self.ypos, 75, 75, radians(0), radians(180));
        
    def destroy(self):
        self.xpos = 600
