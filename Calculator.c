#include <stdio.h>
#include <stdlib.h>
#include <complex.h>

void add_complex(double complex a, double complex b) {
    double complex result = a + b;
    printf("Result: %.2f + %.2fi\n", creal(result), cimag(result));
}

void sub_complex(double complex a, double complex b) {
    double complex result = a - b;
    printf("Result: %.2f + %.2fi\n", creal(result), cimag(result));
}

void mul_complex(double complex a, double complex b) {
    double complex result = a * b;
    printf("Result: %.2f + %.2fi\n", creal(result), cimag(result));
}

void div_complex(double complex a, double complex b) {
    if (cabs(b) == 0) {
        printf("Division by zero error!\n");
        return;
    }
    double complex result = a / b;
    printf("Result: %.2f + %.2fi\n", creal(result), cimag(result));
}

int main() {
    double a_real, a_imag, b_real, b_imag;
    char op;

    printf("Enter the first complex number (real and imaginary): ");
    scanf("%lf %lf", &a_real, &a_imag);
    printf("Enter the second complex number (real and imaginary): ");
    scanf("%lf %lf", &b_real, &b_imag);

    double complex a = a_real + a_imag * I;
    double complex b = b_real + b_imag * I;

    printf("Enter the operation (+, -, *, /): ");
    scanf(" %c", &op);

    switch (op) {
        case '+':
            add_complex(a, b);
            break;
        case '-':
            sub_complex(a, b);
            break;
        case '*':
            mul_complex(a, b);
            break;
        case '/':
            div_complex(a, b);
            break;
        default:
            printf("Invalid operation!\n");
    }

    return 0;
}
