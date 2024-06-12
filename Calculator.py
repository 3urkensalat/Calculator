import cmath
import matplotlib.pyplot as plt

def add_complex(a, b):
    return a + b

def sub_complex(a, b):
    return a - b

def mul_complex(a, b):
    return a * b

def div_complex(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def plot_complex(c):
    plt.figure(figsize=(5, 5))
    plt.plot([0, c.real], [0, c.imag], marker='o')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.title(f'Complex Number: {c.real} + {c.imag}i')
    plt.show()

def main():
    a_real = float(input("Enter the real part of the first complex number: "))
    a_imag = float(input("Enter the imaginary part of the first complex number: "))
    b_real = float(input("Enter the real part of the second complex number: "))
    b_imag = float(input("Enter the imaginary part of the second complex number: "))
    
    a = complex(a_real, a_imag)
    b = complex(b_real, b_imag)
    
    op = input("Enter the operation (+, -, *, /): ")
    
    if op == '+':
        result = add_complex(a, b)
    elif op == '-':
        result = sub_complex(a, b)
    elif op == '*':
        result = mul_complex(a, b)
    elif op == '/':
        try:
            result = div_complex(a, b)
        except ValueError as e:
            print(e)
            return
    else:
        print("Invalid operation!")
        return
    
    print(f"Result: {result.real} + {result.imag}i")
    plot_complex(result)

if __name__ == "__main__":
    main()

