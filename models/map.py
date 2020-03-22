from models.node import Node

class Map(object):
    def __init__(self, mtrx=[], name="", path=""):
        self.matrix =  mtrx
        self.name = name
        self.path = path
        self.available_lands = []
        self.generate_graph()
        #self.first = None
        #self.end = None


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def generate_graph(self):
        aux = self.matrix
        #print("GENERACION DE GRAFO")
        for i in range(len(aux)):
            for j in range(len(aux[i])):
                node = Node(i,j,aux[i][j])
                self.matrix[i][j] = node
    
    def generate_graph_connections(self):
        for i in range(len(aux)):
            for j in range(len(aux[i])):
                node = Node(i,j,aux[i][j])
                try:
                    if i-1 != -1:
                        node.set_new_neighbor(self.matrix[i-1][j])
                except:
                    pass
                try:
                    node.set_new_neighbor(self.matrix[i+1][j])
                except:
                    pass
                try:
                    if j-1 != -1:
                        node.set_new_neighbor(self.matrix[i][j-1])
                except:
                    pass
                try:
                    node.set_new_neighbor(self.matrix[i][j+1])
                except:
                    pass

                #for e in node.get_neighbors():
                    #print("Nodo : ", str(node.get_coord_x()),", ", str(node.get_coord_y()))
                    #print(str(e.get_coord_x()),", ", str(e.get_coord_y()))

    def generate_costs(self,land,c):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() == land:
                    node.set_weight(c)

    def get_cost_of_land(self,land):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() == land:
                    return node.get_weight()
    
    def get_cost_coord(self,row,column):
        return self.matrix[row][column].get_weight()

    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                print(node.get_land())
                print(node.get_weight())
                print(i)
                print(j)
                print("---------")

    def is_complete_configuration(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_weight() == "":
                    return False
        return True

    def get_graph(self):
        return self.matrix

    def is_complete(self):
        ok = True
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() == None:
                    ok = False
                    return ok
        return ok
    
    def store_lands(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_land() not in self.available_lands:
                    self.available_lands.append(node.get_land())

    def get_available_lands(self):
        return self.available_lands
    
    def clear_available_lands(self):
        self.available_lands.clear()
        
    def set_land_node(self,coords,land, path):
        #self.matrix[coords[0]][coords[1]].
        self.matrix[coords[0]][coords[1]].set_land(land)
        self.matrix[coords[0]][coords[1]].set_image(path)

    def set_land_nodes(self,category, land, path): 
        print(category)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                if node.get_category() == category:
                    node.set_land(land)
                    node.set_image(path)
                    self.matrix[i][j] = node

    def set_goal(self,row,column):
        self.matrix[row][column].set_target()

    def clear_visits(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                node = self.matrix[i][j]
                node.clear_visits()

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
    
    def set_visit(self,row,column,n_visit):
        self.matrix[row][column].add_visits(n_visit)

    def get_visits(self,row,column): 
        return self.matrix[row][column].get_visits()

    def get_weight(self,row,column):
        return self.matrix[row][column].get_weight()