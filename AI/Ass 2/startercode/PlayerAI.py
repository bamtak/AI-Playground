from random import randint

from BaseAI import BaseAI

import math


class PlayerAI(BaseAI):

    def getMove(self, grid):
        return self.getBestMove(grid, 4)

    def getBestMove(self, grid, depth):
        moves = grid.getAvailableMoves()
        best_move = moves[0]
        alpha = float('-inf')
        beta = float('inf')
        for i in moves:
            new_grid = grid.clone()
            new_grid.move(i)
            new_score = self.alphabeta(new_grid, depth-1, alpha, beta, max = True)
            if new_score > alpha:
                alpha = new_score
                best_move = i
        return best_move

    def alphabeta(self, grid, depth, alpha, beta, max=False):

        if depth == 0:
            return self.eval(grid)
        if max:
            moves = grid.getAvailableMoves()
            score = float('-inf')
            for i in moves:
                new_grid = grid.clone()
                new_grid.move(i)
                new_score = self.alphabeta(new_grid, depth-1, alpha, beta)
                if new_score > score:
                    score = new_score
                if score > alpha:
                    alpha = new_score
                if beta <= alpha:
                    break
            return score
        else :
            score = float('inf')
            availableCells = grid.getAvailableCells()
            for i in availableCells:
                new_grid = grid.clone()
                new_grid.insertTile(i,4)
                score1 = 0.1 * self.alphabeta(new_grid, depth-1, alpha, beta, max=True)
                new_grid2 = grid.clone()
                new_grid2.insertTile(i,2)
                score2 = 0.9 * self.alphabeta(new_grid2, depth-1, alpha, beta, max=True)
                new_score = score2 + score1
                if new_score < score:
                    score = new_score
                if score < beta:
                    beta = score
                if beta <= alpha:
                    break
            return score

    def eval(self, grid):
        smoothWeight = 1
        monoWeight  = 1 #1
        emptyWeight  = 15 #2.7
        maxWeight    = 1.0
        availableCells = grid.getAvailableCells()
        emptyCell = len(availableCells) if len(availableCells) > 0 else 1
        #return emptyCell * emptyWeight + self.evaluate(grid)
        return emptyCell * emptyWeight + self.smoothness(grid)
        #0 return math.log(emptyCell) * emptyWeight + self.clustering2(grid)
        #1 return math.log(emptyCell) * emptyWeight + self.clustering(grid)
        #2 return math.log(emptyCell) * emptyWeight + self.monotonicity(grid)
        #3 return math.log(emptyCell) * emptyWeight + self.monotonicity(grid) + self.clustering(grid)
        #4 low return emptyCell * emptyWeight + self.monotonicity(grid) + self.clustering(grid)
        #return (grid.getMaxTile()*maxWeight) + (math.log(emptyCell) * emptyWeight) #+ (self.clustering(grid)*smoothWeight) + self.monotonicity(grid)

    def smoothness(self, grid):
        smoothness = 0
        weight = 5
        for i in xrange(4):
            for j in xrange(4):
                if i == 0 and i == 2:
                    weight -=1
                else:
                    weight +=1
                smoothness += grid.getCellValue((j,i))
        return smoothness

    def monotonicity(self, grid):
        scores = [0, 0, 0, 0]

        for i in xrange(4):
            curr = 0
            next = curr + 1
            while next < 4:
                while next < 4 and grid.getCellValue((i,next)) != 0:
                    next +=1
                if next >= 4: next -= 1
                currValue = 0
                if grid.getCellValue((i,curr)) > 0 :
                    currValue = math.log(grid.getCellValue((i,curr)))/math.log(2)
                nextValue = 0
                if grid.getCellValue((i,curr)) > 0 :
                    nextValue = math.log(grid.getCellValue((i,curr)))/math.log(2)
                if currValue > nextValue:
                    scores[0] += currValue - nextValue
                if currValue < nextValue:
                    scores[1] += currValue - nextValue
                curr = next
                next +=1

        for i in xrange(4):
            curr = 0
            next = curr + 1
            while next < 4:
                while next < 4 and grid.getCellValue((next,i)) != 0:
                    next +=1
                if next >= 4: next -= 1
                currValue = 0
                if grid.getCellValue((curr,i)) > 0 :
                    currValue = math.log(grid.getCellValue((curr,i)))/math.log(2)
                nextValue = 0
                if grid.getCellValue((curr,i)) > 0 :
                    nextValue = math.log(grid.getCellValue((curr,i)))/math.log(2)
                if currValue > nextValue:
                    scores[2] += currValue - nextValue
                if currValue < nextValue:
                    scores[3] += currValue - nextValue
                curr = next
                next +=1
        return max(scores[:2]) + max(scores[2:])

    def clustering(self, grid):
        clusteringScore = 0
        weight = 6
        for i in xrange(4):
            innerweight = weight - i
            for j in xrange(4):
                clusteringScore += grid.getCellValue((i,j)) * innerweight
                innerweight -=1
        return clusteringScore

    def clustering2(self, grid):
        clusteringScore = 0
        weight = 5
        for i in xrange(4):
            clusteringScore += grid.getCellValue((i,0)) * weight + grid.getCellValue((0,i)) * weight
            weight -=1
        return clusteringScore
    def evaluate(self, grid):
        snake = []
        for i, col in enumerate(zip(*grid.map)):
            snake.extend(reversed(col) if i % 2 == 0 else col)

        m = max(snake)
        return sum(x/10**n for n, x in enumerate(snake)) - \
               math.pow((grid.getCellValue((3,0)) != m)*abs(grid.getCellValue((3,0)) - m), 2)
