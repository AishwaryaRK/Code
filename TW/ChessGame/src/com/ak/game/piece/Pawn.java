package com.ak.game.piece;

import com.ak.game.Color;
import com.ak.game.cell.Cell;

public class Pawn extends Piece {

	public Pawn(Color color, Cell currentCell) {
		super(color, currentCell);
	}

	@Override
	protected boolean isValidMove(Cell newCell) {
		// TODO Auto-generated method stub
		return false;
	}

}
