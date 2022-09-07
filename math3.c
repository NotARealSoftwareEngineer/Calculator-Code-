#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void lawSineFunction(float pi, double valAr[6]);
void lawCosineFunction(float pi, double valAr[6],char cosAngleSelect, int cosSelection );
void vectorFunction(float pi, double valAr[6], double tempAngle, int vectorType);
void ambiFunction(float pi, double valAr[6], char ambiAngleSelection, char ambiSide1Selection, char ambiSide2Selection);



void lawSineFunction(float pi, double valAr[6])
{
	if (valAr[3] == -0)
	{
		valAr[3] = 180 - (valAr[4] + valAr[5]);
	}
	if (valAr[4] == 0)
	{
		valAr[4] = 180 - (valAr[3] + valAr[5]);
	}
	if (valAr[5] == 0)
	{
		valAr[5] = 180 - (valAr[3] + valAr[4]);
	}

	valAr[3] = valAr[3] * (pi / 180);
	valAr[4] = valAr[4] * (pi / 180);
	valAr[5] = valAr[5] * (pi / 180);
	if (valAr[0] == 0)
	{
		if (valAr[1] != 0)
		{
			double x = sin(valAr[3]);
			double temp = valAr[1] * x;
			double y = sin(valAr[4]);
			valAr[0] = temp / y;
		}
		else if (valAr[1] == 0)
		{
			double x = sin(valAr[3]);
			double temp = valAr[2] * x;
			double y = sin(valAr[5]);
			valAr[0] = temp / y;
		}

	}
	if (valAr[1] == 0)
	{
		double X = sin(valAr[4]);
		double Y = sin(valAr[3]);
		double Temp = valAr[0] * X;
		valAr[1] = Temp / Y;
	}
	if (valAr[2] == 0)
	{
		double x = sin(valAr[5]);
		double y = sin(valAr[3]);
		double temp = valAr[0] * x;
		valAr[2] = temp / y;
	}
	valAr[3] = (valAr[3] / pi) * 180;
	valAr[4] = (valAr[4] / pi) * 180;
	valAr[5] = (valAr[5] / pi) * 180;
	if ((valAr[3] + valAr[4] + valAr[5]) > 180)
	{
		printf("The (below) generated triangle is invalid because the angles are more than 180");
	}
}

void lawCosineFunction(float pi, double valAr[6], char cosAngleSelect, int cosSelection)
{
	
	double a = valAr[0];
	double b = valAr[1];
	double c = valAr[2];
	double A = valAr[3];
	double B = valAr[4];
	double C = valAr[5];
	if (cosSelection == 1)
	{

		if (valAr[2] >= valAr[1] && valAr[2] >= valAr[0])
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
			valAr[0] = a;
			valAr[1] = b;
			valAr[2] = c;
			valAr[3] = A;
			valAr[4] = B;
			valAr[5] = C;
			lawSineFunction(pi, valAr);
			
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
			valAr[0] = a;
			valAr[1] = b;
			valAr[2] = c;
			valAr[3] = A;
			valAr[4] = B;
			valAr[5] = C;
			lawSineFunction(pi, valAr);
		}
		else if (a >= c&& a >= b)
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
			valAr[0] = a;
			valAr[1] = b;
			valAr[2] = c;
			valAr[3] = A;
			valAr[4] = B;
			valAr[5] = C;
			lawSineFunction(pi, valAr);
		}
	}
	else if (cosSelection == 2)
	{
		char  side1Select, side2Select;


		if (cosAngleSelect == 'A')
		{
			A = A * (pi / 180);
			double asq, bsq, csq, x, y, temp;
			bsq = (b*b);
			csq = (c*c);
			x = cos(A);
			y = (b*c);
			temp = (2 * x*y);
			asq = bsq + csq - temp;
			a = sqrt(asq);
			/*finding B below this line*/
			x = sin(A);
			temp = (x*b) / a;
			B = asin(temp);
			A = (A / pi) * 180;
			B = (B / pi) * 180;
			if (a + b > c && a + c > b && b + c > a) {
				valAr[0] = a;
				valAr[1] = b;
				valAr[2] = c;
				valAr[3] = A;
				valAr[4] = B;
				valAr[5] = C;
				lawSineFunction(pi, valAr);
				
			}
			else if (a + b < c || a + c < b || b + c < a)
			{
				printf("Invalid Triangle generated.");
			}

			
		}
		else if (cosAngleSelect == 'B')
		{


			B = B * (pi / 180);

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
				valAr[0] = a;
				valAr[1] = b;
				valAr[2] = c;
				valAr[3] = A;
				valAr[4] = B;
				valAr[5] = C;
				lawSineFunction(pi, valAr);
				
			}
			else if (a + b < c || a + c < b || b + c < a)
			{
				printf("Invalid Triangle generated.");
			}

			
		}
		else if (cosAngleSelect == 'C')
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
			valAr[0] = a;
			valAr[1] = b;
			valAr[2] = c;
			valAr[3] = A;
			valAr[4] = B;
			valAr[5] = C;
			lawSineFunction(pi, valAr);
		

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

