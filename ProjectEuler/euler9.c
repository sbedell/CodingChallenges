#include<stdio.h>

int main() {
	int a, b, c;
	int i, x, y;
	
    for (a = 1; a <= 1000; a++) {
		for (b = 1; b <= 1000; b++) {
			for (c = 1; c <= 1000; c++){
				if (((a + b + c) == 1000) && (((a*a) +(b*b)) == (c*c))) {
					break;
				}
			}
			if ((a + b + c) == 1000) {
				break;
			}
		}
		if ((a + b + c) == 1000) {
			break;
		}
	}
	printf("a = %d\nb = %d\nc = %d\n", a, b, c);
	int result = a*b*c;	
	printf("abc = %d\n",result);
	return 0;
}
