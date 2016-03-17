public static void LIS(int X[]) {
	
	int parent[] = new int[X.length];
	int increasingSub[] = new int[x.length + 1];

	int length = 0;
	
	for (int i = 0; i < X.length; i++){
		int low = 1;
		int high = length;

		while (low < high) {
				int mid = (int) Math.ceil ((low + high) / 2);
				if (X[increasingSub[mid]] < X[i])
						low = mid + 1;
				else 
						high = mid - 1;
		}

		int pos = low;
		parent[i] = increasingSub[pos - 1];
		increasingSub[pos] = i;

		if (pos > length) {
				length = pos;
		}

	}

	int LIS[] = new int[length];
	int k = increasingSub[length];
	for (int j = length - 1; j >= 0; j--){
		LIS[j] = X[k];
		k = parent[k];
	}
}
