from random import randint

from BaseAI import BaseAI

import math


class PlayerAI(BaseAI):

    def getMove(self, grid):
        return self.getBestMove(grid, 3)

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

    def expectimax(self, grid, depth, player = None):
        #print grid

        if depth == 0:
            availableCells = grid.getAvailableCells()
            return self.eval(grid)
        if player == 'Board':
            score = 0
            availableCells = grid.getAvailableCells()

            for i in availableCells:
                new_grid = grid.clone()
                new_grid.insertTile(i,4)
                score1 = self.expectimax(new_grid, depth-1)
                score += 0.1 * score1
                new_grid2 = grid.clone()
                new_grid2.insertTile(i,2)
                score2 = self.expectimax(new_grid2, depth-1)
                score += 0.9 * score2
            return score/len(availableCells) if len(availableCells) > 0 else 0

        else :
            score = 0
            moves = grid.getAvailableMoves()
            for i in moves:
                new_grid = grid.clone()
                new_grid.move(i)
                new_score = self.expectimax(new_grid, depth-1, player = 'Board')
                if new_score > score:
                    score = new_score
            return score
    def eval(self, grid):
        smoothWeight = 0.1
        islandWeight = 0.0
        monoWeight  = 1
        emptyWeight  = 2.7
        maxWeight    = 1.0
        availableCells = grid.getAvailableCells()
        emptyCell = len(availableCells) if len(availableCells) > 0 else 1
        score = grid.getMaxTile() + math.log(grid.getMaxTile())*len(availableCells) - self.clustering(grid)
        return (grid.getMaxTile()*maxWeight) + (math.log(emptyCell) * emptyWeight) + (self.monotonicity(grid)*monoWeight)

    def smoothness(self, grid):
        smoothness = 0
        for i in xrange(4):
            for j in xrange(4):
                if  grid.getCellValue((i,j)) != 0:
                    value = math.log(grid.getCellValue((i,j))) / math.log(2)

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
        neighbors = [-1,0,1]
        for i in xrange(4):
            for j in xrange(4):
                if grid.getCellValue((i,j)) == 0: continue

                numOfneighbors = 0
                sum = 0
                for k in neighbors:
                    x = i + k
                    if x < 0 or x > 4: continue
                    for l in neighbors:
                        y = j+l
                        if y < 0 or y > 4: continue
                        if grid.getCellValue((x,y)) > 0:
                            numOfneighbors +=1
                            sum += abs(grid.getCellValue((i,j)) - grid.getCellValue((x,y)))
                clusteringScore +=sum/numOfneighbors
        return clusteringScore
