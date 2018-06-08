Imports System
Module SalaryCalculator
    ' Programmer: Michael J. Gonzalez, December 1st, 2014
    Sub Main()
        PrintResults() ' This method is used to print the results of the sub data
    End Sub 'end of the sub
    Sub PrintResults()
        Data() ' Uses the sub Data for the code to execute
        Console.ReadLine() ' Pauses to view results
    End Sub 'end of the sub
    Sub Data()
        Dim hours, salary As Double ' Declaring the variables we will be using for data on salary and work hours, named them both doubles due to the possibility of decimals
        Dim verification As Integer ' Delclaring a different variable for when we want to continue to execute the code, made it integer due to the only possible numbers we can choose to continue are 1 or 2
        Do ' used to create a loop until a certain condition is met
            Console.Clear() ' to clear the screen after every new execution of the code
            Console.Write("Entre las horas trabajadas: ") 'Prints the text on the screen and the number we enter for our work hours right next to it
            hours = CInt(Console.ReadLine()) ' This let's us enter a number for work hours
            Console.Write("Entre su salario por hora: $") 'Prints the text on the screen and the number we enter for our salary right next to it
            salary = CInt(Console.ReadLine()) ' This let's us enter a number for our salary
            Console.WriteLine() ' These are used to create a space between sentences on the screen
            Console.WriteLine("Su salario base para esta semana es de ${0}", base(hours, salary)) ' Uses a function to calculate our base salary for the week using our two entered values, also {0} is used to display the first thing we put after the comma in this case our function for base salary
            Console.WriteLine() ' These are used to create a space between sentences on the screen
            Console.WriteLine("Deducciones") ' Our list of deductions 
            Console.WriteLine("Seguro Social: ${0}", socialsecurity(base(hours, salary))) 'Uses a function for calculating social security deduction, for this we enter our base previously
            Console.WriteLine("Contribucion sobre ingresos: ${0}", contribution(base(hours, salary))) ' Same concept as above but instead we use a function for computing our the contribution of income tax
            Console.WriteLine("Total de deducciones: ${0}", totaldeductions(socialsecurity(base(hours, salary)), contribution(base(hours, salary)))) ' Now we use another function to calculate our total amount of deductions, for this we carefully copy and paste both of the above used functions and plug in the possible missing parenthesis'
            Console.WriteLine() ' These are used to create a space between sentences on the screen
            Console.WriteLine("Su salario neto para esta semana es de: ${0}", netsalary((base(hours, salary)), totaldeductions(socialsecurity(base(hours, salary)), contribution(base(hours, salary))))) ' Same concept as above but now we use a function for subtracting the totaldeductions for our base salary to get our net salary, same concept as above, copy paste and insert missing parenthesis' if needed
            Console.WriteLine() ' These are used to create a space between sentences on the screen
            Console.WriteLine("Desea calcular otro salario?") ' Reminder to let us know if we want to continue
            Console.Write("Entre 1 para si o 2 para no: ") ' Enter either 1 or 2, anything else will result in an error
            verification = CInt(Console.ReadLine()) ' Used to enter our number for the above
            check(verification) ' Uses the method to check our number so we can either continue or end the program
        Loop Until (verification = 2) ' termination condition for when we no longer want the program to continue
        Console.WriteLine("End of program, press enter to exit") ' Message used to remind us that the program has ended 
    End Sub 'end of the sub
    Sub check(ByVal verification As Integer) ' Sub used to check if we want to continue or not
        Select Case verification ' Used a select case for certain conditions 
            Case Is = 1 ' This condition will allow for our program to continue
                verification = 1 ' Applies a value of 1 allowing our program to continue
            Case Is = 2 ' This condition will end our program
                verification = 2 ' Applies a value of 2 ending our program 
            Case Else ' Conditions for when we don't enter either 1 or 2
                Console.WriteLine("Error, did not enter 1 or 2, press enter to restart the program to try again") 'Error message
                Console.ReadLine() ' To pause and view results
        End Select ' Ends the case select
    End Sub 'end of the sub
    Function base(ByVal hours As Double, ByVal salary As Double) As Double ' function used to calculate base salary
        Return hours * salary ' Returns the base salary 
    End Function 'end of the function
    Function socialsecurity(ByVal base As Double) As Double ' function used to calculate social security deduction
        Return base * 0.0765 ' Math formula used to return the deduction
    End Function 'end of the function
    Function contribution(ByVal base As Double) As Double ' function used to calculate gross tax income deduction
        Return base * 0.15 ' Math formula used to return the deduction
    End Function 'end of the function
    Function totaldeductions(ByVal socialsecurity As Double, ByVal contribution As Double) As Double ' function used to add both deductions 
        Return socialsecurity + contribution ' Math formula used to return the total deductions
    End Function 'end of the function
    Function netsalary(ByVal base As Double, ByVal totaldeductions As Double) As Double ' function used to get netsalary (basically our salary minues the deductions)
        Return base - totaldeductions ' Math formula used to return the netsalary
    End Function 'end of the function
End Module 'end of the this module or in our case the program

