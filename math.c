#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void lawSine(double a, double b, double c, double A, double B, double C, float pi);
void lawSine(double a, double b, double c, double A, double B, double C, float pi)
{
	if (A == -0)
	{
		A = 180 - (B + C);
	}
	if (B == 0)
	{
		B = 180 - (A + C);
	}
	if (C == 0)
	{
		C = 180 - (A + B);
	}

	A = A * (pi / 180);
	B = B * (pi / 180);
	C = C * (pi / 180);

	if (a == 0)
	{
		if (b != 0)
		{
			double x = sin(A);
			double temp = b * x;
			double y = sin(B);
			a = temp / y;
		}
		else if (b == 0)
		{
			double x = sin(A);
			double temp = c * x;
			double y = sin(C);
			a = temp / y;
		}

	}
	if (b == 0)
	{
		double X = sin(B);
		double Y = sin(A);
		double Temp = a * X;
		b = Temp / Y;
	}
	if (c == 0)
	{
		double x = sin(C);
		double y = sin(A);
		double temp = a * x;
		c = temp / y;
	}
	A = (A / pi) * 180;
	B = (B / pi) * 180;
	C = (C / pi) * 180;

	printf("Angle A is %.5lf\n", A);
	printf("Angle B is %.5lf\n", B);
	printf("Angle C is %.5lf\n", C);
	printf("side a is %.5lf\n", a);
	printf("side b is %.5lf\n", b);
	printf("side c is %.5lf\n", c);

	if (A < 0 || B < 0 || C < 0)
	{
		printf("(The above triangle generated was invalid.)\n\n");
	}
}
void areaFun(double a, double b, double c, double A, double B, double C, float pi);
void areaFun(double a, double b, double c, double A, double B, double C, float pi)
{
	A = A * (pi / 180);
	double x = a * b;
	double y = sin(A);
	double temp = .5*x;
	double area = temp * y;
	printf("Area = %.4lf", area);
}
void ambiFun(double a, double b, double c, double A, double B, double C, float pi);
void ambiFun(double a, double b, double c, double A, double B, double C, float pi)
{
	A = A * (pi / 180);
	double x = sin(A);
	double temp = (x*b) / a;
	printf("sin(angle 2) = %.4lf\n", temp);
	if (temp > 1)
	{
		printf("No Solution\n");
	}
	else if (temp <= 1)
	{
		printf("This is valid.\n");
		double angle2a = asin(temp);
		angle2a = (angle2a / pi) * 180;
		double angle2b = 180 - angle2a;
		if (angle2b <= 180)
		{
			A = (A / pi) * 180;
			B = angle2a;
			C = (C / pi) * 180;
			printf("First Triangle\n");
			double tempa, tempb, tempc, tempA, tempB, tempC, funB;
			tempa = a;
			tempb = b;
			tempc = c;
			tempA = A;
			tempC = C;
			lawSine(a, b, c, A, B, C, pi);
			printf("\n");
			funB = angle2b;
			printf("Second Triangle\n");
			lawSine(tempa, tempb, tempc, tempA, funB, tempC, pi);
		}
	}
}
void lawCosine(double a, double b, double c, double A, double B, double C, float pi, int cosSelection, char angleSelect);
void lawCosine(double a, double b, double c, double A, double B, double C, float pi, int cosSelection, char angleSelect)
{

	if (cosSelection == 1)
	{
		
		if (c >= b && c >= a)
		{
			double asq, bsq, csq, x, y, temp;
			asq = (a*a);
			bsq = (b*b);
			csq = (c*c);
			x = (a*b);
			y = (asq + bsq) - (csq);
			temp = y / (2 * x);
			C = acos(temp);
			x = sin(C);
			temp = (x*a) / c;
			A = asin(temp);
			A = (A / pi) * 180;
			C = (C / pi) * 180;
			lawSine(a, b, c, A, B, C, pi);
		}
		else if (b >= c&& b >= a)
		{
			double asq, bsq, csq, x, y, temp;
			asq = (a*a);
			bsq = (b*b);
			csq = (c*c);
			x = (a*c);
			y = (asq + csq) - (bsq);
			temp = y / (2 * x);
			B = acos(temp);
			x = sin(B);
			temp = (x*a) / b;
			A = asin(temp);
			A = (A / pi) * 180;
			B = (B / pi) * 180;
			lawSine(a, b, c, A, B, C, pi);
		}
		else if ( a>=c&& a>=b)
		{
			double asq, bsq, csq, x, y, temp;
			asq = (a*a);
			bsq = (b*b);
			csq = (c*c);
			x = (b*c);
			y = (bsq + csq) - (asq);
			temp = y / (2 * x);
			A = acos(temp);
			x = sin(A);
			temp = (x*b) / a;
			B = asin(temp);
			
			A = (A / pi) * 180;
			B = (B / pi) * 180;
			lawSine(a, b, c, A, B, C, pi);
		}
	}
	else if (cosSelection == 2)
	{
		char  side1Select, side2Select;
	
		
		if (angleSelect == 'A')
		{
			A = A * (pi / 180);
			double asq, bsq, csq, x, y, temp;
			bsq = (b*b);
			csq = (c*c);
			x = cos(A);
			y = (b*c);
			temp = (2 *x*y);
			asq = bsq + csq - temp;
			a = sqrt(asq);
			/*finding B below this line*/
			x = sin(A);
			temp = (x*b) / a;
			B=asin(temp);
			A = (A / pi) * 180;
			B = (B / pi) * 180;
			if (a + b > c && a + c > b && b + c > a) {
				lawSine(a, b, c, A, B, C, pi);
			}
			else if (a + b < c || a + c < b || b + c < a)
			{
				printf("Invalid Triangle generated.");
			}

		}
		else if (angleSelect == 'B')
		{
			
		
			B= B * (pi / 180);

			double asq, bsq, csq, x, y, temp;
			asq = (a*a);
			csq = (c*c);
			x = cos(B);
			y = (a*c);
			temp = (2 * x*y);
			bsq = asq + csq - temp;
			b = sqrt(bsq);
			/*finding A below this line*/
			x = sin(B);
			temp = (x*a) / b;
			A = asin(temp);
			A = (A / pi) * 180;
			B = (B / pi) * 180;
			if (a + b > c && a + c > b && b + c > a) {
				lawSine(a, b, c, A, B, C, pi);
			}
			else if (a + b < c || a + c < b || b + c < a)
			{
				printf("Invalid Triangle generated.");
			}
		}
		else if (angleSelect == 'C')
		{
			
			C = C * (pi / 180);
			double asq, bsq, csq, x, y, temp;
			asq = (a*a);
			bsq = (b*b);
			x = cos(C);
			y = (a*b);
			temp = (2 * x*y);
			csq = asq + bsq - temp;
			c = sqrt(csq);
			/*finding C below this line*/
			x = sin(C);
			temp = (x*a) / c;
			A = asin(temp);
			A = (A / pi) * 180;
			C = (C / pi) * 180;
			lawSine(a, b, c, A, B, C, pi);

		}
		else
		{
			printf("Invalid selection\n");
		}
	}
	else
	{
		printf("Invalid selection\n");
	}
}
void vector(double a, double b, double c, double A, double B, double C, float pi);
void vector(double a, double b, double c, double A, double B, double C, float pi)
{
	printf("Enter vertical side:\n");
	scanf("%lf", &a);
	printf("Enter horizontal Side: \n");
	scanf("%lf", &b);
	double tempAngle;
	printf("What Angle value is given?\n");
	scanf("%lf", &tempAngle);
	C = 180 - tempAngle;
	int cosSelection = 2;
	char angleSelect = 'C';
	lawCosine(a, b, c, A, B, C, pi, cosSelection, angleSelect);
	printf("The Resulting side is side c.\n");



}

