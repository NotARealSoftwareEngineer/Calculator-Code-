#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>


void main()
{
	double  m, x, y,xc; 
	double ar[8];
	for (int z = 0; z < 8; z++) {//replace number of loops with number of slopes


		printf("Enter X value:\n");
		scanf("%lf", &x);

		printf("%lf\n", x);
		xc = (x * x);//replace for x squared or x cubed
		y = xc - 1; // replace for equation
		printf("Q is found at (%lf,%lf)\n", x, y);
		m = (3 - y) / (2- x);//replace variables 
		printf("M of pq = %lf\n\n\n", m);
		ar[z] = m;
		
	}
	for (int z = 0; z < 8; z++) {
		printf("%lf, ", ar[z]);
	}//replace below with number of slopes youre lookign for
	double avg = (ar[0] + ar[1] + ar[2] + ar[3] + ar[4] + ar[5] + ar[6] + ar[7])/8;
	printf("AVG slope = %lf", avg);
}