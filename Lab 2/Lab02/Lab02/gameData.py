"""Homework 2: Antarctic Survival game state and movement logic.
Author: Cristofer Rojas
Last updated: November 2, 2026
Description: Manages the board, neighbors, penguin movement, fish, seals,
score, and game-over conditions for the Pygame Antarctic Survival game.
"""

import random
from cell import Cell
from preferences import Preferences


class GameData:
    def __init__(self):
        """Create the board and initialize the player, food, and enemies."""
        self.board = [[Cell(row, col) for col in range(Preferences.NUM_COLS)]
                      for row in range(Preferences.NUM_ROWS)]
        self.gameover = False
        self.player = self.board[0][0]
        self.player.become_player()
        self.num_empty_cells = Preferences.NUM_CELLS - 1
        self.food = []
        self.score = 0
        self.enemies = []

    #######################
    # Game Limits Methods #
    #######################

    def at_max_food(self) -> bool:
        """Return True when the board has reached its food limit."""
        return (len(self.food) / max(1, self.num_empty_cells)
                > Preferences.MAX_FOOD)

    def at_max_enemies(self) -> bool:
        """Return True when the board has reached its enemy limit."""
        return (len(self.enemies) / max(1, self.num_empty_cells)
                > Preferences.MAX_ENEMIES)

    def set_game_over(self) -> None:
        """Mark the game as over."""
        self.gameover = True

    ##############################
    # Neighbor Retrieval Methods #
    ##############################

    def get_west_neighbor(self, cell: Cell) -> Cell:
        """Return the existing cell to the left, or None at the edge."""
        # TODO completed: columns decrease as we move left.
        if cell.get_col() == 0:
            return None
        return self.board[cell.get_row()][cell.get_col() - 1]

    def get_east_neighbor(self, cell: Cell) -> Cell:
        """Return the existing cell to the right, or None at the edge."""
        # TODO completed: columns increase as we move right.
        if cell.get_col() >= Preferences.NUM_COLS - 1:
            return None
        return self.board[cell.get_row()][cell.get_col() + 1]

    def get_north_neighbor(self, cell: Cell) -> Cell:
        """Return the existing cell above, or None at the edge."""
        # TODO completed: rows decrease as we move up.
        if cell.get_row() == 0:
            return None
        return self.board[cell.get_row() - 1][cell.get_col()]

    def get_south_neighbor(self, cell: Cell) -> Cell:
        """Return the existing cell below, or None at the edge."""
        # TODO completed: rows increase as we move down.
        if cell.get_row() >= Preferences.NUM_ROWS - 1:
            return None
        return self.board[cell.get_row() + 1][cell.get_col()]

    ###########################
    # Player Movement Methods #
    ###########################

    def move_player_right(self) -> None:
        """Move the player right if a cell exists there."""
        # TODO completed: use the neighbor helper and existing move method.
        cell = self.get_east_neighbor(self.player)
        if cell is not None:
            self.move_player_to_cell(cell)

    def move_player_left(self) -> None:
        """Move the player left if a cell exists there."""
        # TODO completed: prevent movement beyond the left boundary.
        cell = self.get_west_neighbor(self.player)
        if cell is not None:
            self.move_player_to_cell(cell)

    def move_player_up(self) -> None:
        """Move the player up if a cell exists there."""
        # TODO completed: prevent movement beyond the top boundary.
        cell = self.get_north_neighbor(self.player)
        if cell is not None:
            self.move_player_to_cell(cell)

    def move_player_down(self) -> None:
        """Move the player down if a cell exists there."""
        # TODO completed: prevent movement beyond the bottom boundary.
        cell = self.get_south_neighbor(self.player)
        if cell is not None:
            self.move_player_to_cell(cell)

    def move_player_to_cell(self, cell: Cell) -> None:
        """Move to a cell, eating food or ending the game if necessary."""
        if cell.is_food():
            self.eat_food(cell)
            self.update_player_cell(cell)
        elif cell.is_enemy():
            self.player.become_empty()
            self.num_empty_cells += 1
            self.set_game_over()
        else:
            self.update_player_cell(cell)

    def update_player_cell(self, new_cell: Cell) -> None:
        """Change the previous player cell to empty and occupy a new one."""
        self.player.become_empty()
        self.player = new_cell
        self.player.become_player()

    ########################
    # Food Related Methods #
    ########################

    def add_food(self) -> None:
        """Place fish in a randomly selected empty board cell."""
        # TODO completed: choose a random position and check occupancy.
        if self.num_empty_cells <= 0:
            return
        row = random.randrange(0, Preferences.NUM_ROWS)
        col = random.randrange(0, Preferences.NUM_COLS)
        cell = self.board[row][col]
        if cell.is_empty():
            cell.become_food()        # Mark the selected cell as fish.
            self.food.append(cell)   # Keep track of the new fish.
            self.num_empty_cells -= 1

    def eat_food(self, cell: Cell) -> None:
        """Remove eaten fish from the food list and increase the score."""
        # TODO completed: food is replaced by the player, not an empty cell.
        if cell.is_food():
            self.food.remove(cell)
            self.score += 1
            # The old player position becomes empty when movement completes;
            # therefore the number of empty cells stays unchanged.

    ##########################
    # Enemy Movement Methods #
    ##########################

    def add_enemy(self) -> None:
        """Spawn a seal in the bottom-right corner if the cell is available."""
        # TODO completed: find the specified corner, checking its contents.
        cell = self.board[Preferences.NUM_ROWS - 1][Preferences.NUM_COLS - 1]
        if cell.is_enemy():
            return                 # Never place two seals in one cell.
        if cell.is_player():
            self.set_game_over()   # A seal spawning on the penguin ends the game.
            self.player.become_empty()
            cell.become_enemy()
            self.enemies.append(cell)
        else:
            if cell.is_food():
                self.food.remove(cell)  # A seal can replace fish.
            elif cell.is_empty():
                self.num_empty_cells -= 1
            cell.become_enemy()
            self.enemies.append(cell)

    def move_enemy_to_cell(self, enemy_cell: Cell,
                           cell: Cell, idx: int) -> None:
        """Move a seal to a valid cell, handling fish and player collisions."""
        # TODO completed: avoid stacking seals or leaving the board.
        if cell is None or cell.is_enemy():
            return
        if cell.is_player():
            self.set_game_over()   # Seal catches the penguin.
        elif cell.is_food():
            self.food.remove(cell) # Seal consumes/replaces fish.
        elif cell.is_empty():
            self.num_empty_cells -= 1
        enemy_cell.become_empty()  # Free the old seal position.
        self.num_empty_cells += 1
        cell.become_enemy()        # Occupy the destination.
        self.enemies[idx] = cell   # Keep the list synchronized.

    def move_enemy_left(self, idx: int) -> None:
        """Attempt to move the indexed seal one cell left."""
        # TODO completed: reuse the west neighbor helper.
        enemy = self.enemies[idx]
        self.move_enemy_to_cell(enemy, self.get_west_neighbor(enemy), idx)

    def move_enemy_right(self, idx: int) -> None:
        """Attempt to move the indexed seal one cell right."""
        # TODO completed: reuse the east neighbor helper.
        enemy = self.enemies[idx]
        self.move_enemy_to_cell(enemy, self.get_east_neighbor(enemy), idx)

    def move_enemy_up(self, idx: int) -> None:
        """Attempt to move the indexed seal one cell up."""
        # TODO completed: reuse the north neighbor helper.
        enemy = self.enemies[idx]
        self.move_enemy_to_cell(enemy, self.get_north_neighbor(enemy), idx)

    def move_enemy_down(self, idx: int) -> None:
        """Attempt to move the indexed seal one cell down."""
        # TODO completed: reuse the south neighbor helper.
        enemy = self.enemies[idx]
        self.move_enemy_to_cell(enemy, self.get_south_neighbor(enemy), idx)


if __name__ == "__main__":
    gd = GameData()
    # Test an edge case: the top-left penguin has no west neighbor.
    print(gd.get_west_neighbor(gd.player))
