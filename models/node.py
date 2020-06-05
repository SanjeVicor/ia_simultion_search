from extra_images.load import get_black_background 
class Node(object):
    def __init__(self,x,y, category=None):
        self.x = x
        self.y = y
        self.neighbors = []
        #self.name = "(" + str(self.x +1) + "," +  (chr(self.y+ 65)) + ")"
        self.name = "(" + (chr(self.y+ 65)) + "," + str(self.x +1)  + ")"
        self.extra_data = "" #Initial, Target
        self.weight = ""
        self.cumulative_cost = 0.0
        self.distance = 0.0
        self.category = category #int
        self.land = None #string
        self.image = None
        self.target = False
        self.cover = get_black_background()
        self.visits = []
        self.parent = None

    def set_cumulative_cost(self): 
        self.cumulative_cost = self.get_parent().get_cumulative_cost() + float(self.weight)

    def set_distance(self,d):
        self.distance = d

    def get_distance(self):
        return round(self.distance,2)

    def get_cumulative_cost(self):
        return round(float(self.cumulative_cost),2)

    def get_extra_data(self):
        return self.extra_data
    
    def set_extra_data(self,d):
        self.extra_data = d

    def get_cover(self):
        return self.cover

    def set_target(self):
        self.target = True
    
    def is_target(self):
        return self.target

    def clear_visits(self):
        self.visits.clear()

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
        if len(self.neighbors) == 4:
            return
        self.neighbors.append(n)

    def remove_neighbor(self,n):
        self.neighbors.remove(n)

    def get_neighbors(self):
        return self.neighbors

    def print_neighbors(self):
        for e in self.neighbors:
            print(e.name)

    def get_neighbor(self,n=None,idx=None): 
        if idx != None:
            return self.neighbors[idx]
        elif n != None:
            for e in self.neighbors:
                if e.get_name() == n.get_name():
                    return e
        return "Error indice NULO"

    def set_parent(self,p):
        #if self.parent != None:
            #print("P-A ", self.parent.get_name())
        #print("P-N ", p.get_name())
        self.parent = p
    
    def get_parent(self):
        return self.parent