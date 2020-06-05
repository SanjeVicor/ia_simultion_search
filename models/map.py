import math
from models.node import Node

class Map(object):
    def __init__(self,mtrx=[]):
        self.matrix =  mtrx
        self.available_lands = []
        self.generate_graph()
    
    def generate_graph(self):
        aux = self.matrix 
        for i in range(len(aux)):
            for j in range(len(aux[i])):
                node = Node(i,j,aux[i][j])
                self.matrix[i][j] = node

    def get_graph(self):
        return self.matrix

    def destroy(self):
        self.matrix =  []
        self.available_lands = []

    def set_land_nodes(self,category, land, path):  
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_category() == category:
                    node.set_land(land)
                    node.set_image(path)
                    self.matrix[i][j] = node

    def is_complete(self):
        ok = True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() == None:
                    ok = False
                    return ok
        return ok

    def clear_available_lands(self):
        self.available_lands.clear()

    def store_lands(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() not in self.available_lands:
                    self.available_lands.append(node.get_land())

    def get_available_lands(self):
        return self.available_lands

    def generate_costs(self,land,c):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() == land:
                    node.set_weight(c)

    def get_cost_coord(self,row,column):
        return self.matrix[row][column].get_weight()
        
    def is_complete_configuration(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_weight() == "":
                    return False
        return True
    
    def get_cost_of_land(self,land):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() == land:
                    return node.get_weight()
    
    def clear_visits(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                node.clear_visits()

    def set_goal(self,row,column):
        self.matrix[row][column].set_target()

    def set_new_neighbor(self,c_row,c_column,n_row,n_column):
        n = self.matrix[n_row][n_column]
        self.matrix[c_row][c_column].set_new_neighbor(n)
        n.set_cumulative_cost()
        #self.matrix[c_row][c_column].print_neighbors()

    def generate_euclidean(self, t_r, t_c):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                x = math.pow(( t_r - i), 2)
                y = math.pow((t_c - j), 2)
                d = math.sqrt(x+y)
                node.set_distance(d)

    def generate_manhattan(self, t_r, t_c):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                x = math.fabs(i - t_r)
                y = math.fabs(j - t_c)
                d = x+y
                node.set_distance(d)

    """
    KEYBOARD MOVEMENTS
    """
    def return_up_down(self,row,column):
        if row == -1 or row >= len(self.matrix) or self.matrix[row][column].get_weight() == None:
            return False 
        return True
        
    def return_left_right(self,row,column):
        if column == -1 or column >= len(self.matrix[0]) or self.matrix[row][column].get_weight() == None:
            return False
        return True
        
    """
    GET ALL NEIGHBORS
    """
    def is_up_down(self,row,column):
        if row == -1 or row >= len(self.matrix):
            return False 
        return True
        
    def is_left_right(self,row,column):
        if column == -1 or column >= len(self.matrix[0]):
            return False
        return True
    
    """
    NODES
    """
    def set_parent(self,p_r,p_c,c_r,c_c):
        self.matrix[c_r][c_c].set_parent(self.matrix[p_r][p_c])
    
    def get_parent(self,r,c): 
        if r == 0 and c == 0:
            return None
        return self.matrix[r][c].get_parent().get_name()

    
    def get_node(self,r,c):  
        return self.matrix[r][c]
    """
    NODE {VISIST,WEIGHT}
    """
    def set_visit(self,row,column,n_visit):
        self.matrix[row][column].add_visits(n_visit)

    def get_visits(self,row,column): 
        return self.matrix[row][column].get_visits()

    def get_weight(self,row,column):
        return self.matrix[row][column].get_weight()