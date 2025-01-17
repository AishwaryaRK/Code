
public class AppleStocks {

	public static void main(String[] args) {
		int[] stockPricesYesterday = { 9, 23, 3, 8, 13, 1, 12 };
		System.out.println(getBestProfit(stockPricesYesterday));
	}

	private static int getBestProfit(int[] stockPricesYesterday) {
		int purchasePrice = stockPricesYesterday[0];
		int sellingPrice = stockPricesYesterday[1];
		int profitOrLoss = sellingPrice - purchasePrice;
		for (int i = 2; i < stockPricesYesterday.length; i++) {
			if (stockPricesYesterday[i] - purchasePrice > profitOrLoss) {
				profitOrLoss = stockPricesYesterday[i] - purchasePrice;
			}
			if (stockPricesYesterday[i] < purchasePrice) {
				purchasePrice = stockPricesYesterday[i];
			}
		}
		return profitOrLoss;
	}

}
