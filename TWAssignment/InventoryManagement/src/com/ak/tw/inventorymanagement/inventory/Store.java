package com.ak.tw.inventorymanagement.inventory;

import java.util.Map;

import com.ak.tw.inventorymanagement.country.Country;

public class Store {
	private Map<Country, Inventory> inventories;
	private static final int TRANSPORTCOST = 40;
	private static final int PURCHASENOTPOSSIBLE = -1;

	public Store(Map<Country, Inventory> inventories) {
		super();
		this.inventories = inventories;
	}

	public void addInventory(Country country, Inventory inventory) {
		inventories.put(country, inventory);
	}

	public void removeInventory(Inventory inventory) {
		inventories.remove(inventory);
	}

	/**
	 * @param country
	 * @param quantity
	 * @return cost of purchase if purchase in possible in the store else
	 *         returns -1
	 */
	public int purchase(Country country, int quantity) {
		Inventory inventory = getInventories().get(country);
		Inventory minPriceInventory = getMinPriceInventory();
		int minCost = 0;
		int cost = 0;
		if (minPriceInventory.isStockAvailable(quantity)) {
			if (minPriceInventory != inventory) {
				minCost = (minPriceInventory.getPrice() + TRANSPORTCOST) * quantity;
			} else {
				minCost = minPriceInventory.getPrice() * quantity;
			}
		}
		if (inventory.isStockAvailable(quantity)) {
			cost = quantity * inventory.getPrice();
		}
		if (minPriceInventory != inventory && minCost < cost) {
			minPriceInventory.setIpodStock(minPriceInventory.getIpodStock()-quantity);
			return minCost;
		}
		if (inventory.isStockAvailable(quantity)) {
			inventory.setIpodStock(inventory.getIpodStock() - quantity);
			return cost;
		}
		cost = inventory.getIpodStock() * inventory.getPrice();
		quantity -= inventory.getIpodStock();
		int transportStockCost = transportStock(quantity, country);
		if (transportStockCost!=PURCHASENOTPOSSIBLE) {
			inventory.setIpodStock(0);
			return cost + transportStockCost;
		}
		return PURCHASENOTPOSSIBLE;
	}

	private Inventory getMinPriceInventory() {
		Inventory minCostInventory = null;
		for (Inventory inventory : inventories.values()) {
			if (minCostInventory == null) {
				minCostInventory = inventory;
			}
			if (inventory.getPrice() < minCostInventory.getPrice() && inventory.getIpodStock() > 0) {
				minCostInventory = inventory;
			}
		}
		return minCostInventory;
	}

	private int transportStock(int quantity, Country country) {
		for (Inventory inventory : inventories.values()) {
			if (inventory.getCountry() != country && inventory.getIpodStock() >= quantity) {
				inventory.setIpodStock(inventory.getIpodStock() - quantity);
				return (TRANSPORTCOST + inventory.getPrice()) * quantity;
			}
		}
		return PURCHASENOTPOSSIBLE;
	}

	public Inventory getInventory(Country country) {
		return getInventories().get(country);
	}

	public Map<Country, Inventory> getInventories() {
		return inventories;
	}

	private void setInventories(Map<Country, Inventory> inventories) {
		this.inventories = inventories;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append("Store [inventories=");
		builder.append(inventories);
		builder.append("]");
		return builder.toString();
	}

}
