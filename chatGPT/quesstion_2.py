

def functions_in_many_languages():
    """
    "Can you show me how to make a calculator function in Ruby, Lua, C++, C#, and Java"
    Sure! Here are examples of how to create a simple calculator function in Ruby, Lua, C++, C#, and Java:

    ======================================================= Ruby =======================================================
    def calculator(num1, num2, operator)
      case operator
      when '+'
        return num1 + num2
      when '-'
        return num1 - num2
      when '*'
        return num1 * num2
      when '/'
        return num1 / num2
      else
        return "Invalid operator"
      end
    end

    # Example
    puts calculator(10, 5, '+') # Output: 15

    ======================================================= Lua =======================================================
    function calculator(num1, num2, operator)
      if operator == '+' then
        return num1 + num2
      elseif operator == '-' then
        return num1 - num2
      elseif operator == '*' then
        return num1 * num2
      elseif operator == '/' then
        return num1 / num2
      else
        return "Invalid operator"
      end
    end

    -- Example usage
    print(calculator(10, 5, '+')) -- Output: 15

    ======================================================= C++ =======================================================
    #include <iostream>
    using namespace std;

    double calculator(double num1, double num2, char operator)
    {
      switch(operator)
      {
        case '+':
          return num1 + num2;
        case '-':
          return num1 - num2;
        case '*':
          return num1 * num2;
        case '/':
          return num1 / num2;
        default:
          return -1;
      }
    }

    int main()
    {
      // Example usage
      cout << calculator(10, 5, '+') << endl; // Output: 15

      return 0;
    }

    ======================================================== C# ========================================================
    using System;

    class Program
    {
      static double Calculator(double num1, double num2, char operatorChar)
      {
        switch(operatorChar)
        {
          case '+':
            return num1 + num2;
          case '-':
            return num1 - num2;
          case '*':
            return num1 * num2;
          case '/':
            return num1 / num2;
          default:
            return -1;
        }
      }

      static void Main(string[] args)
      {
        // Example usage
        Console.WriteLine(Calculator(10, 5, '+')); // Output: 15
      }
    }

    ======================================================= Java =======================================================
    public class Calculator {
      public static double calculator(double num1, double num2, char operator) {
        switch (operator) {
          case '+':
            return num1 + num2;
          case '-':
            return num1 - num2;
          case '*':
            return num1 * num2;
          case '/':
            return num1 / num2;
          default:
            return -1;
        }
      }

      public static void main(String[] args) {
        // Example usage
        System.out.println(calculator(10, 5, '+')); // Output: 15
      }
    }
    """
