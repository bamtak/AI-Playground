
import time
import sys

from Astar import Astar
from BreadthFirstSearch import BreadthFirstSearch
from DepthFirstSearch import DepthFirstSearch
from IDAstar import IDAstar

from EightPuzzleProblem import EightPuzzleProblem, State

def output(content,time,file):
    o_stdout = sys.stdout
    f = open(file+'.txt', 'w')
    sys.stdout = f
    keys = [ 'path_to_goal: ', 'cost_of_path: ', 'nodes_expanded: ', 'fringe_size: ', \
    'max_fringe_size: ', 'search_depth: ', 'max_search_depth: ', 'running_time: ', 'max_ram_usage: ' ]
    for i in range(0,len(content)):
        if i == 7:
            print keys[i],time
            print keys[i+1],content[i]
        else :
            print keys[i],content[i]
    f.close()
    sys.stdout = o_stdout

if __name__ == '__main__':
    arg_size = len(sys.argv)
    argorithms = {'bfs':BreadthFirstSearch,'dfs':DepthFirstSearch,'ast':Astar,'ida':IDAstar}
    start = [int(x) for x in sys.argv[2].split(',')]
    argorithm = argorithms[sys.argv[1]]
    start_time = time.time()
    problem = EightPuzzleProblem(State(start),State([0,1,2,3,4,5,6,7,8]))
    result = argorithm(problem)
    end_time = time.time() - start_time
    output(result,end_time,sys.argv[1])
