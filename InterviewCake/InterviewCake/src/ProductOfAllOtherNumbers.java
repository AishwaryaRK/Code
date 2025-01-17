
public class ProductOfAllOtherNumbers {

	public static void main(String[] args) {
		int[] input = { 1, 7, 3, 4 };
		int[] productOfAllOtherNumbers = getProductOfAllOtherNumbers(input);
		printArray(productOfAllOtherNumbers);
	}

	private static int[] getProductOfAllOtherNumbers(int[] input) {
		int[] productOfAllOtherNumbers = new int[input.length];
		int productBeforeIndex = 1;
		for (int i = 0; i < productOfAllOtherNumbers.length; i++) {
			productOfAllOtherNumbers[i] = productBeforeIndex;
			productBeforeIndex *= input[i];
		}
		int productAfterIndex = 1;
		for (int j = productOfAllOtherNumbers.length - 1; j >= 0; j--) {
			productOfAllOtherNumbers[j] *= productAfterIndex;
			productAfterIndex *= input[j];
		}
		return productOfAllOtherNumbers;
	}

	private static void printArray(int[] productOfAllOtherNumbers) {
		for (int i = 0; i < productOfAllOtherNumbers.length; i++) {
			System.out.print(productOfAllOtherNumbers[i] + ",");
		}
	}

}
