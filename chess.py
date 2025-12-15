from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Pěšák se pohybuje pouze vpřed.
        Bílý: row + 1
        Černý: row - 1
        """
        row, col = self.position
        moves = []
        
        # Určení směru na základě barvy
        if self.color == 'white':
            new_position = (row + 1, col)
        elif self.color == 'black':
            new_position = (row - 1, col)
        else:
            return [] # Neznámá barva

        # Pokud je pozice na šachovnici, přidáme ji
        if self.is_position_on_board(new_position):
            moves.append(new_position)
            
        return moves
    
    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Střelec se pohybuje po diagonálách libovolně daleko.
        """
        row, col = self.position
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, 8): # Maximálně 7 políček daleko
                new_pos = (row + dr * i, col + dc * i)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break # Narazili jsme na konec desky, dál v tomto směru nejdeme
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Věž se pohybuje vertikálně a horizontálně libovolně daleko.
        """
        row, col = self.position
        moves = []
        # Směry: nahoru, dolů, doprava, doleva
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, 8):
                new_pos = (row + dr * i, col + dc * i)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Dáma kombinuje pohyb Věže a Střelce (všech 8 směrů).
        """
        row, col = self.position
        moves = []
        # Všechny směry dohromady
        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1), # Rook
            (1, 1), (1, -1), (-1, 1), (-1, -1) # Bishop
        ]

        for dr, dc in directions:
            for i in range(1, 8):
                new_pos = (row + dr * i, col + dc * i)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
                else:
                    break
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Král se pohybuje o jedno políčko do libovolného směru.
        """
        row, col = self.position
        # Relativní posuny pro krále
        offsets = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        
        final_moves = []
        for dr, dc in offsets:
            new_pos = (row + dr, col + dc)
            if self.is_position_on_board(new_pos):
                final_moves.append(new_pos)
        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    k = Knight("black", (1, 2))
    print(k)
    print(k.possible_moves())