class Node(object):
    def __init__(self,x,y, category=None):
        self.x = x
        self.y = y
        self.neighbors = []
        self.name = "(" + str(self.x) + "," + str(self.y) + ")"
        self.weight = 1
        self.category = category #int
        self.land = None #string
        self.image = None
        self.target = False
        self.visits = []

    def set_target(self):
        self.target = True
    
    def is_target(self):
        return self.target

    def add_visits(self,v):
        self.visits.append(v)

    def get_visits(self):
        return self.visits

    def set_image(self,path):
        self.image = path
    
    def get_image(self):
        return self.image

    def set_land(self, land):
        self.land = land
    
    def get_land(self):
        return self.land

    def set_category(self,category):
        self.category = category
    
    def get_category(self):
        return self.category

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_weight(self,w):
        self.weight =  w

    def get_weight(self):
        return self.weight
    
    def get_coord_x(self):
        return self.x

    def get_coord_y(self):
        return self.y

    def set_new_neighbor(self,n):
        self.neighbors.append(n)

    def get_neighbors(self):
        return self.neighbors

    def get_neighbor(self,n=None,idx=None): 
        if idx != None:
            return self.neighbors[idx]
        elif n != None:
            for e in self.neighbors:
                if e.get_name() == n.get_name():
                    return e
        return "Error indice NULO"