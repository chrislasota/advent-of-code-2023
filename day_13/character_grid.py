class CharacterGrid():
    def __init__(self, list_of_strings):
        self._height = len(list_of_strings)
        self._width = len(list_of_strings[0])
        self._grid = []
        for row in range(self._height):
            temp_list = []
            for column in range(self._width):
                temp_list.append(list_of_strings[row][column])
            self._grid.append(temp_list)

    def width(self) -> int:
        return self._width

    def height(self) -> int:
        return self._height

    def _list_to_str(self, the_list) -> str:
        temp_str = ""
        for char in the_list:
            temp_str += char
        return temp_str

    def get_row_list(self, row) -> list:
        if row not in range(0, self._height):
            raise IndexError
        return self._grid[row]

    def get_row_str(self, row) -> str:
        temp_list = self.get_row_list(row)
        return self._list_to_str(temp_list)

    def get_column_list(self, col) -> list:
        if col not in range(0, self._width):
            raise IndexError
        temp_list = []
        for row in range(self._height):
            temp_list.append(self._grid[row][col])
        return temp_list

    def get_column_str(self, col) -> str:
        temp_list = self.get_column_list(col)
        return self._list_to_str(temp_list)

    def char_at(self, row, col) -> str:
        if row >= self._height:
            raise IndexError
        if col >= self._width:
            raise IndexError
        return self._grid[row][col]