void vectorFunction(float pi, double valAr[6], double tempAngle, int vectorType)
{
	if (vectorType == 1)
	{
		valAr[5] = 180 - tempAngle;
		int cosSelection = 2;
		char cosAngleSelect = 'C';
		lawCosineFunction(pi, valAr, cosAngleSelect, cosSelection);
		
	}
}

void ambiFunction(float pi, double valAr[6], char ambiAngleSelection, char ambiSide1Selection, char ambiSide2Selection)
{
	double ambiMathAngle, ambiMathSide1, ambiMathSide2;
	if (ambiAngleSelection == 'A')
	{
		ambiMathAngle = valAr[3];
	}
	else if (ambiAngleSelection == 'B')
	{
		ambiMathAngle = valAr[4];
	}
	else if (ambiAngleSelection == 'C')
	{
		ambiMathAngle = valAr[5];
	}


	if (ambiSide1Selection == 'a')
	{
		ambiMathSide1 = valAr[0];
	}
	else if (ambiSide1Selection == 'b')
	{
		ambiMathSide1 = valAr[1];
	}
	else if (ambiSide1Selection == 'c')
	{
		ambiMathSide1 = valAr[2];
	}

	if (ambiSide2Selection == 'a')
	{
		ambiMathSide2 = valAr[0];
	}
	else if (ambiSide2Selection == 'b')
	{
		ambiMathSide2 = valAr[1];
	}
	else if (ambiSide2Selection == 'c')
	{
		ambiMathSide2 = valAr[2];
	}

	ambiMathAngle = ambiMathAngle * (pi / 180);
	double x = sin(ambiMathAngle);
	double temp = (x*ambiMathSide1) / ambiMathSide2;
	if (temp > 1)
	{
		printf("No Solution\n");
	}
	else if (temp <= 1)
	{
		printf("This is valid.\n");
		double ambiMathAngle2a = asin(temp);
		ambiMathAngle2a = (ambiMathAngle2a / pi) * 180;
		double ambiMathAngle2b = 180 - ambiMathAngle2a;
		if (ambiMathAngle2b <= 180)
		{
			if (ambiSide1Selection == 'a')
			{
				valAr[3] = ambiMathAngle2a;
			}
			else if (ambiSide1Selection == 'b')
			{
				valAr[4] = ambiMathAngle2a;
			}
			else if (ambiSide1Selection == 'c')
			{
				valAr[5] = ambiMathAngle2a;
			}
			lawSineFunction(pi, valAr);
			printf("\nFirst Triangle:\n");
			printf("Angle A is %.5lf\n", valAr[3]);
			printf("Angle B is %.5lf\n", valAr[4]);
			printf("Angle C is %.5lf\n", valAr[5]);
			printf("side a is %.5lf\n", valAr[0]);
			printf("side b is %.5lf\n", valAr[1]);
			printf("side c is %.5lf\n", valAr[2]);
			if (ambiSide1Selection == 'a')
			{
				valAr[3] = ambiMathAngle2b;
				if (ambiAngleSelection == 'B')
				{
					valAr[5] = 0;
				}
				else if (ambiAngleSelection == 'C')
				{
					valAr[4] = 0;
				}
			}
			else if (ambiSide1Selection == 'b')
			{
				valAr[4] = ambiMathAngle2b;
				if (ambiAngleSelection == 'A')
				{
					valAr[5] = 0;
				}
				else if (ambiAngleSelection == 'C')
				{
					valAr[3] = 0;
				}
			}
			else if (ambiSide1Selection == 'c')
			{
				valAr[5] = ambiMathAngle2b;
				if (ambiAngleSelection == 'B')
				{
					valAr[3] = 0;
				}
				else if (ambiAngleSelection == 'A')
				{
					valAr[4] = 0;
				}
			}
			lawSineFunction(pi, valAr);
			printf("\nSecond Triangle:\n");
			printf("Angle A is %.5lf\n", valAr[3]);
			printf("Angle B is %.5lf\n", valAr[4]);
			printf("Angle C is %.5lf\n", valAr[5]);
			printf("side a is %.5lf\n", valAr[0]);
			printf("side b is %.5lf\n", valAr[1]);
			printf("side c is %.5lf\n", valAr[2]);
		}

	}
}
void areaFun(double valAr[6], float pi, char angleSelect);
void areaFun(double valAr[6], float pi, char angleSelect)
{
	/*A = A * (pi / 180);
	double x = a * b;
	double y = sin(A);
	double temp = .5*x;
	double area = temp * y;
	printf("Area = %.4lf", area);*/
	double a = valAr[0];
	double b = valAr[1];
	double c = valAr[2];
	double A = valAr[3];
	double B = valAr[4];
	double C = valAr[5];

	if (angleSelect == 'A')
	{
		A = A * (pi / 180);
		double x = c * b;
		double y = sin(A);
		double temp = .5*x;
		double area = temp * y;
		printf("Area = %.4lf", area);
	}
	else if (angleSelect == 'B')
	{
		B = B * (pi / 180);
		double x = a * c;
		double y = sin(B);
		double temp = .5*x;
		double area = temp * y;
		printf("Area = %.4lf", area);
	}
	else if (angleSelect == 'C')
	{
		C = C * (pi / 180);
		double x = a * b;
		double y = sin(C);
		double temp = .5*x;
		double area = temp * y;
		printf("Area = %.4lf", area);

	}
}

