package com.ak.tw.inventorymanagement.inventory;

import com.ak.tw.inventorymanagement.country.Country;

public class Inventory implements Comparable<Inventory> {
	private int ipodStock;
	private int price;
	private Country country;

	public Inventory(int ipodStock, int price, Country country) {
		super();
		this.ipodStock = ipodStock;
		this.price = price;
		this.country = country;
	}

	public boolean isStockAvailable(int quantity) {
		return getIpodStock() >= quantity;
	}

	public int getIpodStock() {
		return ipodStock;
	}

	public void setIpodStock(int ipodStock) {
		this.ipodStock = ipodStock;
	}

	public int getPrice() {
		return price;
	}

	private void setPrice(int price) {
		this.price = price;
	}

	public Country getCountry() {
		return country;
	}

	private void setCountry(Country country) {
		this.country = country;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("Inventory [ipodStock=");
		builder.append(ipodStock);
		builder.append(", price=");
		builder.append(price);
		builder.append(", country=");
		builder.append(country);
		builder.append("]");
		return builder.toString();
	}

	@Override
	public int hashCode() {
		final int prime = 31;
		int result = 1;
		result = prime * result + ((country == null) ? 0 : country.hashCode());
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
		Inventory other = (Inventory) obj;
		if (country != other.country)
			return false;
		return true;
	}

	@Override
	public int compareTo(Inventory inventory) {
		return getCountry().compareTo(inventory.getCountry());
	}

}
