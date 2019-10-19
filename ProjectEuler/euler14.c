#include<stdio.h>
#include<math.h>

int reduce(int n) {
	int i;
	for (i = 0; n != 1; i++){
		if (n < 0 ){
			printf("ohsnapwhatareyoudoing.jpg\n");
			break;
		}
		if ((n % 2) == 0) {
			n = (n/2);
		} else {
			n = ((3 * n) + 1);			
		}
		printf("n = %d ",n);
	}
	return i;
}

int main() {
	int i, result;
	int max = 0;
	///113383
	for (i = 113000; i <= 1000000; i++) {
		if (i == 113390) break;
		printf("%d Found\n", i);
		result = reduce(i);
		if (result > max) {
			max = result;
		}
	}
	printf("i = %d\n", i);
	printf("iterations = %d\n", result);
	printf("max = %d\n", max);

	return 0;
}
