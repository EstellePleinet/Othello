import re
import string
from .direction import Direction

class Position:
    
    def __init__(self, row: int = None, col: int = None, label: str = None):
        if label:
            self._label = label.strip().upper()
            self._from_label()
        elif row is not None and col is not None:
            self._row = row
            self._col = col
            self._to_label()
        else:
            raise ValueError("You must provide either a label or a (row, col) pair.")
    
    @property
    def row(self) -> int:
        return self._row
    
    @property
    def col(self) -> int:
        return self._col
    
    @property
    def label(self) -> str:
        return self._label

    def next_position(self, direction: Direction) -> 'Position':
        d_row, d_col = direction.value
        return Position(row=self._row + d_row, col=self._col + d_col)
    
    @staticmethod
    def is_valid_label_format(label: str) -> bool:
        return bool(re.match(r"^[A-Za-z][0-9]{1,2}$", label.strip()))
    
    def _from_label(self):
        columns = string.ascii_uppercase
        col_letter = self._label[0]
        self._col = columns.index(col_letter)
        self._row = int(self._label[1:]) - 1  # Ex: A10 → row = 9

    def _to_label(self):
        columns = string.ascii_uppercase
        letter = columns[self._col]
        number = str(self._row + 1)
        self._label = f"{letter}{number}"
    
    def __eq__(self, other) -> bool:
        return isinstance(other, Position) and self._row == other._row and self._col == other._col
    
    def __repr__(self) -> str:
        return f"Position(row={self._row}, col={self._col}, label='{self._label}')"