double minDeg(double minDegDeg, double minDegMin, double minDegSec);
double minDeg(double minDegDeg, double minDegMin, double minDegSec)
{
	double result = (minDegDeg)+(minDegMin / 60) + (minDegSec / 60);
	return result;
}

void degMinFun(double degMinVal, double degMin[3]);
void degMinFun(double degMinVal, double degMin[3])
{
	double z;
	int x = (int)degMinVal;
	double yTemp = degMinVal - x;
	double y = (yTemp * 60);

	z = y - (int)y;
	z = z * 60;
	if (z > 0)
	{
		y = y - 1;
	}

	degMin[0] = (double)x;
	degMin[1] = y;
	degMin[2] = z;

}
int main(void)
{
	int selection;
	do {
		double valAr[6] = { 0 };
		double a = 0, b = 0, c = 0, A = 0, B = 0, C = 0;
		/*valAr 0 = a, 1 = b, 2 = c, 3 = A, 4 = B, 5 = C*/
		double pi = 3.14159265358979;
		printf("\nWhich function would you like to use?\n1.) Law of Sines (two angles and a side)\n2.)Ambiguous Case(SSA)\n3.)Law of Cosines(SSS or SAS)\n4.)Vector\n5.)Area\n6.)Minutes to decimal\n7.)Decimal to minutes\n8.)degrees to radians(TO EXIT ENTER 999)\n");
		scanf("%d", &selection);
		if (selection == 1)
		{
			printf("Angle A =\n");
			scanf("%lf", &valAr[3]);
			printf("Angle B=\n");
			scanf("%lf", &valAr[4]);
			printf("Angle C=\n");
			scanf("%lf", &valAr[5]);
			printf("Side a =\n");
			scanf("%lf", &valAr[0]);
			printf("Side b=\n");
			scanf("%lf", &valAr[1]);
			printf("Side c=\n");
			scanf("%lf", &valAr[2]);
			lawSineFunction(pi, valAr);
			//now print all the values
			printf("Angle A is %.5lf\n", valAr[3]);
			printf("Angle B is %.5lf\n", valAr[4]);
			printf("Angle C is %.5lf\n", valAr[5]);
			printf("side a is %.5lf\n", valAr[0]);
			printf("side b is %.5lf\n", valAr[1]);
			printf("side c is %.5lf\n", valAr[2]);
		}
		else if (selection == 2)
		{
			char ambiAngleSelection, ambiSide1Selection, ambiSide2Selection;
			printf("What angle are you given?\n");
			ambiAngleSelection = toupper(getch());
			getchar();

			if (ambiAngleSelection == 'A')
			{
				printf("Enter angle A:\n");
				scanf("%lf", &valAr[3]);
				printf("Enter side a\n");
				scanf("%lf", &valAr[0]);
				printf("Are you given side b or c?\n");
				ambiSide1Selection = tolower(getch());
				getchar();
				ambiSide2Selection = 'a';
				if (ambiSide1Selection == 'b')
				{
					printf("Enter side b\n");
					scanf("%lf", &valAr[1]);
					ambiFunction(pi, valAr, ambiAngleSelection, ambiSide1Selection, ambiSide2Selection);
					//now print the values
				}
				else if (ambiSide1Selection == 'c')
				{
					printf("Enter side c\n");
					scanf("%lf", &valAr[2]);
					ambiFunction(pi, valAr, ambiAngleSelection, ambiSide1Selection, ambiSide2Selection);
					//now print the values
				}
			}

			else if (ambiAngleSelection == 'B')
			{
				printf("Enter angle B:\n");
				scanf("%lf", &valAr[4]);
				printf("Enter side b\n");
				scanf("%lf", &valAr[1]);
				printf("Are you given side a or c?\n");
				ambiSide1Selection = tolower(getch());
				getchar();
				ambiSide2Selection = 'b';
				if (ambiSide1Selection == 'a')
				{
					printf("Enter side a\n");
					scanf("%lf", &valAr[0]);
					ambiFunction(pi, valAr, ambiAngleSelection, ambiSide1Selection, ambiSide2Selection);
					//now print the values
				}
				else if (ambiSide1Selection == 'c')
				{
					printf("Enter side c\n");
					scanf("%lf", &valAr[2]);
					ambiFunction(pi, valAr, ambiAngleSelection, ambiSide1Selection, ambiSide2Selection);
					//now print the values
				}
			}
			else 	if (ambiAngleSelection == 'C')
			{
				printf("Enter angle C:\n");
				scanf("%lf", &valAr[5]);
				printf("Enter side c\n");
				scanf("%lf", &valAr[2]);
				printf("Are you given side B or A?\n");
				ambiSide1Selection = tolower(getch());
				getchar();
				ambiSide2Selection = 'c';
				if (ambiSide1Selection == 'b')
				{
					printf("Enter side b\n");
					scanf("%lf", &valAr[1]);
					ambiFunction(pi, valAr, ambiAngleSelection, ambiSide1Selection, ambiSide2Selection);
					//now print the values
				}
				else if (ambiSide1Selection == 'a')
				{
					printf("Enter side a\n");
					scanf("%lf", &valAr[0]);
					ambiFunction(pi, valAr, ambiAngleSelection, ambiSide1Selection, ambiSide2Selection);
					//now print the values
				}
			}
		}
		if (selection == 3)
		{
			int cosSelection;
			printf("What Information are you given?\n1.)SSS\n2.)SAS\n");
			scanf("%d", &cosSelection);
			char angleSelect;
			if (cosSelection == 1)
			{
				printf("Side a =\n");
				scanf("%lf", &valAr[0]);
				printf("Side b =\n");
				scanf("%lf", &valAr[1]);
				printf("Side c =\n");
				scanf("%lf", &valAr[2]);
				angleSelect = 'D';
			}
			else if (cosSelection == 2)
			{
				printf("Which angle were you given?\n");
				angleSelect = toupper(getch());
				if (angleSelect == 'A')
				{
					printf("Angle A =\n");
					scanf("%lf", &valAr[3]);
					printf("Side b =\n");
					scanf("%lf", &valAr[1]);
					printf("Side c =\n");
					scanf("%lf", &valAr[2]);
				}
				else if (angleSelect == 'B')
				{

					printf("Angle B= \n");
					scanf("%lf", &valAr[4]);
					printf("Side a =\n");
					scanf("%lf", &valAr[0]);
					printf("Side c =\n");
					scanf("%lf", &valAr[2]);
				}
				else if (angleSelect == 'C')
				{
					printf("Angle C=\n");
					scanf("%lf", &valAr[5]);
					printf("Side a =\n");
					scanf("%lf", &valAr[0]);
					printf("Side b =\n");
					scanf("%lf", &valAr[1]);
				}
			
			}
			lawCosineFunction(pi, valAr, angleSelect, cosSelection);
			printf("Angle A is %.5lf\n", valAr[3]);
			printf("Angle B is %.5lf\n", valAr[4]);
			printf("Angle C is %.5lf\n", valAr[5]);
			printf("side a is %.5lf\n", valAr[0]);
			printf("side b is %.5lf\n", valAr[1]);
			printf("side c is %.5lf\n", valAr[2]);
		}
		else if (selection == 4)
		{
			int vectorType;
			double tempAngle;
			printf("1.) Angle or 2.)Required force?\n");
			scanf("%d", &vectorType);
			if (vectorType == 1)
			{
				printf("Vertical Side (a)=\n");
				scanf("%lf", &valAr[0]);
				printf("Horizontal Side (b)=\n");
				scanf("%lf", &valAr[1]);
				printf("Angle between the two sides:\n");
				scanf("%lf", &tempAngle);
				vectorFunction(pi, valAr, tempAngle, vectorType);
				printf("Vertical Side (a)= %.4lf\n", valAr[0]);
				printf("Horizontal Side (b)= %.4lf\n", valAr[1]);
				printf("Resulting Side = %.4lf\n", valAr[2]);
				printf("Angle between resultant (c) and vertical side (a) = %.4lf\n", valAr[4]);
				printf("Angle between resultant (c) and horizontal side (b) = %.4lf\n", valAr[3]);
				double equiAngle = 180 - valAr[4];
				printf("Angle between equilibriant (-c) and vertical side (a) = %.4lf\n", equiAngle);

			}
			else if (vectorType == 2)
			{
				printf("Hypotenuse length (c) =\n");
				scanf("%lf", valAr[2]);
				valAr[5] = 90;
				printf("Angle of plane to horizontal (B):\n");
				scanf("%lf", &valAr[4]);
				
			}
		}
		else if ( selection == 5)
			{
			char angleSelect;
			printf("Which angle were you given?\n");
			angleSelect = toupper(getch());
			if (angleSelect == 'A')
			{
				printf("Angle A =\n");
				scanf("%lf", &valAr[3]);
				printf("Side b =\n");
				scanf("%lf", &valAr[1]);
				printf("Side c =\n");
				scanf("%lf", &valAr[2]);
			}
			else if (angleSelect == 'B')
			{

				printf("Angle B= \n");
				scanf("%lf", &valAr[4]);
				printf("Side a =\n");
				scanf("%lf", &valAr[0]);
				printf("Side c =\n");
				scanf("%lf", &valAr[2]);
			}
			else if (angleSelect == 'C')
			{
				printf("Angle C=\n");
				scanf("%lf", &valAr[5]);
				printf("Side a =\n");
				scanf("%lf", &valAr[0]);
				printf("Side b =\n");
				scanf("%lf", &valAr[1]);
			}
			areaFun(valAr, pi, angleSelect);
		}
		double minDegDeg = 0, minDegMin = 0, minDegSec = 0, degMinVal, degMin[3] = { 0 };
		if (selection == 6)
		{
			printf("Enter Degrees:\n");
			scanf("%lf", &minDegDeg);
			printf("Enter Minutes:\n");
			scanf("%lf", &minDegMin);
			printf("Enter Seconds:\n");
			scanf("%lf", &minDegSec);
			double minDegResult = minDeg(minDegDeg, minDegMin, minDegSec);
			printf("%.0lf degrees, %.0lf minutes, and %.0lf seconds is %.5lf", minDegDeg, minDegMin, minDegSec, minDegResult);
		}
		if (selection == 7)
		{
			printf("Enter value given:\n");
			scanf("%lf", &degMinVal);
			degMinFun(degMinVal, degMin);
			printf("%.0lf degrees, %.0lf minutes, %.0lf Seconds", degMin[0], degMin[1], degMin[2]);

		}
		if (selection == 8)
		{
			double degRadDeg;
			printf("Enter degrees:\n");
			scanf("%lf", &degRadDeg);
			double degRadRad = (degRadDeg * pi )/180;
			printf("%lf", degRadRad);
		}
		if (selection == 9)
		{
			double radDegRad;
			printf("Enter radians:\n");
			scanf("%lf", &radDegRad);
			double radDegDeg = (radDegRad * 180) / pi;
			printf("%lf", radDegDeg );
		}
	}while (selection != 999);
	return 0;
}
