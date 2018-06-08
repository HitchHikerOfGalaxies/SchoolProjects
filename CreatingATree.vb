Module Module1

    Sub Main()
        Console.WriteLine("Bienvenido al programa que dibuja arbolitos de Navidad")
        Console.WriteLine()
        menu()
        Console.WriteLine("Oprima la tecla ENTER para salir")
        Console.ReadLine()
    End Sub
    Sub menu()
        Dim selection As Integer
        Console.WriteLine("Seleccione una de las siguientes opciones: ")
        Console.WriteLine()
        Console.WriteLine(vbTab & "1. Dibujar un arbolito")
        Console.WriteLine(vbTab & "2. Dibujar un arbolito con adornos")
        Console.WriteLine(vbTab & "3. Salir del programa")
        Console.WriteLine()
        Console.Write(vbTab & "Su seleccion: ")
        selection = CInt(Console.ReadLine())
        Select Case selection 'Simple select case for a menu
            Case Is = 1
                tree()
            Case Is = 2
                treedecorated()
            Case Is = 3
                Console.WriteLine()
                Console.WriteLine("Thank you for using the program")
                Console.WriteLine()
            Case Else
                Console.WriteLine()
                Console.WriteLine("Error, didn't enter 1, 2 or 3 for selection, choose from those and try again") 'error message
                Console.WriteLine()
        End Select
    End Sub
    Sub tree()
        Do
            Dim linea As Integer = 0
            Dim lineas As Integer = 0
            Dim counter As Integer = 0
            Console.Clear()
            Console.Write("Cuantas filas deseas imprimir? ")
            linea = CInt(Console.ReadLine())
            lineas = linea
            For linea = linea To 1 Step -1
                If linea = lineas Then ' This creates a condition so we only print one star
                    For espacio As Integer = 0 To (linea - 1) ' This is used to print the number of spaces before printing our star
                        Console.Write(" ")
                    Next
                    Console.WriteLine("*") ' after that is done, we print the star 
                Else ' After the star is printed, the rest of the executions go here unless the enter value is 1
                    For espacio As Integer = 0 To (linea - 1) ' This is used to print the number of spaces before printing our star
                        Console.Write(" ")
                    Next
                    Console.Write("/") ' after that is done, we print the slash after every execution 
                    For espacio As Integer = 0 To (counter) ' earlier we made a counter to consider the spaces inside the tree to 
                        Console.Write(" ")
                    Next
                    Console.WriteLine("\") ' to then print the other slash after every execution
                    counter += 2
                End If
            Next
            Console.Write(" ")
            For i As Integer = 0 To counter ' Now it will print the number of dashes depending on the final counter value
                Console.Write("-")
            Next
            Console.WriteLine()
            Dim one As Integer = lineas
            If one <= 3 Then ' Condition so we only print one stick if we have a tree that is 3 or less
                For linea = 0 To lineas - 1
                    Console.Write(" ")
                Next
                Console.WriteLine("|") ' sticks/barras may appear bigger due to me not knowing how to put the one in the informe
            ElseIf one <= 18 Then '  Condition so we print 2 sticks if we have a tree that is 18 or less
                For linea = 0 To lineas - 3 ' These are used to print the number of spaces before adding our base
                    Console.Write(" ")
                Next
                Console.WriteLine("|  |")
                For linea = 0 To lineas - 3
                    Console.Write(" ")
                Next
                Console.WriteLine("|__|")
            Else ' Condition so we print three sticks if we have a tree that greater than 18
                For linea = 0 To lineas - 4 ' These are used to print the number of spaces before adding our base
                    Console.Write(" ")
                Next
                Console.WriteLine("|     |")
                For linea = 0 To lineas - 4
                    Console.Write(" ")
                Next
                Console.WriteLine("|     |")
                For linea = 0 To lineas - 4
                    Console.Write(" ")
                Next
                Console.WriteLine("|_____|")
            End If
            Console.WriteLine()
            Console.Write("Terminaste? Entre n para no y s para si: ") ' Asks if we want to terminate the program
        Loop While (Console.ReadLine() = "n")
        Console.WriteLine("Presione Enter para terminar")
        Console.ReadLine()
    End Sub
    Sub treedecorated()
        Do
            Dim linea As Integer = 0
            Dim lineas As Integer = 0
            Dim counter As Integer = 0
            Console.Clear()
            Console.Write("Cuantas filas deseas imprimir? ")
            linea = CInt(Console.ReadLine())
            lineas = linea
            Dim simbol As String = "" 'Code is the above but now we added variables for decoratiosn such as this string and change
            For linea = linea To 1 Step -1
                Dim change As Integer = 0
                If linea = lineas Then
                    For espacio As Integer = 0 To (linea - 1)
                        Console.Write(" ")
                    Next
                    Console.WriteLine("*")
                Else
                    For espacio As Integer = 0 To (linea - 1)
                        Console.Write(" ")
                    Next
                    Console.Write("/")
                    For espacio As Integer = 0 To (counter)
                        If change = 0 Then
                            Console.Write(" ") 'Writes a single space between decorations
                            change = 1
                        Else
                            If linea Mod 4 = 0 Then 'Will print + symbols 
                                simbol = "+"
                            ElseIf linea Mod 2 = 0 Then ' Will print o 
                                simbol = "o"
                            Else
                                simbol = "i" ' Will print i 
                            End If
                            Console.Write(simbol) ' actually prints the symbol
                            change = 0
                        End If
                    Next
                    Console.WriteLine("\")
                    counter += 2
                End If
            Next
            Console.Write(" ")
            For i As Integer = 0 To counter
                Console.Write("-")
            Next
            Console.WriteLine()
            Dim one As Integer = lineas
            If one <= 3 Then
                For linea = 0 To lineas - 1
                    Console.Write(" ")
                Next
                Console.WriteLine("|")
            ElseIf one <= 18 Then
                For linea = 0 To lineas - 3
                    Console.Write(" ")
                Next
                Console.WriteLine("|  |")
                For linea = 0 To lineas - 3
                    Console.Write(" ")
                Next
                Console.WriteLine("|__|")
            Else
                For linea = 0 To lineas - 4
                    Console.Write(" ")
                Next
                Console.WriteLine("|     |")
                For linea = 0 To lineas - 4
                    Console.Write(" ")
                Next
                Console.WriteLine("|     |")
                For linea = 0 To lineas - 4
                    Console.Write(" ")
                Next
                Console.WriteLine("|_____|")
            End If
            Console.WriteLine()
            Console.Write("Terminaste? Entre n para no y s para si: ")
        Loop While (Console.ReadLine() = "n")
        Console.WriteLine("Presione Enter para terminar")
        Console.ReadLine()
    End Sub
End Module
