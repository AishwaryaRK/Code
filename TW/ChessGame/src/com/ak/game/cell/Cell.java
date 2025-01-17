package com.ak.game.cell;

import com.ak.game.Color;
import com.ak.game.piece.Piece;

public class Cell {
	private int row;
	private int col;
	private Piece piece;

	public Cell(int row, int col) {
		this(row, col, null);
	}

	public Cell(int row, int col, Piece piece) {
		super();
		this.row = row;
		this.col = col;
		this.piece = piece;
	}

	public boolean isVacant() {
		return getPiece() == null;
	}

	public Color getColor() {
		if ((getRow() + getCol()) % 2 == 0) {
			return Color.WHITE;
		}
		return Color.BLACK;
	}

	public int getRow() {
		return row;
	}

	private void setRow(int row) {
		this.row = row;
	}

	public int getCol() {
		return col;
	}

	private void setCol(int col) {
		this.col = col;
	}

	public Piece getPiece() {
		return piece;
	}

	public void setPiece(Piece piece) {
		this.piece = piece;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("Cell [row=");
		builder.append(row);
		builder.append(", col=");
		builder.append(col);
		builder.append("]");
		return builder.toString();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + col;
		result = prime * result + row;
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
		Cell other = (Cell) obj;
		if (col != other.col)
			return false;
		if (row != other.row)
			return false;
		return true;
	}

}
