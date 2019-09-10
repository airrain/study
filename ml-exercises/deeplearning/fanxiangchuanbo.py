class Node(object):
    def __init__(self,layer_index, node_index):
                self.layer_index = layer_index
        self.node_index = node_index
        self.downstream = []
        self.upstream = []
        self.output = 0
        self.delta = 0
    def set_output(self,output):
        self.output = output
    def append_downstream_connection(self,conn):
        self.downstream.append(conn) 
    def append_upstream_connection(self,):
        self.upstream.append(conn)