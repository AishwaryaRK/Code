package com.ak.game.piece;

import com.ak.game.Color;
import com.ak.game.cell.Cell;

/**
 * @author akaneri Generic piece of chess board no comparisons of pieces is
 *         defined yet but can be defined later concrete pieces (rook, bishop,
 *         king, queen, knight, pawn) must extend from Piece
 */
abstract public class Piece {

	private Color color;
	private Cell currentCell;

	public Piece(Color color, Cell currentCell) {
		super();
		this.color = color;
		this.currentCell = currentCell;
	}

	/**
	 * @param newCell
	 *            - destination cell for piece to move
	 * @return - true if the piece is moved false - if move is invalid
	 */
	public final boolean move(Cell newCell) {
		if (isValidMove(newCell)) {
			setCurrentCell(newCell);
			return true;
		}
		return false;
	};

	protected abstract boolean isValidMove(Cell newCell);

	public boolean isAlive() {
		return getCurrentCell() != null;
	}

	public Color getColor() {
		return color;
	}

	private void setColor(Color color) {
		this.color = color;
	}

	public Cell getCurrentCell() {
		return currentCell;
	}

	private void setCurrentCell(Cell currentCell) {
		this.currentCell = currentCell;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("Piece [color=");
		builder.append(color);
		builder.append(", currentCell=");
		builder.append(currentCell);
		builder.append("]");
		return builder.toString();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((color == null) ? 0 : color.hashCode());
		result = prime * result + ((currentCell == null) ? 0 : currentCell.hashCode());
		return result;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Piece other = (Piece) obj;
		if (color != other.color)
			return false;
		if (currentCell == null) {
			if (other.currentCell != null)
				return false;
		} else if (!currentCell.equals(other.currentCell))
			return false;
		return true;
	}

}
