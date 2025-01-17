package com.ak.tw.inventorymanagement;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

import com.ak.tw.inventorymanagement.country.Country;
import com.ak.tw.inventorymanagement.inventory.Inventory;
import com.ak.tw.inventorymanagement.inventory.Store;

public class TestClient {

	public static void main(String[] args) throws IOException {
		int ipodStockBrazil = 100;
		int priceBrazil = 100;
		Inventory brazilInventory = new Inventory(ipodStockBrazil, priceBrazil, Country.BRAZIL);

		int ipodStockArgentina = 100;
		int priceArgentina = 50;
		Inventory argentinaInventory = new Inventory(ipodStockArgentina, priceArgentina, Country.ARGENTINA);

		Map<Country, Inventory> inventories = new HashMap<Country, Inventory>();
		inventories.put(brazilInventory.getCountry(), brazilInventory);
		inventories.put(argentinaInventory.getCountry(), argentinaInventory);

		Store store = new Store(inventories);

		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
		String input = bufferedReader.readLine();
		String[] splitInput = input.split(":");

		int purchaseQuantity = Integer.parseInt(splitInput[1]);
		String strCountry = splitInput[0];
		Country country = null;
		if (strCountry.equals("Brazil")) {
			country = Country.BRAZIL;
		} else if (strCountry.equals("Argentina")) {
			country = Country.ARGENTINA;
		}
		System.out.println(strCountry);
		int cost = store.purchase(country, purchaseQuantity);

		System.out.println(cost + ":" + store.getInventory(Country.BRAZIL).getIpodStock() + ":"
				+ store.getInventory(Country.ARGENTINA).getIpodStock());
	}

}