int main(void) {
	int selection;
	do {
		double a = 0, b = 0, c = 0, A = 0, B = 0, C = 0;
		float pi = 3.14159;
		/*double valAr[6];*/

		printf("\nWhich function would you like to use?\n1.) Law of Sines (two angles and a side)\n2.) Area of a triangle\n3.)Ambiguous Case(SSA)\n4.)Law of Cosines(SSS or SAS)\n5.)Vector\n");
		scanf("%d", &selection);
		if (selection == 1)
		{
			printf("Angle A =\n");
			scanf("%lf", &A);
			printf("Angle B=\n");
			scanf("%lf", &B);
			printf("Angle C=\n");
			scanf("%lf", &C);
			printf("Side a =\n");
			scanf("%lf", &a);
			printf("Side b=\n");
			scanf("%lf", &b);
			printf("Side c=\n");
			scanf("%lf", &c);
			lawSine(a, b, c, A, B, C, pi);
		}
		if (selection == 2)
		{
			printf("Side 1\n");
			scanf("%lf", &a);
			printf("Side 2\n");
			scanf("%lf", &b);
			printf("Angle\n");
			scanf("%lf", &A);
			areaFun(a, b, c, A, B, C, pi);
		}
		if (selection == 3)
		{
			printf("Side 1\n");
			scanf("%lf", &a);
			printf("Side 2\n");
			scanf("%lf", &b);
			printf("Angle 1\n");
			scanf("%lf", &A);
			ambiFun(a, b, c, A, B, C, pi);
		}
		if (selection == 4)
		{
			int cosSelection;
			printf("What Information are you given?\n1.)SSS\n2.)SAS\n");
			scanf("%d", &cosSelection);
			char angleSelect;
			if (cosSelection == 1)
			{
				printf("Side a =\n");
				scanf_s("%lf", &a);
				printf("Side b=\n");
				scanf_s("%lf", &b);
				printf("Side c=\n");
				scanf_s("%lf", &c);
				angleSelect = 'D';
			}
			else if (cosSelection == 2)
			{
				printf("Which angle were you given?\n");
				angleSelect = toupper(getch());
				if (angleSelect == 'A')
				{
					printf("Angle A= \n");
					scanf("%lf", &A);
					printf("Side b=\n");
					scanf("%lf", &b);
					printf("Side c=\n");
					scanf("%lf", &c);
				}
				else if (angleSelect == 'B')
				{

					printf("Angle B= \n");
					scanf("%lf", &B);
					printf("Side a=\n");
					scanf("%lf", &a);
					printf("Side c=\n");
					scanf("%lf", &c);
				}
				else if (angleSelect == 'C')
				{
					printf("Angle C=\n");
					scanf("%lf", &C);
					printf("Side a =\n");
					scanf("%lf", &a);
					printf("Side b=\n");
					scanf("%lf", &b);
				}
			}
			lawCosine(a, b, c, A, B, C, pi, cosSelection, angleSelect);
		}
		if (selection == 5)
		{
			vector(a, b, c, A, B, C, pi);
		}
	} while (selection != 6);
	return 0;
}